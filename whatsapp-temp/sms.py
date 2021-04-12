
from flask import Flask, request
import requests
import re
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from integracaoBitrix24 import getEmail, getNumber, updateEmail, tresMeses, intencao, contactId, responded,responded2,responded3,responded4,responded5,cont1,cont2,cont3, cont4

app = Flask(__name__)

global dealID
global contactID
global email1

email1=''
dealID=''
contactID=''


@app.route('/sms/<id>', methods=['POST','GET'])


def get(id):
        global dealID
        global contactID
        global responded
        global responded2
        global responded3
        global responded4
        global responded5
        global cont1
        global cont2
        global cont3
        global cont4
        
        responded5=False    
        responded4=False
        responded3=False
        responded2=False
        responded=False
        cont1=0
        cont2=0
        cont3=0
        cont4=0

        
        dealID = id
        contactID = contactId(id)
        toNumber='whatsapp:%s'%getNumber(contactID)      
        inic(toNumber)

        return "<h1>Mensagem enviada!<h1>"

def inic(toNumber):
    account_sid = 'AC4f3ac47295d03d4033c9c138c6ea825b'
    auth_token = 'XXXXXX'
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_='whatsapp:+14155238886', body='Olá, você esta falando com o atendente virtual da Mega Isenções!\nSeu veículo é abaixo ou acima de R$70.000 ?\n1-Abaixo de R$70.000\n2-Acima de R$70.000',to=toNumber)
    print(message.sid)

            

            

@app.route('/sms', methods=['POST','GET'])


    
def sms():


        global dealID
        global contactID
        global email
        
        email="%s"%getEmail(contactID)
        
        
        # Fetch the message
        msg = request.values.get('Body')
        # Create reply
        resp = MessagingResponse()
        mg = resp.message()
        
        

        global responded5
        global responded4
        global responded3
        global responded2
        global responded
        

        
        
        if responded == False:

                mensagem=perg1(msg)
                mg.body(mensagem)
                
                
                
        elif responded2==True:         
                        
                mensagem=perg2(msg, email)
                mg.body(mensagem)
                

        elif responded3==True:         
                        
                mensagem=perg3(msg, email)
                mg.body(mensagem)
                

        elif responded4==True:         
                        
                mensagem=validEmail(contactID, msg, email)
                mg.body(mensagem)

        elif responded5==True:         
                        
                mensagem=end(msg)
                mg.body(mensagem)

        
                
        return str(resp)


def perg1(msg):
    global cont1
    global responded
    global responded2
    global dealID
    
    if msg =='1' and cont1 == 0:
            mensagem=("Tem certeza que seu veículo é abaixo de 70.000?\n1-Sim\n2-Não")
            cont1 = 1
    elif msg =='2' and cont1 == 1:
            mensagem=("Seu veículo é abaixo ou acima de R$70.000 ?\n1-Abaixo de R$70.000\n2-Acima de R$70.000")
            cont1 = 2

    elif msg=='1' and (cont1 == 1 or cont1==2 or cont1==4):
                p1='abaixo de 70.000'
                mensagem=("Ok, seu veículo é %s.\n\nVocê pretende comprar o veículo nos próximos 3 meses ?\n1-Sim\n2-Não"% p1)
                responded = True
                responded2 = True
                intencao(dealID, p1)
    elif msg == '2' and cont1 == 0:
            mensagem=("Tem certeza que seu veículo é acima de 70.000?\n1-Sim\n2-Não")
            cont1 = 3
    elif msg =='2' and cont1 == 3:
            mensagem=("Seu veículo é abaixo ou acima de R$70.000 ?\n1-Abaixo de R$70.000\n2-Acima de R$70.000")
            cont1 = 4
    elif msg=='2' and (cont1 == 4 or  cont1==2) or (msg=='1'and cont1==3) :
                p1='acima de 70.000'
                mensagem=("Ok, seu veículo é %s.\n\nVocê pretende comprar o veículo nos próximos 3 meses ?\n1-Sim\n2-Não"% p1)
                responded = True
                responded2 = True
                intencao(dealID, p1)
    else:
                mensagem="*Digite uma opção valida!*"
                
    return mensagem

