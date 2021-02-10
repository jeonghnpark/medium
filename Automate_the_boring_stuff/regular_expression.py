import re

phoneRegex = re.compile(r'\d\d\d=\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phonenumber is 415-555+4242.')
aa=re.match(r'\d\d\d=\d\d\d-\d\d\d\d','My phonenumber is 415-555+4242.' )
aa.group(1)
# print('phone number found' + mo.group())

m = re.match(r"(..)+", "a1b2c3")
m.group(1)