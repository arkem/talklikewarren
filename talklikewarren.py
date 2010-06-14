#!/usr/bin/env python

import twitter
import urllib2
import time
import re
import random

random.seed()

MIN_WAIT = 60 # In minutes
MAX_WAIT = 6 * 60

PSA_THRESHOLD = 40 # Every N posts will be a random PSA
PSA_TWEET = ["ATTENTION FILTH: Original Talk Like Warren Ellis - http://talklikewarrenellis.com",\
             "ATTENTION FILTH: The Original (and still the best) Warren Ellis - @warrenellis"]
count = 0

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
        api = twitter.Twitter("talklikewarren", "crooked0little0vein")
        api.statuses.update(status = post)
        print "success"
    except Exception:
        pass
    sleepinterval = random.randrange(MIN_WAIT, MAX_WAIT)
    print "Sleeping for %d minutes" % sleepinterval 
    time.sleep(60 * sleepinterval)
    
