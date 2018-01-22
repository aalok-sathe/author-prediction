def calcscore2(classpath1,classpath2,classpath3,tx,scl): #classpath are pointers to actual files in a specific directory e.g. open file 'Desktop/data1', mode 'r' at 0x7f1e971655d0
		
	retlist=[]

	def remuni(text):                    #### Remove Unicode chars
    		return ''.join(i for i in text if ord(i)<128)
	
	import math


	cl1 = (classpath1.readlines())#.split('\n')          # corpus unigrams
	cl2 = (classpath2.readlines())#.split('\n')           # corpus bigrams
	cl3 = (classpath3.readlines())				# corpus trigrams


	totcount1 = int(cl1[0].translate(None, "\n"))
	#print totcount1


	text = remuni(tx.read().translate(None, """\,?#[-/%_@=+*^]{}|'"(;)\:""").lower()).split()
	

######## 					These are functions to get the occurrences from ngram corpus(es) of a certain ngram
	def get1(w,corp):
		for x in corp:
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
	
	
#########
	def scor(txt,cl1,cl2,cl3):
		nic = 0.0
		score = 0.0
		
		lnbase = 85.0

		g1 = get1(txt[0],cl1)
	

		if (g1):			
			score+=math.log(float(g1)/float(totcount1),lnbase)
		else:
			score+=math.log(scl/float(totcount1),lnbase)

		g2 = get2(txt[0],txt[1],cl2)

	

		if (g1 and g2):						#second word order=1
			score+=math.log(float(g2)/float(g1),lnbase)
		else:
			score+=math.log(scl/float(totcount1-1),lnbase)
	
		for x in range(2,len(txt)):				#word[3:] order=2 (prev 2 in context)
			g3 = get3(txt[x-2],txt[x-1],txt[x],cl3)
			g2 = get2(txt[x-2],txt[x-1],cl2)
		
			if (g2 and g3):
				score+=math.log(float(g3)/float(g2),lnbase)
			else:
				score+=math.log(scl/float(totcount1-2),lnbase)

		return score

	
	retlist.append(scor(text,cl1,cl2,cl3))   ### Primary scoring function
	retlist.append(totcount1)		### total count

##### Main FUNCTION RETURN DATA
	return retlist
		
		

		
	
