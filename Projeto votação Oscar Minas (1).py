#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\JC\AppData\Local\Google\Chrome\User Data\Profile Selenium')
navegador = webdriver.Chrome(options=options)

navegador.get('https://docs.google.com/forms/d/e/1FAIpQLSdwYoM3sseh1wf34N_-Z2LO9noB5eviETTuhYjyqAmd4bSVNQ/viewform?pli=1&pli=1&embedded=true&fbzx=-8591113718194750165')


# In[4]:


for i in range(38):

    #time.sleep(2)

    navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys('jose@gmail.com')

    navegador.find_element(By.XPATH, '//*[@id="i135"]/div[3]/div').click()

    navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div[1]/div/span/span').click()

    navegador.refresh()


# In[ ]:





# In[ ]:




