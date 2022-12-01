# ch05

import numpy as np

a = np.array([[2,3],[5,2]])

print(a)

## 슬라이싱
d = np.array([[1,2,3,4,5],[2,4,5,6,7],[5,7,8,9,9]])
print(d)

d[1][2]

d[1:,3:]

## 배열 크기
d = np.array([2,3,4,5,6])
d
d.shape
e = np.array([[1,2,3,4],[5,6,7,8]])
e.shape


## astype : 형변환, dtype : 형확인
d.dtype

data = np.arange(1,5)
data.dtype
data.astype('float64')
data.astype('int32')

## 0, 1, 정수 등
### 0
np.zeros((2,10))
### 1
np.ones((2,10))
### 연속
np.arange(2,10)
### 행열변환
a= np.ones((2,3))
b =np.transpose(a)
b

## 사칙연산 연습
arr1 = np.array([[2,3,4],[6,7,8]])
arr2 = np.array([[12,23,14],[36,47,58]])
plus = arr1 + arr2
mul = arr1*arr2
div = arr1/arr2
print(plus,mul,div)

    # 크기 달라도 됨
arr3 = np.array([100,200,300])
arr1.shape
arr3.shape
arr1 + arr3
## * 행, 열중에 하나는 맞아야 더할 수 있음. 둘 다 다르면 오류 남.
### 2,1 + 2,3 가능.

## 파이썬 리스트 - numpy 배열 차이
d = np.array([[1,2,3,4,5],[2,4,5,6,7],[5,7,8,9,9]])
d_list = [[1,2,3,4,5],[2,4,5,6,7],[5,7,8,9,9]]
print("(d,dlist_",type(d),type(d_list))
d[:2]=0
d

## 인덱싱 슬라이싱 연습
arr4 = np.arange(10)
arr4
arr4[:5]
arr4[-3:]
arr1
arr1[1,2]
arr1[:,2]
