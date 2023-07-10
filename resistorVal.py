#! /usr/bin/env python
import math
import sys
import os
import argparse
import webcolors


colors = [
	'Black',
	'Brown',
	'Red',
	'Orange',
	'Yellow',
	'Green',
	'Blue',
	'Violet',
	'Grey',
	'White'
]

stdValsE12 = [
	10, 12, 15, 18, 22, 27,
	33, 39, 47, 56, 68, 82,
	100
]

stdValsE24 = [
	10, 11, 12, 13, 15, 16,
	18, 20, 22, 24, 27, 30,
	33, 36, 39, 43, 47, 51,
	56, 62, 68, 75, 82, 91,
	100
]

stdVals = stdValsE12


def findClosest(val) -> int:
	index =  list(map(lambda x: x>val, stdVals)).index(True)
	spot = float(stdVals[index] + stdVals[index - 1]) / 2
	if val > spot:
		return stdVals[index]
	else:
		return stdVals[index - 1]

def getBandNumbers(ohms) -> tuple:
		fract, whole = math.modf(math.log10(ohms))
		num = findClosest(int(round(10 ** (fract + 1),0)))
		expp = int(whole - 1)
		return (num * 10**expp, (int(num/10), num%10, expp))

def getBandColors(bandNumbers) -> tuple:
	return (colors[bandNumbers[0]], colors[bandNumbers[1]], colors[bandNumbers[2]])

def main() -> None:
	parser = argparse.ArgumentParser(description='find closest e24 resistor values and the color bands')
	parser.add_argument('resistorVal', metavar='N', type=int, nargs='+', help='desired resistor value')
	args = parser.parse_args()

	for ohms in args.resistorVal:
		bands = getBandNumbers(ohms)
#		print('{}'.format(bands))
		colors = getBandColors(bands[1])
		print('{} -> {}\t{}'.format(ohms, bands[0], colors))
		
if __name__ == '__main__':
	main()


