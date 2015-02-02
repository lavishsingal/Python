# if else use

x = int(input("Enter any number"))

if x < 0 :
	print("negative number is conveted to zero")
	x = 0
elif x == 0:
	print("x=0")
else:
	print(x)

#for use
words = ['cat' , 'dog' , 'cow is nice']
for w in words:
	print(w , len(w))

# using range 
for i in range(1 , 10):
	print(i,end=" ")
print('\n')

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(i , a[i])

# using list
list(range(5))

#defining function
def fib(n):
	a , b = 0 ,1
	while(a < n):
		print(a , end=" ")
		a , b = b , a+b
	print()
# calling function fib created above

fib(100)
""" assigning some value """
f = fib
f(100)

# appending to the array , the list of nums

def fib2(n):
	result = []
	a,b = 0 ,1
	while(a < n):
		result.append(a)
		a , b = b , a+b
	return result

result = fib2(100)
print(result)
for i in result:
	print(i)	

# defining default arguments for in functions
def ask_ok(prompt , tries = 5 , complaint="Yes of no please??"):
	while True:
		ok = input(prompt)
		if ok in ('y' , 'ye' , 'yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		tries -= 1
		if tries < 0:
			raise OSError('bad user')
		print(complaint)

ask_ok("nopeee")




