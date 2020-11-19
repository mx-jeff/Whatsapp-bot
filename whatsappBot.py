from selenium import webdriver
from time import sleep
import json


msg_tag = 'DuUXI'
button_tag = '_2Ujuu'

driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://web.whatsapp.com')

nome = input('Entre com o nome do usuario ou grupo: ')
msg = input('Entre com a mensagem: ')
quantidade = int(input('Enter com a quantidade de mensagens: '))

print(driver.get_cookies())

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath(f'//span[@title = "{nome}"]')
user.click()

msg_box = driver.find_element_by_class_name(msg_tag)
sleep(1)

for i in range(quantidade):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name(button_tag)
    button.click()
    sleep(1)

# continua = str(input("Você deseja continuar? [S/N]")).upper().strip()[0]

# if continua == "N":
#     exit()

driver.quit()