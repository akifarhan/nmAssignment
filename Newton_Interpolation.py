#!/usr/bin/env python
# coding: utf-8

import numpy as np
from fractions import Fraction as frac
import time

def getConstant(x,y):
	n = np.shape(y)[0]
	pyramid = np.zeros([n,n])
	pyramid = pyramid.astype('object')
	pyramid[::,0] = y
	for j in range(1,n):
		for i in range(n-j):
		  pyramid[i][j] = frac((frac(pyramid[i+1][j-1]) - frac(pyramid[i][j-1])),(frac(x[i+j]) - frac(x[i])))
	return pyramid[0]


def addArray(arr,new_value):
  try:
			if '/' in new_value:
			  new_value = frac(new_value)
			else:
			  new_value = int(new_value)
  except:
    new_value = frac(new_value).limit_denominator()
  return np.append(arr,  new_value)

def changeArrayType(arr):
	"""
	Calculate constant

	"""
	for i in range(0, len(arr)):
		try:
			if '/' in arr[i]:
			  arr[i] = frac(arr[i])
			else:
			  arr[i] = int(arr[i])

		except:
			arr[i] = frac(arr[i]).limit_denominator()
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


def findnewX(j):
    total = 0
    for index in range (len(x) - 1):
        if j > index and j < index + 1:
            diff = x[index + 1] - x[index]
            cariX = j - index
            newX = (cariX * diff) + x[index]
    print("Location ",j)
    try:
        print("Value of X at that location:", newX)

        return newX
    except:
        print("Value of X at that location:", x[int(j)])
        return x[int(j)]

def displayResult():
    ## Get Constant Vector
  start_time = time.time()
  constant_vector = getConstant(x,y)
  print('The Constant Vector = ',constant_vector)

  # Get value Y from X based on Polynomial Equation
  formula = getFormula(constant_vector)
  print('')
  print(f"Excecution Time: {time.time()-start_time} seconds ")
  test1 = ''.join(formula).replace('(','*(').replace('x','a').replace('c*','c')
  print(' ')

  # expression to be evaluated
  expr = test1
  while True:
      # variable used in expression
      selection = input("Enter '1' for value of X, '2' for location of x, 'f' for skip: ")
      print(selection)
      if selection == '1':
          a = input("Enter the value of x:")
          try:
              if '/' in a:
                a=frac(a)
              else:
                a = int(a)
          except:
              a = frac(a).limit_denominator()
      elif selection == '2':
          loc = float(input("Enter the location of x:"))
          a = findnewX(loc)
          try:
              if '/' in a:
                a=frac(a)
              else:
                a = int(a)
          except:
              a = frac(a).limit_denominator()
      elif selection == 'f':
        break;
      # evaluating expression
      Y = eval(expr)

      print('Y =', Y)

      ans = input("Do you want to test with other value of x or other location of x? y/n : ")
      if ans =='y':
          continue
      else:
          break

# In[6]:


## ===========================  Main Program =========================
while True:
    x = []
    y = []

    ## GET Input
    print("Enter the values of x: (eg: 1,1/2,3,5,7)")
    x = [i for i in input().split(",")]
    print(x)
    print("Enter the values of y: (eg: 3,-10,2,3/2,1)")
    y = [i for i in input().split(",")]
    print(y)

    ## Change input to ArrayType
    x = np.array(changeArrayType(x))
    y = np.array(changeArrayType(y))

    displayResult()

    while True:
      ans = input("Do you want to add data points? y/n : ")
      if ans =='y':
        b = input("Enter the value of x: ")
        x = addArray(x, b)
        c = input("Enter the value of y: ")
        y = addArray(y, c)
        displayResult()
      else:
          break

    ans = input("Do you want to try with other data points? y/n : ")
    if ans == 'y':
      continue
    else:
      break





