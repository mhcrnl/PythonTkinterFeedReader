import feedparser

d=feedparser.parse('http://www.reddit.com/r/python/.rss')
print d['feed']['title']
print d['feed']['link']

print d.feed.subtitle

print len(d['entries'])

print d['entries'][0]['title']

print d['entries'][0]['link']

for post in d.entries:
    print post.title+":"+post.link+"\n"

