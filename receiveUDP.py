# -*- coding: cp1252 -*-
from socket import *

serverPort = 12000
#Cria o Socket UDP (SOCK_DGRAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_DGRAM)
#Associa o Socket criado com a porta desejada
serverSocket.bind(('', serverPort))
lastPkt = ""
ack = "ack0"
lastArquivo = ""

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

while 1:
    try:
        #Aguarda receber dados do socket
        message, clientAddress = serverSocket.recvfrom(2048)
	nomeArquivo = "arq"+str(clientAddress[1])+".txt"
	if(lastArquivo != nomeArquivo):
		lastArquivo = nomeArquivo
		ack = "ack0"
	arquivo = open(nomeArquivo,'a')
        print(clientAddress)
	message = message.split("<>")
	pkt = message[0]
	#print(message)
	print("pkt: " +pkt+ " - last: " + lastPkt)
	if (pkt == lastPkt):
		print ("Linhas iguais")
		serverSocket.sendto(ack,clientAddress)
		continue
	else:	
		print ("Linhas diferentes. Add arq")
		#print("Vou add no arq: " + message[1])
		arquivo.write(message[1])
		#serverSocket.sendto(estado,clientAddress)
		lastPkt = pkt
		if(message[0] == "pkt0"):
			ack = "ack0"
			serverSocket.sendto(ack,clientAddress)
			continue
		if(message[0] == "pkt1"):
			ack = "ack1"
			serverSocket.sendto(ack,clientAddress)
			continue
        
       
        arquivo.close()
    except (KeyboardInterrupt, SystemExit):
        break

serverSocket.close()

