from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
   #return HttpResponse("Link to the about page: <a href='/rushranking/about/'>About</a>")

   #request context of the request
   #context contains information about client, status, etc.
   context = RequestContext(request)

   #construct dict to pass to template engine as its context
   #note key boldmessage is the same as {{ boldmessage }} in the template
   context_dict = {'boldmessage' : "I am the bold font from the context"}

   #Return a rendered response to send to the client
   #Make use of a shortcut function to simplify
   #note that first parameter is template we want to use
   return render_to_response('rushranking/index.html',context_dict,context)


def about(request):
   context=RequestContext(request)
   context_dict = {'strongmessage' : "Rush started yesterday"}
   return render_to_response('rushranking/about.html',context_dict,context)