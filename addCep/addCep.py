from flask import Flask
from bitrix24 import *
import pycep_correios

app = Flask(__name__)

@app.route('/<id>', methods=['POST','GET'])

def cep(id):   
    bx24 = Bitrix24('https://megaisencoes.bitrix24.com.br/rest/XXXX/XXXXXXX/')
    dealId = id

    chamada= bx24.callMethod("crm.deal.get", id=dealId) 
    cep1=chamada.get('UF_CRM_5DF0204B5D798')
    contactId = chamada.get('CONTACT_ID')
    complemento = chamada.get('UF_CRM_5DF0204B50C64')
    numero= chamada.get('UF_CRM_5DF0204B42F73')
    cpf = chamada.get('UF_CRM_5DF0204BA9076')
    rg = chamada.get('UF_CRM_5DF0204BB3CD4')
    cep = chr_remove(cep1, ' -.,')
    
    endereco = pycep_correios.get_address_from_cep(cep)
    bairro = endereco['bairro']
    cidade = endereco['cidade']
    rua = endereco['logradouro']
    uf = endereco['uf']
    cep = endereco['cep']

    cep2 = cep[0:5]
    zona = getZona(int(cep2))

    bx24.callMethod("crm.deal.update", id=dealId, fields={'UF_CRM_1606240753':zona,'UF_CRM_1606228463':uf, 'UF_CRM_5DF0204B93074':bairro,'UF_CRM_5E18F32827B32':rua,'UF_CRM_5DF0204B68A91':cidade,'UF_CRM_5DF0204B5D798':cep}) 
    bx24.callMethod("crm.contact.update", id=contactId, fields={'UF_CRM_5DE6A1384D99D':complemento,'UF_CRM_5DE6A1384016A':numero,'UF_CRM_1575396704':rg,'UF_CRM_1575396694':cpf,'UF_CRM_1606395844':uf, 'UF_CRM_5DE6A139AD7B0':bairro,'UF_CRM_5E2F1DAA04C4B':rua,'UF_CRM_5DE6A13867AD5':cidade,'UF_CRM_5DE6A1385B8FC':cep}) 
    return '<h3>Endereço preenchido</h3>'
def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string

def getZona(cep):
    if cep > 1000 and cep < 1599:
        return "Centro"
    elif cep > 2000 and cep < 2999:
        return "Zona Norte"
    elif cep > 3000 and cep < 3999 or (cep > 8000 and cep < 8499):
        return "Zona Leste"
    elif cep > 4000 and cep < 4999:
        return "Zona Sul"
    elif cep > 5000 and cep < 5899:
        return "Zona Oeste"
    else:
        return "Cep não pertence a cidade de São Paulo"

if __name__ == '__main__':
    app.run(debug=True)