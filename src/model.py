# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Participant(db.Model):
    name = db.StringProperty()
    email = db.StringProperty()
