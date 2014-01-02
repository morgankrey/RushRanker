from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response,get_object_or_404
from rushranking.models import Brother,Rushee,Comment,UserProfile
from rushranking.forms import RusheeForm,CommentForm,UserForm,UserProfileForm,VoteForm,HorseForm,BrotherForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import random

@login_required
def index(request):
   #request context of the request
   #context contains information about client, status, etc.
   context = RequestContext(request)

   #construct dict to pass to template engine as its context
   topFive = Rushee.objects.order_by('-score')[:5]
   for rushee in topFive:
      rushee.url = rushee.id
   context_dict = {'topFive': topFive}

   brothers = UserProfile.objects.all()
   recentHorses=[]
   for brother in brothers:
      if brother.horse:
         brother.horse.url = brother.horse.id
         recentHorses.append(brother)
   context_dict['recentHorses']=recentHorses

   #Return a rendered response to send to the client
   #Make use of a shortcut function to simplify
   #note that first parameter is template we want to use
   context_instance=RequestContext(request)
   return render_to_response('rushranking/index.html',locals(),context_instance)

@login_required
def about(request):
   context=RequestContext(request)
   context_dict = {'strongmessage' : "Rush started yesterday"}
   context_instance=RequestContext(request)
   return render_to_response('rushranking/about.html',locals(),context_instance)

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

      brothers=UserProfile.objects.filter(horse=rushee)
      context_dict['brothers']=brothers
      brothersMet=Brother.objects.filter(rusheeMet=rushee)
      context_dict['brothersMet']=brothersMet

      canHorse = not UserProfile.objects.filter(user=request.user)
      context_dict['canHorse'] = canHorse
      alert = "You already have a horse"
      context_dict['alert'] = alert
      cameFromRushee=True
      context_dict['cameFromRushee']=cameFromRushee

   except Rushee.DoesNotExist:
      # We get here if we didn't find the specified category.
      # Don't do anything - the template displays the "no rushee" message for us.
      pass

   context_instance=RequestContext(request)
   return render_to_response('rushranking/rushee.html',locals(),context_instance)

@login_required
def rushees(request):
   context=RequestContext(request)
   rushee_list=Rushee.objects.order_by('lastName')
   context_dict={'rushee_list':rushee_list}
   return render_to_response('rushranking/rushees.html',locals(),context)

@login_required
def game(request):
   context=RequestContext(request)
   rushee_list=Rushee.objects.all()
   rushee_1=rushee_list[random.randint(0,len(rushee_list)-1)]
   rushee_2=rushee_list[random.randint(0,len(rushee_list)-1)]
   while(rushee_1.id == rushee_2.id):
      rushee_2=rushee_list[random.randint(0,len(rushee_list)-1)]
   context_dict={'rushee_1':rushee_1}
   context_dict['rushee_2']=rushee_2

   return render_to_response('rushranking/game.html',locals(),context)

def vote(request,rushee_id):
   context=RequestContext(request)
   if request.method=='POST':
      form=VoteForm(request.POST)
      if form.is_valid():
         r=Rushee.objects.get(id=rushee_id)
         r.score+=1
         r.save()
         return game(request)
      else:
         print form.errors
   else:
      form=VoteForm()

   context_dict={'form':form}
   return render_to_response('rushranking/game.html',locals(),context_instance)

@login_required
def add_rushee(request):
   context = RequestContext(request)
   if request.method=='POST':
      form=RusheeForm(request.POST, request.FILES)

      if form.is_valid():
         r = form.save(commit=False)
         if 'picture' in request.FILES:
            r.picture = request.FILES['picture']
         r.save()

         return rushee(request,r.id)

      else:
         print form.errors
   else:
      form = RusheeForm()

   context_instance=RequestContext(request)
   context_dict={'form':form}

   return render_to_response('rushranking/add_rushee.html',locals(),context_instance)

