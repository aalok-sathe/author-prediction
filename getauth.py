#!/usr/bin/env python3
###############################################################################
info='''Requirements: Python 3.3 and above; modules: nltk, numpy. Tested on Ubuntu 16.04\n
Title: Predicting the author as per the writing style using Markov model of language.\n
This code is provided as-is, without any warranty. You may use this code with modifications.
However, you must distribute your code and any modifications you make
in this code under the same license (copy this entire statement in your header).\n
GNU GPL v3\n
Name of the author must be cited --> Copyright (C) Aalok S., 2016. aalok.sathe+py@gmail.com'''
################################################################################
print(info)

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
	
def getlog(x,y): 
	import math
	sr = math.log((float(x)/float(y)),30.0)
	return sr

def calscore(k,n,txt,mdict,udict,tot):
	sc=0.0
	for i in range(k,n): # chained product computation (from k onwards: minimum k words required prior )
		for reduc in range(k+1): # reduce the Markov order till a match is found. Max reduction = k itself => ord=0.
			orde=k-reduc #min,max: 0,k. default: k. This is the actual effective order.
			kwbottom='' # keyword at the bottom of the fraction line. (divide by)
			for j in range(i-orde,i): # for every word among the previous `orde' words
				if j < i-1: kwbottom = kwbottom + txt[j] + ' ' # j is not in the last iteration
				else: kwbottom = kwbottom + txt[j]
				if orde == 0: kwbottom = '-1'
			if not kwbottom == '-1': kwtop = kwbottom + ' ' + txt[i] 
			else: kwtop = txt[i]
			 
			if mdict[k].get(kwbottom,0): break #if we have the bottom kw in data, move on. 
		# worst case scen.: 
		top = 1 + mdict[k].get(kwtop,0)		
		if k != 0 : bottom = mdict[k].get(kwbottom,0) + udict[k].get(kwbottom,0)
		else: bottom = tot + len(mdict[k])
		sc += getlog(top,bottom)
	if k!=0 : return sc + calscore(k-1,k,txt,mdict,udict,tot)
	return sc
		
		
def get_author(textpath,order,authors_list,size,typ): #main function to determine author
	N=order+1
	txt = open(textpath,'r').read().lower().translate(None, """/\:;"`%*<>='_-!?^|,()[]{}""").split()
	scores_list = []
	if not directory_of_MLMs[len(directory_of_MLMs)-1] == '/': directory_of_MLMs = directory_of_MLMs + "/"
	u='uniques'
	tot=0
	for author in authors_list:
		modelsdict,uniquesdict = {},{}
		for i in range(N): 
			tot = open(makedir(['writingstyle',author,typ,'%d'%size,'model%d'%i]),'r').readline()
			modelsdict[i]= open(['writingstyle',author,typ,'%d'%size,'model%d'%i],'r').readlines()
			#if i < N: uniquesdict[i]= open(directory_of_MLMs+author+u+"%d"%i,'r').readline()
			if i < N: uniquesdict[i]= open(['writingstyle',author,typ,'%d'%size,'unique%d'%i],'r').readlines()
		
		it=0
		for i in modelsdict:
			it+=1
			dic = {}
			j=modelsdict[i] #j is a list.
			for line in j:
				s=line.split()
				kw=''
				val=int(s[it])
				for k in range(it): # how many wordsच model?
					if not k+1 == it: kw = kw + s[k]+' '
					if k+1 == it: kw = kw + s[k]
				dic[kw]=val
				
			modelsdict[i] = dic	# switched the list with the dictionary of that list :thumbup:
					
		it=0
		for i in uniquesdict:
			it+=1
			dic = {}
			j=uniquesdict[i] #j is a list.
			for line in j:
				s=line.split()
				kw=''
				val=int(s[it])
				for k in range(it): # how many wordsच unique?
					if not k+1 == it: kw = kw + s[k]+' '
					if k+1 == it: kw = kw + s[k]
				dic[kw]=val
				
			uniquesdict[i] = dic	# switched the list with the dictionary of that list :thumbup:
						
		scores_list.append(calscore(order,len(txt),txt,modelsdict,uniquesdict,tot))
	retlist=zip(scores_list,authors_list)
	retlist.sort()
	autho = retlist[len(retlist)-1][1]
	return autho
		
