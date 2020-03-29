from random import SystemRandom

def generate_cryptsafe_code(n, alpha):
	" Geneate a n digit cryptographically secure ID with given alphabet "
	cryptogen = SystemRandom()

	result = []

	for i in range(n):

		position = cryptogen.randrange(len(alpha))
		position = alpha[position]
		position = str(position)

		result.append(position)

	return "".join(result)
