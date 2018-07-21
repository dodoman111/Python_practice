
# coding: utf-8

# In[ ]:


import pymysql.cursors


# In[9]:


import pymysql.cursors

connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'eoghks12',
    db = 'emp',
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "select  empno, ename, dname from emp,dept where emp.DEPTNO=dept.DEPTNO and dept.deptno = '30'"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
a = result


# In[19]:


result


# In[20]:


result[1]()


# In[27]:


for i in range(len(result)):
    if result[i]['ename'] =='MARTIN':
        print(result[i]['empno'])


# In[24]:


result[1]['ename']


# In[4]:


import pymysql.cursors

connection = pymysql.connect(
    host = 'astronaut.snu.ac.kr',
    user = 'BDE-2018-11',
    password = 'bc9991c342b1',
    db = 'BDE-2018-11',
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "show tables"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
a = result

