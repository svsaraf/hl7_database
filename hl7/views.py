from django.shortcuts import render
from hl7.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
import hl7apy
from hl7apy.parser import parse_message

def index(request):
	context = RequestContext(request)
	if request.method=='POST':
		text = request.POST['hl7doc']
		m = parse_message(text,2,True)
		r = Record()
		r.msh_9 = m.msh.msh_9.to_er7()
		r.msh_10 = m.msh.msh_10.to_er7()
		r.msh_11 = m.msh.msh_11.to_er7()
		r.msh_12 = m.msh.msh_12.to_er7()
		r.pid_5 = m.pid.pid_5.to_er7()
		r.pid_11 = m.pid.pid_11.to_er7()
		r.evn_2 = m.evn.evn_2.to_er7()
		r.evn_4 = m.evn.evn_4.to_er7()
		r.save()
		return HttpResponseRedirect('/')

	records = Record.objects.all()
	return render_to_response('index.html', {'records': records}, context)

# Create your views here.
def recordview(request, num):
	context = RequestContext(request)
	record = Record.objects.get(pk=num)
	return render_to_response('recordview.html', {'record': record}, context)
