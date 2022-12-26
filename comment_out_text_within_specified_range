f = open('input.txt','r')
text = f.read()
f.close()

#print text

minimum=3
maximum=5
import re

#Split up text with newline
newlines = re.split('\n+',text)

count = 0

for line in newlines:
    count += 1
    if count >= minimum and count <=maximum:
        comment = "#" + line
        print(comment)
    else:
        print(line)