def perg2(msg, email):
    global responded3
    global responded2
    global cont2

    if msg =='1' and cont2 == 0:
            mensagem=("Tem certeza que você *pretende* comprar o veículo nos próximos 3 meses ?\n1-Sim\n2-Não")
            cont2 = 1
    elif msg =='2' and cont2 == 1:
            mensagem=("Você pretende comprar o veículo nos próximos 3 meses ?\n1-Sim\n2-Não")
            cont2 = 2
                
    elif msg=='1'and (cont2 == 1 or cont2==2 or cont2==4):
                p2='Sim'
                mensagem=("Ok, você *pretende* comprar o veículo nos próximos 3 meses.\n\n%s\nEsse é o email que você deseja receber as documentações?\n1-Sim\n2-Não"%email)
                responded2 = False
                responded3 = True
                tresMeses(dealID, p2)
                
    elif msg == '2' and cont2 == 0:
            mensagem=("Tem certeza que você *não pretende* comprar o veículo nos próximos 3 meses ?\n1-Sim\n2-Não")
            cont2 = 3
    elif msg =='2' and cont2 == 3:
            mensagem=("Você pretende comprar o veículo nos próximos 3 meses ?\n1-Sim\n2-Não")
            cont2 = 4      
    elif msg=='2' and (cont2 == 4 or cont2==2) or (msg=='1'and cont2==3):
                p2='Não'
                mensagem=("Ok, você *não pretende* comprar o veículo nos próximos 3 meses.\n\n%s\nEsse é o email que você deseja receber as documentações?\n1-Sim\n2-Não"%email)
                responded2 = False
                responded3 = True
                tresMeses(dealID, p2)
    else:
                mensagem="*Digite uma opção valida!*"
                
    return mensagem

def perg3(msg, email):
        global responded5
        global responded4
        global responded3
        global cont3

        if msg =='1' and cont3 == 0:
            mensagem=("%s\nTem certeza que esse *é* o email que você deseja receber as documentações?\n1-Sim\n2-Não"%email)
            cont3 = 1
        elif msg =='2' and cont3 == 1:
            mensagem=("%s\nEsse é o email que você deseja receber as documentações?\n1-Sim\n2-Não"%email)
            cont3 = 2

        elif msg=='1'and (cont3 == 1 or cont3==2 or cont3==4):
                
                mensagem="Ok, email cadastrado!"
                responded3 = False
                responded5= True

        elif msg == '2' and cont3 == 0:
            mensagem=("%s\nTem certeza que esse *não* é o email que você deseja receber as documentações?\n1-Sim\n2-Não"%email)
            cont3 = 3
        elif msg =='2' and cont3 == 3:
            mensagem=("%s\nEsse é o email que você deseja receber as documentações?\n1-Sim\n2-Não"%email)
            cont3 = 4     
                
        elif msg=='2' and (cont3 == 4 or cont3==2)or (msg=='1'and cont3==3):
                mensagem="Digite um email para fazer o cadastro: "
                responded3 = False
                responded4 = True


        else:
                mensagem="*Digite uma opção valida!*"

        return mensagem
                
def validEmail(id, msg, email):
        global responded4
        global responded5
        global contactID
        global cont4
        global email1
        

        if re.search(r'^[a-zA-Z0-9._-]+@([a-z0-9]+)(\.[a-z]{2,3})+$', msg) and (cont4 == 0 or cont4 == 2):
            email1 = msg
            mensagem=("%s\nTem certeza que esse *é* o email que você deseja cadastrar?\n1-Sim\n2-Não"%email1)
            cont4 = 1
        elif msg =='2' and cont4 == 1:
            mensagem=("Digite o email que você deseja receber as documentações:")
            cont4 = 2

        elif msg=='1'and cont4 == 1:
            email = email1
            mensagem=("O email %s foi cadastrado!"% email)
            updateEmail(contactID, email)
            responded4 = False
            responded5 = True
            
        elif not re.search(r'^[a-zA-Z0-9._-]+@([a-z0-9]+)(\.[a-z]{2,3})+$', msg) and (cont4 == 0 or cont4 == 2):
            mensagem='O email digitado não é valido, digite novamente: '
            responded4 = True

        return mensagem
