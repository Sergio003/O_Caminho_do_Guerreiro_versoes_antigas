# Jogo de rpg em python
# Produzido por Sérgio

# Módulos, pacotes e bibliotecas

import time
import sys
from random import randint

def escrita_rpg(texto):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.03)
def desenho_inicial_rpg(texto):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.004)
def desenho_creditos_rpg(texto):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.004)    




# Menu principal, créditos e sair do jogo


print('\n\n========================== MENU PRINCIPAL ===========================\n')                        
print('                        [1] Iniciar Jogo  ')                              
print('                        [2] Abrir Créditos')
print('                        [3] Sair  ')
print('\n')
print('='*69)
escolha = int(input('\nEscolha uma opção: '))
print('\n')
print('='*69)
print('\n')


if escolha == 1:
  time.sleep(2)
  texto = 'Por favor aguarde...\n'
  escrita_rpg(texto)
  texto = 'Abrindo o Jogo...\n'
  escrita_rpg(texto)
  time.sleep(2)
  desenho_inicial_rpg
  print('\n')
  print('='*197)
  print('='*197)
  texto = '''\n
  
  #####              ####     ##     ##   ##   ####    ##   ##  ##   ##   #####            #####     #####              ####   ##   ##  #######  ######   ######   #######   ####    ######    #####
 ##   ##            ##  ##   ####    ### ###    ##     ###  ##  ##   ##  ##   ##            ## ##   ##   ##            ##  ##  ##   ##   ##   #   ##  ##   ##  ##   ##   #    ##      ##  ##  ##   ##
 ##   ##           ##       ##  ##   #######    ##     #### ##  ##   ##  ##   ##            ##  ##  ##   ##           ##       ##   ##   ## #     ##  ##   ##  ##   ## #      ##      ##  ##  ##   ##
 ##   ##           ##       ##  ##   #######    ##     ## ####  #######  ##   ##            ##  ##  ##   ##           ##       ##   ##   ####     #####    #####    ####      ##      #####   ##   ##
 ##   ##           ##       ######   ## # ##    ##     ##  ###  ##   ##  ##   ##            ##  ##  ##   ##           ##  ###  ##   ##   ## #     ## ##    ## ##    ## #      ##      ## ##   ##   ##
 ##   ##            ##  ##  ##  ##   ##   ##    ##     ##   ##  ##   ##  ##   ##            ## ##   ##   ##            ##  ##  ##   ##   ##   #   ##  ##   ##  ##   ##   #    ##      ##  ##  ##   ##
  #####              ####   ##  ##   ##   ##   ####    ##   ##  ##   ##   #####            #####     #####              #####   #####   #######  #### ##  #### ##  #######   ####    #### ##   #####



                                                                              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⣟⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣻⠽⡝⡎⡏⠭⡪⠪⡒⣽⣽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⣿⣿⣿⣿⡿⣻⢝⢎⢝⢜⠸⡨⢊⢌⠪⡈⢪⢸⢸⢽⢯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⣿⣿⢟⢵⠹⡘⠔⡡⠑⢠⣕⣬⣖⣮⡾⠯⢟⣆⠣⡫⡹⡱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⣿⣿⣵⡥⡊⠄⣗⢶⡛⠖⣶⣿⣟⡗⠞⢿⢯⣗⡇⢅⠣⡱⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⣿⣿⣿⡯⠌⡮⣿⣿⡇⠄⣿⣿⣿⡇⠄⢸⣟⢮⡺⡔⠡⡊⡎⡼⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⣿⣵⡹⡙⡇⢟⣿⣿⣿⣾⣿⣟⣾⣻⣟⣟⣞⡝⡞⡆⡑⡘⡨⢨⡢⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⣿⣷⣟⡯⡇⠪⡿⣞⣯⡿⣫⣖⢮⢜⢮⡺⡜⡎⡇⡃⢜⢼⠸⢑⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⣿⣿⣿⡯⣣⣥⠷⣿⣮⡝⢕⠵⡹⡪⡣⡣⡣⡣⢃⢂⠂⢇⢆⣢⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⣿⣿⠿⡫⣵⣕⣛⣽⣕⠿⡷⣧⣈⡢⡁⠅⢁⢂⢂⢢⣿⣔⠅⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⡯⢏⣞⣯⣟⣛⢿⢽⢟⡽⣎⢯⢝⡝⡦⡁⢆⠐⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⡿⡸⡪⣓⣛⣛⡝⡿⢿⢝⢞⢎⢇⢵⢹⢌⢢⠑⢌⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⢎⡎⡌⠪⢸⡑⡘⡜⠅⡃⡱⠡⡣⡣⡣⢃⠪⡊⢆⠌⠨⣻⣿⡿⠛⢋⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣧⢻⢌⢬⢜⠸⠨⡨⡐⢔⢌⢌⢎⠎⠆⢂⠑⢌⡂⠅⢌⢢⢛⠠⠊⡄⡛⡻⡻⡿⢿⢿⠿⡿⡿⢿⢿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⢜⡤⡱⢸⠨⠪⡐⡨⡰⡑⡅⡇⠅⠨⢈⠐⠠⢘⠠⠐⡐⠄⡂⢕⢦⢪⢦⣗⣮⣷⣭⣮⣮⣾⡵⣧⣧⡻⣿⣿
                                                                              ⣿⣿⣿⣿⣪⡣⣝⢭⢊⢆⢇⢇⠇⠡⢐⠨⠐⢌⠊⠅⠅⢌⢻⣄⢕⢰⣶⣾⣼⣵⣷⣽⣺⡯⡿⣷⣿⡯⡺⣚⣮⣾⣿
                                                                              ⣿⣿⣿⣿⣿⣾⣜⢜⢜⡮⠘⠂⠆⠅⢢⣡⠑⠐⠁⡁⠅⠱⢿⣿⣴⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⣿⣿⣿⣿⣿⡿⡹⠈⠄⠠⠄⣿⣿⡈⠄⡀⠄⠄⠐⡐⠐⠽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                              ⣿⣿⣿⣿⣿⣿⣿⣿⣇⡊⠄⠡⢈⣄⣿⣿⣿⣷⣶⣶⣷⣶⣶⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
                                                                              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
'''

