# Swetal Bhatt, Jie Song, Buqing Wang
# CS 590D
# Spring 2016
# Barna Saha

# HW 1 - Q 3.2
# bloom filter implementation

import hashlib
import random
import string

# set k to number of hash functions
k = 2

# memory size is 400KB, 3200000 bits
filtersize = 45000

# my_hash creates k hash functions and returns list of k hashed words
def my_hash(word, k):
	ret = list()
	print word
	for x in range(1, k+1):
		hash_object = hashlib.md5(unicode(word, errors='ignore').encode())
		i = ( (2*x) * (int(hash_object.hexdigest(), 16)) + (3+x*x) ) % filtersize
		ret.append(i);
	return ret

# read dictionary file
f = open('testdictionary.txt', 'r')
dictionary = f.readlines()
f.close()

# create bloom filter structure as python list of 3200000 theoretical bits
b_filter = [0] * filtersize


# initialize the filter using membership set from dictionary list object 
for word in dictionary:
	for x in my_hash(word, k):	
		b_filter.insert( x, 1 )
print dictionary

# initialize list for holding random generated words
random_words = list()

# generate random 5 letter words
for j in range(100):
	random_words.append(''.join(random.choice(string.lowercase) for x in range(5)))

# initialize varaibles for calculating empirical false positive rate
fp = tn = 0

# filter random_words and calculate false positive rate
for word in random_words:
	count = 0
	for x in my_hash(word, k): 
		if b_filter[x] == 1:
			count = count + 1
	if count == k:
		if word not in dictionary:
			fp = fp + 1
	else:
		tn = tn + 1
	
fp_rate = (fp/float(fp + tn))

# output results
print 'fp: ', fp
print 'tn: ', tn
print fp_rate