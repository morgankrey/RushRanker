from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from rushranking.models import Brother,Rushee,Comment
from rushranking.forms import RusheeForm,CommentForm,UserForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def about(request):
   context=RequestContext(request)
   context_dict = {'strongmessage' : "Rush started yesterday"}
   return render_to_response('rushranking/about.html',context_dict,context)

@login_required
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

@login_required
def add_rushee(request):
   context = RequestContext(request)
   if request.method=='POST':
      form=RusheeForm(request.POST, request.FILES)

      if form.is_valid():
         r = form.save(commit=False)
         r.picture = request.FILES['picture']
         r.save()

         return rushee(request,r.id)

      else:
         print form.errors
   else:
      form = RusheeForm()

   return render_to_response('rushranking/add_rushee.html',{'form':form},context)

@login_required
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

@login_required
def register(request):
   context=RequestContext(request)
   registered = False

   if request.method=='POST':
      user_form = UserForm(data=request.POST)
      profile_form=UserProfileForm(data=request.POST)

      if user_form.is_valid():
         user = user_form.save()
         user.set_password(user.password)
         user.save()

         profile = profile_form.save(commit=False)
         profile.user = user
         profile.save()

         registered=True
      else:
         print user_form.errors, profile_form.errors

   else:
      user_form=UserForm()
      profile_form=UserProfileForm()

   return render_to_response('rushranking/register.html',{'user_form':user_form,'profile_form':profile_form, 'registered':registered},context)

def user_login(request):
   context=RequestContext(request)
   if request.method=='POST':
      username=request.POST['username']
      password=request.POST['password']

      user = authenticate(username=username,password=password)

      if user is not None:
         if user.is_active:
            login(request,user)
            return HttpResponseRedirect('/rushranking/')
         else:
            return HttpResponse('Your account was disabled')
      else:
         print "Invalid login details: {0} {1}".format(username,password)
         return HttpResponse("Invalid login details supplied")

   else:
      return render_to_response('rushranking/login.html',{},context)

@login_required
def user_logout(request):
   logout(request)
   return HttpResponseRedirect('/rushranking/')









