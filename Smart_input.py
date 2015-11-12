'''Program for calling the function for smart input'''
import get_input

default_length = 30

input_type=""
length = 0
action = "lenient"

ch = raw_input("What type of Input do you Want (1 - Name   2-Number)   :   ")
if ch == "1":
	input_type = "name"
elif ch =="2":
	input_type = "number"

d=raw_input("\n\nEnter the Max Length : ")
try:
	length = int(d)
except:
	length = default_length

if input_type == "number":
	action = raw_input("\n\nEnter the Mode for length (strict or lenient) :")
	action = action.lower()

print ""

print get_input.get_input(input_type,length,action)