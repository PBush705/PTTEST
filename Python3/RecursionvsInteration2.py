fibo = int(input("Input"))
lst = []
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return(fibonacci(num-1) + fibonacci(num-2))

for i in range(fibo):
    lst.append(fibonacci(i))
print(lst)