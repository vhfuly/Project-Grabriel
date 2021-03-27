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
    
API.change_balance(changeBs)


profile = API.get_profile_ansyc()
print(profile)



