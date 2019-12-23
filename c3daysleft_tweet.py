__author__ = 'd3non'

from c3daysleft import sleep, twitter, get_teweet, get_format
from c3daysleft import SLEEP_MAX, SLEEP_MIN, OAUTH_FILE

import bot_apikeys


if __name__ == "__main__":
    sleep(SLEEP_MIN, SLEEP_MAX)
    oauth = twitter.read_token_file(OAUTH_FILE)
    t = twitter.Twitter(auth=twitter.OAuth(oauth[0], oauth[1], bot_apikeys.CONSUMER_KEY, bot_apikeys.CONSUMER_SECRET))
    format_data = get_format()
    format_string = get_teweet()[0 if format_data["days_left"] == 1 else 1]
    text = format_string.format(**format_data)
    print("tweeting: %s" % text)
    t.statuses.update(status=text)
