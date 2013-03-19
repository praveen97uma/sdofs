from django.http import HttpResponse
from fandjango.decorators import facebook_authorization_required as fb_authorize

FB_GRAPH_API_URL = 'https://graph.facebook.com/'

@fb_authorize
def miner(request):
    #if not request.facebook.user:
    #    return HttpResponse('Not authorized')
    current_user = request.facebook.user
    graph = current_user.graph
    # extend the expiry of the access token that the user has granted
    #current_user.oauth_token.extend()
    user_id = current_user.facebook_id
    #FEED_URL = 'me/statuses?limit=100'
    #statuses = graph.get(FEED_URL)
    response = ""
    if request.facebook.user:
        response = "Hi, %s!"%request.facebook.user.facebook_username
    else:
        response = "Go Away"
    return HttpResponse(response)


