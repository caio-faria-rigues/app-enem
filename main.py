# para o back-end
import requests
from bs4 import BeautifulSoup
from random import shuffle

# para o front_end
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

kivy.require('1.9.1')


def multiplereplace(text):
    return "".join([char if char in "ABCDE" else "" for char in text])


def resposta(link, num):
    url = link
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

    # lista de matérias
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    grids = str(soup.find_all('table', id='tabela-respostas'))
    gridslist = list(grids)
    grid = multiplereplace(gridslist)
    return grid[num]


def spaces(quest_beta):
    espacos = ["						", "                        ", "                         ",
               "	", "						 ", "						 ", "						 "]
    for voids in espacos:
        if voids in quest_beta:
            quest_beta = quest_beta.replace(voids, "")
    return quest_beta


math_ans = ''
bio_ans = ''
chemistry_ans = ''
physics_ans = ''
history_ans = ''
languages_ans = ''
humans_ans = ''

questMath = ''
questBio = ''
questChe = ''
questHis = ''
questFis = ''
questLin = ''
questHum = ''

# funções de cada questão:


def math():
    global questMath
    global math_ans
    url = 'https://projetoagathaedu.com.br/banco-de-questoes/matematica.php'
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

    # lista de matérias
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    grids = soup.find_all('div', class_='opcao')

    # pega um indice de matéria aleatória
    index_list = list(range(41))
    shuffle(index_list)
    index = index_list.pop()

    # pega a caixa da matéria
    grid = grids[index]

    # pega o link da matéria
    str_link = str(grid.find('a', href=True))
    list_link = str_link.split("\n")
    href = list_link[0]
    link = href[11:len(href) - 2]
    url2 = f'https://projetoagathaedu.com.br{link}'

    # quantidade de questões da matéria
    quest_qtd = grid.find('div', class_='lista-tema-numero').get_text()

    # lista de questões
    quest_bank = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(quest_bank.content, 'html.parser')
    quest_head = soup2.find_all('div', class_='questoes-enem-vestibular')

    # pega o indice da questão
    quests_list = list(range(int(quest_qtd)))
    shuffle(quests_list)
    quest_index = quests_list.pop()

    # pega uma questão
    try:
        quest_beta = (quest_head[quest_index]).get_text().strip()
    except:
        quest_beta = 'Erro: Não achamos essa questão :(. Tente Novamente'

    # pega a resposta
    try:
        math_ans = resposta(url2, quest_index)
    except:
        math_ans = f"Algo deu errado. Tente novamente ou verifique a resposta em: {url2}"

    questMath = spaces(quest_beta)
    return str(questMath)


def bio():
    global questBio
    global bio_ans
    url = 'https://projetoagathaedu.com.br/banco-de-questoes/biologia.php'
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

    # lista de matérias
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    grids = soup.find_all('div', class_='opcao')

    # pega um indice de matéria aleatória
    index_list = list(range(26))
    shuffle(index_list)
    index = index_list.pop()

    # pega a caixa da matéria
    grid = grids[index]

    # pega o link da matéria
    str_link = str(grid.find('a', href=True))
    list_link = str_link.split("\n")
    href = list_link[0]
    link = href[11:len(href) - 2]
    url2 = f'https://projetoagathaedu.com.br{link}'

    # quantidade de questões da matéria
    quest_qtd = grid.find('div', class_='lista-tema-numero').get_text()

    # lista de questões
    quest_bank = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(quest_bank.content, 'html.parser')
    quest_head = soup2.find_all('div', class_='questoes-enem-vestibular')

    # pega um indice de questão aleatória
    quests_list = list(range(int(quest_qtd)))
    shuffle(quests_list)
    quest_index = quests_list.pop()

    # pega uma questão
    try:
        quest_beta = (quest_head[quest_index]).get_text().strip()
    except:
        quest_beta = 'Erro: Não achamos essa questão :(. Tente Novamente'

    # pega a resposta
    try:
        bio_ans = resposta(url2, quest_index)
    except:
        bio_ans = f"Algo deu errado. Tente novamente ou verifique a resposta em: {url2}"

    questBio = spaces(quest_beta)
    return str(questBio)


def chemistry():
    global questChe
    global chemistry_ans
    url = 'https://projetoagathaedu.com.br/banco-de-questoes/quimica.php'
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

    # lista de matérias
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    grids = soup.find_all('div', class_='opcao')

    # pega um indice de matéria aleatória
    index_list = list(range(21))
    shuffle(index_list)
    index = index_list.pop()

    # pega a caixa da matéria
    grid = grids[index]

    # pega o link da matéria
    str_link = str(grid.find('a', href=True))
    list_link = str_link.split("\n")
    href = list_link[0]
    link = href[11:len(href) - 2]
    url2 = f'https://projetoagathaedu.com.br{link}'

    # quantidade de questões da matéria
    quest_qtd = grid.find('div', class_='lista-tema-numero').get_text()

    # lista de questões
    quest_bank = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(quest_bank.content, 'html.parser')
    quest_head = soup2.find_all('div', class_='questoes-enem-vestibular')

    # pega um indice de questão aleatória
    quests_list = list(range(int(quest_qtd)))
    shuffle(quests_list)
    quest_index = quests_list.pop()

    # pega uma questão
    try:
        quest_beta = (quest_head[quest_index]).get_text().strip()
    except:
        quest_beta = 'Erro: Não achamos essa questão :(. Tente Novamente'

    # pega a resposta
    try:
        chemistry_ans = resposta(url2, quest_index)
    except:
        chemistry_ans = f"Algo deu errado. Tente novamente ou verifique a resposta em: {url2}"

    questChe = spaces(quest_beta)
    return str(questChe)


