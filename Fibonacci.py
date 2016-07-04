def fib(n):
	first = 0
	second = 1
	for x in range(n):
		if(x<=1):
			print x
		else:
			temp = first+second
			first,second = second,temp
			print temp

if __name__ == "__main__":
	fib(7)


	