from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
from bs4 import BeautifulSoup


class segundainstancia:
    def __init__(self, processo):
        self.processo = processo
    
    def acessar_url(self, url):
        num_processo = self.processo
        processo_limpo = num_processo.split(".")
        numero_unificado = ".".join(processo_limpo[:2])  # "0710802-55.2018"
        foro = processo_limpo[-1]
        
        interface = Options()
        interface.headless = True
        driver = webdriver.Chrome(options=interface)
        driver.get(url)
        digitando = driver.find_element(By.ID, 'numeroDigitoAnoUnificado')
        digitando.send_keys(numero_unificado)
        digitando = driver.find_element(By.ID, 'foroNumeroUnificado')
        digitando.send_keys(foro)
        botao = driver.find_element(By.ID, "pbConsultar")
        botao.click()
        pagina = False
        try:
            checked = driver.find_element(By.ID, "processoSelecionado")
            checked.click()
            botao = driver.find_element(By.ID, "botaoEnviarIncidente")
            botao.click()
            soup = BeautifulSoup(driver.page_source, "html.parser")
            pagina = True
        except:
            driver.close()
            pagina = False
        if pagina:
            driver.quit()
            return soup
        else:
            return None
        

    def extrair_dados(self, soup):
        classe2 = soup.find("div", id="classeProcesso")
        assunto2 = soup.find("div", id="assuntoProcesso")
        relator2 = soup.find("div", id="relatorProcesso")
        movimentacoes = soup.find("tbody", id="tabelaTodasMovimentacoes")
        movimentacao = []
        for x in movimentacoes:
            clear = re.compile("<.*?>")
            y = re.sub(clear, "", str(x)).replace("\t", "").replace("\n", "")
            padrao = r"(\d)([A-Za-z])"
            substituicao = r"\1 \2" 
            movi = re.sub(padrao, substituicao, y)
            movimen = re.sub(r"\s+", " ", movi)
            movimentacao.append(movimen)
            moviment2 = list(filter(None, movimentacao))
        return classe2.text, assunto2.text, relator2.text, moviment2
        
    def buscar_dados(self):
        processo = self.processo
        extraindo = re.compile(r"8\.02")
        Alagoas = re.search(extraindo, processo)
        extraindo2 = re.compile(r"8\.06")
        Ceara = re.search(extraindo2, processo)

        if Alagoas:
            url = "https://www2.tjal.jus.br/cposg5/open.do"
        elif Ceara:
            url = "https://esaj.tjce.jus.br/cposg5/open.do"
        else:
            return None


        soup = self.acessar_url(url)
        if soup != None:
            dados2 = self.extrair_dados(soup)
        else:
            dados2 = None
        return dados2
