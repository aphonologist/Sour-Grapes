# Call with python 2
# Andrew Lamont (2018)

def s1(input):
	# left-subsequential machine
	## spreads in local contexts (k <= 4)
	## adds markup in unbounded spreading contexts

	# transition function
	# state : {input : [state, output]}
	transition = {
	0 : {'m' : [1,'m'   ], 'a' : [0,'a'], 's' : [0,'s'   ] },
	1 : {'m' : [1,'m'   ], 'a' : [2,'' ], 's' : [5,'s'   ] },
	2 : {'m' : [1,'mm'  ], 'a' : [3,'' ], 's' : [5,'as'  ] },
	3 : {'m' : [1,'mmm' ], 'a' : [4,'' ], 's' : [5,'aas' ] },
	4 : {'m' : [1,'amam'], 'a' : [4,'a'], 's' : [5,'aaas'] },
	5 : {'m' : [1,'m'   ], 'a' : [5,'a'], 's' : [5,'s'   ] }
	}

	# terminal function
	terminal = {
	0 : '',
	1 : '',
	2 : 'm',
	3 : 'mm',
	4 : 'mam',
	5 : ''
	}

	# run the machine
	output = ''
	state = 0

	for c in input:
		output = output + transition[state][c][1]
		state = transition[state][c][0]

	output = output + terminal[state]

	return output

def s2(input):
	# right-subsequential machine
	## interprets markup and spreads in unbounded environments

	# transition function
	# state : {input : [state, output]}
	transition = {
	0 : {'m' : [1,''  ], 'a' : [0,'a' ], 's' : [0,'s' ] },
	1 : {'m' : [1,'m' ], 'a' : [2,'m' ], 's' : [0,'sm'] },
	2 : {'m' : [3,'mm'], 'a' : [0,'aa'], 's' : [0,'sa'] },
	3 : {'m' : [1,''  ], 'a' : [3,'m' ], 's' : [0,'s' ] }
	}

	# terminal function
	terminal = {
	0 : '',
	1 : 'm',
	2 : 'a',
	3 : ''
	}

	# run the machine
	output = ''
	state = 0

	for c in input[::-1]:
		output = transition[state][c][1] + output
		state = transition[state][c][0]

	output = terminal[state] + output

	return output

def sg(input):
	# non-deterministic machine
	## A -> M / MA*_A*M
	## A -> M / MA*_A*#

	# it's simpler to use a stack rather than explicitly coding the non-deterministic fst
	stack = ''
	output = ''
	trigger = False
	for c in input:
		if trigger:
			if c == 's':
				# dump stack faithfully
				output = output + stack + c
				stack = ''
				trigger = False
			elif c == 'a':
				# add to stack
				stack = stack + c
			elif c == 'm':
				# dump stack; spread nasals
				for a in stack:
					output = output + 'm'
				output = output + c
				stack = ''
		else:
			# faithfully write to string
			output = output + c

		if c == 'm':
			trigger = True
	if stack:
		if trigger:
			for a in stack:
				output = output + 'm'
		else:
			output = output + stack
	return output

import itertools, sys

alphabet = ['m', 'a', 's']

# check whether user passed in a string to test
if len(sys.argv) > 1:
	input = sys.argv[1]
	for i in input:
		if i not in alphabet:
			print "Invalid input; please only use 'm', 'a', 's'"
			sys.exit()
	a = s1(input)
	b = s2(a)
	c = sg(input)

	print 'Input:', input
	print 'Output of S1:', a
	print 'Output of S2:', b
	print 'Output of SG:', c
	print 'Success:', b == c

# test all strings of a certain length
else:
	# tested for all strings of length 1-19
	n = 3
	total = 3**n
	success = True

	print 'Total strings to test:', total

	# For every string s over the alphabet up to length n, test whether s2(s1(s)) == sg(s)
	for t in itertools.product(alphabet, repeat=count):
		if len(t) == count:
			a = s1(t) # input -> s1
			b = s2(a) # input -> s1 -> s2
			c = sg(t) # input -> sg
			if b != c:
				print ''.join(t), '\t', a, '\t', b, '\t', c, '\t', b == c
				success = False
			total -= 1
			if total % 10000000 == 0:
				print 'Total strings remaining:', total

	print 'SUCCESSFUL?', success
