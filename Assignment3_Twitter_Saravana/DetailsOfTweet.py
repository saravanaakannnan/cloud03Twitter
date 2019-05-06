from google.appengine.ext import ndb
class Tweet(ndb.Model):
    user_name = ndb.StringProperty()
    desc = ndb.StringProperty()
    tweets = ndb.StringProperty(repeated=True)
    no_of_followers = ndb.StringProperty(repeated=True)
    no_of_following = ndb.StringProperty(repeated=True)

class TweetList(ndb.Model):
    all_tweets = ndb.StringProperty(repeated = True)
    user = ndb.StringProperty(repeated = True)
