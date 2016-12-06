# -*- coding: utf-8 -*-
import logging

from google.appengine.ext import ndb

class Greeting(ndb.Model):
    no = ndb.StringProperty(indexed=True)
