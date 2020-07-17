# Hepsiburada sistesinde yorum çekme
import requests
from bs4 import BeautifulSoup

# r = requests.get("https://www.hepsiburada.com/poco-f2-pro-128-gb-poco-turkiye-garantili-p-HBV00000UPERS")
# print(r.status_code) # Eğer Veri Geldiyse 200 değeri döner

# print(r.content) # Sistedeki var olan verileri döner 


i = 1;
j = 1;
size = 0;
# Burada Belirtiğimiz değer sayfa sayısı sayfa sayısı var olan sayfa sayısından fazla ise otomatik olarak başa dönderir
# yapılması gereken sayfa sayısına bakmak ve ona göre veri yazmak.4

matris = [
    ["https://www.hepsiburada.com/xiaomi-redmi-note-9-128-gb-xiaomi-turkiye-garantili-p-HBV00000UGU4C-yorumlari?sayfa={}",3],
    ["https://www.hepsiburada.com/iphone-11-64-gb-p-HBV00000NSBZ6-yorumlari?sayfa={}",27]
    ["https://www.hepsiburada.com/poco-f2-pro-128-gb-poco-turkiye-garantili-p-HBV00000UPERS-yorumlari?sayfa={}",4]]
while size < len(matris):
    while i <= matris[size][1]:
        r = requests.get(matris[size][0].format(i))
        soup = BeautifulSoup(r.content,"lxml")
        comments = soup.find_all("div",attrs={"class":"ReviewCard-module-34AJ_"})
        for comment in comments:
            # Şimdilik sadece yorumları kim yaptı ise onların isimlerini çektik.
            print("{}-) Name : {} \n \t Comment:{}".format(j,comment.find("div",attrs={"class":"ReviewCard-module-2dVP9"}).strong.string,comment.find("div",attrs={"class":"ReviewCard-module-2dVP9"}).span.string))
            j+=1
            # ilk Başta bir yorumu aldık aldıktan sonra o yorumun içinde strong ve span da yazan verileri çektik
            # print(comment.find("div",attrs={"class":"ReviewCard-module-2dVP9"}).strong.string) 
            # print(comment.find("div",attrs={"class":"ReviewCard-module-2dVP9"}).span.string) 
        i+=1
    i = 1;
    size+=1