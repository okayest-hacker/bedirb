import os
import re
import time
import urllib3
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from PIL import Image
ss = 0
cwd = os.getcwd()
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('--disable-blink-features-AutomationControlled')
option.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options=option)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
host = input("What host do you want to scan(example: https://172.16.0.1/): ")
hosted = re.sub('[htps:/]','',host)
print(hosted)
z = requests.get(host, verify=False)
zx = z.headers
#zy = zx.get('Content-Length')
zy = 675
limited = str(zy)
print(limited) 
mylist = open("/usr/share/seclists/Discovery/Web-Content/CGIs.txt", "r")
mylister = [line.rstrip('\n') for line in mylist]
RED = "\u001b[31m"
CYAN = "\u001b[36m"
END = "\u001b[0m"
if not os.path.exists(cwd + '/'+ hosted):
	os.mkdir(cwd + '/'+ hosted)
for i in mylister:
	ss += 1
	r = requests.get(host + i, verify=False)
	printy = r.headers
	size = str(printy.get('Content-Length'))
	if size > limited or size < limited:
		print("server:",RED + printy.get('Server') + END ,"status code:",RED + str(r.status_code) + END,"content length:",RED + str(printy.get('Content-Length')) + END ,CYAN + "Directory:" + END,i)
		driver.get(host + i)
		time.sleep(3)
		locoy = 'screenshot%s.png' %ss
		loco = '%s/%s' % (hosted, locoy)
		print("Printed :",loco)
		driver.save_screenshot(loco)

mylist.close()
