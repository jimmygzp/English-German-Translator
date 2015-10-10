import gzip, sys
from collections import defaultdict


class EM:

	def __init__(self, e_file, f_file, mode, iterations):

		## initialize corpus
		self.e_corpus = gzip.open(e_file, 'rb')
		self.f_corpus = gzip.open(f_file, 'rb')


		##initialize default count files, value to 0
		self.cef = defaultdict{int}
		self.ce = defaultdict{int}
		self.cjilm = defaultdict{int}
		self.cilm = defaultdict{int}

		## initialize Foreign word vocabulary set (most likely useless)
		self.vocabulary = set()

		## initialize t value (only need to run over foreign words)
		self.t_init = self.initial_t()
		
		## start the algorithm!
		self.run(iterations, mode)
	

	def initial_t(self): ## run once;

		self.vocabulary.add("")

		## make sure we have the NULL word included

		for l in self.g_corpus:
			sentence = l.strip().split()
			for a in sentence:
				self.vocabulary.add(a)

		return float( 1 / len(self.vocabulary))


	def initial_q(self, l):

		return float (1 / (l+1))



	def t(self, f, e, run):

		## Any run that's not the first gives you the ML result

		if run == 1:
			return self.t_init
		else:
			return float (self.cef[(e, f)] / self. ce[e])


	def q(j, i, l, m, run):

		if run == 1:
			return self.initial_q(l)
		else:
			return float (self.cjilm[(j, i, l, m)] / self.cilm[(i,l,m)]



	def run(self, iterations, mode):
		
		runs  =  0 ## having not run at all
		
		## this needs to be kept independently of teh while loop ##

		while runs < iterations:

			## setting default dictionary values for new counts##


			## we need to make a clean, dummy copy of all the count dictionaries
			## and put them back in the end, to make sure the d{} are not contaminated on the run

			t_cef = self.cef.copy()
			t_ce = self.ce.copy()
			t_cjilm = self.cjilm.copy()
			t_cilm = self.cilm.copy()


			delta = {} ## need a clean slate for delta values

			k = 1 ## tracking which line we are at, to help track delta

			for e in self.e_corpus:
				
				## while we get a new line from e_corpus, we also get a new line from f_corpus ##
				f = self.f_corpus.readline()
				
				## split the french word and english word into arrays, with index 0 = "NULL"
				fn[0] = ""
				en[0] = ""
				fn[len(fn):] = f.split()
				en[len(fn):] = e.split()

				## take note of their length
				m = len(fn)
				l = len(en)

				## note: we cannot simply set t and q to be dictionaries; 
				##we need to define accessor functions to make things efficient
				##because they are defined to be functions of counts (dictionaries)

				for i in range(1, m): ## for all French words

					for j in range(0, l): ## for all English words

						## each individual word logged
						fi = fn[i]
						ej = en[j]

						if (k, i, j) not in delta:
							## if d(k,i,j) is not yet available/calculated
							if mode == '1':
								## if in IBM MODEL I
								
								t_sum = 0
								for s in range(0, l): ## this way, "NULL" is included
									t_sum = t_sum + self.t(fi, en[s], run)
								delta.set((k, i, j)) = d = float (self.t(fi, ej) / t_sum)
							else:
								pass
						else:
							if mode == '1':
								d = delta[(k, i, j)]
							else:
								pass

						## add the delta values to the count dictionaries
						t_cef[(ej, fi)] += d
						t_ce[ej] += d
						t_cjilm[(j, i, l, m]+= d
						t_cilm[(i, l, l)] += d

				k++

			## copy back the stock count after one run.
			self.cef = t_cef.copy()
			self.ce = t_ce.copy()
			self.cjilm = t_cjilm.copy()
			self.cilm = t_cilm.copy()

			## count up run
			runs++

	











						















			





