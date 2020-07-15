# Hepsiburada sistesinde yorum çekme
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.hepsiburada.com/poco-f2-pro-128-gb-poco-turkiye-garantili-p-HBV00000UPERS")
print(r.status_code) # Eğer Veri Geldiyse 200 değeri döner

print(r.content) # Sistedeki var olan verileri döner 

