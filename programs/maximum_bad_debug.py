def maximum(numbers):
    #pass # pass means "do nothing", add your code here
    max_value = 0
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

print(maximum([-1, -2, -3])) # notice vs code is giving you a warning about variable name! 
