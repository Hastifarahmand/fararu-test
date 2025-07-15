import requests
from bs4 import BeautifulSoup
web=requests.get("https://fararu.com/")
soup=BeautifulSoup(web.content)
f1=open("22.txt","rt",encoding="utf-8")
s=f1.read()
links=s.strip().split("\n")
for link in links:
    web=requests.get(link)
    soup=BeautifulSoup(web.content)
    dvs=soup.find_all("div",{"class":"primary_files"})
    # print(dvs)
    
    img=dvs[0].find_all("img")[0]["src"]
    n=img.strip().split("/")[-1]
    f2=open("images/"+n,"wb")
    web=requests.get(img)
    f2.write(web.content)
    f2.close()
    
# print(len(dvs))