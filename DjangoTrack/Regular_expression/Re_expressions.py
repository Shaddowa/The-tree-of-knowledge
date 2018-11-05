import re #Regular expression module
names_file = open("names.txt",encoding="utf-8")
data = names_file.read() #Reads the file
names_file.close() #Closes the file

print(re.match(r'Andrew, data))    
#r' == raw string
#re.match (Finding words at the start of the string) = 2 arguments
#(string we want to match, data where we match the string) 

#BASIC               
""" 
\w (Matches any word) \W (Matches anything that isn't words)
\s (Matches any whitespace) \S (Matches anything that isn't whitespace)
\d (Matches any number from 0 to 9) \D (Matches anything that isn't a number)
\b (Matches any word boundaries or edges of a word) \B (Matches anything that isn't the edge of a word)
"""

print(re.search(r'\(\d\d\d\)-\d\d\d\d, data))
#re.search (Finding words anywhere in the string)
#We use \ in front of the parentheses *\(\d\d\d\)* because if we don't, they act as a group which we don't want.

#COUNTS
""""
{3,}  Something that occours 3 or more times
{3,5} something that occours 3, 4 or 5 times
?     something that occours 0 or 1 times
*     something that occours at least 0 times
+     something that occours at least once
""""

print(re.findall(r'\w+\d+, data))  
#re.findall() finds all the instances of what we are trying to match against.

                 
#SETS & Flags
"""
[apple] -> Matches apple
[a-z] -> Matches any lovercase letters from a to z
[^2] -> Matches anything that is not 2



If adding more flags use *|* in the middle of the flags.

re.IGNORECASE || re.I -> Ignores the CASING, alloweing Uppercase and Lowercase to pass the matching

re.VERBOSE || re.X -> Ignores all of the spaces, tabes, half-tabs, that are in our patterns
re.MULTILINE || re.M -> Allow patterns spanning multiple lines in our editor
"""


#Groups                 
"""
line = re.search(r'''
  ^(?P<name>[-\w]*,\s[-\w]+)\t #Last and first names
  (?P<email>[-\w\d.+]+@[-\w\d.]+)\t #Email
  (?P<Phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #Phone
  (?P<job>[\w\s]+,\s[\w\s.]+)\t? #Job and company
  (?P<twitter>@[\w\d]+)?$ #Twitter

''', data, re.X|re.M)

print(line)
print(line.groupdict())
"""


#Comiling Regular expressions and subgroups
"""                 
line = re.compile(r'''
  ^(?P<name>(?P<last>[-\w]*),\s(?P<first>[-\w]+))\t #Last and first names
  (?P<email>[-\w\d.+]+@[-\w\d.]+)\t #Email
  (?P<Phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #Phone
  (?P<job>[\w\s]+,\s[\w\s.]+)\t? #Job and company
  (?P<twitter>@[\w\d]+)?$ #Twitter

''', re.X|re.M)

print(re.search(line,data).groupdict())
print(line.search(data).groupdict())

for match in line.finditer(data):
    print(match.group('name'))
    print('{first} {last} <{email}>'.format(**match.groupdict()))
"""