import re
import requests
from bs4 import BeautifulSoup

class primeiraInstancia():
    def __init__(self, processo):
        self.processo = processo
    
    def acessar_url(self, url):
        session = requests.session()
        session.get(url)
        pagina = f"{url[:-8]}/search.do?conversationId=&dadosConsulta.localPesquisa.cdLocal=-1&cbPesquisa=NUMPROC&dadosConsulta.tipoNuProcesso=SAJ&numeroDigitoAnoUnificado=&foroNumeroUnificado=&dadosConsulta.valorConsultaNuUnificado=&dadosConsulta.valorConsulta={self.processo}&uuidCaptcha="
        response = session.get(pagina)
        return BeautifulSoup(response.content, "html.parser")

    def extrair_dados(self, soup):
        classe = soup.find("span", id="classeProcesso")
        areacru = soup.find("div", id="areaProcesso")
        clear = re.compile("<.*?>")
        area = re.sub(clear, "", str(areacru))
        assunto = soup.find("span", id="assuntoProcesso")
        distribuicao = soup.find("div", id="dataHoraDistribuicaoProcesso")
        juiz = soup.find("span", id="juizProcesso")
        if juiz != None:
            juiz = juiz.text
        valor = soup.find("div", id="valorAcaoProcesso")
        if valor != None:
            valor = valor.text
        partes = soup.find_all("td", class_="nomeParteEAdvogado")
        nomes = []
        for parte in partes:
            nome = parte.text.strip().replace("\n", "").replace("\t", "")
            nomes.append(nome)
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
        moviment = list(filter(None, movimentacao))
        return classe.text, area, assunto.text, distribuicao.text, juiz, valor, nomes, moviment
        
    def buscar_dados(self):
        processo = self.processo
        extraindo = re.compile(r"8\.02")
        Alagoas = re.search(extraindo, processo)
        extraindo2 = re.compile(r"8\.06")
        Ceara = re.search(extraindo2, processo)

        if Alagoas:
            url = "https://www2.tjal.jus.br/cpopg/open.do"
        elif Ceara:
            url = "https://esaj.tjce.jus.br/cpopg/open.do"
        else:
            return None

        soup = self.acessar_url(url)
        dados = self.extrair_dados(soup)
        return dados
