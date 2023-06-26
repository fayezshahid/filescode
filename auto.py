from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
import os
from datetime import datetime

date = input("Enter date: ")

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    "download.default_directory": r"C:\Users\USER\Downloads", #Change default directory for downloads
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})

driver = webdriver.Chrome(options=options)

driver.get('https://envio.tcscourier.com/')
# driver.maximize_window()

if 'w ' in date:
    driver.find_element(By.ID, "login-username").send_keys("deforelsig")
if 'f ' in date:
    driver.find_element(By.ID, "login-username").send_keys("floir2")
    pwd = 'Pass@123'
else:
    driver.find_element(By.ID, "login-username").send_keys("deforels2")
    pwd = 'password123#'

driver.find_element(By.ID, "login-password").send_keys(pwd)

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/form/div[5]/button').click()

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div[1]/div/nav/ul/li[1]/ul/li[3]/a'))).click()
sleep(5)

driver.get('https://envio.tcscourier.com/CNRePrinting/Index')
# driver.maximize_window()

sleep(10)

select = Select(driver.find_element(By.ID, 'ddlCostCenter'))
if 'w ' in date:
    select.select_by_value('63379')
if 'f ' in date:
    select.select_by_value('130664')
else:
    select.select_by_value('81617')

select = Select(driver.find_element(By.ID, 'PrintDDL'))
select.select_by_value('4')

# driver.find_element(By.ID, "rngCREATEDON").clear()
# driver.find_element(By.ID, "rngCREATEDON").send_keys(f"03/{datetime.now().strftime('%d')}/2023 - 03/{datetime.now().strftime('%d')}/2023")
# driver.find_element(By.ID, "rngCREATEDON").send_keys("03/15/2023 - 03/15/2023")

driver.find_element(By.ID, "btnGenrateReport").click()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'btnGenrateReport'))).click()

sleep(3)

select = Select(driver.find_element(By.XPATH, '//*[@id="tblReport_length"]/label/select'))
select.select_by_value('1000')

table =  driver.find_element(By.ID, 'tblReport')

records = int(driver.find_element(By.ID, "tblReport_info").text.split(" ")[5])

for i in range(1, records+1):
    x = driver.find_element(By.XPATH, f'//*[@id="tblReport"]/tbody/tr[{i}]/td[4]').text
    x = x.split(" ")
    if x[0] == 'FLOIR':
        x = x[1] + ' ' + x[2]
    elif len(x) == 3:
        x = x[2]
    else:
        x = x[2] + ' ' + x[3]
    # if 'w ' in date:
    #     x = ''
    # if 'f ' in date:
    #     x = 'FLOIR ' + date
    # else:
    #     x = 'DEFOR ' + date
    if date == x:
        driver.find_element(By.XPATH, f'//*[@id="tblReport"]/tbody/tr[{i}]/td[12]/div/input').click()
        

sleep(3)

driver.find_element(By.ID, "btnGetPDF").click()

sleep(3)

month = datetime.now().strftime('%h')

path = r"C:\Users\USER\Downloads"
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]

if 'GenerateLabels' in newest:
    os.rename(newest, f'{date} {month}.pdf')

