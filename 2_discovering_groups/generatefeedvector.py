import feedparser
import re

# Retrusn title and dictionary of word counts for an RSS feed
def getwordcounts(url)
  d = feedparser.parse(url)
  wc = {}

  for e in d.entries:
    if 'summary' in e: summary = e.summary
    else: summary = e.description

    words = getwords(e.title + ' '+summary)
    for word in words:
      wc.setdefault(word, 0)
      wc[word] += 1
  return d.feed.title, wc

def getwords(html)
  # Remove all the HTML tags
  txt = re.compile(r'<[^>]+>').sub(''. html)

  # Split words by all non-alpha characters
  words = re.compile(r'[^A-Z^a-z]+').split(txt)

  return [word.lower() for word in words if word != ""]

apcount = {}
wordcounts = {}
for feedurl in file('feedlist.txt'):
  title, wc=getwordcounts(feedurl)
  wordcounts[title] = wc
  for word, count in wc.items():
    apcount.setdefault(word, 0)
    if count > 1:
      apcount[word] += 1

wordlist = []
for w, bc in apcount.items():
  frac = float(bc)/len(feedlist)
  if frac > 0.1 and frac < 0.5: wordlist.append(w)

out = file('blogdata.txt', 'w')
out.write('Blog')
for word in wordlist: out.write('\t%d' % wc[word])
out.write('\n')
for blog,wc in wordcounts.items():
  out.write(blog)
  for word in wordlist:
    if word in wc: out.write('\t%d' % wc[word])
    else: out.write('\t0')
  out.write('\n')
