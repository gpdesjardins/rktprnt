import re

letters = "abC"
numbers = "123"

letter_regex = re.compile('[a-zA-Z]+')
captured_letters_string = letter_regex.match(letters).group()
print "letters: " + captured_letters_string
print type(captured_letters_string)

#following line will fail if uncommented.. can convert "abc" to int
#captured_letters_int = int(captured_letters_string)
#you can use a try / catch to avoid exception from attempting to cast "Abc" to int

try:
    captured_letters_int = int(captured_letters_string)
except:
    #handle or disregard strings that you don't want
    print "cannot convert abc to int"
else:
    #handle numbers which are useful variable values for you
    print "here are your numbers " + captured_letters_int

number_regex = re.compile('[0-9]+')
captured_numbers_string = number_regex.match(numbers).group()
print "numbers: " + captured_numbers_string
print type(captured_numbers_string)
captured_numbers_int = int(captured_numbers_string)
print type(captured_numbers_int)