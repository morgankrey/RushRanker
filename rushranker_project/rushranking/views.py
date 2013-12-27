from django.http import HttpResponse

def index(request):
   return HttpResponse("Link to the about page: <a href='/rushranking/about/'>About</a>")

def about(request):
   return HttpResponse("This is the about page. Back to the index page: <a href='/rushranking/'>Index</a>")