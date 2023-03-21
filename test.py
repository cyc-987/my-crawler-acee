import re
import requests
from bs4 import BeautifulSoup as bs
import lxml

i = 1
for x in range(1,20):
    temp_str = 'div[' + str(i) + ']/div/div[2]/'
    i = i + 1
    print(temp_str)