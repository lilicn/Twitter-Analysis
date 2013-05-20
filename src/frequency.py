import sys
import json

total = 0
var = {}

def lines(fp):
    for line in fp:
  line.encode("utf-8")
    	jsline = json.loads(line)
	if 'text' in jsline:
	    text = jsline["text"]
	    compute(text)
    output()

def output():
    for term in var:
	print term.encode("utf-8")+" "+ str(var[term]/total)

def compute(text):
    strs = text.split()
    for term in strs:
	global total
	total += 1
	if term in var:
	    var[term] += 1.0
	else:
	    var[term] = 1.0

def main():
    tweet_file = open(sys.argv[1])
    lines(tweet_file)

if __name__ == '__main__':
    main()
