import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights


twitter_consumer_key = 'HGIKWfrDX31AvkqbAuA2RLLus'
twitter_consumer_secret = '9TUIxCcP4JYxnbHBKCSICLM6B5SkImKkOIOynRHWsoTtQvCsSD'
twitter_access_token = '129396151-IPabzUTf0WTPLOzT9SGal9vyCKY9rSLcyXm3oVVD'
twitter_access_secret = 'IZfiLmXb4jc7D5Y7b10DoGsRZnvG8BBi9T4PPp1z6W8Ui'
twitter_api = twitter.Api(consumer_key = twitter_consumer_key,consumer_secret = twitter_consumer_secret, access_token_key = twitter_access_token,access_token_secret = twitter_access_secret)
handle = "@GenChuckYeager"
statuses = twitter_api.GetUserTimeline(screen_name = handle, count = 200, include_rts = False)

text = ""

for status in statuses:
  if(status.lang =='en'): 
    text += status.text.encode('utf-8')
# Bluemix Credentials
  pi_password = "6OXkj4ddJ0KP"
  pi_username = "dd78e177-d5b8-4e68-9955-a9c6932f40c2"

personality_insights = PersonalityInsights( pi_username,pi_password)
