#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from plyer import notification       #use plyer for notification in WINDOWS
import requests                       #for requesting the URL
from bs4 import BeautifulSoup         #for web scraping
import time
from win10toast import ToastNotifier  #for notification

def Notifyme(title,message):
    toast=ToastNotifier()
    toast.show_toast(title, message, 
                        icon_path = "C:/Users/ANISH/Downloads/covid.ico",duration=3)  #timeout use for how much second it will show

def get_data(URL):
    req=requests.get(URL)
    return req.text


if __name__=="__main__":
    while True:
        mydata=get_data('https://www.mohfw.gov.in/')

        soup=BeautifulSoup(mydata,'html.parser')    #for parsing of html file


        #print(soup.prettify())                  #Prettify() function enable to view how the tags are nested in the document


        string1=""
        for tr in soup.find_all('tbody')[0].find_all('tr'):    #FOR ALL THE tr from the body of the table
            string1+=tr.get_text()


        string1=string1[1:]     #As first value is the blank one    
        #for splitting the data according to state statistics    
        new_data=string1.split("\n\n")


        state=["West Bengal","Uttar Pradesh","Tamil Nadu","Puducherry","Jammu and Kashmir","Delhi","Maharashtra","Assam"]

        #generate list of particular states
        for item in new_data[0:35]:      #for taking only 35 states and union territory
            Final_list=item.split("\n")
            if Final_list[1] in state:
                print(Final_list[1])
                noti_title="COVID-19 cases in the state: "
                noti_text=f"State name: {Final_list[1]} \n Active cases:{Final_list[2]} \n Cured:{Final_list[3]}\n Deaths:{Final_list[4]}\n Total Cases:{Final_list[5]}"
                Notifyme(noti_title,noti_text)
                time.sleep(3)
        time.sleep(3600)           # for each one hour notification      


# In[ ]:





# In[ ]:




