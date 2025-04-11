import argparse
from cryptography.fernet import Fernet
import os
import time

print('------------------ *_* EncryptMe *_* ------------------')

# criando o parse
parser = argparse.ArgumentParser(description="Encriptador de arquivos rápido")

def salvar_chave(chave, caminho_chave='Chave.key'):
    """Salva a chave em um arquivo externo para reutilização futura."""
    with open(caminho_chave, 'wb') as chave_arquivo:
        chave_arquivo.write(chave)
if not os.path.exists('Chave.key'):
    salvar_chave(Fernet.generate_key())

def ler_chave(caminho_chave='Chave.key'):
    """Lê a chave salva em um arquivo externo."""
    with open(caminho_chave, 'rb') as chave_arquivo:
        return chave_arquivo.read()
fernet = Fernet(ler_chave())

def encriptar_arquivo(caminho_arquivo: str):
    """função para encriptar o arquivo"""

    with open(caminho_arquivo, 'rb') as ler_arquivo:
        dados = ler_arquivo.read()
    encriptado = fernet.encrypt(dados)
    with open(caminho_arquivo, 'wb') as encriptar:
        print('Encriptando...*_*\n')
        time.sleep(3)
        print('Arquivo encriptado com sucesso :)...')
        encriptar.write(encriptado)

def decriptografar_arquivo(caminho_arquivo: str):
    """função responsável por decriptografar o arquivo"""

    with open(caminho_arquivo, 'rb') as ler_arquivo:
        dados_encriptado = ler_arquivo.read()
    try:
        decriptografar = fernet.decrypt(dados_encriptado)
        with open(caminho_arquivo, 'wb') as dados_decriptografado:
            print('Decriptografando...*O*')
            time.sleep(3)
            print('Arquivo decriptado com sucesso :)...')
            dados_decriptografado.write(decriptografar)
    except Exception as error:
        print(f'Avalie o erro e tente novamente: {error}')

if __name__=="__main__":
    # adicionando argumentos na linha de comando
    parser.add_argument('-a', '--arquivo', help='Nome do arquivo', required=True)
    parser.add_argument('-e', '--encriptar', help='Encriptar arquivo', action='store_true')
    parser.add_argument('-d', '--decriptografar', help='Decriptografar arquivo', action='store_true')
    args = parser.parse_args()

    # verifica as opções escolhidas pelo usuario e faz o devido processo
    if args.arquivo and args.encriptar:
        encriptar_arquivo(args.arquivo)
    elif args.arquivo and args.decriptografar:
        decriptografar_arquivo(args.arquivo)
    else:
        print('Digite um comando válido -_-')