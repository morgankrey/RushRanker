from django.contrib import admin
from rushranking.models import Brother,Rushee,Comment,UserProfile

class rusheeAdmin(admin.ModelAdmin):
   list_display = ('firstName','preferredName','lastName','hometown','highSchool','grade','score')

class commentAdmin(admin.ModelAdmin):
   list_display = ('rushee','brother','text')

class userAdmin(admin.ModelAdmin):
   list_display = ('user','horse')

admin.site.register(UserProfile,userAdmin)
admin.site.register(Brother)
admin.site.register(Rushee,rusheeAdmin)
admin.site.register(Comment,commentAdmin)