import re

string = "pccccccccccccccccccccppeng123"
regex_str ='.*(p.*p).*'
match = re.match(regex_str, string)
print(match.group(0))
print(match.group(1))
# print(match.group(2))


