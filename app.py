# Hepsiburada sistesinde yorum çekme
import requests
from bs4 import BeautifulSoup

# r = requests.get("https://www.hepsiburada.com/poco-f2-pro-128-gb-poco-turkiye-garantili-p-HBV00000UPERS")
# print(r.status_code) # Eğer Veri Geldiyse 200 değeri döner

# print(r.content) # Sistedeki var olan verileri döner 


i = 1;
j = 1;
while i < 5:
    r = requests.get("https://www.hepsiburada.com/poco-f2-pro-128-gb-poco-turkiye-garantili-p-HBV00000UPERS-yorumlari?sayfa={}".format(i))
    soup = BeautifulSoup(r.content,"lxml")
    comments = soup.find_all("div",attrs={"class":"ReviewCard-module-34AJ_"})
    for comment in comments:
        # Şimdilik sadece yorumları kim yaptı ise onların isimlerini çektik.
        print("{}-) Name : {} \n \t Comment:{}".format(j,comment.find("div",attrs={"class":"ReviewCard-module-2dVP9"}).strong.string,comment.find("div",attrs={"class":"ReviewCard-module-2dVP9"}).span.string))
        j+=1
        # print(comment.find("div",attrs={"class":"ReviewCard-module-2dVP9"}).strong.string) 
        # print(comment.find("div",attrs={"class":"ReviewCard-module-2dVP9"}).span.string) 
        # print(comment.find("strong"))
    i+=1