from __future__ import absolute_import

import semaphore
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property

from sentry.db.models import Model
from sentry.relay import config


class Relay(Model):
    __core__ = True

    relay_id = models.CharField(max_length=64, unique=True)
    public_key = models.CharField(max_length=200)
    first_seen = models.DateTimeField(default=timezone.now)
    last_seen = models.DateTimeField(default=timezone.now)
    is_internal = models.BooleanField(default=False)

    class Meta:
        app_label = 'sentry'
        db_table = 'sentry_relay'

    @cached_property
    def public_key_object(self):
        return semaphore.PublicKey.parse(self.public_key)

    def has_org_access(self, org):
        return config.relay_has_org_access(self, org)
