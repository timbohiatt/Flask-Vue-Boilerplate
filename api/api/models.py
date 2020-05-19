# api/models.py
from datetime import datetime, timedelta
from hashlib import md5
from flask import current_app as app
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
from sqlalchemy import func
from sqlalchemy.ext.declarative import declared_attr
from werkzeug.security import generate_password_hash, check_password_hash
from api import db, ma, login
from decimal import Decimal
import base64, os, random


class SearchableMixin(object):
	@classmethod
	def search(cls, expression, page, per_page):
		ids, total = query_index(cls.__tablename__, expression, page, per_page)
		if total == 0:
			return cls.query.filter_by(id=0), 0
		when = []
		for i in range(len(ids)):
			when.append((ids[i], i))
		return cls.query.filter(cls.id.in_(ids)).order_by(
			db.case(when, value=cls.id)), total

	@classmethod
	def before_commit(cls, session):
		# print("Committing")
		session._changes = {
			'add': list(session.new),
			'update': list(session.dirty),
			'delete': list(session.deleted)
		}

	@classmethod
	def after_commit(cls, session):
		for obj in session._changes['add']:
			if isinstance(obj, SearchableMixin):
				add_to_index(obj.__tablename__, obj)
		for obj in session._changes['update']:
			if isinstance(obj, SearchableMixin):
				add_to_index(obj.__tablename__, obj)
		for obj in session._changes['delete']:
			if isinstance(obj, SearchableMixin):
				remove_from_index(obj.__tablename__, obj)
		session._changes = None

	@classmethod
	def reindex(cls):
		for obj in cls.query:
			add_to_index(cls.__tablename__, obj)


db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)


class PaginatedAPIMixin(object):
	@staticmethod
	def to_collection_dict(query, page, per_page, endpoint, **kwargs):
		resources = query.paginate(page, per_page, False)
		data = {
			'items': [item.to_dict() for item in resources.items],
			'_meta': {
				'page': page,
				'per_page': per_page,
				'total_pages': resources.pages,
				'total_items': resources.total
			},
			'_links': {
				'self': url_for(endpoint, page=page, per_page=per_page,
								**kwargs),
				'next': url_for(endpoint, page=page + 1, per_page=per_page,
								**kwargs) if resources.has_next else None,
				'prev': url_for(endpoint, page=page - 1, per_page=per_page,
								**kwargs) if resources.has_prev else None
			}
		}
		return data

class CoreMixin(object):

	@declared_attr
	def __tablename__(cls):
		return cls.__name__.lower()

	__mapper_args__= {'always_refresh': True}

	# CORE ID COLUMN 
	ID = db.Column(db.Integer, primary_key=True)  # Table Row ID
	# SYSTEM COLUMNS META DATA
	sys_active = db.Column(db.Boolean, default=True)
	sys_created = db.Column(db.DateTime, default=datetime.utcnow)
	sys_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

	#Mixin Functions
	@classmethod
	def get_by_id(self, vID=None):
		return self.query.filter(self.ID == vID).first()
	@classmethod
	def get_active_by_id(self, vID=None):
		return self.query.filter(self.ID == vID, self.sys_active==True).first()
	
	def set_inactive(self):
		self.sys_active = False
		return self
	
	def set_active(self):
		self.sys_active = True
		return self


'''
--------------------------------------------------------------------------------------------------------
	Table:          user  
	Class:          User
	Description:    TEMPLATE DESCRIPTION
--------------------------------------------------------------------------------------------------------
'''
class User(CoreMixin, db.Model):
	Username = db.Column(db.String(30))
	FirstName = db.Column(db.String(300))
	LastName = db.Column(db.String(300))
	Email = db.Column(db.String(300))

