info='''Requirements: Python 3.x; additional modules: nltk, numpy.
Title: Predicting the author as per the writing style using Markov model of language
This code is provided as-is without any warranty. You may use this code in your project
with modifications. However, you must release your code and any modifications you make
in this code under the same license (copy this entire statement in your header). 
Name of the author must be cited --> Copyright (C) Aalok Sathe, 2016. aalok.sathe@gmail.com'''
################################################################################
print(info)
from modelsmaker import makedir
from modelsmaker import direc

def kullback_leibler_divergence(modeldic1,modeldic2,tot):
	vardic = {}
	dist = 0.0
	from math import log
	for i in modeldic1:
		vardic[i]=vardic.get(i,0)+1
	for i in modeldic2:
		vardic[i]=vardic.get(i,0)+1
		
	for variable in vardic:
		P_i = (modeldic1.get(variable,0)+1)/(tot+len(modeldic1)+1)
		Q_i = (modeldic2.get(variable,0)+1)/(tot+len(modeldic2)+1)
		dist += P_i * log(P_i / Q_i)
		
	return dist
	
def D_KL_symm(**kwargs): #kws: size, order, authors_list(of 2 authors), type=words/chars
	twomodels={}
	tot=0
	for author in kwargs['authors_list']:
		tot = open(makedir(['writingstyle',author,kwargs['type'],'%d'%kwargs['size']]+'model%d'%kwargs['order'],'r').readline()
		modeltxt= open(makedir(['writingstyle',author,kwargs['type'],'%d'%kwargs['size']]+'model%d'%kwargs['order'],'r').readlines()
		discdic = {}
		for line in modeltxt:
			s=''
			for i in range(kwargs['order']+1):
				if not i == kwargs['order']: s+= line.split()[i] + ' '
				else: s+= line.split()[i]
			discdic[s]=discdic.get(s,0)+1
		twomodels[author]=discdic	
	kld = kullback_leibler_divergence
	dist=0.0
	for i in list(range(2)):
		j=1-i
		dist += kld(twomodels[kwargs['authors_list'][i]],twomodels[kwargs['authors_list'][j]],tot)
			
	return dist			
				
				
				
				
				
				
				
				
				
				
				
				
