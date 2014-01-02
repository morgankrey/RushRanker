from django.db import models
from django.contrib.auth.models import User
from rushranker_project import settings

class Rushee(models.Model):
   firstName = models.CharField(max_length=128)
   lastName = models.CharField(max_length=128)
   preferredName = models.CharField(max_length=128,blank=True)
   hometown = models.CharField(max_length=128, blank=True)
   highSchool = models.CharField(max_length=128, blank=True)
   picture = models.ImageField(upload_to='settings.MEDIA_ROOT', default='settings.STATIC_PATH/chance.jpg')
   FRESHMAN='FR'
   SOPHOMORE='SO'
   JUNIOR='JR'
   GRADE_CHOICES=(
      (FRESHMAN,'Freshman'),
      (SOPHOMORE,'Sophomore'),
      (JUNIOR,"Junior"),
   )
   grade = models.CharField(max_length=2,
                           choices=GRADE_CHOICES,
                           null=True,
                           default=FRESHMAN)
   score = models.IntegerField(default=0)

   def __unicode__(self):
      return str(self.firstName)+" "+str(self.lastName)

class Brother(models.Model):
   user = models.OneToOneField(User)
   rusheeMet = models.ManyToManyField(Rushee,null=True)

   def __unicode__(self):
      return str(self.user.first_name)+" "+str(self.user.last_name)

class UserProfile(models.Model):
   user = models.OneToOneField(User)
   horse = models.ForeignKey(Rushee,null=True)
   horsedYet = models.BooleanField(default=False)

   def __unicode__(self):
      return str(self.user.first_name)+" "+str(self.user.last_name)

class Comment(models.Model):
   text = models.CharField(max_length=1000)
   brother = models.ForeignKey(User)
   rushee = models.ForeignKey(Rushee)
   time = models.DateTimeField(auto_now_add=True)

   def __unicode__(self):
      return self.text