def calcscore3(classpath1,classpath2,classpath3,classpath4,tx,scl): #classpath are pointers to actual files in a specific directory e.g. open file 'Desktop/data1', mode 'r' at 0x7f1e971655d0
		
	retlist=[]

	def remuni(text):                    #### Remove Unicode chars
    		return ''.join(i for i in text if ord(i)<128)
	
	import math


	cl1 = (classpath1.readlines())#.split('\n')          # corpus unigrams
	cl2 = (classpath2.readlines())#.split('\n')           # corpus bigrams
	cl3 = (classpath3.readlines())				# corpus trigrams
	cl4 = (classpath4.readlines())				 # corpus 4-grams


	totcount1 = int(cl1[0].translate(None, "\n"))
	#print totcount1


	text = remuni(tx.read().translate(None, """\,?#[-/%_@=+*^]{}|'"(;)\:""").lower()).split()
	

######## 					These are functions to get the occurrences from ngram corpus(es) of a certain ngram
	def get1(w,corp):

		for x in corp:
			#print x.split()[0]
			if (x.split()[0]==w):
				return scl+float(x.split()[1])
		return scl

	def get2(w1, w2, corp):

		for y in corp:
			if (w1==y.split()[0] and w2==y.split()[1]):
				return scl+float(y.split()[2])
		return 0

	def get3(w1, w2, w3, corp):

		for z in corp:
			if (w1==z.split()[0] and w2==z.split()[1] and w3==z.split()[2]):
				return scl+float(z.split()[3])
		return 0
	def get4(w1,w2,w3,w4,corp):
		for w in corp:
			if (w1==w.split()[0] and w2==w.split()[1] and w3==w.split()[2] and w4==w.split()[3]):
				return scl+float(w.split()[4])
	
	
#########
	def scor(txt,cl1,cl2,cl3,cl4):
		nic = 0.0
		score = 0.0
		
		lnbase = 85.0

		g1 = get1(txt[0],cl1)
		g2 = get2(txt[0],txt[1],cl2)
		g3 = get3(txt[0],txt[1],txt[2],cl3)
		
		if (g1):						
			score+=math.log(float(g1)/float(totcount1),lnbase)
		else:
			score+=math.log(scl/float(totcount1),lnbase)

		if (g1 and g2):						
			score+=math.log(float(g2)/float(g1),lnbase)
		else:
			score+=math.log(scl/float(totcount1-1),lnbase)
			
		if (g2 and g3):
			score+=math.log(float(g3)/float(g2),lnbase)
		else:
			score+=math.log(scl/float(totcount1-2),lnbase)
			
		for x in range(3,len(txt)):
			g4 = get4(txt[x-3],txt[x-2],txt[x-1],txt[x],cl4)				#word[4:] order=3 (prev 3 in context)
			g3 = get3(txt[x-3],txt[x-2],txt[x-1],cl3)
				
			if (g3 and g4):
				score+=math.log(float(g4)/float(g3),lnbase)
			else:
				score+=math.log(scl/float(totcount1-3),lnbase)

		return score


	#print 'total data in corpus ',totcount1
	
	retlist.append(scor(text,cl1,cl2,cl3,cl4))   ### Primary scoring function
	retlist.append(totcount1)		### total count
	#print retlist

##### Main FUNCTION RETURN DATA
	return retlist
		
		

		
	
