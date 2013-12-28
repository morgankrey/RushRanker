from django.db import models

class Brother(models.Model):
   firstName = models.CharField(max_length=128, unique=True)
   lastName = models.CharField(max_length=128, unique=True)

   def __unicode__(self):
      return str(self.firstName)+" "+str(self.lastName)

class Comment(models.Model):
   text = models.CharField(max_length=1000)
   brother = models.OneToOneField(Brother)

   def __unicode__(self):
      return self.text

class Rushee(models.Model):
   firstName = models.CharField(max_length=128, unique=True)
   lastName = models.CharField(max_length=128, unique=True)
   preferredName = models.CharField(max_length=128, unique=True)
   hometown = models.CharField(max_length=128, unique=True, null=True)
   highSchool = models.CharField(max_length=128, unique=True,null=True)
   grade = models.CharField(max_length=128, unique=True,null=True)
   score = models.IntegerField(default=0)
   comment = models.ForeignKey(Comment)

   def __unicode__(self):
      return str(self.firstName)+" "+str(self.lastName)