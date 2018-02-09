# -*- coding: utf-8 -*-
from logging import basicConfig, getLogger, DEBUG

from google.appengine.ext import ndb

basicConfig(level=DEBUG)
logger = getLogger(__name__)


class MyUser(ndb.Model):
    id = ndb.StringProperty(indexed=False, default='')
    name = ndb.StringProperty(indexed=False, default='')


class Class(ndb.Model):
    id = ndb.StringProperty(indexed=False, default='')
    name = ndb.StringProperty(indexed=False, default='')
	users = ndb.StructuredProperty(MyUser, indexed=False, repeated=True)

	@classmethod
	def get_by_id(cls, id):
		key = ndb.Key(cls, "%s_sufix" % str(id))
		entity = key.get()
		if entity:
			logger.info('Get Class: %r ' % id)
			return entity
		else:
			logger.info('Create Class: %r ' % id)
			return cls(key=key, profile=Profile())

	@classmethod
	def update(cls, class_info):
		_id = class_info.get('id')
		entity = cls.get_by_id(_id)
		entity.populate(
			id='id',
			name='name',
			users=MyUser(
				id='user_id',
				name='user_name',
			)
		)
		entity.put()
		logger.info('Update Class: %r ' % _id)
		return entity

	@classmethod
	def delete(cls, class_info):
		_id = class_info.get('id')
		key = cls.key_from_id(id)
		logger.info('Delete Class: %r ' % _id)
		return key.delete()
