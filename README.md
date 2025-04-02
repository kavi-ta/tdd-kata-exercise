**TDD in Python - String Calculator**

This repository demonstrates **Test-Driven Development** (TDD) in Python by implementing a String Calculator using **pytest**.

**Implementation Details**

Function: add(num_string)

Handles empty strings by returning 0

Extracts custom delimiters if defined

Uses re.split() to split numbers based on multiple delimiters

Converts extracted values to integers and computes the sum

Raises a custom error for negative numbers and value error for invalid inputs
