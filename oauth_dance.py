#!/usr/bin/env python
import twitter
import bot_apikeys
import sys

if len(sys.argv) > 1:
    tokenfile = sys.argv[1]
else:
    tokenfile = None

twitter.oauth_dance('c3daysleftbot', bot_apikeys.CONSUMER_KEY, bot_apikeys.CONSUMER_SECRET, tokenfile)
