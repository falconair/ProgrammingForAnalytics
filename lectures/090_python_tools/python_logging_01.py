
import logging

logging.basicConfig(level=logging.INFO)


def maximum(numbers):
    #pass # pass means "do nothing", add your code here
    max_value = 0
    for num in numbers:
        logging.debug(f"num:{num}, max_value:{max_value}")
        if num > max_value:
            logging.debug("max > max_value branch taken. Setting new max_value")
            max_value = num
    return max_value

def main():
    logging.info("Let us find the maximum value from the following list:")
    list_of_nums = [1,2,3]
    max_value = maximum(list_of_nums)
    logging.info(max_value)

    logging.info("Let us find the maximum value from another list:")
    list_of_nums = [-1, -2, -3]
    max_value = maximum(list_of_nums)
    logging.info(max_value)
    
if __name__ == "__main__":
    logging.warning(f"This program is being run from the command line")
    main()
