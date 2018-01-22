#!/usr/bin/env python3
###############################################################################
info='''Requirements: Python 3.3 and above; modules: nltk, numpy. Tested on Ubuntu 16.04\n
Title: Predicting the author as per the writing style using Markov model of language.\n
This software is provided as-is, without any warranty. You may use this code with modifications.
However, you must distribute the code and any modifications you make
in this code under the same license (copy this entire statement in your header).\n
Name of the author must be cited. Copyright (C) Aalok S., 2016-2017. aalok.sathe+py@gmail.com\n'''
################################################################################
print(info)
import sys, os

rootitems = {0:"Whatis",1:"Train",2:"Identify",3:"Switch project",4:"Manage ongoing projects"}
def root():
	os.system('clear')
	print(info)
	for i in range(5):
		print(i,rootitems[i])
	choice=input('\n>>>')
	
	
root()
