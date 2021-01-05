from bs4 import BeautifulSoup

'''newFile=[]
t=open('index.html','w')
for i in study:
    if 'href=' in i and 'https' not in i:
        sp=i[0].split()
        equal=i.find("=")
        new=i[equal+2:-2]
        i="href='{% static "+new+" %}"
    newFile.append(i)

t.write(str(newFile))
'''

f=open('index.html','r')
html_doc=f.read()
'''for i in range(len(study)):
    if study[i:i+4]=="href":

        print(study[i:i+4])
p=study.find("href=")
'''
soup = BeautifulSoup(html_doc, 'html.parser')

for link in soup.find_all('a'):
    lin="{%static "+link.get('href')+" %}"

t=open('indexx.html','w')
bir=soup.find_all('a')
for lin in bir:
    soup = BeautifulSoup(html_doc, 'html.parser')
    sin="{%static "+lin.get('href')+" %}"
    soup.a['href'] =sin
    print(soup.a)

t.write(str(soup))

t.close()