def end(msg):
    
    if msg:
        mensagem="Para mais informações ligue em nossa central de atendimento: (11) 2344-8400"
    return mensagem

@app.errorhandler(500)

    
    
def sms(error):


        global dealID
        global contactID
        global email
        
        email="%s"%getEmail(contactID)
        
        
        # Fetch the message
        msg = request.values.get('Body')
        # Create reply
        resp = MessagingResponse()
        mg = resp.message()
        
        

        global responded5
        global responded4
        global responded3
        global responded2
        global responded
        

        
        
        if responded == False:

                mensagem=perg1(msg)
                mg.body(mensagem)
                
                
                
        elif responded2==True:         
                        
                mensagem=perg2(msg, email)
                mg.body(mensagem)
                

        elif responded3==True:         
                        
                mensagem=perg3(msg, email)
                mg.body(mensagem)
                

        elif responded4==True:         
                        
                mensagem=validEmail(contactID, msg, email)
                mg.body(mensagem)

        elif responded5==True:         
                        
                mensagem=end(msg)
                mg.body(mensagem)

        
                
        return str(resp)


@app.errorhandler(500)

    
    
def sms(error):


        global dealID
        global contactID
        global email
        
        email="%s"%getEmail(contactID)
        
        
        # Fetch the message
        msg = request.values.get('Body')
        # Create reply
        resp = MessagingResponse()
        mg = resp.message()
        
        

        global responded5
        global responded4
        global responded3
        global responded2
        global responded
        

        
        
        if responded == False:

                mensagem=perg1(msg)
                mg.body(mensagem)
                
                
                
        elif responded2==True:         
                        
                mensagem=perg2(msg, email)
                mg.body(mensagem)
                

        elif responded3==True:         
                        
                mensagem=perg3(msg, email)
                mg.body(mensagem)
                

        elif responded4==True:         
                        
                mensagem=validEmail(contactID, msg, email)
                mg.body(mensagem)

        elif responded5==True:         
                        
                mensagem=end(msg)
                mg.body(mensagem)

        
                
        return str(resp)

@app.errorhandler(500)

    
    
def sms(error):


        global dealID
        global contactID
        global email
        
        email="%s"%getEmail(contactID)
        
        
        # Fetch the message
        msg = request.values.get('Body')
        # Create reply
        resp = MessagingResponse()
        mg = resp.message()
        
        

        global responded5
        global responded4
        global responded3
        global responded2
        global responded
        

        
        
        if responded == False:

                mensagem=perg1(msg)
                mg.body(mensagem)
                
                
                
        elif responded2==True:         
                        
                mensagem=perg2(msg, email)
                mg.body(mensagem)
                

        elif responded3==True:         
                        
                mensagem=perg3(msg, email)
                mg.body(mensagem)
                

        elif responded4==True:         
                        
                mensagem=validEmail(contactID, msg, email)
                mg.body(mensagem)

        elif responded5==True:         
                        
                mensagem=end(msg)
                mg.body(mensagem)

        
                
        return str(resp)

@app.errorhandler(500)

    
    
def sms(error):


        global dealID
        global contactID
        global email
        
        email="%s"%getEmail(contactID)
        
        
        # Fetch the message
        msg = request.values.get('Body')
        # Create reply
        resp = MessagingResponse()
        mg = resp.message()
        
        

        global responded5
        global responded4
        global responded3
        global responded2
        global responded
        

        
        
        if responded == False:

                mensagem=perg1(msg)
                mg.body(mensagem)
                
                
                
        elif responded2==True:         
                        
                mensagem=perg2(msg, email)
                mg.body(mensagem)
                

        elif responded3==True:         
                        
                mensagem=perg3(msg, email)
                mg.body(mensagem)
                

        elif responded4==True:         
                        
                mensagem=validEmail(contactID, msg, email)
                mg.body(mensagem)

        elif responded5==True:         
                        
                mensagem=end(msg)
                mg.body(mensagem)

        
                
        return str(resp)

