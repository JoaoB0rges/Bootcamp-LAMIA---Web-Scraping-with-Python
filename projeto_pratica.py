from bs4 import BeautifulSoup
import requests

print('Insira a(s) criptomoeda(s) do qual deseja informacoes:\n')
crypto = input('>').split() #busca o input do usuario e o divide em uma lista caso digite mais de uma cripto

def find_crypto():
    link = requests.get('https://www.coingecko.com/pt') #faz a requisicao para a pagina
    soup = BeautifulSoup(link.text, 'lxml') #realiza o parser
    #encontra cada linha que estao presentes as criptos na pagina
    coins = soup.find_all('tr', class_ ='hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm' )

    for ind,coin in enumerate(coins):
        #encontra o nome, preco e link pra mais informacoes dentro da pagina
        coin_name = coin.find('div', class_ = 'tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5').text.replace(' ', '').split()[0]
        coin_price = coin.find('td', class_ = 'tw-text-end tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-gray-900 dark:tw-text-moon-50').text
        more_info = coin.a['href']

        if coin_name in crypto: #busca os nomes das criptos digitadas pelo usuario
            with open(f'criptos/cripto{ind}.txt', 'w') as file: #abre arquivo em modo escrita
                #escreve as informacoes
                file.write(f'Nome Criptomoeda: {coin_name.strip()}\n')
                file.write(f'Valor Criptomoeda: {coin_price.strip()}\n')
                file.write(f'Mais informacoes da Criptomoeda: https://www.coingecko.com{more_info}\n')

#executa o programa somente se o modulo estiver rodando diretamente
if __name__ == '__main__':
    find_crypto()