import sys
import json
var = {}
state={}
def hw(fp):
    for line in fp:
  temp = line.split("\t")
	var[temp[0]]=float(temp[1])

def compute(text):
    sc = 0
    str = text.split()
    for term in str:
	if term in var:
		sc += float(var[term])
    return sc

def addState(f):
    for line in f:
    	jsline = json.loads(line)
	if 'place' in jsline and jsline["place"] != None:
	    place = jsline["place"]
	    if 'country_code' in  place:
		country = place["country_code"]
		if country == "US":
		    if 'full_name' in place:
			full_name = place["full_name"]	
			st=full_name.split(", ")[1]		
			if 'text' in jsline:
		    	    text = jsline["text"]
			    score = compute(text)
			    if st not in state:
				state[st] = score
			    else:
				state[st] += score


def output():
    max = 0
    maxSt = ""
    for st in state:
	if state[st] >= max:
	    max = state[st]
	    maxSt = st
    print maxSt

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file)
    addState(tweet_file)
    output()

if __name__ == '__main__':
    main()
