import argparse
import whois
import nmap

# nome da ferramenta no console
parse = argparse.ArgumentParser(description="PyToolHacking")
nm = nmap.PortScanner()

# função responsavel pela logica da passagem de argumentos
def argumentscli():
    # adicionando argumentos para o terminal
    parse.add_argument("-a", "--alvo", help="Dominio", required=True)
    parse.add_argument('-i', '--ip', help="Ip", type=str, required=False)
    parse.add_argument("-p", "--porta", help="Porta", type=str, default=80, required=False)
    args = parse.parse_args()

    # associando os comandos a chamada das funções de outras bibliotecas
    alvo = whois.whois(args.alvo)
    scanear_alvo = nm.scan(args.ip, args.porta)

    # salva os dados e informações em um arquivo txt
    with open('alvo.txt', 'w', encoding='utf-8') as file:
        file.write(f'Informações salvas: '
                   f'{alvo}\n\n{scanear_alvo.items()}')
    print('Informações salva em alvo.txt')

if __name__=="__main__":
   argumentscli()