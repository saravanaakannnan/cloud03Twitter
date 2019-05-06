import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from DetailsOfTweet import Tweet
from DetailsOfTweet import TweetList
import os

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

class Main(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        url = ''
        url_string = ''
        welcome = 'Welcome back'
        detailsOfTweet = None
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'
            email = users.get_current_user().email()
            detailsOfTweet_key = ndb.Key('DetailsOfTweet',email)
            detailsOfTweet = detailsOfTweet_key.get()
            detk = ndb.Key('TweetList','dk')
            det = detk.get()
            if det == None:
                det = TweetList(id='dk')
                det.put()
            if detailsOfTweet == None:
                welcome = 'Welcome to Twitter'
                detailsOfTweet = DetailsOfTweet(id=email)
                detailsOfTweet.put()
            if detailsOfTweet.user_name = None:
                self.redirect('/user')
        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'
        query = Tweet.query().fetch()
        user_name = self.request.get('searchuser')
        final_user = None
        i =0
        tweet_search = self.request.get('searchtweet')
        final_tweet = []
        j =0
        action.self.request.get('button')
        if action == 'Search':
            for x in query:
                if x.username == user_name:
                    i = i+1
                    final_user = user_name
        if action == 'Tweet Search':
            for x in query:
                if y in x.tweet:
                    if tweet_search in y:
                        j = j+1
                        final_tweet.append(y)
        listOfFollowers = 0
        listOfFollowing = 0
        if detailsOfTweet != None:
            for x in detailsOfTweet.no_of_followers:
                listOfFollowers = listOfFollowers + 1
            for y in detailsOfTweet.no_of_following:
                listOfFollowing = listOfFollowing + 1

        tweet_key = ndb.Key('TweetList','dk')
        tkey = tweet_key.get()
        tweet1 = []
        tweetun = []
        if tkey! = None:
            for i in reversed(tkey.all_tweets):
                tweet1.append(i)
            tweet1 = tweet[:50]
            for j in reversed(tkey.user):
                tweetun.append(j)
            tweetun = tweetun[:50]
        tweetf = map(' --> '.join,zip(tweetun,tweet1))

        template_values = {'url' : url,'url_string' : url_string,'user' : user,'welcome' : welcome,'detailsOfTweet' : detailsOfTweet,'i':i,'final_user':final_user,'j':j,'final_tweet':final_tweet,'listOfFollowers':listOfFollowers,'listOfFollowing':listOfFollowing,'tweetf':tweetf}
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values

 class User(webapp2.RequestHandler):
     def get(self):
         email = users.get_current_user().email()
         detailsOfTweet_key = ndb.Key('Tweet', email)
         detailsOfTweet = detailsOfTweet_key.get()
         self.response.out.write("<html><head></head><body>")
         self.response.out.write("""<form method='get' action='/user'>""")
         self.response.out.write("""USERNAME:<br/><input type='text' name='input' required='True'/><br/>""")
         self.response.out.write("""BIO:<br/><input style="height:200px;width:1000px;font-size:14pt;" type='text' name='input1' required='True' maxlength="280"/><br/>""")
         self.response.out.write("""<input type='submit' name='button' value='Submit'/>""")
         self.response.out.write("""</form>""")
         action=self.request.get('button')
         url = users.create_logout_url(self.request.uri)
         if action == 'Submit':
             user_name = self.request.get('input')
             desc = self.request.get('input__a')
             detailsOfTweet.user_name = user_name
             detailsOfTweet.desc = desc
             detailsOfTweet.put()
             self.redirect('/')
        self.response.write('<br/><a href="/">Logout</a>')
        self.response.out.write("</body></html>")

    class EditUser(webapp2.RequestHandler):
        def get(self):
            email = users.get_current_user().email()
            detailsOfTweet_key = ndb.Key('Tweet', email)
            detailsOfTweet = detailsOfTweet_key.get()
            self.response.out.write("<html><head></head><body>")
            self.response.out.write("Edit the user information below:<br/>")
            self.response.out.write("""<form method='get' action='/edit'>""")
            a=detailsOfTweet.desc
            self.response.out.write("""BIO:<br/><input style="height:200px;width:1000px;font-size:14pt;" type='text' name='input__a' required='True' maxlength="280" placeholder="%s"/><br/>"""%(a))
            self.response.out.write("""<input type='submit' name='button' value='Submit'/>""")
            self.response.out.write("""</form>""")
            self.response.out.write("<a href='/'>Home</a>")
            action=self.request.get('button')
            if action == 'Submit':
                desc=self.request.get('input__a')
                detailsOfTweet.desc=desc
                detailsOfTweet.put()
                self.redirect('/')
            self.response.out.write("</body></html>")

        def post(self):
            email = users.get_current_user().email()
            detailsOfTweet_key = ndb.Key('Tweet', email)
            detailsOfTweet = detailsOfTweet_key.get()
            action=self.request.get('button')
            detk = ndb.Key('TweetList','dk')
            det = detk.get()
            name=detailsOfTweet.user_name
            if action == 'Submit':
                tweet=self.request.get('tweet')
                detailsOfTweet.tweet.append(tweet)
                det.tweetall.append(tweet)
                det.user.append(name)
                m.put()
                myuser.put()
                self.redirect('/')

 class ProfilePage(webapp2.RequestHandler):
     def get(self,id):
         self.response.headers['content-Type'] = 'text/html'
         me = id
         query = Tweet.query(Tweet.user_name == me)
         list = []
         for i in query:
             for j in reversed(i.tweet):
                list.append(j)
        list = list[:50]
        template_values = {'query':query,'list':list}
        template=JINJA_ENVIRONMENT.get_template('profilepage.html')
        self.response.write(template.render(template_values))

    def post(self,id):
        email = users.get_current_user().email()
        detailsOfTweet_key = ndb.Key('Tweet',email)
        detailsOfTweet = detailsOfTweet_key.get()
        user_name = detailsOfTweet.username
        me = id
        emailf = None
        follow_username = None
        query = Tweet.query(Tweet.user_name == me)
        for x in query:
            emailf = x.key.id()
        action = self.request.get('button')
        if action == 'FOLLOW' :
            detailsOfTweet_keyf = ndb.Key('Tweet', emailf)
            detailsOfTweetf = detailsOfTweet_keyf.get()
            f_username = detailsOfTweetf.username
            if username == detailsOfTweetf.username:
                self.redirect('/profilepage/%s'%(me))
            else:
                if username in detailsOfTweetf.followers:
                    self.redirect('/profilepage/%s'%(me))
                else:
                    detailsOfTweetf.followers.append(username)
                    detailsOfTweet.following.append(follow_username)
                    detailsOfTweet.put()
                    detailsOfTweetf.put()
                    self.redirect('/profilepage/%s'%(me))
        if action == 'UNFOLLOW' :
            detailsOfTweet_keyf = ndb.Key('Tweet', emailf)
            detailsOfTweetf = detailsOfTweet_keyf.get()
            f_username = detailsOfTweetf.username
            if username in detailsOfTweetf.followers:
                detailsOfTweetf.followers.remove(username)
                detailsOfTweetf.put()
                if f_username in detailsOfTweet.following:
                    detailsOfTweet.following.remove(f_username)
                    detailsOfTweet.put()
            self.redirect('/profilepage/%s'%(me))


class Delete(wenapp2.RequestHandler):
    def get(self, id):
        self.response.headers['Content-Type'] = 'text/html'
        me = id
        email = users.get_current_user().email()
        detailsOfTweet_key = ndb.Key('Tweet', email)
        detailsOfTweet = detailsOfTweet_key.get()
        list = detailsOfTweet.tweet
        list = list[::-1]
        template_values={'detailsOfTweet':detailsOfTweet,'list':list}
        template=JINJA_ENVIRONMENT.get_template('delete.html')
        self.response.write(template.render(template_values))

    def post(self, id):
        action = self.request.get('button')
        email = users.get_current_user().email()
        detailsOfTweet_key = ndb.Key('Tweet', email)
        detailsOfTweet = detailsOfTweet_key.get()
        dl_key = ndb.Key('TweetList', 'dk')
        dl = dl_key.get()
        me = id
        twi = None
        if action == 'delete':
            list = detailsOfTweet.tweet
            list = list[::-1]
            del list[int(self.request.get('index')) - 1]
            list = list[::-1]
            detailsOfTweet.tweet = l
            detailsOfTweet.put()
            twi = self.request.get('users_name')
            dl.tweetall.remove(twi)
            dl.put()
            self.redirect('/delete/%s'%(me))
        if action=='Edit':
            twi = self.request.get('users_name')
            list = detailsOfTweet.tweet
            list=list[::-1]
            twi1=list[int(self.request.get('index'))-1]
            list=detailsOfTweet.tweet
            list=list[::-1]
            list[int(self.request.get('index'))-1]=self.request.get('users_name')
            list=list[::-1]
            myuser.tweet=l
            myuser.put()
            dl.tweetall[db.tweetall.index(twi1)] = twi
            dl.put()
            self.redirect('/deleted/%s'%(me))
