# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'FacebookInviteRequest'
        db.delete_table('canvas_facebookinviterequest')

        # Adding field 'FacebookUser.email'
        db.add_column('canvas_facebookuser', 'email', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'FacebookUser.first_name'
        db.add_column('canvas_facebookuser', 'first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'FacebookUser.last_name'
        db.add_column('canvas_facebookuser', 'last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Changing field 'FacebookUser.user'
        db.alter_column('canvas_facebookuser', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True))


    def backwards(self, orm):
        
        # Adding model 'FacebookInviteRequest'
        db.create_table('canvas_facebookinviterequest', (
            ('fb_uid', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('canvas', ['FacebookInviteRequest'])

        # Deleting field 'FacebookUser.email'
        db.delete_column('canvas_facebookuser', 'email')

        # Deleting field 'FacebookUser.first_name'
        db.delete_column('canvas_facebookuser', 'first_name')

        # Deleting field 'FacebookUser.last_name'
        db.delete_column('canvas_facebookuser', 'last_name')

        # Changing field 'FacebookUser.user'
        db.alter_column('canvas_facebookuser', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'canvas.comment': {
            'Meta': {'object_name': 'Comment'},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'default': "'0.0.0.0'", 'max_length': '15'}),
            'parent_content': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comments'", 'null': 'True', 'to': "orm['canvas.Content']"}),
            'replied_comment': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['canvas.Comment']", 'null': 'True', 'blank': 'True'}),
            'reply_content': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'used_in_comments'", 'null': 'True', 'to': "orm['canvas.Content']"}),
            'reply_text': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.FloatField', [], {}),
            'visibility': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'canvas.content': {
            'Meta': {'object_name': 'Content'},
            'alpha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'animated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'default': "'0.0.0.0'", 'max_length': '15'}),
            'remix_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'remixes'", 'null': 'True', 'to': "orm['canvas.Content']"}),
            'score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'stamps_used': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'used_as_stamp'", 'blank': 'True', 'to': "orm['canvas.Content']"}),
            'timestamp': ('django.db.models.fields.FloatField', [], {}),
            'url_mapping': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canvas.ContentUrlMapping']", 'null': 'True', 'blank': 'True'}),
            'visibility': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'canvas.contentsticker': {
            'Meta': {'object_name': 'ContentSticker'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stickers'", 'to': "orm['canvas.Content']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'timestamp': ('django.db.models.fields.FloatField', [], {}),
            'type_id': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'canvas.contenturlmapping': {
            'Meta': {'object_name': 'ContentUrlMapping'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'canvas.facebookuser': {
            'Meta': {'object_name': 'FacebookUser'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fb_uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'canvas.invitecode': {
            'Meta': {'object_name': 'InviteCode'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitee': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'canvas.stashcontent': {
            'Meta': {'object_name': 'StashContent'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canvas.Content']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'canvas.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'free_invites': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_anonymously': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['canvas']
