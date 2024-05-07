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