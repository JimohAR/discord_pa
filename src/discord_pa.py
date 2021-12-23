#!/usr/bin/env python
# coding: utf-8

# ### objectives
# * send message at a given time
# 
# * send message at intervals
# * send images

# <a href="https://colab.research.google.com/github/JimohAR/it_core_project1/blob/main/notebooks/task1_exp.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[1]:


import requests
from json import dumps

import datetime

import os
import sys

import random


# In[2]:


url = "https://discord.com/api/v8/channels/{}/messages"

tokens = {
    "main" : "ODkwNDU5Njc0Mjc1NjM1MjIw.Yb_o_Q.j8OR05ut75Y0b_9QITyuoAhU_Bg",
    "one" : "ODkwNDU1NDI4OTYwNDg5NTMz.Yb_uww.M70-FoiaxNU59QIbEtaDvtus7S8",
    "two" : "ODkwNDUwMTAzMjM4ODE1NzY1.Yb_wIw.TYOKdljlIDWz7atUd0BM57YskYA",
    "three" : "ODkwNDc5MzI4Mzk4MjgyNzcy.Yb_w3A.fFkeH2YLCIU_-pIZ-3WiA9l9Tw4",
    "four" : "ODkwODAwNzU0NjYxNjcwOTMz.Yb_xZA.lzhYNmyz3mvDzvbXl6vO7kdx1wI"
}
token = tokens["main"]

channel_ids = {
    "element_general" : 895560750494515231,
    "element_offtopic" : 895560960520118292,
    "element_memes" : 895564654967930910,
    "element_levelup" : 895603334520668190,
    "CG_internal" : 922747763484139541
}
channel_id = channel_ids["CG_internal"]


# In[3]:


seed = random.seed = 0
rand_time = random.choice([("22:" + str(random.randint(47,59))), ("23:0" + str(random.randint(0,3)))])


# In[4]:


def send_txt(txt = "SHIFT ON", time = rand_time, channel_id = channel_id, token = token):
    sys.stdout.write(f"{time} chosen\n")
    payload = {
        "content": txt,
        "tts" : "false"
    }
    payload = dumps(payload)
    
    headers =  {
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:94.0.2) Gecko/20100101 Firefox/94.0.2",
        "authorization": token,
    }
    
    while True:
        if (datetime.time.fromisoformat(time) <= datetime.datetime.now().time()):
            with requests.Session() as s:
                r = s.post(url.format(channel_id), data = payload, headers = headers)
                return (r.reason, r.raise_for_status)
        else:
            continue


# In[5]:


def send_image(path_img, time, channel_id = channel_id, txt = "", token = token):
    payload = {
        "content": txt,
        "tts" : "false"
    }
    
    headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:94.0.2) Gecko/20100101 Firefox/94.0.2",
    "authorization": token,
    }
        
    with open(path_img, 'rb') as img:
        name_img= os.path.basename(path_img)
        files= {
            'image': (name_img, img, 'multipart/form-data', {'Expires': '0'})
        }
        
        while True:
            if (datetime.time.fromisoformat(time) <= datetime.datetime.now().time()):
                with requests.Session() as s:
                    r = s.post(url.format(channel_id), data = payload, files = files, headers = headers)
                    return(r.reason, r.raise_for_status)
            else:
                continue


# In[6]:


# send_image("C:/Users/abola/Pictures/day3.png", "20:40", 894498733373419520, txt= "okay")


# In[7]:


# test channel : 922306149750030346


# In[8]:


txt = """SHIFT OFF 

CG REPORT 

1.  tanque#8645
2. farzi#0880
3. schwan#7978
4. romeo#5093
5. promise#6629 (main account)

GROUP MODERATED : ELEMENT BLACK

Beginning Message : https://discord.com/channels/893123687409156146/895560750494515231/923340337999654944

Ending Message : https://discord.com/channels/893123687409156146/895560750494515231/923413999775801345"""


# In[9]:


# send_txt("okay")


# In[10]:


if __name__ == "__main__":
    # print(send_txt(txt, "05:01",))
    # print(send_image("C:\\Users\\abola\\Pictures\\cg1.png", "05:02"))
    # print(send_image("C:\\Users\\abola\\Pictures\\cg2.png", "05:02"))
    sys.stdout.write("yes")

