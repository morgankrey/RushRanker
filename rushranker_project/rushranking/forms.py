from django import forms
from rushranking.models import Brother,Rushee,Comment

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

   class Meta:
      model = Rushee

class CommentForm(forms.ModelForm):
   class Meta:
      model = Comment
      fields = ('text','brotherInitials')

   text = forms.CharField(max_length=20,help_text="Comment: ")
   brotherInitials = forms.CharField(max_length=3,help_text="Brother Initials: ")