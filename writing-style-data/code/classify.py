def classif(textsamplepath,modelsinitpath,authorlist,order):
	from getscore import calcscore
	#template: def calcscore(classpath1,classpath2,classpath3,tx):
	
	def calc_appropt_score(t1,t2,t3,t4,tex,scale_factor):
		if order is

	#print author

	scorelist=[]
	totlist=[]

	scalelist=[]
	maxsize=0
	
	for author in authorlist:
		i = open(modelsinitpath+author+str(1),'r')
		num = i.read().split()[0]
		scalelist.append(int(num))
		if int(num) > maxsize:
			maxsize = int(num)
	minnum=maxsize
	for author in authorlist:
		i = open(modelsinitpath+author+str(1),'r')
		num = i.read().split()[0]
		scalelist.append(int(num))
		if int(num) < minnum:
			minnum = int(num)

	for author in authorlist:
		f1 = open(modelsinitpath+author+str(1),'r')
		f2 = open(modelsinitpath+author+str(2),'r')
		f3 = open(modelsinitpath+author+str(3),'r')
		f4 = open(modelsinitpath+author+str(4),'r')
		size = f1.read().split()[0]
		f1 = open(modelsinitpath+author+str(1),'r')
		tx = open(textsamplepath,'r')
		scl = float(size)/float(maxsize)
	
		calc_appropt_score(f1,f2,f3,f4,tx,scl)
		
		scorelist.append(float(retlist[0]))
		totlist.append(float(retlist[1]))



	tx = open(textsample,'r')
	allwrd = len(tx.read().split())
	
	print '\n',tx,' size of text to be processed: ',allwrd,'\n'

	return zip(scorelist,author,totlist) #,totlist#,author[mxind]

#print classify()
	#############################

	## REGEX Page .* Harry Potter and the Philosophers Stone - J.K. Rowling
	#       
	#32043: hp3

	#mxind = scorelist.index(sorted(scorelist)[len(scorelist)-1])
