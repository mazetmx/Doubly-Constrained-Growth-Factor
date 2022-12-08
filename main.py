from utils import *

present_trips = [
	[591, 381, 152, 317 ,197, 643, 389, 364, 977, 633],
	[315, 676, 152, 518, 333, 905, 716, 471, 872, 806],
	[608, 831, 827, 959, 932, 708, 161, 921, 596, 253],
	[109, 885, 133, 770, 936, 679, 810, 953, 970, 136],
	[145, 501, 744, 189, 795, 225, 852, 207, 474, 898],
	[717, 908, 330, 985, 140, 889, 608, 464, 867, 478],
	[174, 164, 191, 832, 759, 848, 929, 683, 360, 873],
	[494, 462, 711, 208, 444, 699, 658, 105, 877, 301],
	[407, 451, 352, 682, 357, 254, 173, 807, 484, 481],
	[911, 673, 109, 580, 712, 508, 414, 236, 441, 373]
]

production = [
	[4900],
	[6000],
	[7000],
	[6500],
	[5400],
	[6600],
	[6200],
	[5300],
	[4700],
	[5200]
]

attraction = [
	[4700],
	[6300],
	[4000],
	[6300],
	[5900],
	[6600],
	[6000],
	[5500],
	[7300],
	[5500]
]

future_trips = []

a_factors = []
b_factors = []

for i in range(len(present_trips)):
	a_factors.insert(0, 1)
	b_factors.insert(0, 1)
	future_trips.insert(0, [])

number_of_iterations = 10

def main():
	# Factors calculations
	for iteration in range(number_of_iterations):
		for i in range(len(a_factors)):
			a_factors[i] = production[i][0] / calculate_denominator(present_trips, b_factors)[i]

		for i in range(len(b_factors)):
			b_factors[i] = attraction[i][0] / calculate_denominator(transpose(present_trips), a_factors)[i]

	# Future trip matrix costruction
	for i in range(len(a_factors)):
		for j in range(len(b_factors)):
			future_trips[i].insert(j ,present_trips[i][j] * a_factors[i] * b_factors[j])

	# Results display
	print(f"Number of iterations: {number_of_iterations}")

	print("a factors:")
	for i in range(len(a_factors)):
		print(f"\ta{i+1} = {a_factors[i]}")
	
	print("b factors:")
	for i in range(len(b_factors)):
		print(f"\tb{i+1} = {b_factors[i]}")

	print("Future trips matrix:")
	print("\t", future_trips)

# Program entry point
if __name__ == "__main__":
	main()