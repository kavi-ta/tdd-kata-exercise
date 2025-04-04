import re
from custom_exceptions import NegativeNumberException

def string_calculator(string_of_nums):
    try:
        if not isinstance(string_of_nums, str) :
            raise ValueError("Invalid input. Input should be a string")
        if not string_of_nums.strip():
            # empty string
            return 0
        else:
            # clean data: only accept csv numbers
           
            # default delimiter
            delimiter = ","
            delimiter_pattern = r"^//(\[.*?\])+\n"
            delimiter_exists = re.match(delimiter_pattern, string_of_nums)

            if delimiter_exists:
                delimiter_string, string_of_nums = string_of_nums.split('\n', 1)
                delimiter = re.findall(r"\[(.*?)\]",delimiter_string)
            postive_numbers = []
            negative_numbers = []
            split_pattern = "|".join(map(re.escape, delimiter))
            for line in string_of_nums.split("\n"):

                for num in re.split(split_pattern, line):
                    num = num.strip()
                    if not num:
                        raise ValueError("Invalid Input")
                    if not num.lstrip('-').isdigit():
                        raise ValueError("Invalid Input")
                    num = int(num)
                    if num>=0 and num<=1000:
                        postive_numbers.append(num)
                    elif num<0:
                        negative_numbers.append(num)
            if negative_numbers:
                raise NegativeNumberException(negative_numbers)
            return sum(postive_numbers,0)
    except Exception as e:
        raise e


    
