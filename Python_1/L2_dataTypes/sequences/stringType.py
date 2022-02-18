

str = ' This Is a String i i '

print(len(str))
print(str.lower())
print(str.upper())
print(str.count('i'))  # number that the current string contains the sequence of symbols 'i'

str2 = 'this is lower case string'
print(str2)
str2 = 'this is lower case string with capitalize function'
print(str2.capitalize())

str = 'line'
print(str)

strInt = "123456" # number only
print(strInt.isnumeric())
strAbc = "letters" # letters only
print(strAbc.isalpha())
strAbcNumbs = "abs123456" # letters and/or numbers only, no spaces
print(strAbcNumbs.isalnum())

for c in str:
    print(c)
