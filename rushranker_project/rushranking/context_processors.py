# context_processors.py

from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from rushranking.models import Brother,Rushee,Comment
from rushranking.forms import RusheeForm,CommentForm,UserForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def default(request):

   # you can declare any variable that you would like and pass
   # them as a dictionary to be added to each template's context like so:
   rushee_list=Rushee.objects.order_by('-score')
   for r in rushee_list:
      r.url=r.id
   comment_list=Comment.objects.order_by('-time')[:5]
   return dict(rushees=rushee_list,comments=comment_list)