import re,os

'''
f = open('friends101.txt','r')
s101 = f.read()

# print(s101)
f.close()

print(s101[:100])
# Monica: 다음에 아무 문자나 반복되는 패턴을 찾아 List로 반환.
monica = re.findall(r'Monica:.+', s101)

# print(Line[:3])

Mon = ""
f = open('monica.txt','w')
for i in monica:
    monica += i+'\n'
    f.write(Mon)

f.close()

#####

char = re.findall(r"[A-Z][a-z]{1:7}:")
ch = []
for c in list(set(char)):
    ch += [re.sub(r':','',c)]
    
print(ch)


\(._>\)

f = open('friends101.txt','r')
s101 = f.readlines()
f.close()

would=[]

for line in s101:
    if re.match(r'[A-Z][a-z]+.:',line) and re.search(r'would', line):
        would.append(line)

for line in would:
    print(line)
    

'''

kk = false
kr = False