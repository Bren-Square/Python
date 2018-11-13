import os
import praw


def get_length(comment_object):
    i = 0
    for comment in comment_object.comments.new():
        i = i+1
    return i


session = praw.Reddit(client_id=os.environ['REDDIT_CLIENT_ID'],
                      client_secret=os.environ['REDDIT_CLIENT_SECRET'],
                      user_agent=os.environ['REDDIT_USER_AGENT'],
                      username=os.environ['REDDIT_USER_NAME'],
                      password=os.environ['REDDIT_PASSWORD'])


user_to_del = session.redditor(os.environ['REDDIT_USER_NAME'])
initialization_point = get_length(user_to_del)

while (initialization_point != 0):
    for comment in user_to_del.comments.new():
        comment_to_delete = session.comment(comment.id)
        comment_to_delete.delete()
    initialization_point = get_length(user_to_del)
