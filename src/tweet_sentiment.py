import sys
import json
var = {}
def hw(fp):
    for line in fp:
  temp = line.split("\t")
	var[temp[0]]=float(temp[1])

def lines(fp):
    for line in fp:
    	jsline = json.loads(line)
	if 'text' in jsline:
	    text = jsline["text"]
	    score = compute(text)
	    print score

def compute(text):
    sc = 0
    str = text.split()
    for term in str:
	if term in var:
		sc += float(var[term])
    return sc

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
