import re

def string_calculator(string_of_nums):
    try:
        if not string_of_nums.strip():
            # empty string
            return 0
        else:
            # clean data: only accept csv numbers
            sum_value = 0
            # default delimiter
            delimiter = ","
            delimiter_pattern = r"^//(.*?)\n"
            delimiter_exists = re.match(delimiter_pattern, string_of_nums)

            if delimiter_exists:
                delimiter_string, string_of_nums = string_of_nums.split('\n', 1)
                delimiter = delimiter_string[2:]
                print("delimiter", delimiter)
            for line in string_of_nums.split("\n"):
                for num in line.split(delimiter):
                    if num=="":
                        raise ValueError("Invalid Input")
                    sum_value+=int(num)
            return sum_value
    except Exception as e:
        raise e

    
