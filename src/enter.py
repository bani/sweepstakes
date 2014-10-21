# -*- coding: utf-8 -*-

import cgi
import logging
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from model import Participant

class Enter(webapp.RequestHandler):
    """Inserts a new person in the database"""
    def get(self):
        name = cgi.escape(self.request.get('name'))
        email = cgi.escape(self.request.get('email'))

        exists = db.GqlQuery("SELECT * FROM Participant WHERE email = :1", email).count(1)
        if not exists:
            logging.info("Adding %s"  % (email))
            participant = Participant(email=email, name=name)
            participant.put()
            self.redirect("/success")
        else:
            self.redirect("/error")

application = webapp.WSGIApplication(
                                     [('/enter', Enter),],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
