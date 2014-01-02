import os

def populate():
   test_rushee1 = add_Rushee("Cole","Koeniguer",'',"Kansas City",'',"Freshman")
   test_user1 = add_User('mkrey','morgankrey@gmail.com','Morgan','Krey','Djgonzo1')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('jbejany','','Joe','Bejany','kI2WxbU')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('kbennert','','Kevin','Bennert','SrhGpZS')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('bbernstein','','Brendan','Bernstein','jtdjlbf')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('wboeckman','','Will','Boeckman','bXg5g25')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('cbrown','','Chris','Brown','i2aU5Wc')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('dbrown','','Dylan','Brown','hzJhJHX')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('wbyers','','Welby','Byers','iTFQ3KB')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('scameron','','Stephen','Cameron','xV4fwTA')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('bcarney','','Brooks','Carney','xHJnnJA')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('mcogo','','Michael','Cogo','CPmDRHW')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('gcooper','','Griffin','Cooper','x0rkubX')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('jcooper','','Jake','Cooper','EPrYG94')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('ddorchuck','','Daniel','Dorchuck','lYkO15h')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('jdyslin','','Jordan','Dyslin','02HDrRP')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('mfindlay','','Mac','Findlay','Y9lsE2w')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('lfisher','','Lucas','Fisher','f8VUf3z')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('ifraynd','','Isaac','Fraynd','t7iaCFQ')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('tgarrambone','','Thomas','Garrambone','5fnB8P4')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('sgasparini','','Steve','Gasparini','6ZE9V0Y')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)
   test_user1 = add_User('agersovitz','','Alex','Gersovitz','EkOCec9')
   test_profile1 = add_Profile(test_user1)
   test_brother1 = add_Brother(test_user1)


   test_comment1 = add_Comment("Kid sucks",test_user1,test_rushee1)
   test_comment2 = add_Comment("BOOOO",test_user1,test_rushee1)
   add_Rushee('Matt','Harper','','','','')
   add_Rushee('Michael','Schaffer','','','','')
   add_Rushee('Andrew','Smith','','','','')
   add_Rushee('Kyle','Wellner','','','','')
   add_Rushee('Tripp','Hostedder','','','','')
   add_Rushee('Will','Burns','','','','')
   add_Rushee('Teddy','Henderson','','','','')
   add_Rushee('Davis','English','','','','')
   add_Rushee('Parker','Fox','','','','')
   add_Rushee('Vinny','Fry','','','','')
   add_Rushee('Cameron','Simpson','','','','')
   add_Rushee('Ben','Taylor','','','','')
   add_Rushee('David','Soled','','','','')
   add_Rushee('Nathaniel','Sizemore','','','','')
   add_Rushee('Chase','Moyle','','','','')
   add_Rushee('Osuma','Ayogu','','','','')
   add_Rushee('Liam','Brennan','','','','')
   add_Rushee('Daniel','Herron','','','','')
   add_Rushee('Jack','McGovern','','','','')
   add_Rushee('Jon','Payne','','','','')
   add_Rushee('Kevin','Hatch','','','','')
   add_Rushee('Spencer','Steinberg','','','','')
   add_Rushee('Tom','Santinelli','','','','')
   add_Rushee('Travis','Buck','','','','')
   add_Rushee('Test1','Test1','','','','')
   add_Rushee('Test2','Test2','','','','')
   add_Rushee('Test3','Test3','','','','')
   add_Rushee('El','Autismo','','','','')
   add_Rushee('Jesus','Cogo','','','','')

   # Print out what we have added to the user.
   print "Brothers: "
   for p in UserProfile.objects.all():
      print "  {0} {1}".format(str(p.user.first_name), str(p.user.last_name))

   print "Rushees: "
   for r in Rushee.objects.all():
      print " {0} {1} ({2}), {3}, {4}, {5}".format(str(r.firstName),str(r.lastName),str(r.preferredName),str(r.hometown),str(r.highSchool),str(r.grade))

   print "Comments: "
   for c in Comment.objects.all():
      print "{0} about {1}: {2}".format(str(c.brother),str(c.rushee),str(c.text))

def add_User(un,email,fn,ln,pw):
   u=User.objects.create_user(username=un,
      email=email,
      password=pw,
      first_name=fn,
      last_name=ln)
   return u

def add_Profile(u):
   p=UserProfile.objects.get_or_create(user=u)
   return p

def add_Brother(u):
   b = Brother.objects.get_or_create(user=u)
   return b

def add_Rushee(fn,ln,pn,home,hs,grd):
   r = Rushee.objects.get_or_create(firstName=fn,
      lastName=ln,
      preferredName=pn,
      hometown=home,
      highSchool=hs,
      grade=grd)[0]
   return r

def add_Comment(txt,u,r):
   c = Comment.objects.get_or_create(text=txt,
      brother=u,
      rushee=r)[0]
   return c

if __name__ == '__main__':
   print "Starting population script:"
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rushranker_project.settings')
   from rushranking.models import Brother,Rushee,Comment,UserProfile
   from django.contrib.auth.models import User
   populate()