elif escolha == 3:
  input('Tem certeza que deseja sair do jogo? \nDigite [1] Sim [2] Não: ')
  exit()

elif escolha == 2:
  texto = 'Abrindo Créditos...\n'
  escrita_rpg(texto)
  print('\n')
  print('='*69)
  time.sleep(2)
  texto = '''
        
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⢄⢄⠢⡠⡀⢀⠄⡀⡀⠄⠄⠄⠄⠐⠡⠄⠉⠻⣻⣟⣿⣿⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⢣⠣⡎⡪⢂⠊⡜⣔⠰⡐⠠⠄⡾⠄⠈⠠⡁⡂⠄⠔⠸⣻⣿⣿⣯⢂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠐⢰⡱⣝⢕⡇⡪⢂⢊⢪⢎⢗⠕⢕⢠⣻⠄⠄⠄⠂⠢⠌⡀⠄⠨⢚⢿⣿⣧⢄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡐⡈⠌⠄⠄⠄⠄⠄⠄⠄⡧⣟⢼⣕⢝⢬⠨⡪⡚⡺⡸⡌⡆⠜⣾⠄⠄⠄⠁⡐⠠⣐⠨⠄⠁⠹⡹⡻⣷⡕⢄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢄⠇⠂⠄⠄⠄⠄⠄⠄⠄⢸⣻⣕⢗⠵⣍⣖⣕⡼⡼⣕⢭⢮⡆⠱⣽⡇⠄⠄⠂⠁⠄⢁⠢⡁⠄⠄⠐⠈⠺⢽⣳⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢔⢕⢌⠄⠄⠄⠄⠄⢀⠄⠄⣾⢯⢳⠹⠪⡺⡺⣚⢜⣽⣮⣳⡻⡇⡙⣜⡇⠄⠄⢸⠄⠄⠂⡀⢠⠂⠄⢶⠊⢉⡁⠨⡒⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡨⣪⣿⢰⠈⠄⠄⠄⡀⠄⠄⠄⣽⣵⢿⣸⢵⣫⣳⢅⠕⡗⣝⣼⣺⠇⡘⡲⠇⠄⠄⠨⠄⠐⢀⠐⠐⠡⢰⠁⠄⣴⣾⣷⣮⣇⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡮⣷⣿⠪⠄⠄⠄⠠⠄⠂⠠⠄⡿⡞⡇⡟⣺⣺⢷⣿⣱⢕⢵⢺⢼⡁⠪⣘⡇⠄⠄⢨⠄⠐⠄⠄⢀⠄⢸⠄⠄⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣺⣿⣿⣇⠄⠄⠄⠄⢀⣤⣖⢯⣻⡑⢕⢭⢷⣻⣽⡾⣮⡳⡵⣕⣗⡇⠡⡣⣃⠄⠄⠸⠄⠄⠄⠄⠄⠄⠈⠄⠄⢻⣿⣿⣵⡿⣹⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣟⣯⢄⢤⢲⣺⣻⣻⡺⡕⡔⡊⡎⡮⣿⣿⣽⡿⣿⣻⣼⣼⣺⡇⡀⢎⢨⢐⢄⡀⠄⢁⠠⠄⠄⠐⠄⠣⠄⠸⣿⣿⣯⣷⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⢽⠲⡑⢕⢵⢱⢪⡳⣕⢇⢕⡕⣟⣽⣽⣿⣿⣿⣿⣿⣿⣿⢗⢜⢜⢬⡳⣝⢸⣢⢀⠄⠄⠐⢀⠄⡀⠆⠄⠸⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⢽⣝⢎⡪⡰⡢⡱⡝⡮⡪⡣⣫⢎⣿⣿⣿⣿⣿⣿⠟⠋⠄⢄⠄⠈⠑⠑⠭⡪⡪⢏⠗⡦⡀⠐⠄⠄⠈⠄⠄⠙⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⡲⣝⢮⢪⢊⢎⢪⢺⠪⣝⢮⣯⢯⣟⡯⠷⠋⢀⣠⣶⣾⡿⠿⢀⣴⣖⢅⠪⠘⡌⡎⢍⣻⠠⠅⠄⠄⠈⠢⠄⠄⠙⠿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣽⢺⢍⢎⢎⢪⡪⡮⣪⣿⣞⡟⠛⠋⢁⣠⣶⣿⡿⠛⠋⢀⣤⢾⢿⣕⢇⠡⢁⢑⠪⡳⡏⠄⠄⠄⠄⠄⠄⢑⠤⢀⢠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣟⣮⡳⣭⢪⡣⡯⡮⠗⠋⠁⠄⠄⠈⠿⠟⠋⣁⣀⣴⣾⣿⣗⡯⡳⡕⡕⡕⡡⢂⠊⢮⠃⠄⠄⠄⠄⠄⢀⠐⠨⢁⠨⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⣿⣿⠷⠯⠽⠐⠁⠁⢀⡀⣤⢖⣽⢿⣦⣶⣾⣿⣿⣿⣿⣿⣿⢎⠇⡪⣸⡪⡮⠊⠄⠌⠎⡄⠄⠄⠄⠄⠄⠄⡂⢁⠉⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠛⠚⠒⠵⣶⣶⣶⣶⢪⢃⢇⠏⡳⡕⣝⢽⡽⣻⣿⣿⣿⣿⡿⣺⠰⡱⢜⢮⡟⠁⠄⠄⠅⠅⢂⠐⠄⠐⢀⠄⠄⠄⠂⡁⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠰⠄⠐⢒⣠⣿⣟⢖⠅⠆⢝⢸⡪⡗⡅⡯⣻⣺⢯⡷⡯⡏⡇⡅⡏⣯⡟⠄⠄⠄⠨⡊⢔⢁⠠⠄⠄⠄⠄⠄⢀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣿⣿⢿⢕⢇⢣⢸⢐⢇⢯⢪⢪⠢⡣⠣⢱⢑⢑⠰⡸⡸⡇⠁⠄⠄⠠⡱⠨⢘⠄⠂⡀⠂⠄⠄⠄⠄⠈⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣟⣝⢔⢅⠸⡘⢌⠮⡨⡪⠨⡂⠅⡑⡠⢂⢇⢇⢿⠁⠄⢀⠠⠨⡘⢌⡐⡈⠄⠄⠠⠄⠄⠄⠄⠄⠄⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣿⣯⢢⢊⢌⢂⠢⠑⠔⢌⡂⢎⠔⢔⢌⠎⡎⡮⡃⢀⠐⡐⠨⡐⠌⠄⡑⠄⢂⠐⢀⠄⠄⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣯⠂⡀⠔⢔⠡⡹⠰⡑⡅⡕⡱⠰⡑⡜⣜⡅⡢⡈⡢⡑⡢⠁⠰⠄⠨⢀⠐⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⢿⣿⣷⣢⢱⠡⡊⢌⠌⡪⢨⢘⠜⡌⢆⢕⢢⢇⢆⢪⢢⡑⡅⢁⡖⡄⠄⠄⠄⢀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠛⢿⣿⣵⡝⣜⢐⠕⢌⠢⡑⢌⠌⠆⠅⠑⠑⠑⠝⢜⠌⠠⢯⡚⡜⢕⢄⠄⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⣷⡣⣇⠃⠅⠁⠈⡠⡠⡔⠜⠜⣿⣗⡖⡦⣰⢹⢸⢸⢸⡘⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠋⢍⣠⡤⡆⣎⢇⣇⢧⡳⡍⡆⢿⣯⢯⣞⡮⣗⣝⢎⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⣿⣿⣎⢦⠣⠳⠑⠓⠑⠃⠩⠉⠈⠈⠉⠄⠁⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡿⡞⠁⠄⠄⢀⠐⢐⠠⠈⡌⠌⠂⡁⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢂⢂⢀⠡⠄⣈⠠⢄⠡⠒⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠢⠠⠊⠨⠐⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄

              ***** Jogo Desenvolvido Por Sérgio ***** \n'''
  
