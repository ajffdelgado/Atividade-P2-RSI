# -*- coding: cp1252 -*-
from socket import *

serverPort = 12000
#Cria o Socket UDP (SOCK_DGRAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_DGRAM)
#Associa o Socket criado com a porta desejada
serverSocket.bind(('', serverPort))
lastID = 0
ack = "ack0"

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

while 1:
    try:
        #Aguarda receber dados do socket
        message, clientAddress = serverSocket.recvfrom(2048)
	nomeArquivo = "arq"+str(clientAddress[1])+".txt"
	arquivo = open(nomeArquivo,'a')
        print(clientAddress)
	message = message.split("<>")
	indice = message[0]
	print(message)
	if (indice == lastID):
		print ("Linhas iguais")
		serverSocket.sendto(ack,clientAddress)
		continue
	else:	
		print ("Linhas diferentes. Add arq")
		print("Vou add no arq: " + message[2])
		arquivo.write(message[2])
		#serverSocket.sendto(estado,clientAddress)
		lastID = indice
		if(message[1] == "pkt0"):
			ack = "ack0"
			serverSocket.sendto(ack,clientAddress)
			continue
		if(message[1] == "pkt1"):
			ack = "ack1"
			serverSocket.sendto(ack,clientAddress)
			continue
       # modifiedMessage = message.upper()
        print (modifiedMessage)
        #serverSocket.sendto("ack", clientAddress)
        arquivo.close()
    except (KeyboardInterrupt, SystemExit):
        break

serverSocket.close()

