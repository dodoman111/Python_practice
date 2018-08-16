
# coding: utf-8

# # matplotlib 과제

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv('example.csv')


# In[4]:


data.columns


# In[5]:


data.head()


# In[6]:


data.tail()


# In[11]:


import seaborn as sns
sns.set(style="ticks")
sns.pairplot(df, hue="Class", diag_kind="kde")


# In[7]:


#plt.subplot(211)
plt.scatter(data['V17'],data['V27'],s=1,c=data['Class'])
plt.title('Class 좌표')
plt.xlabel('V17')
plt.ylabel('V27')
plt.grid(True)
#plt.axis([0,10,0,10])
#plt.legend((data['Class']),('class0', 'class1'))


# In[8]:


#plt.subplot(211)
plt.scatter(data['V17'],data['V27'],s=10,c=data['Class'])
plt.title('Class 좌표')
plt.xlabel('V17')
plt.ylabel('V27')
plt.grid(True)
plt.axis([-25,-15,-10,10])


# In[10]:


plt.hist(data['V24'],bins=1000)
plt.xlabel('V24')


# In[11]:


boxdata =[data['V3'],data['V17']]
plt.boxplot(boxdata,0,'')
plt.xticks([1,2],['V3','V17'])


# # sklearn 과제

# In[21]:


from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=1)


# In[29]:


X = data.loc[:,'V1':'V28']
Y = data['Class']


# In[30]:


X.head(2)


# In[31]:


Y.head(2)


# # Random Forest를 이용한 변수 Selection

# In[32]:


classify = clf.fit(X,Y)


# In[33]:


a= clf.feature_importances_


# In[34]:


a


# In[35]:


ev =[]            #유효변수 선정
for i in range(len(a)):
    if a[i] != 0:
        ev.append('V'+str(i+1))


# In[36]:


ev


# # 학습데이터 세팅

# In[40]:


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X[ev],Y,test_size=0.2)


# # 1. 분류알고리즘 실행(DicisionTree)

# In[41]:


from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf_t = clf.fit(X_train,y_train)


# In[53]:


clf_t


# In[56]:


pred_t=clf.predict(X_test)
pred_t


# # 모형검증

# In[57]:


pd.crosstab(pred_t,y_test)


# In[68]:


from sklearn.metrics import confusion_matrix

conf_matrix = pd.DataFrame(
    confusion_matrix(y_test, pred_t),
    columns=['Predicted Type 0', 'Predicted  Type 1'],
    index=['True Type 0', 'True Type 1']
)
conf_matrix


# In[65]:


print('Prediction Accuracy: ', clf.score(X_test,  y_test))


# # Tree그림그리기~~~

# In[16]:


from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image

dot_data = export_graphviz(data, out_file=None, feature_names=['class1', 'class0'],
                          class_names=data['Class'], filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())


# # 2.로짓알고리즘 실행

# In[46]:


from sklearn import linear_model
logit = linear_model.LogisticRegression()
logit.fit(X_train,y_train)


# In[47]:


logit.intercept_


# In[48]:


logit.coef_


# In[54]:


pred_l = logit.predict(X_test)
pred_l


# In[61]:


len(y_test[y_test==0])


# # 모형검증

# In[55]:


pd.crosstab(pred_l, y_test)


# In[67]:


from sklearn.metrics import confusion_matrix

conf_matrix = pd.DataFrame(
    confusion_matrix(y_test, pred_l),
    columns=['Predicted Type 0', 'Predicted  Type 1'],
    index=['True Type 0', 'True Type 1']
)
conf_matrix


# In[64]:


print('Prediction Accuracy: ', logit.score(X_test, y_test))


# # Tree와 Logit 정확성비교
# (Tree가 아주 근소한 차이로 우수)

# In[66]:


clf.score(X = X_test, y = y_test)-logit.score(X_test, y_test)

