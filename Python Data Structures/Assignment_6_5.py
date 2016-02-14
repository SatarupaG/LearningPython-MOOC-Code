text = "X-DSPAM-Confidence:    0.8475"
# Code to find the position of the space in the string
space_position = text.find(" ")
# Code to extract out the desired portion out of the string
number = text[space_position:]
# Code to format the string to a float number
formatted_number = float(number)
# Code to display the number
print formatted_number
