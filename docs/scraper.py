import bs4 as bs
import urllib.request
import json
import re

sauce = urllib.request.urlopen('http://localhost:5252/api.html').read()
soup = bs.BeautifulSoup(sauce, 'html.parser')
title = soup.select('li > strong')
data = soup.select('li > p')
newData = []
newTitle = []

for d in data:
    d = re.sub('<.*?>', '', str(d))
    newData.append(d)

for t in title:
    t = re.sub('<.*?>', '', str(t))
    newTitle.append(t)

api = []
f = {}
for i in range(len(newData)):
    if((i > 0) and (newTitle[i] == "Função: ")):
        api.append(f)
        print(f)
        f = {}
        f[newTitle[i]] = newData[i]
        continue
    f[newTitle[i]] = newData[i]

output_file = open('output.json', 'w')
json.dump(api, output_file)
output_file.close

# print(len(newData))
    

# for i in data:
#     api.append(re.sub('<.*?>', '', str(i)))
