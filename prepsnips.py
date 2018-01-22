info='''Requirements: Python 3.x; additional modules: nltk, numpy.
Title: Predicting the author as per the writing style using Markov model of language
This code is provided as-is without any warranty. You may use this code in your project
with modifications. However, you must release your code and any modifications you make
in this code under the same license (copy this entire statement in your header). 
Name of the author must be cited --> Copyright (C) Aalok Sathe, 2016. aalok.sathe@gmail.com'''
################################################################################
print(info)

def direc(path):
	if not path[len(path)-1] == '/': path = path + '/'
	return path

def makedir(sequential_names_list_ahead_of_home):
	import os
	lis = sequential_names_list_ahead_of_home
	before = ''
	for name in lis:
		if not os.path.isdir(direc(before + name)): os.mkdir(direc(before + name))
		before += direc(name)
	return direc(before)
		
def makesnips(path_to_training_data='/home/aalok/Desktop/authors_folder'):
	import os,itertools,shutil,random

	authors = list_of_authors = os.listdir(direc(path_to_training_data))
	#list_of_sizes = sizes = []	# looks like we're still varying training size
	#maxorder = N = 6 # form models for all orders up to this: say 6 for words and 10 for characters
	training = path_to_training_data
	snippet_size = 750

	for author in authors:
		all_words = []
		path = direc(training) + direc(author)
		training_files = os.listdir(path)
		
		for training_file in training_files:
			all_words += open(path+training_file,'r').read().split()
			
		totwords = len(all_words)
	
		findir = makedir(['writingstyle',author,'snipdump'])
		
		totfiles=totwords//snippet_size
		lis=list(range(totfiles))
		random.shuffle(lis) # convention : pick from beginning to train model, pick from end to test.
		for i in lis:
			f = open("writingstyle/%s/snipdump/%d"%(author,i),'w')
			for j in range(snippet_size):
				if j != snippet_size-1 : f.write(all_words[i*snippet_size + j]+'\n')
				else: f.write(all_words[i*snippet_size + j])
makesnips()	
