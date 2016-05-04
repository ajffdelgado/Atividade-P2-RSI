import socket,socketerror

HOST = ''
PORT = 12000
s = socketerror.socketError(socket.AF_INET, socket.SOCK_DGRAM)
s.setErrorProb(0.1)
s.settimeout(2.0)
s.connect((HOST, PORT))
arquivo = open("teste.txt",'r')
arqTam = open("teste.txt",'r')
cont = 0
pkt = "pkt0"
ack = ""
while arqTam.read(1000) != "":
    pacote = arquivo.read(1000)
    #print("parte a ser enviada: "+pacote)
    while 1:
        ind = str(cont)
        s.sendWithError(pkt+"<>"+pacote)
        if (pkt == "pkt0"):
            ack = "ack0"
        if (pkt == "pkt1"):
            ack = "ack1"
        try:
            data = s.recvWithError(1024)
            print(data)
            if (data == ack):
                if (ack == "ack0"):
                    pkt = "pkt1"
                    print("mudei de pkt0 para " + pkt)
                    break
                if (ack == "ack1"):
                    pkt = "pkt0"
                    print("mudei de pkt1 para " + pkt)
                    break
            else:
                continue
        except socket.timeout:
            print("Timeout")
            continue
    cont = cont +1


s.close()
arquivo.close()
arqTam.close()
