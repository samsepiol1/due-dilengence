from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

import time






driver = webdriver.Chrome()

driver.get('https://pje.trt4.jus.br/certidoes/trabalhista/emissao')

time.sleep(10)

cpf_select = driver.find_element(By.XPATH, '/html/body/pje-root/main/pje-emissor-certidao-trabalhista/section/form/mat-card/mat-card-content/p[1]/mat-radio-group/mat-radio-button[2]')
time.sleep(5)
cpf_select.click()
time.sleep(5)

cpf = driver.find_element(By.XPATH, '/html/body/pje-root/main/pje-emissor-certidao-trabalhista/section/form/mat-card/mat-card-content/p[2]/mat-form-field/div/div[1]/div/input')
time.sleep(5)
cpf.send_keys('Insert CPF Here')
time.sleep(4)

not_robot = driver.find_element(By.XPATH,'/html/body/div[2]')

not_robot.click()
