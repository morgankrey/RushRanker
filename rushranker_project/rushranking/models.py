from django.db import models

class Brother(models.Model):
   firstName = models.CharField(max_length=128)
   lastName = models.CharField(max_length=128)

   def __unicode__(self):
      return str(self.firstName)+" "+str(self.lastName)

class Rushee(models.Model):
   firstName = models.CharField(max_length=128)
   lastName = models.CharField(max_length=128)
   preferredName = models.CharField(max_length=128,blank=True)
   hometown = models.CharField(max_length=128, blank=True)
   highSchool = models.CharField(max_length=128, blank=True)
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

class Comment(models.Model):
   text = models.CharField(max_length=1000)
   brotherInitials = models.CharField(max_length=3)
   rushee = models.ForeignKey(Rushee)

   def __unicode__(self):
      return self.text