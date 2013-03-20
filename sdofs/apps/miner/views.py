from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

from fandjango.decorators import facebook_authorization_required as fb_authorize
from fandjango.models import User

import json

from miner.models import Post
from miner.models import Comment
from miner.models import UsersVisited

from miner.tasks import fetchStatuses

def userAlreadySuppliedInfo(user):
    try:
        UsersVisited.objects.get(facebook_id=user.facebook_id)
    except ObjectDoesNotExist:
        return False
    return True

def playGame(request):
    return render(request, 'miner/test.html')

@fb_authorize
def miner(request):
    current_user = request.facebook.user
    if not userAlreadySuppliedInfo(current_user):
        fetchStatuses.delay(current_user)
    return playGame(request)