@app.errorhandler(500)

    
    
def sms(error):


        global dealID
        global contactID
        global email
        
        email="%s"%getEmail(contactID)
        
        
        # Fetch the message
        msg = request.values.get('Body')
        # Create reply
        resp = MessagingResponse()
        mg = resp.message()
        
        

        global responded5
        global responded4
        global responded3
        global responded2
        global responded
        

        
        
        if responded == False:

                mensagem=perg1(msg)
                mg.body(mensagem)
                
                
                
        elif responded2==True:         
                        
                mensagem=perg2(msg, email)
                mg.body(mensagem)
                

        elif responded3==True:         
                        
                mensagem=perg3(msg, email)
                mg.body(mensagem)
                

        elif responded4==True:         
                        
                mensagem=validEmail(contactID, msg, email)
                mg.body(mensagem)

        elif responded5==True:         
                        
                mensagem=end(msg)
                mg.body(mensagem)

        
                
        return str(resp)


@app.errorhandler(500)

    
    
def sms(error):


        global dealID
        global contactID
        global email
        
        email="%s"%getEmail(contactID)
        
        
        # Fetch the message
        msg = request.values.get('Body')
        # Create reply
        resp = MessagingResponse()
        mg = resp.message()
        
        

        global responded5
        global responded4
        global responded3
        global responded2
        global responded
        

        
        
        if responded == False:

                mensagem=perg1(msg)
                mg.body(mensagem)
                
                
                
        elif responded2==True:         
                        
                mensagem=perg2(msg, email)
                mg.body(mensagem)
                

        elif responded3==True:         
                        
                mensagem=perg3(msg, email)
                mg.body(mensagem)
                

        elif responded4==True:         
                        
                mensagem=validEmail(contactID, msg, email)
                mg.body(mensagem)

        elif responded5==True:         
                        
                mensagem=end(msg)
                mg.body(mensagem)

        
                
        return str(resp)

@app.errorhandler(500)

    
    
def sms(error):


        global dealID
        global contactID
        global email
        
        email="%s"%getEmail(contactID)
        
        
        # Fetch the message
        msg = request.values.get('Body')
        # Create reply
        resp = MessagingResponse()
        mg = resp.message()
        
        

        global responded5
        global responded4
        global responded3
        global responded2
        global responded
        

        
        
        if responded == False:

                mensagem=perg1(msg)
                mg.body(mensagem)
                
                
                
        elif responded2==True:         
                        
                mensagem=perg2(msg, email)
                mg.body(mensagem)
                

        elif responded3==True:         
                        
                mensagem=perg3(msg, email)
                mg.body(mensagem)
                

        elif responded4==True:         
                        
                mensagem=validEmail(contactID, msg, email)
                mg.body(mensagem)

        elif responded5==True:         
                        
                mensagem=end(msg)
                mg.body(mensagem)

        
                
        return str(resp)

@app.errorhandler(500)

    
    
def sms(error):


        global dealID
        global contactID
        global email
        
        email="%s"%getEmail(contactID)
        
        
        # Fetch the message
        msg = request.values.get('Body')
        # Create reply
        resp = MessagingResponse()
        mg = resp.message()
        
        

        global responded5
        global responded4
        global responded3
        global responded2
        global responded
        

        
        
        if responded == False:

                mensagem=perg1(msg)
                mg.body(mensagem)
                
                
                
        elif responded2==True:         
                        
                mensagem=perg2(msg, email)
                mg.body(mensagem)
                

        elif responded3==True:         
                        
                mensagem=perg3(msg, email)
                mg.body(mensagem)
                

        elif responded4==True:         
                        
                mensagem=validEmail(contactID, msg, email)
                mg.body(mensagem)

        elif responded5==True:         
                        
                mensagem=end(msg)
                mg.body(mensagem)

        
                
        return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
