from __future__ import absolute_import

from sentry import tagstore
from sentry.api.base import DocSection, EnvironmentMixin
from sentry.api.bases.group import GroupEndpoint
from sentry.api.exceptions import ResourceDoesNotExist
from sentry.api.serializers import serialize
from sentry.api.serializers.models.tagvalue import UserTagValueSerializer
from sentry.models import Environment, Group
from sentry.utils.apidocs import scenario


@scenario('ListTagValues')
def list_tag_values_scenario(runner):
    group = Group.objects.filter(project=runner.default_project).first()
    runner.request(
        method='GET',
        path='/issues/%s/tags/%s/values/' % (group.id, 'browser'),
    )


class GroupTagKeyValuesEndpoint(GroupEndpoint, EnvironmentMixin):
    doc_section = DocSection.EVENTS

    # XXX: this scenario does not work for some inexplicable reasons
    # @attach_scenarios([list_tag_values_scenario])
    def get(self, request, group, key):
        """
        List a Tag's Values
        ```````````````````

        Return a list of values associated with this key for an issue.

        :pparam string issue_id: the ID of the issue to retrieve.
        :pparam string key: the tag key to look the values up for.
        :auth: required
        """
        lookup_key = tagstore.prefix_reserved_key(key)

        try:
            environment_id = self._get_environment_id_from_request(
                request, group.project.organization_id)
        except Environment.DoesNotExist:
            # if the environment doesn't exist then the tag can't possibly exist
            raise ResourceDoesNotExist

        try:
            tagstore.get_tag_key(group.project_id, environment_id, lookup_key)
        except tagstore.TagKeyNotFound:
            raise ResourceDoesNotExist

        sort = request.GET.get('sort')
        if sort == 'date':
            order_by = '-last_seen'
        elif sort == 'age':
            order_by = '-first_seen'
        else:
            order_by = '-id'

        if key == 'user':
            serializer_cls = UserTagValueSerializer(group.project_id)
        else:
            serializer_cls = None

        paginator = tagstore.get_group_tag_value_paginator(
            group.project_id, group.id, environment_id, lookup_key, order_by=order_by
        )

        return self.paginate(
            request=request,
            paginator=paginator,
            on_results=lambda results: serialize(results, request.user, serializer_cls),
        )
