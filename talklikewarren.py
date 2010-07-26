#!/usr/bin/env python

import tweepy
import urllib2
import time
import re
import random

random.seed()

# CREDENTIALS FOR REFERENCE "talklikewarren", "crooked0little0vein"
CONSUMER_KEY = "3QaD3dIS6p34alezA6qw1Q"
CONSUMER_SECRET = "ktic1IvdWVE4iDg8yLSthJT5NNK6BsRGhwCAaJKGU"
TOKEN_KEY = "69410961-uFltGP7XbWQZrU9uj8JRPuvtZzsmhvbC9cB0LpcAH"
TOKEN_SECRET = "VD0yKqhK6AnWVHMNaJGzdJRCvfp00ZMMgZZOXjkhqI"

MIN_WAIT = 60 # In minutes
MAX_WAIT = 6 * 60

PSA_THRESHOLD = 40 # Every N posts will be a random PSA
PSA_TWEET = ["ATTENTION FILTH: Original Talk Like Warren Ellis - http://talklikewarrenellis.com",\
             "ATTENTION FILTH: The Original (and still the best) Warren Ellis - @warrenellis"]
count = 0

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

while (True):
    try:
        if PSA_THRESHOLD > 0 and count == PSA_THRESHOLD:
            post = PSA_TWEET[random.randrange(0, len(PSA_TWEET))]
            count = 0
        else:
            page = urllib2.urlopen('http://talklikewarrenellis.com/').read()
            post = re.search("<h1>(.*)</h1>", page, re.M).group(1)
            count = count + 1
        print post
        api.update_status(post)
        print "success"
    except Exception as e:
        print e
        pass
    sleepinterval = random.randrange(MIN_WAIT, MAX_WAIT)
    print "Sleeping for %d minutes" % sleepinterval 
    time.sleep(60 * sleepinterval)
    
