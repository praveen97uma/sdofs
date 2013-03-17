from django.http import HttpResponse

def home(request):
	return HttpResponse("Yeah! You got that right")	
