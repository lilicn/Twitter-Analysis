import sys
import json
import operator 

var = {}
def lines(fp):
    for line in fp:
      jsline = json.loads(line)
	if 'entities' in jsline:
	    entities = jsline["entities"]
	    if 'hashtags' in entities:
		hashtags = entities["hashtags"]
		for hash in hashtags:
		    if 'text' in hash:
		    	text = hash["text"]
		   	addVar(text)
		     

def addVar(tag):
    if tag not in var:
	var[tag] = 1
    else:
	var[tag] += 1

def output():
    ns = sorted(var.iteritems(), key = operator.itemgetter(1),reverse = True)
    count = 0
    for a,b in ns:
	if count<10:
	    print a.encode("utf-8")+" "+str(float(b))
	else:
	    break
	count += 1
    
    

def main():
    tweet_file = open(sys.argv[1])
    lines(tweet_file)
    output()

if __name__ == '__main__':
    main()
