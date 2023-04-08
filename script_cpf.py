from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

import time

import requests




driver = webdriver.Chrome()

driver.get('https://www.tjrs.jus.br/novo/processos-e-servicos/servicos-processuais/emissao-de-antecedentes-e-certidoes//')

time.sleep(10)

# Simular Clique do Select para achar civel

iframe = driver.find_element(By.XPATH, '//*[@id="conteudo-page"]/div[2]/div[2]/div/div[2]/p[2]/iframe')

driver.switch_to.frame(iframe)

select_civel = Select(driver.find_element(By.XPATH, '//*[@id="tipoDocumento"]'))

time.sleep(2)

select_civel.select_by_visible_text('Certidão Judicial Cível Negativa de 1º Grau')

select_civel.select_by_value('3')

time.sleep(2)

nome_completo = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/input")

time.sleep(2)

nome_completo.send_keys('Lucas Matheus Alves da Silva')

time.sleep(2)

cpf = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/input")

time.sleep(2)

cpf.send_keys('12501504429')

time.sleep(2)

nome_mae = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[8]/input")
time.sleep(2)
nome_mae.send_keys('Roziana Dantas dos Santos')
time.sleep(2)

nome_pai = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[9]/input")

time.sleep(2)
nome_pai.send_keys('Valber Alves da Silva')
time.sleep(2)

data_nascimento = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[10]/input")
time.sleep(2)
data_nascimento.send_keys('17/02/2000')
time.sleep(2)

rg = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[13]/input[1]")
time.sleep(2)
rg.send_keys('003720055')
time.sleep(2)


orgao = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[13]/input[2]")
time.sleep(2)
orgao.send_keys('ses')
time.sleep(2)



endereco = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[14]/input")
time.sleep(2)
endereco.send_keys('Rua Perimental Nosso Refúgio')
time.sleep(2)

emitir_documento = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[15]/input")
time.sleep(2)
emitir_documento.click()
time.sleep(5)


#alternar drive para nova aba

janelas = driver.window_handles
driver.switch_to.window(janelas[1])


url_nova_aba = driver.current_url

# Imprima a URL da nova aba
time.sleep(5)


#Baixar PDF
response = requests.get(url_nova_aba, verify=False)

with open("arquivo.pdf", "wb") as f:
    f.write(response.content)


driver.quit()




# Implementar lógica da nacionalidade



#select_civel = Select(driver.find_element(By.XPATH, '/html/body/div[1]/form/div[1]'))

#time.sleep(10)

#select_civel.select_by_visible_text('Certidão Judicial Cível Negativa de 1º Grau')

#time.sleep(10)

#select_civel.select_by_value('3')

#time.sleep(10)