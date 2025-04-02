import re
from custom_exceptions import NegativeNumberException

def string_calculator(string_of_nums):
    try:
        if not string_of_nums.strip():
            # empty string
            return 0
        else:
            # clean data: only accept csv numbers
           
            # default delimiter
            delimiter = ","
            delimiter_pattern = r"^//(.*?)\n"
            delimiter_exists = re.match(delimiter_pattern, string_of_nums)

            if delimiter_exists:
                delimiter_string, string_of_nums = string_of_nums.split('\n', 1)
                delimiter = delimiter_string[2:]

            postive_numbers = []
            negative_numbers = []
            for line in string_of_nums.split("\n"):
                for num in line.split(delimiter):
                    if num=="":
                        raise ValueError("Invalid Input")
                    if int(num)>0:
                        postive_numbers.append(int(num))
                    else :
                        negative_numbers.append(int(num))
            if negative_numbers:
                raise NegativeNumberException(negative_numbers)
            return sum(postive_numbers)
    except Exception as e:
        raise e


    
