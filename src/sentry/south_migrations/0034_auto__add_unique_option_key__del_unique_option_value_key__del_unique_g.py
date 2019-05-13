# encoding: utf-8
import datetime

from django.db import models
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):

        # Removing unique constraint on 'ProjectOption', fields ['project', 'value', 'key']
        try:
            db.delete_unique('sentry_projectoptions', ['project_id', 'value', 'key'])
        except Exception:
            pass

        # Removing unique constraint on 'GroupMeta', fields ['group', 'value', 'key']
        try:
            db.delete_unique('sentry_groupmeta', ['group_id', 'value', 'key'])
        except Exception:
            pass

        # Removing unique constraint on 'Option', fields ['value', 'key']
        try:
            db.delete_unique('sentry_option', ['value', 'key'])
        except Exception:
            pass

        # Adding unique constraint on 'ProjectOption', fields ['project', 'key']
        try:
            db.create_unique('sentry_projectoptions', ['project_id', 'key'])
        except Exception:
            pass

    def backwards(self, orm):

        # Removing unique constraint on 'ProjectOption', fields ['project', 'key']
        db.delete_unique('sentry_projectoptions', ['project_id', 'key'])

        # Adding unique constraint on 'Option', fields ['value', 'key']
        db.create_unique('sentry_option', ['value', 'key'])

        # Adding unique constraint on 'GroupMeta', fields ['group', 'value', 'key']
        db.create_unique('sentry_groupmeta', ['group_id', 'value', 'key'])

        # Adding unique constraint on 'ProjectOption', fields ['project', 'value', 'key']
        db.create_unique('sentry_projectoptions', ['project_id', 'value', 'key'])

    models = {
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
        'contenttypes.contenttype': {
            'Meta': {
                'ordering': "('name',)",
                'unique_together': "(('app_label', 'model'),)",
                'object_name': 'ContentType',
                'db_table': "'django_content_type'"
            },
            'app_label': ('django.db.models.fields.CharField', [], {
                'max_length': '100'
            }),
            'id':
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
        'sentry.event': {
            'Meta': {
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
                    'unique': 'True',
                    'null': 'True',
                    'db_column': "'message_id'"
                }
            ),
            'group': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'blank': 'True',
                    'related_name': "'event_set'",
                    'null': 'True',
                    'to': "orm['sentry.Group']"
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
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': "orm['sentry.Project']",
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
            'time_spent': ('django.db.models.fields.FloatField', [], {
                'null': 'True'
            })
        },
        'sentry.filtervalue': {
            'Meta': {
                'unique_together': "(('project', 'key', 'value'),)",
                'object_name': 'FilterValue'
            },
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'key': ('django.db.models.fields.CharField', [], {
                'max_length': '32'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': "orm['sentry.Project']",
                    'null': 'True'
                }
            ),
            'value': ('django.db.models.fields.CharField', [], {
                'max_length': '200'
            })
        },
        'sentry.group': {
            'Meta': {
                'unique_together': "(('project', 'logger', 'culprit', 'checksum'),)",
                'object_name': 'Group',
                'db_table': "'sentry_groupedmessage'"
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
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': "orm['sentry.Project']",
                    'null': 'True'
                }
            ),
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
            'time_spent_total': ('django.db.models.fields.FloatField', [], {
                'default': '0'
            }),
            'times_seen': (
                'django.db.models.fields.PositiveIntegerField', [], {
                    'default': '1',
                    'db_index': 'True'
                }
            ),
            'views': (
                'django.db.models.fields.related.ManyToManyField', [], {
                    'to': "orm['sentry.View']",
                    'symmetrical': 'False',
                    'blank': 'True'
                }
            )
        },
        'sentry.groupbookmark': {
            'Meta': {
                'unique_together': "(('project', 'user', 'group'),)",
                'object_name': 'GroupBookmark'
            },
            'group': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'bookmark_set'",
                    'to': "orm['sentry.Group']"
                }
            ),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'bookmark_set'",
                    'to': "orm['sentry.Project']"
                }
            ),
            'user': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'bookmark_set'",
                    'to': "orm['sentry.User']"
                }
            )
        },
        'sentry.groupmeta': {
            'Meta': {
                'unique_together': "(('group', 'key'),)",
                'object_name': 'GroupMeta'
            },
            'group':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': "orm['sentry.Group']"
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
        'sentry.messagecountbyminute': {
            'Meta': {
                'unique_together': "(('project', 'group', 'date'),)",
                'object_name': 'MessageCountByMinute'
            },
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'group':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': "orm['sentry.Group']"
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'to': "orm['sentry.Project']",
                    'null': 'True'
                }
            ),
            'time_spent_count': ('django.db.models.fields.IntegerField', [], {
                'default': '0'
            }),
            'time_spent_total': ('django.db.models.fields.FloatField', [], {
                'default': '0'
            }),
            'times_seen': ('django.db.models.fields.PositiveIntegerField', [], {
                'default': '0'
            })
        },
        'sentry.messagefiltervalue': {
            'Meta': {
                'unique_together': "(('project', 'key', 'value', 'group'),)",
                'object_name': 'MessageFilterValue'
            },
            'group':
            ('sentry.db.models.fields.FlexibleForeignKey', [], {
                'to': "orm['sentry.Group']"
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
                    'to': "orm['sentry.Project']",
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
        'sentry.messageindex': {
            'Meta': {
                'unique_together': "(('column', 'value', 'object_id'),)",
                'object_name': 'MessageIndex'
            },
            'column': ('django.db.models.fields.CharField', [], {
                'max_length': '32'
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'value': ('django.db.models.fields.CharField', [], {
                'max_length': '128'
            })
        },
        'sentry.option': {
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
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'sentry.project': {
            'Meta': {
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
                    'related_name': "'owned_project_set'",
                    'null': 'True',
                    'to': "orm['sentry.User']"
                }
            ),
            'public': ('django.db.models.fields.BooleanField', [], {
                'default': 'False'
            }),
            'status': (
                'django.db.models.fields.PositiveIntegerField', [], {
                    'default': '0',
                    'db_index': 'True'
                }
            )
        },
        'sentry.projectdomain': {
            'Meta': {
                'unique_together': "(('project', 'domain'),)",
                'object_name': 'ProjectDomain'
            },
            'domain': ('django.db.models.fields.CharField', [], {
                'max_length': '128'
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'domain_set'",
                    'to': "orm['sentry.Project']"
                }
            )
        },
        'sentry.projectmember': {
            'Meta': {
                'unique_together': "(('project', 'user'),)",
                'object_name': 'ProjectMember'
            },
            'date_added':
            ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime.now'
            }),
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'project': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'member_set'",
                    'to': "orm['sentry.Project']"
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
            'type': ('django.db.models.fields.IntegerField', [], {
                'default': '0'
            }),
            'user': (
                'sentry.db.models.fields.FlexibleForeignKey', [], {
                    'related_name': "'project_set'",
                    'to': "orm['sentry.User']"
                }
            )
        },
        'sentry.projectoption': {
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
                'to': "orm['sentry.Project']"
            }),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'sentry.view': {
            'Meta': {
                'object_name': 'View'
            },
            'id':
            ('sentry.db.models.fields.bounded.BoundedBigAutoField', [], {
                'primary_key': 'True'
            }),
            'path':
            ('django.db.models.fields.CharField', [], {
                'unique': 'True',
                'max_length': '100'
            }),
            'verbose_name':
            ('django.db.models.fields.CharField', [], {
                'max_length': '200',
                'null': 'True'
            }),
            'verbose_name_plural':
            ('django.db.models.fields.CharField', [], {
                'max_length': '200',
                'null': 'True'
            })
        }
    }

    complete_apps = ['sentry']
