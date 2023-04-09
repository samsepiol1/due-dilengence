from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import requests


class TJRSWebScraper:
    def __init__(self):
        #chrome_options = Options()
        #chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome()
       

    def __del__(self):
        self.driver.quit()

    def navigate_to_url(self, url):
        self.driver.get(url)
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(10)

    def select_tipo_documento(self, tipo_documento):
        iframe = self.driver.find_element(By.XPATH, '//*[@id="conteudo-page"]/div[2]/div[2]/div/div[2]/p[2]/iframe')
        self.driver.switch_to.frame(iframe)

        select_civel = Select(self.driver.find_element(By.XPATH, '//*[@id="tipoDocumento"]'))
        time.sleep(2)

        select_civel.select_by_visible_text(tipo_documento)
        select_civel.select_by_value('3')
    

    def preencher_dados_cnpj(self, nome_completo, cnpj, endereco):

        cnpj_select = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[3]/input[2]")
        time.sleep(2)

        cnpj_select.click()

        time.sleep(2)
        nome_completo_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/input")
        time.sleep(2)
        nome_completo_element.send_keys(nome_completo)
        time.sleep(2)

        cnpj_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[7]/input")
        time.sleep(2)
        cnpj_element.send_keys(cnpj)
        time.sleep(2)

        endereco_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[14]/input")
        time.sleep(2)
        endereco_element.send_keys(endereco)
        time.sleep(5)
        enviar = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[15]/input")
        time.sleep(5)
        enviar.click()
        time.sleep(5)


    def preencher_dados_pessoais_cpf(self, nome, sexo, cpf, nome_mae,nome_pai, data_nascimento, rg, orgao, endereco):
        nome_completo = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/input")
        nome_completo.send_keys(nome)

        sexo_select = Select(self.driver.find_element(By.XPATH, '/html/body/div[1]/form/div[5]/select'))

        if sexo == 'M':
            sexo_select.select_by_visible_text('Masculino')
            sexo_select.select_by_value('M')
        else:
            sexo_select.select_by_visible_text('Feminino')
            sexo_select.select_by_value('F')


            

        cpf_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/input")
        cpf_element.send_keys(cpf)

        nome_mae_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[8]/input")
        nome_mae_element.send_keys(nome_mae)

        nome_pai_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[9]/input")
        nome_pai_element.send_keys(nome_pai)

        data_nascimento_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[10]/input")
        data_nascimento_element.send_keys(data_nascimento)

        rg_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[13]/input[1]")
        rg_element.send_keys(rg)

        orgao_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[13]/input[2]")
        orgao_element.send_keys(orgao)

        endereco_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[14]/input")
        endereco_element.send_keys(endereco)

    def emitir_documento(self):
        emitir_documento = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div[15]/input")
        time.sleep(2)
        emitir_documento.click()
        time.sleep(5)

    def download_pdf(self):
        janelas = self.driver.window_handles
        self.driver.switch_to.window(janelas[1])
        url_nova_aba = self.driver.current_url
        time.sleep(5)

        response = requests.get(url_nova_aba, verify=False)

        with open("arquivo.pdf", "wb") as f:
            f.write(response.content)

scraper = TJRSWebScraper()
scraper.navigate_to_url('https://www.tjrs.jus.br/novo/processos-e-servicos/servicos-processuais/emissao-de-antecedentes-e-certidoes//')
scraper.select_tipo_documento('Certidão Judicial Cível Negativa de 1º Grau')
#scraper.preencher_dados_cnpj('Lucas Matheus Alves da Silva', '49294076000166', 'Rua Perimental Nosso Refúgio')
#scraper.preencher_dados_pessoais_cpf('Lucas Matheus Alves da Silva', 'F', '12501504429', 'Roziana Dantas dos Santos', 'Valber Alves da Silva', '17/02/2000', '003720055', 'ses', 'Rua Perimental Nosso Refúgio')
scraper.emitir_documento()
scraper.download_pdf()
scraper.driver.quit()

