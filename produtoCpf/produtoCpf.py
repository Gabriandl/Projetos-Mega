from flask import Flask
from bitrix24 import *

app = Flask(__name__)

@app.route('/<id>', methods=['POST','GET'])

def addDealField(id):
    
    try:
        bx24 = Bitrix24('https://megaisencoes.bitrix24.com.br/rest/XXXX/XXXXXXX/')

        produto=''
        produto2=''
        produto3=''
        produto4=''
        dealID=id
        Cpf(dealID, bx24)
        chamada=bx24.callMethod("crm.deal.productrows.get", id=dealID)
        campoProduto=chamada[0]
        produto=campoProduto['PRODUCT_NAME']

        campoProduto1=chamada[1]
        produto2=campoProduto1['PRODUCT_NAME']

        campoProduto2=chamada[2]
        produto3=campoProduto2['PRODUCT_NAME']

        campoProduto3=chamada[3]
        produto4=campoProduto3['PRODUCT_NAME']

        produtoFinal="%s | %s | %s | %s"%(produto, produto2, produto3, produto4)
        bx24.callMethod("crm.deal.update", id=dealID, fields={'UF_CRM_1605031656':produtoFinal})

    except IndexError:
        Cpf(dealID,bx24)
        produtoFinal="%s | %s | %s | %s"%(produto, produto2, produto3, produto4)
        bx24.callMethod("crm.deal.update", id=dealID, fields={'UF_CRM_1605031656':produtoFinal})

    return "<h3>Produto adicionado ao campo e CPF atualizado.</h3>"

def Cpf(id, bx24):
    
    teste= getCpf(contactId(id,bx24), bx24)
    cpf = chr_remove(teste," .-,")
    updateCpf(id,contactId(id, bx24),cpf,bx24)

def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string
def contactId(dealID, bx24):
    chamada = bx24.callMethod("crm.deal.contact.items.get", id=dealID)
    contactTemp2 = chamada[0]
    contactId= contactTemp2["CONTACT_ID"]
    return contactId   
def getCpf(ID, bx24):
    chamada = bx24.callMethod("crm.contact.get", id=ID)
    cpf = chamada['UF_CRM_1575396694']
    return cpf
def updateCpf(Id,ID, cpf,bx24):
    bx24.callMethod("crm.contact.update", id=ID, fields={'UF_CRM_1575396694':cpf}) 
    bx24.callMethod("crm.deal.update", id=Id, fields={'UF_CRM_5DF0204BA9076':cpf}) 


if __name__ == '__main__':
    app.run(debug=True)

