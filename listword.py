import sys
import EM.py


if __name__ == "__main__":


	## findng the top 10 candidates for each given word
	## argv[0] is the english corpus
	## argv[1] is the french corpus
	## argv[2] is the list of english words

	em = EM.EM(sys.argv[0], sys.argv[1], 1, 5)

	

	

