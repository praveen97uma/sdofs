from django.http import HttpResponse
from fandjango.decorators import facebook_authorization_required as fb_authorize

@fb_authorize
def miner(request):
	return HttpResponse("Hey! How you doing")    