import logging.config
import json
import os

with open("logging.json", "r") as f:
        json_config = json.load(f)
        logging.config.dictConfig(json_config)

fname = os.path.basename(__file__)
log = logging.getLogger(fname) # <= This lines makes the logger name more useful

def maximum(numbers):
    #pass # pass means "do nothing", add your code here
    max_value = 0
    for num in numbers:
        log.debug(f"num:{num}, max_value:{max_value}")
        if num > max_value:
            log.debug("max > max_value branch taken. Setting new max_value")
            max_value = num
    return max_value

def main():
    log.info("Let us find the maximum value from the following list:")
    list_of_nums = [1,2,3]
    max_value = maximum(list_of_nums)
    log.info(max_value)

    log.info("Let us find the maximum value from another list:")
    list_of_nums = [-1, -2, -3]
    max_value = maximum(list_of_nums)
    log.info(max_value)
    
if __name__ == "__main__":
    log.warning(f"This program is being run from the command line")
    main()
