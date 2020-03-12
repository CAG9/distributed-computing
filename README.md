# Project Readme
Tittle: Correlation between tweets with the word donald trump and the price of the amaerican dollar

Authors: César Arcos Gonzalez, Saul Armas Gamiño

Contact information: César Arcos Gonzalez: racec9999@gmail.com, Saul Armas Gamiño:luasikirfl@gmail.com

License : CC BY-NC

Installation and execution information: to run the file you need to use python and install tweepy,set the twitter credentials in a file named twitter_credentials.py

Introductions: we set the principal libraries to get the  twitter data and we did a test with the words Donald Trump

implementation: code : racec9999/distributed-computing/witter_streamer.py

Results: we got a lot of tweets data like this:
{"created_at":"Thu Mar 12 00:45:20 +0000 2020","id":1237902461748346880,"id_str":"1237902461748346880","text":"RT @tech_faq: I will never forgive the Democrats for forcing me to support Donald Trump.","source":"\u003ca href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\"\u003eTwitter Web App\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":1607184968,"id_str":"1607184968","name":"\ud83d\udc09\u26a1\ufe0f","screen_name":"caseyjonez_","location":"Terminus, CT","url":"https:\/\/jftna.org\/jft\/","description":"we at odds till we even \ud83d\udc50\ud83c\udffc","translator_type":"none","protected":false,"verified":false,"followers_count":1156,"friends_count":938,"listed_count":22,"favourites_count":8409,"statuses_count":56216,"created_at":"Sat Jul 20 01:51:06 +0000 2013","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"1A1B1F","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme9\/bg.gif","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme9\/bg.gif","profile_background_tile":false,"profile_link_color":"2FC2EF","profile_sidebar_border_color":"FFFFFF","profile_sidebar_fill_color":"252429","profile_text_color":"666666","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1222714559720558592\/c3dIdnoj_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1222714559720558592\/c3dIdnoj_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/1607184968\/1546197978","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Wed Mar 11 03:37:33 +0000 2020","id":1237583411197272066,"id_str":"1237583411197272066","text":"I will never forgive the Democrats for forcing me to support Donald Trump.","source":"\u003ca href=\"http:\/\/twitter.com\" rel=\"nofollow\"\u003eTwitter Web Client\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":323138380,"id_str":"323138380","name":"Tech-FAQ","screen_name":"tech_faq","location":null,"url":"http:\/\/www.tech-faq.com","description":"Technology, Science, Futurism, Security, Privacy, Free Speech, Education, and Bad Jokes.   I hate your political party. Sir \/ Master.","translator_type":"none","protected":false,"verified":false,"followers_count":47128,"friends_count":12572,"listed_count":1221,"favourites_count":801,"statuses_count":9611,"created_at":"Fri Jun 24 09:46:16 +0000 2011","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"022330","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme15\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme15\/bg.png","profile_background_tile":false,"profile_link_color":"0084B4","profile_sidebar_border_color":"A8C7F7","profile_sidebar_fill_color":"C0DFEC","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1206694529673416710\/JTsR6Qh6_normal.png","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1206694529673416710\/JTsR6Qh6_normal.png","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/323138380\/1580525630","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"quote_count":0,"reply_count":0,"retweet_count":3,"favorite_count":5,"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en"},"is_quote_status":false,"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[],"user_mentions":[{"screen_name":"tech_faq","name":"Tech-FAQ","id":323138380,"id_str":"323138380","indices":[3,12]}],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en","timestamp_ms":"1583973920653"}


Project definition: We are going to track the count of tweets countains Donald Trump words in a day. with that data we are going to try to find a correlation between Donald Trump count tweets with the usd dollar in mexcan pesos.

General objectives:
- Get the twitter streaming 
- Counts  daily Donald Trump words tweets
- Get the daily usd dollar price in mexican pesos
- Find correlations between tweets count and usd dollar price
- Show  the correlation with a graph

Software tools:
- Tweepy
- Python



Data source:
- Twitter

