import tweepy
import time
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)
user = api.me()

#print(user.followers_count)

def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I like that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break





#for follwer in limit_handle(tweepy.Cursor(api.followers).items()):
#    if follwer.name == 'Arturo':
#        follwer.follow()