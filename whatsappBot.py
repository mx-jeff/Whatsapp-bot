from selenium import webdriver

while True:
    driver = webdriver.Chrome("webdriver/chromedriver.exe")
    driver.get('http://web.whatsapp.com')

    nome = input('Entre com o nome do usuario ou grupo: ')
    msg = input('Entre com a mensagem: ')
    quantidade = int(input('Enter com a quantidade de mensagens: '))

    #Scan the code before proceeding further
    input('Enter anything after scanning QR code')

    user = driver.find_element_by_xpath(f'//span[@title = "{nome}"]')
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')

    for i in range(quantidade):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()

    continua = str(input("Você deseja continuar? [S/N]")).upper().strip()[0]

    if continua == "N":
        exit()

