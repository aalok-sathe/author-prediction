def getauthor(textsamplepath,modelsinitpath,authorlist,order):
	#unified function
	from classify import classif

	retlist = classif(textsamplepath,modelsinitpath,authorlist,order) #,score,author,tot
	retlist.sort()
	
	if len(retlist):
		closestauthor = retlist[len(retlist)-1][1]
	
	st1 = 'The text looks like it has been written by: # %s #\n' % closestauthor
	st2 = 'rather than '
	st3 = 'The scores are (least to best): '
	print st1

	return closestauthor	
	#for i in range(len(retlist)):
	#	print str(retlist[i][1]) + ' score --> ' + str(retlist[i][0]) + ' corpus size: ' + str(retlist[i][2])




# REDUNDANT CODE
	#first=1
	#maxscore=0
	#mxind=0
	#for i in range(len(retlist)):
	#	if first:
	#		maxscore=retlist[i][0]
	#		mxind=i
	#		first=0
	#	else:
	#		if retlist[i][0]>maxscore:
	#			maxscore=retlist[i][0]
	#			mxind=i
	#print st1 + str(retlist[mxind][1]) + st2
	#for i in range(len(retlist)):
	#	if not i == mxind:
	#		print retlist[i][1]
	#print '\n'
	
