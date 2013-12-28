import os

def populate():
   test_brother = add_Brother("Morgan","Krey")
   print 'Added brother'
   test_rushee1 = add_Rushee("Cole","Koeniguer",'',"Kansas City",'',"Freshman")
   test_comment1 = add_Comment("Kid sucks","MWK",test_rushee1)
   test_comment2 = add_Comment("BOOOO","MWK",test_rushee1)

   # Print out what we have added to the user.
   print "Brothers: "
   for b in Brother.objects.all():
      print "  {0} {1}".format(str(b.firstName), str(b.lastName))

   print "Rushees: "
   for r in Rushee.objects.all():
      print " {0} {1} ({2}), {3}, {4}, {5}".format(str(r.firstName),str(r.lastName),str(r.preferredName),str(r.hometown),str(r.highSchool),str(r.grade))

   print "Comments: "
   for c in Comment.objects.all():
      print "{0} about {1}: {2}".format(str(c.brotherInitials),str(c.rushee),str(c.text))

def add_Brother(fn,ln):
   b = Brother.objects.get_or_create(firstName=fn,
      lastName=ln)[0]
   return b

def add_Rushee(fn,ln,pn,home,hs,grd):
   r = Rushee.objects.get_or_create(firstName=fn,
      lastName=ln,
      preferredName=pn,
      hometown=home,
      highSchool=hs,
      grade=grd)[0]
   return r

def add_Comment(txt,bi,r):
   c = Comment.objects.get_or_create(text=txt,
      brotherInitials=bi,
      rushee=r)[0]
   return c

if __name__ == '__main__':
   print "Starting population script:"
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rushranker_project.settings')
   from rushranking.models import Brother,Rushee,Comment
   populate()