def physics():
    global questFis
    global physics_ans
    url = 'https://projetoagathaedu.com.br/banco-de-questoes/fisica.php'
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

    # lista de matérias
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    grids = soup.find_all('div', class_='opcao')

    # pega um indice de matéria aleatória
    index_list = list(range(26))
    shuffle(index_list)
    index = index_list.pop()

    # pega a caixa da matéria
    grid = grids[index]

    # pega o link da matéria
    str_link = str(grid.find('a', href=True))
    list_link = str_link.split("\n")
    href = list_link[0]
    link = href[11:len(href) - 2]
    url2 = f'https://projetoagathaedu.com.br{link}'

    # quantidade de questões da matéria
    quest_qtd = grid.find('div', class_='lista-tema-numero').get_text()

    # lista de questões
    quest_bank = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(quest_bank.content, 'html.parser')
    quest_head = soup2.find_all('div', class_='questoes-enem-vestibular')

    # pega um indice de questão aleatória
    quests_list = list(range(int(quest_qtd)))
    shuffle(quests_list)
    quest_index = quests_list.pop()

    # pega uma questão
    try:
        quest_beta = (quest_head[quest_index]).get_text().strip()
    except:
        quest_beta = 'Erro: Não achamos essa questão :(. Tente Novamente'

    # pega a resposta
    try:
        physics_ans = resposta(url2, quest_index)
    except:
        physics_ans = f"Algo deu errado. Tente novamente ou verifique a resposta em: {url2}"

    questFis = spaces(quest_beta)
    return str(questFis)


def history():
    global questHis
    global history_ans
    url = 'https://projetoagathaedu.com.br/banco-de-questoes/historia.php'
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

    # lista de matérias
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    grids = soup.find_all('div', class_='opcao')

    # pega um indice de matéria aleatória
    index_list = list(range(19))
    shuffle(index_list)
    index = index_list.pop()

    # pega a caixa da matéria
    grid = grids[index]

    # pega o link da matéria
    str_link = str(grid.find('a', href=True))
    list_link = str_link.split("\n")
    href = list_link[0]
    link = href[11:len(href) - 2]
    url2 = f'https://projetoagathaedu.com.br{link}'

    # quantidade de questões da matéria
    quest_qtd = grid.find('div', class_='lista-tema-numero').get_text()

    # lista de questões
    quest_bank = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(quest_bank.content, 'html.parser')
    quest_head = soup2.find_all('div', class_='questoes-enem-vestibular')

    # pega um indice de questão aleatória
    quests_list = list(range(int(quest_qtd)))
    shuffle(quests_list)
    quest_index = quests_list.pop()

    # pega uma questão
    try:
        quest_beta = (quest_head[quest_index]).get_text().strip()
    except:
        quest_beta = 'Erro: Não achamos essa questão :(. Tente Novamente'

    # pega a resposta
    try:
        history_ans = resposta(url2, quest_index)
    except:
        history_ans = f"Algo deu errado. Tente novamente ou verifique a resposta em: {url2}"

    questHis = spaces(quest_beta)
    return str(questHis)


def languages():
    global questLin
    global languages_ans
    url = 'https://projetoagathaedu.com.br/banco-de-questoes/linguagens.php'
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

    # lista de matérias
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    grids = soup.find_all('div', class_='opcao')

    # pega um indice de matéria aleatória
    index_list = list(range(41))
    shuffle(index_list)
    index = index_list.pop()

    # pega a caixa da matéria
    grid = grids[index]

    # pega o link da matéria
    str_link = str(grid.find('a', href=True))
    list_link = str_link.split("\n")
    href = list_link[0]
    link = href[11:len(href) - 2]
    url2 = f'https://projetoagathaedu.com.br{link}'

    # quantidade de questões da matéria
    quest_qtd = grid.find('div', class_='lista-tema-numero').get_text()

    # lista de questões
    quest_bank = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(quest_bank.content, 'html.parser')
    quest_head = soup2.find_all('div', class_='questoes-enem-vestibular')

    # pega um indice de questão aleatória
    quests_list = list(range(int(quest_qtd)))
    shuffle(quests_list)
    quest_index = quests_list.pop()

    # pega uma questão
    try:
        quest_beta = (quest_head[quest_index]).get_text().strip()
    except:
        quest_beta = 'Erro: Não achamos essa questão :(. Tente Novamente'

    # pega a resposta
    try:
        languages_ans = resposta(url2, quest_index)
    except:
        languages_ans = f"Algo deu errado. Tente novamente ou verifique a resposta em: {url2}"

    questLin = spaces(quest_beta)
    return str(questLin)