desenho_creditos_rpg(texto)
print('\n')


time.sleep(2)
print('\n')
print('='*197)
print('='*197)
  


# Nome do(a) personagem

time.sleep(2)
nome = input('\n\nQual é o seu nome? ')
time.sleep(2)
texto = f'Olá {nome} seja muito bem vindo ao jogo caminho do guerreiro.\n'
escrita_rpg(texto)
time.sleep(2)
texto = 'Vamos juntos encarar uma grande aventura! '
escrita_rpg(texto)

# Inicio história do jogo

time.sleep(2)
print('\n')
print('='*197)
print('\n')
time.sleep(2)
texto = 'Capítulo 1: O Início da Jornada '
escrita_rpg(texto)
print('\n')
time.sleep(2)
texto = 'Há muito tempo, em um mundo mágico e misterioso, existia uma pedra elemental poderosa que possuía o controle sobre os quatro elementos fundamentais: água, fogo, terra e ar.\n'
escrita_rpg(texto)
texto = ('Esta pedra, conhecida como "A Pedra Elemental da Harmonia", era guardada no coração de um antigo lugar proibido chamado Reino de Saquarema.\n')
escrita_rpg(texto)
texto = ('Um dia, um vilão muito famoso conhecido como Sephiroth, em sua busca insaciável por poder, conseguiu roubar a Pedra Elemental da Harmonia e a quebrou em quatro partes.\n')
escrita_rpg(texto)
texto = ('O mundo ficou instável, com furacões, terremotos, tsunamis e queimadas, pois cada parte da pedra continha o poder para controlar um elemento vital a humanidade.\n')
escrita_rpg(texto)
texto = ('Sephiroth escondeu as quatro partes elementais quebradas em diferentes reinos espalhados pelo mundo:\nReino de Jaconé, Reino de Barra Nova, Reino de Boqueirão e Reino de Bacaxá.\n')
escrita_rpg(texto)
texto = (f'Um(a) destemido(a) aventureiro(a) chamado(a) {nome}, foi convocado(a) por um antigo oráculo para recuperar as partes da Pedra Elemental da Harmonia e impedir\nque Sephiroth usasse seu poder para subjugar o mundo.\n')
escrita_rpg(texto)
print('\n')
print('='*197)
time.sleep(2)


