def find_fibonacci_value(number_value):
	if number_value == 2 or number_value == 1:
		fib_value = 1
	else:
		fib_value = find_fibonacci_value(number_value - 1)+find_fibonacci_value(number_value - 2)
	return fib_value

x = int(input("input number of Fibonacci's value "))
print(find_fibonacci_value(x))
