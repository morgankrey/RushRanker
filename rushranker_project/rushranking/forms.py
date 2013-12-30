from django import forms
from rushranker_project import settings
from rushranking.models import Brother,Rushee,Comment,UserProfile
from django.contrib.auth.models import User

class RusheeForm(forms.ModelForm):
   FRESHMAN='FR'
   SOPHOMORE='SO'
   JUNIOR='JR'
   GRADE_CHOICES=((FRESHMAN,'Freshman'),(SOPHOMORE,'Sophomore'),(JUNIOR,"Junior"),)
   firstName = forms.CharField(max_length=128,help_text = "First name: ")
   lastName = forms.CharField(max_length=128,help_text = "Last name: ")
   preferredName = forms.CharField(max_length=128,help_text = "Preferred name: ",required=False)
   hometown = forms.CharField(max_length=128,help_text = "Hometown: ",required=False)
   highSchool = forms.CharField(max_length=128,help_text = "High School: ",required=False)
   grade = forms.ChoiceField(help_text = "Grade: ",choices=GRADE_CHOICES)
   score = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
   picture = forms.ImageField(required=False)

   class Meta:
      model = Rushee

class CommentForm(forms.ModelForm):
   text = forms.CharField(max_length=500,help_text="Comment: ")

   class Meta:
      model = Comment
      fields = ('text',)

class UserForm(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput())

   class Meta:
      model = User
      fields = ('username','first_name', 'last_name', 'email', 'password')

class UserProfileForm(forms.ModelForm):
   class Meta:
      model = UserProfile
      fields = {}

class VoteForm(forms.ModelForm):
   class Meta:
      model=Rushee
      fields={}