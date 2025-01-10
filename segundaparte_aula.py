from bs4 import BeautifulSoup
import requests
import time

#armazena na variavel unfamiliar_skill a habilidade que nao possui para filtra-la posteriormente
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
#realiza o request para a URL do timesjobs
html_link = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=')
html_text = html_link.text #extrai o texto HTML
soup = BeautifulSoup(html_text, 'lxml') #realiza o parser HTML 
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx') #localiza todas as tag li que possuem a classe especificada

def find_jobs():
    for index,job in enumerate(jobs): #itera sobre cada vaga e utiliza enumerate para obter indice e valor
        published_date = job.find('span', class_ = 'sim-posted').span.text #localiza a publicacao de cada data
        if 'few' in published_date: #condicional para somente obter datas recentes
            #obtem o nome e habilidades removendo espaços e tabulacoes
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '').replace('\t', '')
            skills = job.find('div', class_='more-skills-sections').text.replace(' ', '').replace('\t', '')
            #obtem todas as tags a que possuem href para obter o link de acesso para a pagina com mais informacoes
            more_info = job.a['href']

            if unfamiliar_skill not in skills: #verifica se a string do input nao esta presentes na lista skills
                with open(f'posts/{index}.txt', 'w') as f: #abre o arquivo em modo de escrita
                    #a cada loop escreve as informacoes nas variaveis abaixo
                    f.write(f'Company Name: {company_name.strip()}\n')
                    f.write(f'Required Skills: {skills.strip()}\n')
                    f.write(f'More info: {more_info}\n')
        
#verifica se o arquivo nao esta sendo executado em modulo
if __name__ ==  '__main__':
    while True:
        find_jobs()
        time_wait = 10 #define o tempo de espera para atualizar as vagas na pasta posts
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)