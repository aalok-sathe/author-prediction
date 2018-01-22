info='''Requirements: Python 3.x; additional modules: nltk, numpy.
Title: Predicting the author as per the writing style using Markov model of language
This code is provided as-is without any warranty. You may use this code in your project
with modifications. However, you must release your code and any modifications you make
in this code under the same license (copy this entire statement in your header). 
Name of the author must be cited --> Copyright (C) Aalok Sathe, 2016. aalok.sathe@gmail.com'''
################################################################################
print(info)

typ = 0 #char
typ = 1 #word
def direc(path):
	if not path[len(path)-1] == '/': path = path + '/'
	return path

def makedir(sequential_names_list_ahead_of_home_dir):
	import os
	lis = sequential_names_list_ahead_of_home_dir
	before = ''
	for name in lis:
		if not os.path.isdir(direc(before + name)): 
			os.mkdir(direc(before + name))
			print('directory %s Did Not Exist. Making it now.\t'%before+name)
		before += direc(name)
	return before

def get_string_from_tuple(tup):
	st=''
	for item in tuple: st+=item+' '
	st = st[:len(st)-1]
	return st
	
def process(inp,author,size,maxord):

	from nltk import ngrams
	import re
	N = maxord+1
	for n in list(range(1,N+1)):
		modeldic = {}
		uniqdic = {}
		if typ: Ngrams = list(ngrams(inp.split(),n))
		else: Ngrams = list(ngrams(re.sub(' ','~',re.sub('\n','~',inp)),n))
			
		for Ngram in Ngrams:
			if n-1: 
				uniqgm = get_string_from_tuple(Ngram[:len(Ngram)-1])
				uniqdic[uniqgm] = uniqdic.get(uniqgm,0)+1
			Ngram = get_string_from_tuple(Ngram)
			modeldic[Ngram]=modeldic.get(Ngram,0)+1
			
		if typ: 
			fil = open(makedir(['writingstyle',author,'words','%d'%size]+'model%d'%n-1),'w')
			if n-1: fil2 =open(makedir(['writingstyle',author,'words','%d'%size]+'unique%d'%n-1),'w')
			
		else: 
			fil = open(makedir(['writingstyle',author,'chars','%d'%size]+'model%d'%n-1),'w')
			if n-1: fil2 =open(makedir(['writingstyle',author,'chars','%d'%size]+'unique%d'%n-1),'w')
			
		writetext=''
		for kw in modeldic: writetext+=kw+' '+str(modeldic[kw])+'\n'
		fil.write(writetext[:len(writetext)-1])
		
		writetext=''
		if n-1:
			for kw in uniqdic: writetext+=kw+' '+str(uniqdic[kw])+'\n'
			fil2.write(writetext[:len(writetext)-1])
	
def makemodels():	
	size_of_snip = 750
	list_of_sizes_of_training = nlist = []
	authors_list = os.listdir('writingstyle/')
	if typ: max_order_of_models = k = 7
	else: k = 15

	for author in authors_list:
		for n in nlist: # sizes of training data
			findir = makedir(['writingstyle',author,'%d'%n])
			numsnips = n // size_of_snip + 1
			raw_text_in=[]
			for i in list(range(numsnips)):
				raw_text_in += open(makedir(['writingstyle',author,snipdump]) + '%d'%i,'r').read().split()
		
			raw_text_in = raw_text_in[:n]
		
			process(raw_text_in, author, n, k)
