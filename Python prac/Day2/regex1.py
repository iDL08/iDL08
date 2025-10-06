import re

text = "this is to test the regex function"

pattern = r"regex"

search = re.search(pattern, text)

if search:
    print("Match found:", search.group())
else:
    print ("Match not found")