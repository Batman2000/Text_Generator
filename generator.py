import argparse
import json
import sys
import random
parser = argparse.ArgumentParser()
parser.add_argument('--model', type = str, help = "place where analise is written")
parser.add_argument('--seed', type = str, default = None, help = 'first_word')
parser.add_argument('--length', type = int, help = 'how many words should be generated')
parser.add_argument('--output', type = str, default = None, help = 'output file')
args = parser.parse_args()
input = open(args.model, "r")
output = sys.stdout
if(args.output != None):
	output = open(args.output, "w")
def main_generator(count, length):
	q = json.load(input)
	if count == None:
		count = random.choice(list(q.keys()))
	for index in range(length):
		mas = []
		if(len(q) == 0):
			count = random.choice(list(q.keys))
		else:
			for i in q[count]:
				f = i
				for z in range(q[count][f]):
					mas.append(f)
			count = random.choice(mas)
		output.write(count + ' ')
main_generator(args.seed, args.length)
print()



