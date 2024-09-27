fibo = int(input("Input"))
lst = []
def fibonacci(num):
        if num == num:
            lst.append(num)
        else:
            print(lst)
            return(fibonacci(num-1) + fibonacci(num-2))
        	
total = []

for i in range(fibo):
    total.append(i)
    fibonacci(i)
print(total)