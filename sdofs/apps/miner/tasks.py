from sdofs.apps.miner.models import Post
from sdofs.apps.miner.models import Comment
from sdofs.apps.miner.models import UsersVisited
from celery import Celery
from celery.decorators import task

import logging


#celery = Celery('tasks')


@task()
def fetchStatuses(user):
    graph = user.graph
    # extend the expiry of the access token that the user has granted
    #current_user.oauth_token.extend()
    user_id = user.facebook_id
    FEED_URL = 'me/statuses'
    statuses = graph.get(FEED_URL, limit=100) 
    data = statuses.get('data', [])
    
    for status in data:
        like_count = 0
        if status.has_key('likes'):
            like_count = len(status['likes']['data'])
        
        status_data = {
            'post_id': status['id'],
            'message': status.get('message', 'None'),
            'like_count': like_count,
            'user_id': user_id,
        }
        try:
	    post = Post(**status_data)
            post.save()
	except Exception:
	   continue
        
        if status.has_key('comments'):
            all_comments = status.get('comments', []).get('data', [])
            for comment in all_comments:
                comment_data = {
                    'comment_id': comment.get('id', '0'),
                    'user_id': (comment.get('from')).get('id', '0'),
                    'message': comment.get('message', None),
                    'user_likes': int(comment.get('user_likes') == 'true'),
                    'like_count': comment.get('like_count', 0),
                    'post': post,
                }
		try:
                    comment_entity = Comment(**comment_data)
                    comment_entity.save()
		except Exception:
		    pass
    visited_user = UsersVisited(facebook_id=user.facebook_id, user=user)
    visited_user.save()
    logging.info("Data of %s saved successfully"%(user.first_name))
