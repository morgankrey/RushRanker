import os

def populate():
   python_Krey = add_Brother("Morgan","Krey")

   # Print out what we have added to the user.
   print "Brothers: "
   for b in Brother.objects.all():
      print "  {0} {1}".format(str(b.firstName), str(b.lastName))

def add_Brother(fn,ln):
   b = Brother.objects.get_or_create(firstName=fn,lastName=ln)[0]
   return b

if __name__ == '__main__':
   print "Starting population script:"
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rushranker_project.settings')
   from rushranking.models import Brother
   populate()