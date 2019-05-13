# -*- coding: utf-8 -*-
import datetime

from django.db import models
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    """
    A no-op migration to ensure the new search backend is clean.
    """

    def forwards(self, orm):
        pass

    def backwards(self, orm):
        pass

    models = {
        u'auth.group': {
            'Meta': {
                'object_name': 'Group'
            },
            u'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'name':
            ('django.db.models.fields.CharField', [], {
                'unique': 'True',
                'max_length': '80'
            }),
            'permissions': (
                'django.db.models.fields.related.ManyToManyField', [], {
                    'to': u"orm['auth.Permission']",
                    'symmetrical': 'False',
                    'blank': 'True'
                }
            )
        },
        u'auth.permission': {
            'Meta': {
                'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')",
                'unique_together': "((u'content_type', u'codename'),)",
                'object_name': 'Permission'
            },
            'codename': ('django.db.models.fields.CharField', [], {
                'max_length': '100'
            }),
            'content_type': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['contenttypes.ContentType']"
                }
            ),
            u'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'name': ('django.db.models.fields.CharField', [], {
                'max_length': '50'
            })
        },
        'sentry.user': {
            'Meta': {
                'object_name': 'User',
                'db_table': "'auth_user'"
            },
            'date_joined':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'email':
            ('django.db.models.fields.EmailField', [], {
                'max_length': '75',
                'blank': 'True'
            }),
            'first_name':
            ('django.db.models.fields.CharField', [], {
                'max_length': '30',
                'blank': 'True'
            }),
            'id': ('django.db.models.fields.AutoField', [], {
                'primary_key': 'True'
            }),
            'is_active': ('django.db.models.fields.BooleanField', [], {
                'default': 'True'
            }),
            'is_staff': ('django.db.models.fields.BooleanField', [], {
                'default': 'False'
            }),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {
                'default': 'False'
            }),
            'last_login':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'last_name':
            ('django.db.models.fields.CharField', [], {
                'max_length': '30',
                'blank': 'True'
            }),
            'password': ('django.db.models.fields.CharField', [], {
                'max_length': '128'
            }),
            'username':
            ('django.db.models.fields.CharField', [], {
                'unique': 'True',
                'max_length': '30'
            })
        },
        u'contenttypes.contenttype': {
            'Meta': {
                'ordering': "('name',)",
                'unique_together': "(('app_label', 'model'),)",
                'object_name': 'ContentType',
                'db_table': "'django_content_type'"
            },
            'app_label': ('django.db.models.fields.CharField', [], {
                'max_length': '100'
            }),
            u'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'model': ('django.db.models.fields.CharField', [], {
                'max_length': '100'
            }),
            'name': ('django.db.models.fields.CharField', [], {
                'max_length': '100'
            })
        },
        u'sentry.accessgroup': {
            'Meta': {
                'unique_together': "(('team', 'name'),)",
                'object_name': 'AccessGroup'
            },
            'data': ('django.db.models.fields.TextField', [], {
                'null': 'True',
                'blank': 'True'
            }),
            'date_added':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'managed': ('django.db.models.fields.BooleanField', [], {
                'default': 'False'
            }),
            'members': (
                'django.db.models.fields.related.ManyToManyField', [], {
                    'to': u"orm['sentry.User']",
                    'symmetrical': 'False'
                }
            ),
            'name': ('django.db.models.fields.CharField', [], {
                'max_length': '64'
            }),
            'projects': (
                'django.db.models.fields.related.ManyToManyField', [], {
                    'to': u"orm['sentry.Project']",
                    'symmetrical': 'False'
                }
            ),
            'team':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Team']"
            }),
            'type': ('django.db.models.fields.IntegerField', [], {
                'default': '50'
            })
        },
        u'sentry.activity': {
            'Meta': {
                'object_name': 'Activity'
            },
            'data': ('django.db.models.fields.TextField', [], {
                'null': 'True'
            }),
            'datetime':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'event': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Event']",
                    'null': 'True'
                }
            ),
            'group': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Group']",
                    'null': 'True'
                }
            ),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'ident':
            ('django.db.models.fields.CharField', [], {
                'max_length': '64',
                'null': 'True'
            }),
            'project':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Project']"
            }),
            'type': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'user': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.User']",
                    'null': 'True'
                }
            )
        },
        u'sentry.alert': {
            'Meta': {
                'object_name': 'Alert'
            },
            'data': ('django.db.models.fields.TextField', [], {
                'null': 'True'
            }),
            'datetime':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'group': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Group']",
                    'null': 'True'
                }
            ),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'message': ('django.db.models.fields.TextField', [], {}),
            'project':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Project']"
            }),
            'related_groups': (
                'django.db.models.fields.related.ManyToManyField', [], {
                    'related_name': "'related_alerts'",
                    'symmetrical': 'False',
                    'through': u"orm['sentry.AlertRelatedGroup']",
                    'to': u"orm['sentry.Group']"
                }
            ),
            'status': (
                'django.db.models.fields.PositiveIntegerField', [], {
                    'default': '0',
                    'db_index': 'True'
                }
            )
        },
        u'sentry.alertrelatedgroup': {
            'Meta': {
                'unique_together': "(('group', 'alert'),)",
                'object_name': 'AlertRelatedGroup'
            },
            'alert':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Alert']"
            }),
            'data': ('django.db.models.fields.TextField', [], {
                'null': 'True'
            }),
            'group':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Group']"
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            })
        },
        u'sentry.event': {
            'Meta': {
                'unique_together': "(('project', 'event_id'),)",
                'object_name': 'Event',
                'db_table': "'sentry_message'"
            },
            'checksum':
            ('django.db.models.fields.CharField', [], {
                'max_length': '32',
                'db_index': 'True'
            }),
            'culprit': (
                'django.db.models.fields.CharField', [], {
                    'max_length': '200',
                    'null': 'True',
                    'db_column': "'view'",
                    'blank': 'True'
                }
            ),
            'data': ('django.db.models.fields.TextField', [], {
                'null': 'True',
                'blank': 'True'
            }),
            'datetime': (
                'django.db.models.fields.DateTimeField', [], {
                    'default': 'datetime.datetime.now',
                    'db_index': 'True'
                }
            ),
            'event_id': (
                'django.db.models.fields.CharField', [], {
                    'max_length': '32',
                    'null': 'True',
                    'db_column': "'message_id'"
                }
            ),
            'group': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'blank': 'True',
                    'related_name': "'event_set'",
                    'null': 'True',
                    'to': u"orm['sentry.Group']"
                }
            ),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'level': (
                'django.db.models.fields.PositiveIntegerField', [], {
                    'default': '40',
                    'db_index': 'True',
                    'blank': 'True'
                }
            ),
            'logger': (
                'django.db.models.fields.CharField', [], {
                    'default': "'root'",
                    'max_length': '64',
                    'db_index': 'True',
                    'blank': 'True'
                }
            ),
            'message': ('django.db.models.fields.TextField', [], {}),
            'num_comments':
            ('django.db.models.fields.PositiveIntegerField', [], {
                'default': '0',
                'null': 'True'
            }),
            'platform':
            ('django.db.models.fields.CharField', [], {
                'max_length': '64',
                'null': 'True'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Project']",
                    'null': 'True'
                }
            ),
            'server_name': (
                'django.db.models.fields.CharField', [], {
                    'max_length': '128',
                    'null': 'True',
                    'db_index': 'True'
                }
            ),
            'site': (
                'django.db.models.fields.CharField', [], {
                    'max_length': '128',
                    'null': 'True',
                    'db_index': 'True'
                }
            ),
            'time_spent': ('django.db.models.fields.IntegerField', [], {
                'null': 'True'
            })
        },
        u'sentry.eventmapping': {
            'Meta': {
                'unique_together': "(('project', 'event_id'),)",
                'object_name': 'EventMapping'
            },
            'date_added':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'event_id': ('django.db.models.fields.CharField', [], {
                'max_length': '32'
            }),
            'group':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Group']"
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'project':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Project']"
            })
        },
        u'sentry.group': {
            'Meta': {
                'unique_together': "(('project', 'checksum'),)",
                'object_name': 'Group',
                'db_table': "'sentry_groupedmessage'"
            },
            'active_at':
            ('django.db.models.fields.DateTimeField', [], {
                'null': 'True',
                'db_index': 'True'
            }),
            'checksum':
            ('django.db.models.fields.CharField', [], {
                'max_length': '32',
                'db_index': 'True'
            }),
            'culprit': (
                'django.db.models.fields.CharField', [], {
                    'max_length': '200',
                    'null': 'True',
                    'db_column': "'view'",
                    'blank': 'True'
                }
            ),
            'data': ('django.db.models.fields.TextField', [], {
                'null': 'True',
                'blank': 'True'
            }),
            'first_seen': (
                'django.db.models.fields.DateTimeField', [], {
                    'default': 'datetime.datetime.now',
                    'db_index': 'True'
                }
            ),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'is_public': (
                'django.db.models.fields.NullBooleanField', [], {
                    'default': 'False',
                    'null': 'True',
                    'blank': 'True'
                }
            ),
            'last_seen': (
                'django.db.models.fields.DateTimeField', [], {
                    'default': 'datetime.datetime.now',
                    'db_index': 'True'
                }
            ),
            'level': (
                'django.db.models.fields.PositiveIntegerField', [], {
                    'default': '40',
                    'db_index': 'True',
                    'blank': 'True'
                }
            ),
            'logger': (
                'django.db.models.fields.CharField', [], {
                    'default': "'root'",
                    'max_length': '64',
                    'db_index': 'True',
                    'blank': 'True'
                }
            ),
            'message': ('django.db.models.fields.TextField', [], {}),
            'num_comments':
            ('django.db.models.fields.PositiveIntegerField', [], {
                'default': '0',
                'null': 'True'
            }),
            'platform':
            ('django.db.models.fields.CharField', [], {
                'max_length': '64',
                'null': 'True'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Project']",
                    'null': 'True'
                }
            ),
            'resolved_at':
            ('django.db.models.fields.DateTimeField', [], {
                'null': 'True',
                'db_index': 'True'
            }),
            'score': ('django.db.models.fields.IntegerField', [], {
                'default': '0'
            }),
            'status': (
                'django.db.models.fields.PositiveIntegerField', [], {
                    'default': '0',
                    'db_index': 'True'
                }
            ),
            'time_spent_count': ('django.db.models.fields.IntegerField', [], {
                'default': '0'
            }),
            'time_spent_total': ('django.db.models.fields.IntegerField', [], {
                'default': '0'
            }),
            'times_seen': (
                'django.db.models.fields.PositiveIntegerField', [], {
                    'default': '1',
                    'db_index': 'True'
                }
            )
        },
        u'sentry.groupbookmark': {
            'Meta': {
                'unique_together': "(('project', 'user', 'group'),)",
                'object_name': 'GroupBookmark'
            },
            'group': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'bookmark_set'",
                    'to': u"orm['sentry.Group']"
                }
            ),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'bookmark_set'",
                    'to': u"orm['sentry.Project']"
                }
            ),
            'user': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'sentry_bookmark_set'",
                    'to': u"orm['sentry.User']"
                }
            )
        },
        u'sentry.groupcountbyminute': {
            'Meta': {
                'unique_together': "(('project', 'group', 'date'),)",
                'object_name': 'GroupCountByMinute',
                'db_table': "'sentry_messagecountbyminute'"
            },
            'date': ('django.db.models.fields.DateTimeField', [], {
                'db_index': 'True'
            }),
            'group':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Group']"
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Project']",
                    'null': 'True'
                }
            ),
            'time_spent_count': ('django.db.models.fields.IntegerField', [], {
                'default': '0'
            }),
            'time_spent_total': ('django.db.models.fields.IntegerField', [], {
                'default': '0'
            }),
            'times_seen': ('django.db.models.fields.PositiveIntegerField', [], {
                'default': '0'
            })
        },
        u'sentry.groupmeta': {
            'Meta': {
                'unique_together': "(('group', 'key'),)",
                'object_name': 'GroupMeta'
            },
            'group':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Group']"
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'key': ('django.db.models.fields.CharField', [], {
                'max_length': '64'
            }),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'sentry.groupseen': {
            'Meta': {
                'unique_together': "(('user', 'group'),)",
                'object_name': 'GroupSeen'
            },
            'group':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Group']"
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'last_seen':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'project':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Project']"
            }),
            'user': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.User']",
                    'db_index': 'False'
                }
            )
        },
        u'sentry.grouptag': {
            'Meta': {
                'unique_together': "(('project', 'key', 'value', 'group'),)",
                'object_name': 'GroupTag',
                'db_table': "'sentry_messagefiltervalue'"
            },
            'first_seen': (
                'django.db.models.fields.DateTimeField', [], {
                    'default': 'datetime.datetime.now',
                    'null': 'True',
                    'db_index': 'True'
                }
            ),
            'group':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Group']"
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'key': ('django.db.models.fields.CharField', [], {
                'max_length': '32'
            }),
            'last_seen': (
                'django.db.models.fields.DateTimeField', [], {
                    'default': 'datetime.datetime.now',
                    'null': 'True',
                    'db_index': 'True'
                }
            ),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Project']",
                    'null': 'True'
                }
            ),
            'times_seen': ('django.db.models.fields.PositiveIntegerField', [], {
                'default': '0'
            }),
            'value': ('django.db.models.fields.CharField', [], {
                'max_length': '200'
            })
        },
        u'sentry.grouptagkey': {
            'Meta': {
                'unique_together': "(('project', 'group', 'key'),)",
                'object_name': 'GroupTagKey'
            },
            'group':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Group']"
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'key': ('django.db.models.fields.CharField', [], {
                'max_length': '32'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Project']",
                    'null': 'True'
                }
            ),
            'values_seen': ('django.db.models.fields.PositiveIntegerField', [], {
                'default': '0'
            })
        },
        u'sentry.lostpasswordhash': {
            'Meta': {
                'object_name': 'LostPasswordHash'
            },
            'date_added':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'hash': ('django.db.models.fields.CharField', [], {
                'max_length': '32'
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'user': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.User']",
                    'unique': 'True'
                }
            )
        },
        u'sentry.option': {
            'Meta': {
                'object_name': 'Option'
            },
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'key':
            ('django.db.models.fields.CharField', [], {
                'unique': 'True',
                'max_length': '64'
            }),
            'value': ('picklefield.fields.PickledObjectField', [], {})
        },
        u'sentry.pendingteammember': {
            'Meta': {
                'unique_together': "(('team', 'email'),)",
                'object_name': 'PendingTeamMember'
            },
            'date_added':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'email': ('django.db.models.fields.EmailField', [], {
                'max_length': '75'
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'team': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'pending_member_set'",
                    'to': u"orm['sentry.Team']"
                }
            ),
            'type': ('django.db.models.fields.IntegerField', [], {
                'default': '50'
            })
        },
        u'sentry.project': {
            'Meta': {
                'unique_together': "(('team', 'slug'),)",
                'object_name': 'Project'
            },
            'date_added':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'name': ('django.db.models.fields.CharField', [], {
                'max_length': '200'
            }),
            'owner': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'sentry_owned_project_set'",
                    'null': 'True',
                    'to': u"orm['sentry.User']"
                }
            ),
            'platform':
            ('django.db.models.fields.CharField', [], {
                'max_length': '32',
                'null': 'True'
            }),
            'public': ('django.db.models.fields.BooleanField', [], {
                'default': 'False'
            }),
            'slug': ('django.db.models.fields.SlugField', [], {
                'max_length': '50',
                'null': 'True'
            }),
            'status': (
                'django.db.models.fields.PositiveIntegerField', [], {
                    'default': '0',
                    'db_index': 'True'
                }
            ),
            'team': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Team']",
                    'null': 'True'
                }
            )
        },
        u'sentry.projectcountbyminute': {
            'Meta': {
                'unique_together': "(('project', 'date'),)",
                'object_name': 'ProjectCountByMinute'
            },
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Project']",
                    'null': 'True'
                }
            ),
            'time_spent_count': ('django.db.models.fields.IntegerField', [], {
                'default': '0'
            }),
            'time_spent_total': ('django.db.models.fields.IntegerField', [], {
                'default': '0'
            }),
            'times_seen': ('django.db.models.fields.PositiveIntegerField', [], {
                'default': '0'
            })
        },
        u'sentry.projectkey': {
            'Meta': {
                'object_name': 'ProjectKey'
            },
            'date_added': (
                'django.db.models.fields.DateTimeField', [], {
                    'default': 'datetime.datetime.now',
                    'null': 'True'
                }
            ),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'key_set'",
                    'to': u"orm['sentry.Project']"
                }
            ),
            'public_key': (
                'django.db.models.fields.CharField', [], {
                    'max_length': '32',
                    'unique': 'True',
                    'null': 'True'
                }
            ),
            'secret_key': (
                'django.db.models.fields.CharField', [], {
                    'max_length': '32',
                    'unique': 'True',
                    'null': 'True'
                }
            ),
            'user': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.User']",
                    'null': 'True'
                }
            ),
            'user_added': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'keys_added_set'",
                    'null': 'True',
                    'to': u"orm['sentry.User']"
                }
            )
        },
        u'sentry.projectoption': {
            'Meta': {
                'unique_together': "(('project', 'key'),)",
                'object_name': 'ProjectOption',
                'db_table': "'sentry_projectoptions'"
            },
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'key': ('django.db.models.fields.CharField', [], {
                'max_length': '64'
            }),
            'project':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Project']"
            }),
            'value': ('picklefield.fields.PickledObjectField', [], {})
        },
        u'sentry.tagkey': {
            'Meta': {
                'unique_together': "(('project', 'key'),)",
                'object_name': 'TagKey',
                'db_table': "'sentry_filterkey'"
            },
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'key': ('django.db.models.fields.CharField', [], {
                'max_length': '32'
            }),
            'label':
            ('django.db.models.fields.CharField', [], {
                'max_length': '64',
                'null': 'True'
            }),
            'project':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.Project']"
            }),
            'values_seen': ('django.db.models.fields.PositiveIntegerField', [], {
                'default': '0'
            })
        },
        u'sentry.tagvalue': {
            'Meta': {
                'unique_together': "(('project', 'key', 'value'),)",
                'object_name': 'TagValue',
                'db_table': "'sentry_filtervalue'"
            },
            'data': ('django.db.models.fields.TextField', [], {
                'null': 'True',
                'blank': 'True'
            }),
            'first_seen': (
                'django.db.models.fields.DateTimeField', [], {
                    'default': 'datetime.datetime.now',
                    'null': 'True',
                    'db_index': 'True'
                }
            ),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'key': ('django.db.models.fields.CharField', [], {
                'max_length': '32'
            }),
            'last_seen': (
                'django.db.models.fields.DateTimeField', [], {
                    'default': 'datetime.datetime.now',
                    'null': 'True',
                    'db_index': 'True'
                }
            ),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Project']",
                    'null': 'True'
                }
            ),
            'times_seen': ('django.db.models.fields.PositiveIntegerField', [], {
                'default': '0'
            }),
            'value': ('django.db.models.fields.CharField', [], {
                'max_length': '200'
            })
        },
        u'sentry.team': {
            'Meta': {
                'object_name': 'Team'
            },
            'date_added': (
                'django.db.models.fields.DateTimeField', [], {
                    'default': 'datetime.datetime.now',
                    'null': 'True'
                }
            ),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'members': (
                'django.db.models.fields.related.ManyToManyField', [], {
                    'related_name': "'team_memberships'",
                    'symmetrical': 'False',
                    'through': u"orm['sentry.TeamMember']",
                    'to': u"orm['sentry.User']"
                }
            ),
            'name': ('django.db.models.fields.CharField', [], {
                'max_length': '64'
            }),
            'owner':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.User']"
            }),
            'slug':
            ('django.db.models.fields.SlugField', [], {
                'unique': 'True',
                'max_length': '50'
            })
        },
        u'sentry.teammember': {
            'Meta': {
                'unique_together': "(('team', 'user'),)",
                'object_name': 'TeamMember'
            },
            'date_added':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'team': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'member_set'",
                    'to': u"orm['sentry.Team']"
                }
            ),
            'type': ('django.db.models.fields.IntegerField', [], {
                'default': '50'
            }),
            'user': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'sentry_teammember_set'",
                    'to': u"orm['sentry.User']"
                }
            )
        },
        u'sentry.useroption': {
            'Meta': {
                'unique_together': "(('user', 'project', 'key'),)",
                'object_name': 'UserOption'
            },
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'key': ('django.db.models.fields.CharField', [], {
                'max_length': '64'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': u"orm['sentry.Project']",
                    'null': 'True'
                }
            ),
            'user':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': u"orm['sentry.User']"
            }),
            'value': ('picklefield.fields.PickledObjectField', [], {})
        }
    }

    complete_apps = ['sentry']
