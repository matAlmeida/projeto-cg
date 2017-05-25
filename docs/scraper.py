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

sauce = urllib.request.urlopen('http://localhost:5252/modeloTutorial.html').read()
soup = bs.BeautifulSoup(sauce, 'html.parser')

tutorialNumbers = soup.findAll('div', {'class' : 'numeroTutorial'})
titles = soup.findAll('div', {'class' : 'titulo'})
links = soup.findAll('div', {'class' : 'linkdotutorial'})
library = soup.findAll('div', {'class' : 'bibliotecas'})
description = soup.findAll('div', {'class' : 'descricao'})

tutorialNumbers = clean(tutorialNumbers, '<div class="numeroTutorial">', '</div>')
titles = clean(titles, '<div class="titulo">', '</div>')
links = clean(links, '<div class="linkdotutorial">', '</div>')
library = clean(library, '<div class="bibliotecas">', '</div>')
description = clean(description, '<div class="descricao">', '</div>')

titulos = ['Numero', 'Titulo', 'Link', 'Bibliotecas', 'Descricao']
tutoriais = []

for i in range(len(tutorialNumbers)):
    elementos = [tutorialNumbers[i], titles[i], links[i], library[i], description[i]]
    tutoriais.append(my_dictfy(titulos, elementos))

funcName = 'function get_info_api() {\n return ' + str(tutoriais) + '; }'
funcName = funcName.replace('return [', 'return [\n')
funcName = funcName.replace('];', '\n];\n')
funcName = funcName.replace('},', '},\n')

myJs = open('res/tutorial-info.js', 'w')
myJs.write(funcName)
myJs.close()

#function get_info_api() { return []; }

# title = soup.select('section > div')
# data = soup.select('li > p')
# newData = []
# newTitle = []

# for d in data:
#     d = re.sub('<.*?>', '', str(d))
#     newData.append(d)

# for t in title:
#     t = re.sub('<.*?>', '', str(t))
#     newTitle.append(t)

# api = []
# f = {}
# for i in range(len(newData)):
#     if((i > 0) and (newTitle[i] == "Função: ")):
#         api.append(f)
#         print(f)
#         f = {}
#         f[newTitle[i]] = newData[i]
#         continue
#     f[newTitle[i]] = newData[i]

# output_file = open('output.json', 'w')
# json.dump(api, output_file)
# output_file.close

# print(len(newData))
    

# for i in data:
#     api.append(re.sub('<.*?>', '', str(i)))