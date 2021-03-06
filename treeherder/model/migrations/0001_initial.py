# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'model', ['Product'])

        # Adding model 'BuildPlatform'
        db.create_table(u'build_platform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('os_name', self.gf('django.db.models.fields.CharField')(max_length=25L)),
            ('platform', self.gf('django.db.models.fields.CharField')(max_length=25L)),
            ('architecture', self.gf('django.db.models.fields.CharField')(max_length=25L, blank=True)),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'model', ['BuildPlatform'])

        # Adding model 'Option'
        db.create_table(u'option', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'model', ['Option'])

        # Adding model 'RepositoryGroup'
        db.create_table(u'repository_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'model', ['RepositoryGroup'])

        # Adding model 'Repository'
        db.create_table(u'repository', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('repository_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['model.RepositoryGroup'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('dvcs_type', self.gf('django.db.models.fields.CharField')(max_length=25L)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('codebase', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'model', ['Repository'])

        # Adding model 'MachinePlatform'
        db.create_table(u'machine_platform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('os_name', self.gf('django.db.models.fields.CharField')(max_length=25L)),
            ('platform', self.gf('django.db.models.fields.CharField')(max_length=25L)),
            ('architecture', self.gf('django.db.models.fields.CharField')(max_length=25L, blank=True)),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'model', ['MachinePlatform'])

        # Adding model 'Bugscache'
        db.create_table(u'bugscache', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=64L, blank=True)),
            ('resolution', self.gf('django.db.models.fields.CharField')(max_length=64L, blank=True)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('crash_signature', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('os', self.gf('django.db.models.fields.CharField')(max_length=64L, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'model', ['Bugscache'])

        # Adding model 'Machine'
        db.create_table(u'machine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('first_timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('last_timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'model', ['Machine'])

        # Adding model 'MachineNote'
        db.create_table(u'machine_note', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('machine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['model.Machine'])),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('machine_timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'model', ['MachineNote'])

        # Adding model 'Datasource'
        db.create_table(u'datasource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=25L)),
            ('contenttype', self.gf('django.db.models.fields.CharField')(max_length=25L)),
            ('dataset', self.gf('django.db.models.fields.IntegerField')()),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=128L)),
            ('read_only_host', self.gf('django.db.models.fields.CharField')(max_length=128L, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128L)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=25L)),
            ('oauth_consumer_key', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('oauth_consumer_secret', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('cron_batch', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
        ))
        db.send_create_signal(u'model', ['Datasource'])

        # Adding model 'JobGroup'
        db.create_table(u'job_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'model', ['JobGroup'])

        # Adding model 'RepositoryVersion'
        db.create_table(u'repository_version', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('repository', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['model.Repository'])),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('version_timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'model', ['RepositoryVersion'])

        # Adding model 'OptionCollection'
        db.create_table(u'option_collection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['model.Option'])),
            ('option_collection_hash', self.gf('django.db.models.fields.CharField')(max_length=40L)),
        ))
        db.send_create_signal(u'model', ['OptionCollection'])

        # Adding model 'JobType'
        db.create_table(u'job_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['model.JobGroup'], null=True, blank=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'model', ['JobType'])

        # Adding model 'FailureClassification'
        db.create_table(u'failure_classification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active_status', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'model', ['FailureClassification'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'product')

        # Deleting model 'BuildPlatform'
        db.delete_table(u'build_platform')

        # Deleting model 'Option'
        db.delete_table(u'option')

        # Deleting model 'RepositoryGroup'
        db.delete_table(u'repository_group')

        # Deleting model 'Repository'
        db.delete_table(u'repository')

        # Deleting model 'MachinePlatform'
        db.delete_table(u'machine_platform')

        # Deleting model 'Bugscache'
        db.delete_table(u'bugscache')

        # Deleting model 'Machine'
        db.delete_table(u'machine')

        # Deleting model 'MachineNote'
        db.delete_table(u'machine_note')

        # Deleting model 'Datasource'
        db.delete_table(u'datasource')

        # Deleting model 'JobGroup'
        db.delete_table(u'job_group')

        # Deleting model 'RepositoryVersion'
        db.delete_table(u'repository_version')

        # Deleting model 'OptionCollection'
        db.delete_table(u'option_collection')

        # Deleting model 'JobType'
        db.delete_table(u'job_type')

        # Deleting model 'FailureClassification'
        db.delete_table(u'failure_classification')


    models = {
        u'model.bugscache': {
            'Meta': {'object_name': 'Bugscache', 'db_table': "u'bugscache'"},
            'crash_signature': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'blank': 'True'}),
            'resolution': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255L'})
        },
        u'model.buildplatform': {
            'Meta': {'object_name': 'BuildPlatform', 'db_table': "u'build_platform'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'architecture': ('django.db.models.fields.CharField', [], {'max_length': '25L', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'os_name': ('django.db.models.fields.CharField', [], {'max_length': '25L'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '25L'})
        },
        u'model.datasource': {
            'Meta': {'object_name': 'Datasource', 'db_table': "u'datasource'"},
            'contenttype': ('django.db.models.fields.CharField', [], {'max_length': '25L'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'cron_batch': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'dataset': ('django.db.models.fields.IntegerField', [], {}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'oauth_consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'oauth_consumer_secret': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '25L'}),
            'read_only_host': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25L'})
        },
        u'model.failureclassification': {
            'Meta': {'object_name': 'FailureClassification', 'db_table': "u'failure_classification'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'model.jobgroup': {
            'Meta': {'object_name': 'JobGroup', 'db_table': "u'job_group'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10L'})
        },
        u'model.jobtype': {
            'Meta': {'object_name': 'JobType', 'db_table': "u'job_type'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['model.JobGroup']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10L'})
        },
        u'model.machine': {
            'Meta': {'object_name': 'Machine', 'db_table': "u'machine'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'first_timestamp': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_timestamp': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'model.machinenote': {
            'Meta': {'object_name': 'MachineNote', 'db_table': "u'machine_note'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['model.Machine']"}),
            'machine_timestamp': ('django.db.models.fields.IntegerField', [], {}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'model.machineplatform': {
            'Meta': {'object_name': 'MachinePlatform', 'db_table': "u'machine_platform'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'architecture': ('django.db.models.fields.CharField', [], {'max_length': '25L', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'os_name': ('django.db.models.fields.CharField', [], {'max_length': '25L'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '25L'})
        },
        u'model.option': {
            'Meta': {'object_name': 'Option', 'db_table': "u'option'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'model.optioncollection': {
            'Meta': {'object_name': 'OptionCollection', 'db_table': "u'option_collection'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['model.Option']"}),
            'option_collection_hash': ('django.db.models.fields.CharField', [], {'max_length': '40L',})
        },
        u'model.product': {
            'Meta': {'object_name': 'Product', 'db_table': "u'product'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'model.repository': {
            'Meta': {'object_name': 'Repository', 'db_table': "u'repository'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'codebase': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'repository_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['model.RepositoryGroup']"}),
            'dvcs_type': ('django.db.models.fields.CharField', [], {'max_length': '25L'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255L'})
        },
        u'model.repositorygroup': {
            'Meta': {'object_name': 'RepositoryGroup', 'db_table': "u'repository_group'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'model.repositoryversion': {
            'Meta': {'object_name': 'RepositoryVersion', 'db_table': "u'repository_version'"},
            'active_status': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['model.Repository']"}),
            'version_timestamp': ('django.db.models.fields.IntegerField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        }
    }

    complete_apps = ['model']
