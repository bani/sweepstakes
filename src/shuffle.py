# -*- coding: utf-8 -*-

import logging
import cgi
import os
from random import shuffle
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from model import Participant


class Shuffle(webapp.RequestHandler):
    def get(self):
        people = db.GqlQuery("SELECT * FROM Participant").fetch(None)
        shuffle(people)
        path = os.path.join(os.path.dirname(__file__), 'shuffle.html')
        self.response.out.write(template.render(path, {'people': people}))

        
application = webapp.WSGIApplication(
                                     [('/shuffle', Shuffle),],
                                     debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
