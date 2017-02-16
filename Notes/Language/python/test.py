import re

pattern = r"(\D+\d)"

match = re.match(pattern, "asdwfwegfwgwD12312312Hi 9")

if match:
   print("Match 1")

match = re.match(pattern, "k91, 23H456!")
if match:
   print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")

pattern = r"\b(cat)\b"
match = re.search(pattern, "The cat sat!")
if match:
   print ("Match 4")

match = re.search(pattern, "We s>cat<tered?")
if match:
   print ("Match 5")

match = re.search(pattern, "We scattered.")

if match:
   print ("Match 6")


pattern = r"^(cat)$"
match = re.search(pattern, "1cat")

if match:
   print ("Match cat6")
