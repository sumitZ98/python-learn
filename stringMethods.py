import re
# Concatenation in string

Fname = "Sumit"
Lname = "Mitra"
print(Fname + " " + Lname);

#string length 
length = len(Fname);
print(length);

#Lower to upper and upper to lower
uppercase = Fname.upper()
lowercase = Lname.lower()
print("uppercase:", uppercase)
print("lowercase:", lowercase)

#string replace 

text = "Today is a good day"
newText = text.replace("good", "great")
print("modified text:", newText);

#string split 

text = "today is a very good day to go out"
words = text.split()
print("Words:", words);

#string strip

text = "      there are some spaces      "
newText = text.strip()
print("New text:", newText)

# Sub string 

text = "python is a very cool language"
substring = "cool"
if substring in text:
    print(substring,"found in the text")

#other than normal +,-,*,// there is rounding off

num1 = 1.2547893
res = round(num1,3)
print(res);

#absolute value

num = -25 
res = abs(num)
print(res)

# Regex match and search
text = "The quick brown fox"
pattern = r"fox"
# search = re.match(pattern, text)
search = re.search(pattern,text)
if search:
    print("pattern found", search.group())
else: 
    print("pattern not found")

# replace using regex

text = "The quick brown fox"
pattern = r"brown"
replacement = "green"

newText = re.sub(pattern, replacement, text)
print(newText)

#split

text = "a,b,c,d,e"
pattern = r","

res = re.split(pattern, text)
print(res)