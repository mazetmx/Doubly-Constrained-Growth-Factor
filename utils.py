####################
# Helper functions #
####################

def transpose(m):
	'''
	Transposes matrix m
	'''
	return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def within_margin(new_value, old_value, margin):
	'''
	Checks if the new value is within margin of error of the old valus
	'''
	return (abs((new_value - old_value) / old_value) * 100) <= margin

def calculate_denominator(trips, factors):
	'''
	Used to add the divisor of the selected factors matrix
	'''
	denominator = []
	for i in range(len(trips)):
		denominator.insert(i, 0)
		for j in range(len(trips)):
			denominator[i] += trips[i][j]*factors[j]

	return denominator