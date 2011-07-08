# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Contact.required_initials'
        db.add_column('cmsplugin_contact', 'required_initials', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Contact.required_lastname'
        db.add_column('cmsplugin_contact', 'required_lastname', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Contact.required_abbreviation'
        db.add_column('cmsplugin_contact', 'required_abbreviation', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Contact.required_company'
        db.add_column('cmsplugin_contact', 'required_company', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Contact.required_function'
        db.add_column('cmsplugin_contact', 'required_function', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Contact.required_address'
        db.add_column('cmsplugin_contact', 'required_address', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Contact.required_zipcode'
        db.add_column('cmsplugin_contact', 'required_zipcode', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Contact.required_city'
        db.add_column('cmsplugin_contact', 'required_city', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Contact.required_phone'
        db.add_column('cmsplugin_contact', 'required_phone', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Contact.required_mobile_phone'
        db.add_column('cmsplugin_contact', 'required_mobile_phone', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Contact.required_email'
        db.add_column('cmsplugin_contact', 'required_email', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Contact.required_website'
        db.add_column('cmsplugin_contact', 'required_website', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Contact.required_initials'
        db.delete_column('cmsplugin_contact', 'required_initials')

        # Deleting field 'Contact.required_lastname'
        db.delete_column('cmsplugin_contact', 'required_lastname')

        # Deleting field 'Contact.required_abbreviation'
        db.delete_column('cmsplugin_contact', 'required_abbreviation')

        # Deleting field 'Contact.required_company'
        db.delete_column('cmsplugin_contact', 'required_company')

        # Deleting field 'Contact.required_function'
        db.delete_column('cmsplugin_contact', 'required_function')

        # Deleting field 'Contact.required_address'
        db.delete_column('cmsplugin_contact', 'required_address')

        # Deleting field 'Contact.required_zipcode'
        db.delete_column('cmsplugin_contact', 'required_zipcode')

        # Deleting field 'Contact.required_city'
        db.delete_column('cmsplugin_contact', 'required_city')

        # Deleting field 'Contact.required_phone'
        db.delete_column('cmsplugin_contact', 'required_phone')

        # Deleting field 'Contact.required_mobile_phone'
        db.delete_column('cmsplugin_contact', 'required_mobile_phone')

        # Deleting field 'Contact.required_email'
        db.delete_column('cmsplugin_contact', 'required_email')

        # Deleting field 'Contact.required_website'
        db.delete_column('cmsplugin_contact', 'required_website')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_contact.contact': {
            'Meta': {'object_name': 'Contact', 'db_table': "'cmsplugin_contact'", '_ormbases': ['cms.CMSPlugin']},
            'akismet_api_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'content_label': ('django.db.models.fields.CharField', [], {'default': "u'Message'", 'max_length': '100'}),
            'email_label': ('django.db.models.fields.CharField', [], {'default': "u'Your email address'", 'max_length': '100'}),
            'recaptcha_private_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'recaptcha_public_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'recaptcha_theme': ('django.db.models.fields.CharField', [], {'default': "'clean'", 'max_length': '20'}),
            'required_abbreviation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_address': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_city': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_company': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_function': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_initials': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_lastname': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_mobile_phone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_phone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_website': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_zipcode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'spam_protection_method': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'subject_label': ('django.db.models.fields.CharField', [], {'default': "u'Subject'", 'max_length': '200'}),
            'submit': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '30'}),
            'thanks': ('django.db.models.fields.TextField', [], {'default': "u'Thank you for your message.'", 'max_length': '200'})
        }
    }

    complete_apps = ['cmsplugin_contact']
