import numpy as np
from fractions import Fraction as frac

## =============  Functions  ==================================
def getConstant(x,y):
	n = np.shape(y)[0]
	pyramid = np.zeros([n,n])
	pyramid = pyramid.astype('object')
	pyramid[::,0] = y
	for j in range(1,n):
		for i in range(n-j):
		  pyramid[i][j] = frac((frac(pyramid[i+1][j-1]) - frac(pyramid[i][j-1])),(frac(x[i+j]) - frac(x[i])))
	return pyramid[0]

def changeArrayType(arr):
	"""
	Calculate constant

	"""
	for i in range(0, len(arr)):
		if '/' in arr[i]:
		  arr[i] = frac(arr[i])
		else:
		  arr[i] = int(arr[i])
	return arr

def getFormula(constant_vector):
	'''
	Get Formula from a constant
	'''
	print("Formula: ", end = '')
	formula=[]
	for index , coef in enumerate(constant_vector):
		coef = str(coef)
		print(f'{coef}', end = "")
		try:
			if '/' in str(coef):
			# print(f"frac('{coef}')")
				formula.append(f"frac('{coef}')")
			else:
				formula.append(f'{coef}')
		except:
			print('err')
			formula.append(f'{coef}')

		if index > 0:
			for i in range(index):
				print(f'(x - {x[i]})', end = '')
				x[i]=str(x[i])
				try:
					if '/' in str(x[i]):
					# print(frac(x[i]))
						formula.append(f"(x - frac('{x[i]}'))")
					else:
						formula.append(f'(x - {x[i]})')
				except:
					print('err')
					formula.append(f'(x - {x[i]})')

		if index < len(constant_vector) - 1:
			print(" + ", end = "")
			formula.append(" + ")
	return formula

## ===========================  Main Program =========================


while True:
	x = []
	y = []

	## GET Input
	print("Enter the values of x: (eg: 1 1/2 3 5 7)")
	x = [i for i in input().split()]

	print("Enter the values of y: (eg: 3 -10 2 3/2 1)")
	y = [i for i in input().split()]

	## Change input to ArrayType
	x = np.array(changeArrayType(x))
	y = np.array(changeArrayType(y))

	## Get Constant Vector
	constant_vector = getConstant(x,y)
	print('The Constant Vector = ',constant_vector)

	# Get value Y from X based on Polynomial Equation
	formula = getFormula(constant_vector)
	test1 = ''.join(formula).replace('(','*(').replace('x','a').replace('c*','c')
	print(' ')
	# expression to be evaluated
	expr = test1
	while True:
		# variable used in expression
		a = input("Enter the value of x:")
		if '/' in a:
		  a=frac(a)
		else:
		  a = int(a)

		# evaluating expression
		Y = eval(expr)

		print('Y =', Y)

		ans = input("Do you want to test with other value of x? y/n : ")
		if ans =='y':
			continue
		else:
			break
	ans = input("Do you want to try with other data points? y/n : ")
	if ans == 'y':
		continue
	else:
		break
