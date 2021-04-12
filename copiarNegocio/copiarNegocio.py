from flask import Flask
from bitrix24 import *

app = Flask(__name__)

@app.route('/acessorios/<id>', methods=['POST','GET'])

def acessorios(id):                       
    bx24 = Bitrix24('https://megaisencoes.bitrix24.com.br/rest/XXXX/XXXXXXX/')
    dealID=id
    chamada = bx24.callMethod("crm.deal.get", id=dealID)
    contact= chamada.get('CONTACT_ID')
    nomeNegocioPai= chamada.get('TITLE')
    cpf = chamada.get('UF_CRM_5DF0204BA9076')

    
    bx24.callMethod("crm.deal.add",fields={'TITLE':nomeNegocioPai+' - Acessórios', 'CONTACT_ID':contact,'CATEGORY_ID':71,'UF_CRM_1596463793':dealID,'UF_CRM_5DF0204BA9076':cpf})

    listaId = bx24.callMethod("crm.deal.list",filter={'UF_CRM_1596463793':dealID})
    idAcessorios1 = listaId[0]
    idAcessorios = idAcessorios1['ID'] 

    bx24.callMethod("crm.deal.update",id=dealID,fields={'UF_CRM_1597353860':idAcessorios})

    return "<h1>Negocio Acessorio Criado</h1>"


@app.route('/<id>', methods=['POST','GET'])

def addDeal(id):

    bx24 = Bitrix24('https://megaisencoes.bitrix24.com.br/rest/8347/h4dww3v07j081obd/')
    dealID=id
    chamada = bx24.callMethod("crm.deal.get", id=dealID)
    contact= chamada.get('CONTACT_ID')
    nomeNegocioPai= chamada.get('TITLE')
    cpf = chamada.get('UF_CRM_5DF0204BA9076')


    bx24.callMethod("crm.deal.add",fields={'TITLE':nomeNegocioPai+' - Despachante', 'CONTACT_ID':contact,'CATEGORY_ID':60,'UF_CRM_1596463793':dealID,'UF_CRM_5DF0204BA9076':cpf})

    bx24.callMethod("crm.deal.add",fields={'TITLE':nomeNegocioPai+' - Seguros', 'CONTACT_ID':contact,'CATEGORY_ID':73,'UF_CRM_1596463793':dealID,'UF_CRM_5DF0204BA9076':cpf}) 

    listaId = bx24.callMethod("crm.deal.list",filter={'UF_CRM_1596463793':dealID})

    idDespachante1 = listaId[1]
    idDespachante = idDespachante1['ID']

    idSeguros1 = listaId[2]
    idSeguros = idSeguros1['ID']

    bx24.callMethod("crm.deal.update",id=dealID,fields={'UF_CRM_1596463807':idDespachante, 'UF_CRM_1597354994':idSeguros})

    return "<h1>Negocio Criado</h1>"


   

if __name__ == '__main__':
    app.run(debug=True)