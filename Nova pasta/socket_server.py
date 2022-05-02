"""
Lado do Servidor: Abre um TCP/IP numa port, espera por uma menssagem
de um cliente, e manda essa mensagem de volta como resposta.
Usamos aqui a biblioteca socketserver para realizar este trabalho.
Esta biblioteca fornece TCPServer, ThreadingTCPServer, ForkingTCPServer,
UDP variações destes, entre outras coisas, e redireciona cada cliente
para um 'request handler' para utilizar se método 'handle' para lidar
com o requisito do cliente.
"""
import socketserver, time
meuHost = ''
minhaPort = 50007

def agora():
    return time.ctime(time.time())

class LidaComCliente(socketserver.BaseRequestHandler):
    def handle(self):
        # Para cada conexão com cliente nós:

        # Imprimimos a identificação do cliente e o tempo
        print(self.client_address, agora())

        
        # Simulamos uma atividade
        time.sleep(5)

        while True:
            # Recebe data do cliente
            infodata = self.request.recv(1024)

            zenit, polar = 'zenit' , 'polar'
            final_message = ''
            message = str(infodata.decode())
            n = 0
            for i in range(len(message)):
                x = message[n]
                if x in zenit:
                    x = int(zenit.find(message[n]))
                    final_message += polar[x]
                elif x in polar:
                    x = int(polar.find(message[n]))
                    final_message += zenit[x]
                else:
                    final_message += message[n]
                n += 1

            if not final_message: break

            # Escreve e manda resposta para o cliente
            resposta = 'Eco=>%s as %s' % (final_message, agora())
            self.request.send(resposta.encode())

        self.request.close()

# Cria um thread server e lida com a entrada e requisitos de clientes
meuendro = (meuHost, minhaPort)
server = socketserver.ThreadingTCPServer(meuendro, LidaComCliente)
server.serve_forever()