def humans():
    global questHum
    global humans_ans
    url = 'https://projetoagathaedu.com.br/banco-de-questoes/geografia-sociologia-e-filosofia.php'
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

    # lista de matérias
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    grids = soup.find_all('div', class_='opcao')

    # pega um indice de matéria aleatória
    index_list = list(range(11))
    shuffle(index_list)
    index = index_list.pop()

    # pega a caixa da matéria
    grid = grids[index]

    # pega o link da matéria
    str_link = str(grid.find('a', href=True))
    list_link = str_link.split("\n")
    href = list_link[0]
    link = href[11:len(href) - 2]
    url2 = f'https://projetoagathaedu.com.br{link}'

    # quantidade de questões da matéria
    quest_qtd = grid.find('div', class_='lista-tema-numero').get_text()

    # lista de questões
    quest_bank = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(quest_bank.content, 'html.parser')
    quest_head = soup2.find_all('div', class_='questoes-enem-vestibular')

    # pega um indice de questão aleatória
    quests_list = list(range(int(quest_qtd)))
    shuffle(quests_list)
    quest_index = quests_list.pop()

    # pega uma questão
    try:
        quest_beta = (quest_head[quest_index]).get_text().strip()
    except:
        quest_beta = 'Erro: Não achamos essa questão :(. Tente Novamente'

    # pega a resposta
    try:
        humans_ans = resposta(url2, quest_index)
    except:
        humans_ans = f"Algo deu errado. Tente novamente ou verifique a resposta em: {url2}"

    questHum = spaces(quest_beta)
    return str(questHum)


class Manager(ScreenManager):
    pass


class Menu(Screen):
    pass


class QuestMath(Screen):

    def print_quest(self):
        global questMath
        questMath = ''
        math()
        return questMath

    def press(self):
        self.ids.questMathScreen.text = ' '
        questMath = math()
        self.ids.questMathScreen.text = questMath
        self.ids.respostamath.text = 'Mostrar Resposta'

    def answerclick(self):
        global math_ans
        self.ids.respostamath.text = math_ans


class QuestLang(Screen):
    def print_quest(self):
        global questLin
        questLin = ''
        languages()
        return questLin

    def press(self):
        self.ids.questLinScreen.text = ' '
        questLin = languages()
        self.ids.questLinScreen.text = questLin
        self.ids.respostalang.text = 'Mostrar Resposta'

    def answerclick(self):
        global languages_ans
        self.ids.respostalang.text = languages_ans


class QuestBio(Screen):
    def print_quest(self):
        global questBio
        questBio = ''
        bio()
        return questBio

    def press(self):
        self.ids.questBioScreen.text = ' '
        questBio = bio()
        self.ids.questBioScreen.text = questBio
        self.ids.respostabio.text = 'Mostrar Resposta'

    def answerclick(self):
        global bio_ans
        self.ids.respostabio.text = bio_ans


class QuestQuim(Screen):
    def print_quest(self):
        global questChe
        questChe = ''
        chemistry()
        return questChe

    def press(self):
        self.ids.questQuiScreen.text = ' '
        questQui = chemistry()
        self.ids.questQuiScreen.text = questChe
        self.ids.respostaquim.text = 'Mostrar Resposta'

    def answerclick(self):
        global chemistry_ans
        self.ids.respostaquim.text = chemistry_ans


class QuestFis(Screen):
    def print_quest(self):
        global questFis
        questFis = ''
        physics()
        return questFis

    def press(self):
        self.ids.questFisScreen.text = ' '
        questFis = physics()
        self.ids.questFisScreen.text = questFis
        self.ids.respostafis.text = 'Mostrar Resposta'

    def answerclick(self):
        global physics_ans
        self.ids.respostafis.text = physics_ans


class QuestHist(Screen):
    def print_quest(self):
        global questHis
        questHis = ''
        history()
        return questHis

    def press(self):
        self.ids.questHisScreen.text = ' '
        questHis = history()
        self.ids.questHisScreen.text = questHis
        self.ids.respostahis.text = 'Mostrar Resposta'

    def answerclick(self):
        global history_ans
        self.ids.respostahis.text = history_ans


class QuestHum(Screen):
    def print_quest(self):
        global questHum
        questHum = ''
        humans()
        return questHum

    def press(self):
        self.ids.questHumScreen.text = ' '
        questHum = humans()
        self.ids.questHumScreen.text = questHum
        self.ids.respostahum.text = 'Mostrar Resposta'

    def answerclick(self):
        global humans_ans
        self.ids.respostahum.text = humans_ans


class EnemApp(App):
    pass


EnemApp().run()
