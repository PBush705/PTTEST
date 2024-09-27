lst = []
fibo = int(input())
for i in range(fibo):
    def fibonacci(num):
        if num < 1:
            return lst.append(num)
        else:
            return(fibonacci(num-1) + fibonacci(num-2))

print(lst)


fibonacci(fibo)
