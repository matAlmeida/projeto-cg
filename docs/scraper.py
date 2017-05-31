import bs4 as bs
import urllib.request
import json
import re

def clean(soup, bStr, aStr):

    newSoup = []
    for x in soup:
        i = str(x).replace(bStr, '')
        r = i.replace(aStr, '')
        newSoup.append(r)
    
    return newSoup

def my_dictfy(titles, elements):  

    my_dict = {}

    for i in range(len(titles)):
        my_dict[titles[i]] = elements[i]
    
    return my_dict

def get_my_letter(soup, className):
    
    return clean(soup.findAll('div', {'class' : className}), '<div class="'+ className +'">', '</div>')

def updateTutoriais():
    sauce = urllib.request.urlopen('http://localhost:5252/modeloTutorial.html').read()
    soup = bs.BeautifulSoup(sauce, 'html.parser')

    tutorialNumbers = get_my_letter(soup, 'numeroTutorial')
    titles = get_my_letter(soup, 'titulo')
    links = get_my_letter(soup, 'linkdotutorial')
    library = get_my_letter(soup, 'bibliotecas')
    description = get_my_letter(soup, 'descricao')

    titulos = ['Numero', 'Titulo', 'Link', 'Bibliotecas', 'Descricao']
    tutoriais = []

    for i in range(len(tutorialNumbers)):
        elementos = [tutorialNumbers[i], titles[i], links[i], library[i], description[i]]
        tutoriais.append(my_dictfy(titulos, elementos))

    funcName = 'function get_info_tuto() {\n return ' + str(tutoriais) + '; }'
    funcName = funcName.replace('return [', '\treturn [\n')
    funcName = funcName.replace('];', '\n\t];\n')
    funcName = funcName.replace('},', '},\n')

    myJs = open('res/tutorial-info.js', 'w')
    myJs.write(funcName)
    myJs.close()

def updateApi():
    sauce2 = urllib.request.urlopen('http://localhost:5252/modeloAPI.html').read()
    soup2 = bs.BeautifulSoup(sauce2, 'html.parser')

    funcoes = get_my_letter(soup2, 'nomeFuncao')
    descricoes = get_my_letter(soup2, 'descricao')
    params = get_my_letter(soup2, 'parametros')
    retornos = get_my_letter(soup2, 'retorno')
    protot = get_my_letter(soup2, 'prototipo')
    vari = get_my_letter(soup2, 'variacoes')

    uhum = ['Função', 'Descrição', 'Parâmetros', 'Retorno', 'Protótipo', 'Variações da Função']
    infos = []

    for i in range(len(funcoes)):
        elementos = [funcoes[i], descricoes[i], params[i], retornos[i], protot[i], vari[i]]
        infos.append(my_dictfy(uhum, elementos))

    apinames = 'function get_info_api() {\n return ' + str(infos) + '; }'
    apinames = apinames.replace('return [', '\treturn [\n')
    apinames = apinames.replace('];', '\n\t];\n')
    apinames = apinames.replace('},', '},\n')

    myJs = open('res/api-info.js', 'w')
    myJs.write(apinames)
    myJs.close()

updateTutoriais()
updateApi()