# coding: utf-8

# In[1]:


# 1
import numpy as np

a = np.zeros(10)
a


# In[2]:


# 2
a[4] = 1
a


# In[3]:


# 3
import numpy as np

b = np.array(range(10, 50))
b


# In[4]:


# 4
import numpy as np

d = np.array(range(0, 25)).reshape((5, 5))
d


# In[5]:


# 5
e = np.eye(5)
e


# In[6]:


# 6
import random

import numpy as np

f = np.array(random.sample(range(1, 26), 25)).reshape((5, 5))
print(f.max())
print(f.min())


# In[7]:


# 7
g = np.matrix(np.full((4, 3), 1))
h = np.matrix(random.sample(range(1, 7), 6)).reshape(3, 2)
print("g:", g)
print("h:", h)
g * h


# In[8]:


# 8
print("matrix: ", g.transpose())
print("matrix: ", h.transpose())


# In[9]:


# 9
import numpy as np

i = np.matrix(range(0, 25)).reshape(5, 5)
j = np.matrix(range(25, 50)).reshape(5, 5)
print("add two mat :", i + j)
print("subtract two mat :", i - j)


# Q1~6

# In[10]:


# Q1
import numpy.linalg as LA


# In[10]:


# Q1
import numpy.linalg as LA

a1_1 = np.array([[1, 2], [3, 4]])
a1_2 = np.array([[1, 2], [3, 4], [5, 6]])

print(LA.eig(a1_1))
try:
    print(LA.eig(a1_2))  # Last 2 dimensions of the array must be square
except:
    print("\nLA.eig(a1_2) : Last 2 dimensions of the array must be square\n\n")
print(LA.svd(a1_1, full_matrices=True))
print(LA.svd(a1_1, full_matrices=False))
print(LA.svd(a1_2, full_matrices=True))
print(LA.svd(a1_2, full_matrices=False))


# In[11]:


# Q2
a2 = np.array([[7, 1], [1, 7]])
x, y = LA.eig(a2)
x, y
"""
x는 eigen value
y는 eigen vector로
각각 scale변환,
방향을 의미한다."""


# In[12]:


# Q3
a3 = np.array(
    [
        [1, 1, 1, 0, 0],
        [3, 3, 3, 0, 0],
        [4, 4, 4, 0, 0],
        [5, 5, 5, 0, 0],
        [0, 2, 0, 4, 4],
        [0, 0, 0, 5, 5],
        [0, 1, 0, 2, 2],
    ]
)
U, S, V = LA.svd(a3, full_matrices=False)
U, S, V
"""
U는 rotation
S는 scale 변환값
V는 rotation"""


# In[13]:


# Q4
a4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
# A의 코드
a4_1 = a4.reshape(3, 2, 3)
a4_1
# B의 코드
for i in a4_1:
    for j in i:
        print(j)
        print("----")


# In[14]:


# Q5
a5 = np.array([[1, 2], [3, 4]])
b5 = np.array([[1, 3], [2, 4]])
print("dot", np.dot(a5, b5))
print("*", a5 * b5)
"""
np.dot은 내적
*은 같은 행렬 각 원소의 곱"""


# In[21]:


# Q6-1
a6_1 = np.zeros((5, 5))
a6_1 += np.array(5)
a6_1


# In[30]:


# Q6-2

a6_2 = np.full((4, 5, 3), 3)
# np.cov(a6_2) # has more than 2 dimensions
a6_2
