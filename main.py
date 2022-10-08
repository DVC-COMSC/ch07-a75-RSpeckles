
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num1) > len(num2):
	print ('False')
	sys.exit(0)

#This variable counts how many numbers from num1 in a row have been found in num2
#This is later used to check if all of the values in num2 have been found in num1
count = 0
#This is turned to 1 if all the values of num2 are found in num1
flag = 0

#the outermost for loop checks if any of the numbers in num2 are the same as the first value of num1
#if any matching values are found, the second for loop runs through the rest of num1's values to see if they all match
for i in range(len(num2)):
	if num2[i] == num1[0]:
		for j in range(len(num1)):
			#try, except used in case the values being compared would run beyong num2's length
			try:
				if count == len(num1):
					#If all the numbers in num1 are found, flag is set to 1 and the loop breaks
					flag = 1
					break
				elif num2[i+j] == num1[j]:
					count += 1
				else:
					#if all values are not found, count resets so program can continue to check for num1 in num2
					count = 0
			except IndexError:
				break


if flag == 1:
	print(True)
else:
	print(False)

# print ('True') or ('False')
