import feedparser

feed= feedparser.parse('https://sg.entertainment.yahoo.com/rss/')

title = feed['entries'][1].title
description = feed['entries'][1].summary,
url = feed['entries'][1].link,

print title
print url
print description

posts = []
for i in range (0, len(feed['entries'])):
    posts.append({
        'title':feed['entries'][i].title,
        'description':feed['entries'][i].summary,
        'url':feed['entries'][i].link,
        })
    print title
    print description
    print url
"""
https://iamrafiul.wordpress.com/2013/04/25
/rss-feed-parsing-in-python-using-feedparser-a-quick-yet
-complete-tutorial/
"""
