# Python Operators

Python operators are symbols that perform operations on variables and values. Here are some of the types of operators commonly used in Python:

## Arithmetic Operator
Arithmetic operators are used to perform mathematical operations. 
Examples include addition (+), subtraction (-), multiplication (*), division (/), etc.

## Relational/Comparison Operator
Relational operators are used to compare two values. 
Examples include equal to (==), not equal to (!=), greater than (>), less than (<), etc.

## Assignment Operator
Assignment operators are used to assign values to variables. Examples include equals (=), plus equals (+=), minus equals (-=), etc.

## Logical Operator
Logical operators are used to combine conditional statements. Examples include and, or, not.

## Membership Operator
Membership operators are used to test if a sequence is present in an object. Examples include in, not in.

## Identity Operator
Identity operators are used to compare the memory locations of two objects. Examples include is, is not.

## Bitwise Operator
Bitwise operators are used to perform bitwise operations on integers. Examples include AND (&), OR (|), XOR (^).

### Note:
- Variable declaration is implicit in Python.
- Operator precedence: not > and > or.

## Escape Sequence of Characters 
Tabs in the string (/t)

## Slicing
Accessing parts of a string
- Syntax: str[starting_index:ending_index]

## String Functions
- str.endswith("er.") # Returns true if string ends with substr
- str.capitalize() # Capitalizes the 1st Characters
- str.replace(old, new) # replaces all occurances of old with new
- str.find(word) #returs 1st index of 1st occurance
- str.count("am") # Counts the occurance of substr in string

## Lists in Python
- A built-in data type that stores set of values
- It can store elements of different data types (Integer, Float, string etc)
- Strings are immutable in Python while lists are mutable

  ## List Methods
  list = [50,60,70]
- list.appent(80) # add one element at the end [50,60,70,80]
- list.sort() # Sorts in ascending order [1,2,3]
- list.sort(reverse=True) # sorts in descending order [3,2,1]
- list.reverse() #reverse the list
- list.insert(idx, el) #insert element at index
- list.remove(1) #removes first occurance of the element
- list.pop(idx) # removes element at index
  
  ## Tuples in Python
 - A built-in data type that lets us create immutable sequence of values
   tup = (87,65,33,95,76)
   tup[0] = 75 # It is not allowed in Python
  - tup.index(ele) # returns index at first occurance tup.index(1) is 1
  - tup.count(el) # counts total occurances tup.count(1) is 2.

## Function is Python

  
