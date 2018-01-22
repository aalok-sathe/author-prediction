def calcscore0(classpath1,tx,scl): #classpath are pointers to actual files in a specific directory e.g. open file 'Desktop/data1', mode 'r' at 0x7f1e971655d0
		
	retlist=[]

	def remuni(text):                    #### Remove Unicode chars
    		return ''.join(i for i in text if ord(i)<128)
	
	import math


	cl1 = (classpath1.readlines())#.split('\n')          # corpus unigrams


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
	
#########
	def scor(txt,cl1):
		nic = 0.0
		score = 0.0
		
		lnbase = 85.0

	
		for x in range(len(txt)):				#word[3+] order=2 (prev 2 in context)
			
			g1 = get1(txt[x],cl1)
		
			if (g1):
				score+=math.log(float(g1)/float(totcount1),lnbase)
			else:
				score+=math.log(scl/float(totcount1),lnbase)

		return score

	
	retlist.append(scor(text,cl1))   ### Primary scoring function
	retlist.append(totcount1)		### total count
	#print retlist

##### Main FUNCTION RETURN DATA
	return retlist
		
		

		
	
