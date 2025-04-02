def string_calculator(string_of_nums):
    try:
        if not string_of_nums.strip():
            # empty string
            return 0
        else:
            # clean data: only accept csv numbers
            sum_value = 0
            for line in string_of_nums.split("\n"):
                print("line", line)
                for num in line.split(","):
                    if num=="":
                        raise ValueError("Invalid Input")
                    sum_value+=int(num)

            return sum_value
    except Exception as e:
        raise e

    
