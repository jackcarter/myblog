# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'blog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'blog', ['Category'])

        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 12, 16, 0, 0))),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding model 'Comment'
        db.create_table(u'blog_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Post'])),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'blog', ['Comment'])

        # Adding model 'CategoryToPost'
        db.create_table(u'blog_categorytopost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Post'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Category'])),
        ))
        db.send_create_signal(u'blog', ['CategoryToPost'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'blog_category')

        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Deleting model 'Comment'
        db.delete_table(u'blog_comment')

        # Deleting model 'CategoryToPost'
        db.delete_table(u'blog_categorytopost')


    models = {
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'blog.categorytopost': {
            'Meta': {'object_name': 'CategoryToPost'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"})
        },
        u'blog.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['blog.Category']", 'null': 'True', 'through': u"orm['blog.CategoryToPost']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 12, 16, 0, 0)'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']