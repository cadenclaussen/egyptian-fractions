import math

fraction_first = input("What is the fraction? ").split("/")

numer = fraction_first[0]
denom = fraction_first[1]

print(numer + "/" + denom)

frac_list = []

if numer > denom/2:
	for i in range(denom):
		if i * numer