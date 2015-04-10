from django.shortcuts import render
from hl7.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
	context = RequestContext(request)
	if request.method=='POST':
		text = request.POST['hl7doc']
		doc = Document()
		msh = ComponentMSH()
		msh.doc = doc.docid
		msh.text = text
		doc.save()
		msh.save()
		return HttpResponseRedirect('/')
	return render_to_response('index.html', {}, context)

# Create your views here.
