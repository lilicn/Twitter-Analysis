import sys
import json
var = {}
newVar = {}
number = {}
def hw(fp):
    for line in fp:
  temp = line.split("\t")
	var[temp[0]]=float(temp[1])

def lines(fp):
    for line in fp:
	line.encode("utf-8")
    	jsline = json.loads(line)
	if 'text' in jsline:
	    text = jsline["text"]
	    current = float(compute(text))
	    check(text,current)	
    output()

def output():
    for key in newVar:
	print key.encode("utf-8") + " " + str(newVar[key]/number[key])

def compute(text):
    sc = 0
    str = text.split()
    for term in str:
	if term in var:
	    sc += float(var[term])
    return sc    

def check(text,current):
    str = text.split()
    for term in str:
        if term not in var:
	    if term not in number:
		number[term] = 1
		newVar[term] = float(current)
	    else:
		number[term] += 1
		newVar[term] += float(current)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
