#!/bin/env python3
import twitter
import bot_apikeys
import datetime
import random
import json

TWEETS_DEFAULT_FILE = "c3daysleft_tweets_default.json"
TWEETS_SPECIAL_FILE = "c3daysleft_tweets_special.json"
    
OAUTH_FILE = "account.oauth"

SLEEP_MIN = 60*30
SLEEP_MAX = 3600*23


def get_nextC3date(date=datetime.date.today()):
    if date.month == 12 and date.day > 30:  # YYYY-12-30 will stay the last day of C3? ;)
        nextC3date = datetime.date(date.year + 1, 12, 27)
    else:
        nextC3date = datetime.date(date.year, 12, 27)
    return nextC3date


def weighted_random(pairs):
    total = sum(pair[0] for pair in pairs)
    r = random.randint(1, total)
    for (weight, value) in pairs:
        r -= weight
        if r <= 0:
            return value


def get_teweet(date=datetime.date.today(), special_file=TWEETS_SPECIAL_FILE,
               default_file=TWEETS_DEFAULT_FILE):
    s = str(date.today())
    special = json.load(open(special_file, 'r'))
    if s in special:
        return special[s]
    normal = json.load(open(default_file, 'r'))
    normal_pairs = [(normal[x], x) for x in normal]
    return weighted_random(normal_pairs)


def get_format(date=datetime.date.today(), nextC3date=None):
    if nextC3date is None:
        nextC3date = get_nextC3date(date)
    return {
        'days_left': (nextC3date - date).days,
        'nextC3_date': nextC3date,
        'nextC3': "%sC3" % (nextC3date.year - 1983)
    }


def sleep(sleep_min, sleep_max=None):
    if sleep_max is None:
        sleep_max = sleep_min
    if sleep_min and sleep_max and (sleep_max >= sleep_min):
        from time import sleep
        sleeptime = random.randint(sleep_min, sleep_max)
        print("sleeping for %ss" % sleeptime)
        sleep(sleeptime)