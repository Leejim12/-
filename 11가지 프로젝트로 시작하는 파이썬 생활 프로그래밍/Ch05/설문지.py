## 설문지 데이터 전처리
import os, usecsv
import numpy as np
os.chdir(r'C:\공부\11가지 프로젝트로 시작하는 파이썬 생활 프로그래밍\Ch05')
quest = np.array(usecsv.switch(usecsv.opencsv('quest.csv')))
quest
