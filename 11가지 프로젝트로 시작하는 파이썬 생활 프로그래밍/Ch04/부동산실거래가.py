## 부동산 실거래가
import re
import usecsv

apt = usecsv.opencsv('apt_20221130.csv')
apt = usecsv.switch(apt)


## 면적 120 이상, 금액 3억 이하, 소재지 강원도
for i in apt:
   try:
       if i[5]>=120 and i[8]<=30000 and re.match('강원',i[0]):
           print(f"{i[0]}{i[5]}{i[8]}{i[4]}")
   except:
       pass
   
new_list=[]
for i in apt:
    try:
        if i[5]>=120 and i[8]<=30000 and re.search(r'김해',i[0]):
            new_list.append([i[0],i[5],i[8],i[4]])
            print(new_list)
    except:
        pass
    
## match : 시작부터
## search : 그냥 검색
usecsv.writecsv('김해over120_lower30000.csv', new_list)


