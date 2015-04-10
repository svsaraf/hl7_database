from django.shortcuts import render
from hl7.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
	context = RequestContext(request)
	return render_to_response('index.html', {}, context)

# Create your views here.
