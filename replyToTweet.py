import tweepy
import random
from apikey import *
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)
tweets = api.home_timeline(screen_name="iABD_ol")  #Put User ID of person you want to reply
api.update_status('@iabd_ol Testing tweet?',1403602692124016642) # Give tweet ID