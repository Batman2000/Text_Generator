def main_action(f):
	s1 = ""
	s = input.readline()
	q = dict()
	while s != s1:
		s = s.rstrip()
		if(f == True):
			s = s.lower()
		a = [1]*len(s)
		for i in range(len(s)):
			if not (s[i].isalpha() or s[i] == ' ') :
				a[i] = 0
		s2 = str()
		for i in range(len(s)):
			if(a[i]):
				s2+=s[i]
		words = [""] + s2.split()
		words.append("")
		for i in range(len(words) - 1):
			first_word =  words[i]
			second_word = words[i+1]
			if first_word in q and second_word in q[first_word]:
				q[first_word][second_word]+=1
			elif first_word in q:
				q[first_word].update({second_word:1})
			else:
				q.update({first_word:{second_word:1}})
		s = input.readline()
	json.dump(q, output)
import json
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('--model', type = str, help = "place where analise is written")
parser.add_argument('--i', '--input-dir', type = str, default = None, help = "source of data")
parser.add_argument('--lc', action = 'store_true', default = False, help ='going to lowercase')
args = parser.parse_args()
print(args.model)
input = sys.stdin
if(args.i != None):
	input = open(args.i, "r")
output = open(args.model, "w")
t = False
if(args.lc != False):
	t = True
main_action(t)
input.close()
output.close()