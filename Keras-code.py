#!/usr/bin/env python
# coding: utf-8

# In[3]:


import keras
from keras.models import Sequential
from keras.layers import MaxPooling2D
from keras.layers import Convolution2D, BatchNormalization, Dropout
from keras.layers import Dense
from keras.layers import Flatten
from keras.datasets import fashion_mnist


# In[4]:


data = fashion_mnist.load_data()
(x_train, y_train),(x_test,y_test) = data
img_rows, img_cols = 28, 28


# In[5]:


x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
y_train = keras.utils.to_categorical(y_train,10 )
y_test = keras.utils.to_categorical(y_test,10)
x_train /= 255
x_test /= 255


# In[ ]:





# In[ ]:





# In[6]:


model=Sequential()
model.add(Convolution2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                   input_shape=(28,28,1)
                       ))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Convolution2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=10 , activation = 'softmax'))
model.compile(loss = 'categorical_crossentropy',
              optimizer = keras.optimizers.Adam(),
              metrics = ['accuracy'])
model.fit( x_train, y_train,
          batch_size=128,
          epochs=1,
          verbose=1,
          validation_data=(x_test, y_test))


# In[18]:


from keras.models import save_model
 


# In[15]:


filepath = './saved'
save_model(model ,filepath  )


# In[20]:


model1=load_model("saved")


# model1.summary

# In[21]:





# In[22]:


 


# In[ ]:




