from iqoptionapi.stable_api import IQ_Option
import logging
import userdata

asset = "EURUSD-OTC"
maxdict = 10
size = 300

logging.disable(level=(logging.DEBUG))
print('Aguarde enquanto o login está sendo feito...')
user = userdata.mainUser
API = IQ_Option(user["username"], user["password"])
check, reason =API.connect()
while True:
	if API.check_connect() == False:
		print('Erro ao se conectar')
		API.connect()
	else:
		print('Conectado!')
		break
	
	time.sleep(1)

changeB = input("Pratica ou Real? 1- Pratica 2- Real:")
if changeB == '1':
    changeBs = 'PRACTICE'
elif changeB == '2':
    changeBs = 'REAL'
    
primeiro_nome = input('\nDigite o primeiro nome caso souber: ')
outro_nome = input('\nCaso souber outra parte do nome, digite: ')
outro_nome = '3214768413168431354684' if outro_nome == '' else outro_nome

print('\nEscreva a sigla do pais ou deixe vazio', end='')
while True:
	pais = input(':')
	if pais != '':
		if pais.upper() in Pais.ID:
			break
	else:
		break
		
print('\n1 - Metodo Rapido: Busca apenas pelo primeiro nome')
print('2 - Metodo Lento: Realiza uma busca completa')
print('3 - Metodo Misto: Se o primeiro nome for igual, procura pelo outro nome')
metodo = input('Digite a opcao: ')
metodo = 3 if metodo == '' or int(metodo) >= 4 else metodo

print('\n Busca iniciada, aguarde..\n')

last = 1
for i in range(1, 1000):
	quantidade = int(i) * 500
	
	data = API.get_leader_board('Worldwide' if pais == '' else pais.upper(), last, quantidade, 0)
	
	for colocacao in data['result']['positional']:
		nome_ranking = data['result']['positional'][colocacao]['user_name']

		if int(metodo) == 2 or int(metodo) == 3 and primeiro_nome.lower() in nome_ranking.lower():
			segunda_busca = API.get_user_profile_client(data['result']['positional'][colocacao]['user_id'])
		else:
			segunda_busca = {'user_name': '', 'registration_time': 0}
		
		if (int(metodo) == 1 and primeiro_nome.lower() in nome_ranking.lower()) or (int(metodo) == 2 and primeiro_nome.lower() in nome_ranking.lower() or outro_nome.lower() in segunda_busca['user_name'].lower()) or (int(metodo) == 3 and primeiro_nome.lower() in nome_ranking.lower() and outro_nome.lower() in segunda_busca['user_name'].lower()): 
		
			if int(metodo) != 2:
				segunda_busca = API.get_user_profile_client(data['result']['positional'][colocacao]['user_id'])
			
			print('\n\n ['+str(colocacao)+']Nome:',nome_ranking,'/',segunda_busca['user_name'])
			print(' User ID:',data['result']['positional'][colocacao]['user_id'])
			print(' Pais: '+data['result']['positional'][colocacao]['flag'])
			print(' status:', segunda_busca['status'])
			print(' Faturamento esta semana:',round(data['result']['positional'][colocacao]['score'], 2))
			print('\n')
			input('Deseja continuar? Aperte enter, para encerrar o codigo, aperte CRTL+C\n')

	if len(data) == 0:
		print('\nBusca finalizada\n')
		break
	
	last = quantidade



