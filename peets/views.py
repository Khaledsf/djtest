from django.http import HttpResponse
   # - create function(action)


def greeting(request):
	return HttpResponse("Hello World!")

def sayhi(request):
   return HttpResponse("This is <b>sayhi</b> action")