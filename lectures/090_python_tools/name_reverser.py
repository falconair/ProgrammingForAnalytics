# This library parses names and presents them in a professional, reverse name order

def name_reverse_order(full_name):
    if full_name == "": # Handle the case where an empty string is passed
        return ""
    else:
        first, last = full_name.split(' ')
        return f'{last}, {first}'