def edit_rushee(request,rushee_id):
   context=RequestContext(request)
   context_dict={'rushee_id':rushee_id}
   rusheeObj=Rushee.objects.get(id=rushee_id)
   if request.POST:
      form = RusheeForm(request.POST, instance=rusheeObj)
      if form.is_valid():
         r=form.save(commit=False)
         if 'picture' in request.FILES:
            r.picture = request.FILES['picture']
         r.save()
         return rushee(request,rushee_id)
      else:
         print form.errors
   else:
      form=RusheeForm(instance=rusheeObj)

   context_dict['form']=form
   context_dict['rushee']=rusheeObj
   return render_to_response('rushranking/edit_rushee.html',locals(),context)

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
         comment.brother=request.user
         comment.save()
         return rushee(request,rushee_id)

      else:
         print form.errors
   else:
      form=CommentForm()

   context_instance=RequestContext(request)
   context_dict={'rushee_id':rushee_id,'form':form}
   return render_to_response('rushranking/add_comment.html',locals(),context_instance)

@login_required
def register(request):
   context=RequestContext(request)
   registered = False

   if request.method=='POST':
      user_form = UserForm(data=request.POST)
      profile_form=UserProfileForm(data=request.POST)
      brother_form = BrotherForm(data=request.POST)

      if user_form.is_valid():
         user = user_form.save()
         user.set_password(user.password)
         user.save()

         profile = profile_form.save(commit=False)
         profile.user = user
         profile.save()

         brother = brother_form.save(commit=False)
         brother.user = user
         brother.save()

         registered=True
      else:
         print user_form.errors, profile_form.errors

   else:
      user_form=UserForm()
      profile_form=UserProfileForm()

   context_instance=RequestContext(request)
   context_dict={'user_form':user_form,'profile_form':profile_form, 'registered':registered}
   return render_to_response('rushranking/register.html',locals(),context_instance)

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
      context_instance=RequestContext(request)
      return render_to_response('rushranking/login.html',locals(),context_instance)

@login_required
def horse(request,rushee_id):
   context=RequestContext(request)
   context_dict={'rushee_id':rushee_id}

   rusheeObj=Rushee.objects.get(id=rushee_id)
   context_dict['rushee']=rusheeObj

   profile = UserProfile.objects.get(user=request.user)
   context_dict['profile']=profile

   brothers = UserProfile.objects.filter(horse=rusheeObj)
   context_dict['brothers']=brothers

   canHorse = True
   context_dict['canHorse'] = canHorse
   alert = "You already have a horse"
   context_dict['alert'] = alert
   cameFromRushee=False
   context_dict['cameFromRushee']=cameFromRushee

   if request.method=='POST':
      profile_form=HorseForm(request.POST,instance=profile)

      if profile_form.is_valid():
         profile = profile_form.save(commit=False)
         if profile.horsedYet==False:
            profile.user = request.user
            profile.horse = rusheeObj
            profile.horsedYet = True
            profile.save()
            return rushee(request,rusheeObj.id)
         else:
            canHorse=False
            return rushee(request,rusheeObj.id)

      else:
         print profile_form.errors
   else:
      profile_form=HorseForm()

   context_instance=RequestContext(request)
   context_dict={'rushee_id':rushee_id,'form':profile_form,'brothers':brothers,'rushee':rusheeObj}
   return render_to_response('rushranking/rushee.html',locals(),context_instance)

@login_required
def brotherMet(request,rushee_id):
   context=RequestContext(request)
   context_dict={'rushee_id':rushee_id}

   rusheeObj=Rushee.objects.get(id=rushee_id)
   context_dict['rushee']=rusheeObj

   brother = Brother.objects.get(user=request.user)
   context_dict['brother']=brother

   brothersMet = Brother.objects.filter(rusheeMet=rusheeObj)
   context_dict['brothersMet']=brothersMet

   if request.method=='POST':
      brother_form=BrotherForm(request.POST,instance=brother)

      if brother_form.is_valid():
         brother = brother_form.save(commit=False)
         brother.user = request.user
         brother.rusheeMet = rusheeObj
         brother.save()
         return rushee(request,rusheeObj.id)
      else:
         print brother_form.errors

   else:
      brother_form=BrotherForm()

   context_instance=RequestContext(request)
   context_dict={'rushee_id':rushee_id,'form':brother_form}
   return render_to_response('rushranking/rushee.html',locals(),context_instance)

@login_required
def user_logout(request):
   logout(request)
   return HttpResponseRedirect('/rushranking/')









