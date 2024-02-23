def maximum(numbers):
    #pass # pass means "do nothing", add your code here
    max_value = 0
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def main():
    print("Let us find the maximum value from the following list:")
    list_of_nums = [1,2,3]
    max_value = maximum(list_of_nums)
    print(max_value)

    print("Let us find the maximum value from another list:")
    list_of_nums = [-1, -2, -3]
    max_value = maximum(list_of_nums)
    print(max_value)
    
print(f"Value of __name__ is {__name__}")

if __name__ == "__main__":
    main()
