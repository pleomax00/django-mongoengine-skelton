from django.http import *
from django.shortcuts import *
from lib.modifiers import GenericView

class Index (GenericView):

    def GET (self, request):
        return render_to_response ("index.html", locals ())
