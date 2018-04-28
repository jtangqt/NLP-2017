import random

with open('TC_provided/corpus2_train.labels') as source:
	data = [(random.random(), line) for line in source]
data.sort()

i = 1
train2 = open('train_c2', 'w')
test2 = open('test_c2.ans', 'w')

for _, line in data:
	if i > 600:
		test2.write(line)
	else: 
		train2.write(line)
	i += 1.

i = 1
train3 = open('train_c3', 'w')
test3 = open('test_c3.ans', 'w')
with open('TC_provided/corpus3_train.labels') as source:
	data = [(random.random(), line) for line in source]
data.sort()

for _, line in data:
	if i > 650:
		test3.write(line)
	else: 
		train3.write(line)
	i += 1.

train2.close()
train3.close()
test2.close()
test3.close()

test2 = open('test_c2.ans', 'r')
test3 = open('test_c3.ans', 'r')

line2 = test2.read().splitlines()
line3 = test3.read().splitlines()

out2 = open('test_c2', 'w')
out3 = open('test_c3', 'w')

for line in line2:
	one_line = line.split()
	out2.write(one_line[0] + '\n')

for line in line3:
	one_line = line.split()
	out3.write(one_line[0] + '\n')	