from bs4 import BeautifulSoup #importa a biblioteca

with open('home_aula.html', 'r') as html_file: #abre no modo leitura o arquivo 'home_aula' e executa em leitura
    content = html_file.read() #le o arquivo
    
    soup = BeautifulSoup(content, 'lxml') #utiliza o parser lxml ao invés do padrao python
    
    course_cards = soup.find_all('div', class_='card') #procura todas as divs com a classe card

    for course in course_cards: #loop para iterar sobre todos os elementos card 
        course_name = course.h5.text #acessa os elementos da classe card que possuem a tag h5 e extrai somente texto
        course_price = course.a.text.split()[-1] #acessa a tag 'a' e o texto, divide com split e extrai somente ultimo elemento

        print(f'{course_name} costs {course_price}')