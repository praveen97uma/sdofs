from django.http import HttpResponse
from fandjango.decorators import facebook_authorization_required as fb_authorize
import json
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
    FEED_URL = 'me/statuses'
    status = graph.get(FEED_URL)
    statuses =status.keys()
    #for s in status:
    #	statuses.append(s)
    #statuses.append(status.next())
    response = ""
    if request.facebook.user:
        response = "Hi, %s!"%request.facebook.user.facebook_username
    else:
        response = "Go Away"
    return HttpResponse(response+json.dumps(statuses))


