from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rushranking.models import Brother,Rushee,Comment
from rushranking.forms import RusheeForm,CommentForm

def index(request):
   #request context of the request
   #context contains information about client, status, etc.
   context = RequestContext(request)

   #construct dict to pass to template engine as its context
   rushee_list = Rushee.objects.order_by('-score')[:5]
   context_dict = {'rushees': rushee_list}

   for rushee in rushee_list:
      rushee.url = rushee.id

   #Return a rendered response to send to the client
   #Make use of a shortcut function to simplify
   #note that first parameter is template we want to use
   return render_to_response('rushranking/index.html',context_dict,context)


def about(request):
   context=RequestContext(request)
   context_dict = {'strongmessage' : "Rush started yesterday"}
   return render_to_response('rushranking/about.html',context_dict,context)

def rushee(request,rushee_id):
   context=RequestContext(request)
   context_dict={'rushee_id':rushee_id}

   try:
      # Can we find a rushee with the given id?
      # If we can't, the .get() method raises a DoesNotExist exception.
      # So the .get() method returns one model instance or raises an exception.
      rushee = Rushee.objects.get(id=rushee_id)

      # Retrieve all of the associated comments.
      # Note that filter returns >= 1 model instance.
      comments = Comment.objects.filter(rushee=rushee)

      # Adds our results list to the template context under name pages.
      context_dict['comments']=comments
      # We also add the category object from the database to the context dictionary.
      # We'll use this in the template to verify that the category exists.
      context_dict['rushee']=rushee

   except Rushee.DoesNotExist:
      # We get here if we didn't find the specified category.
      # Don't do anything - the template displays the "no rushee" message for us.
      pass

   return render_to_response('rushranking/rushee.html',context_dict, context)

def add_rushee(request):
   context = RequestContext(request)
   if request.method=='POST':
      form=RusheeForm(request.POST)

      if form.is_valid():
         form.save(commit=True)
         return index(request)

      else:
         print form.errors
   else:
      form = RusheeForm()

   return render_to_response('rushranking/add_rushee.html',{'form':form},context)

def add_comment(request,rushee_id):
   context=RequestContext(request)
   context_dict={'rushee_id':rushee_id}

   try:
      rusheeObj = Rushee.objects.get(id=rushee_id)
      comments = Comment.objects.filter(rushee=rusheeObj)
      context_dict['comments']=comments
      context_dict['rushee']=rusheeObj
   except Rushee.DoesNotExist:
      pass

   if request.method=='POST':
      form=CommentForm(request.POST)

      if form.is_valid():
         comment = form.save(commit=False)
         comment.rushee=rusheeObj
         comment.save()
         return rushee(request,rushee_id)

      else:
         print form.errors
   else:
      form=CommentForm()

   return render_to_response('rushranking/add_comment.html',{'rushee_id':rushee_id,'form':form},context)







