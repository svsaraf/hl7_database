from django.shortcuts import render
from hl7.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from hl7apy.parser import parse_message

def index(request):
	context = RequestContext(request)
	if request.method=='POST':
		text = request.POST['hl7doc']
		message = parse_message(text,2,True)
		r = Record()
		r.msh_9 = message.msh.msh_9
    	r.msh_10 = message.msh.msh_10
    	r.msh_11 = message.msh.msh_11
    	r.msh_12 = message.msh.msh_12
    	r.pid_5 = message.pid.pid_5
    	r.pid_11 = message.pid.pid_11
        r.evn_2 = message.evn.evn_2
    	r.evn_4 = message.evn.evn_4
    	r.save()
		return HttpResponseRedirect('/')
	return render_to_response('index.html', {}, context)

# Create your views here.
