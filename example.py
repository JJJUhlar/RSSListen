from listen import RSSListen

listen = RSSListen('http://www.hellointernet.fm/podcast?format=rss')
listen.getFeed()
result_3 = listen.transcribeAll("text")
print(result_3)