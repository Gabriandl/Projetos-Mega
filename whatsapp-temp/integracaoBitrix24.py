import requests
from bitrix24 import *



bx24 = Bitrix24('https://megaisencoes.bitrix24.com.br/rest/XXXX/XXXXXXX/')

responded5=False    
responded4=False
responded3=False
responded2=False
responded=False
cont1=0
cont2=0
cont3=0
cont4=0


def getEmail(ID):
    global bx24
    chamada = bx24.callMethod("crm.contact.get", id=ID)
    emailTemp2 = chamada.get("EMAIL")
    emailTemp3= emailTemp2[0]
    emailBx=emailTemp3["VALUE"]
    return emailBx
def updateEmail(ID, email):
    global bx24
    emailTeste = email
    bx24.callMethod("crm.contact.update", id=ID, fields={'EMAIL':{'0':{"VALUE":emailTeste}}})    
    
def getNumber (ID):
    global bx24
    chamada = bx24.callMethod("crm.contact.get", id=ID)
    phoneTemp = chamada.get("PHONE")
    phoneTemp2 = phoneTemp[0]
    numero = phoneTemp2["VALUE"]
    return numero

def tresMeses (ID, compra):
    global bx24
    if compra == 'Sim':
        bx24.callMethod("crm.deal.update", id=ID, fields={'UF_CRM_1591467538':'8992'})
    if compra == 'Não':
        bx24.callMethod("crm.deal.update", id=ID, fields={'UF_CRM_1591467538':'8994'})

def intencao (ID, intencao):
    global bx24
    
    if intencao == 'abaixo de 70.000':
        bx24.callMethod("crm.deal.update", id=ID, fields={'UF_CRM_1585868957':'5070'})
    if intencao == 'acima de 70.000':
        bx24.callMethod("crm.deal.update", id=ID, fields={'UF_CRM_1585868957':'5068'})

def contactId(dealID):
    global bx24
    chamada = bx24.callMethod("crm.deal.contact.items.get", id=dealID)
    contactTemp2 = chamada[0]
    contactId= contactTemp2["CONTACT_ID"]
    return contactId