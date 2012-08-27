from mongoengine import *

class Page (Document):
    
    name = StringField ()
    markup = StringField ()

