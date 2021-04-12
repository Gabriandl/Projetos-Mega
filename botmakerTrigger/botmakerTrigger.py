import requests
from urllib.parse import unquote
import json
import botmaker
import os
from flask import Flask

app = Flask(__name__)
os.environ['BOTMAKER_ACCESS_TOKEN'] = "TOKEN=XXXXXXXXXX"

@app.route('/prevendas/reagendamento/<id>', methods=['POST'])

def prevendastrigger(id):
    telefone=unquote(id)
    
    client = botmaker.Client()  # Will use the env var BOTMAKER_ACCESS_TOKEN

    # Send from '5215500000000' to '5215522222222'
    client.template_messages.create(
        '551123448400', telefone,
        'pre_vendas_reagendamento'
    )
    return "<h1>OK! </h1>"

@app.route('/retomar/<id>', methods=['POST'])

def retomar(id):
    telefone=unquote(id)
    
    client = botmaker.Client()  # Will use the env var BOTMAKER_ACCESS_TOKEN

    # Send from '5215500000000' to '5215522222222'
    client.template_messages.create(
        '551123448400', telefone,
        'retomar_contato'
    )
    return "<h1>OK! </h1>"

@app.route('/prevendas/consulta/presencial/<string:id>/<string:nomeCliente>/<string:dia>/<string:mes>/<string:dataHora>/<string:enderecoLoja>', methods=['POST'])

def consultaPresencialTrigger(id, nomeCliente,dia,mes,dataHora,enderecoLoja):
    telefone=unquote(id)
    nomeCliente=unquote(nomeCliente)
    dataHora=unquote(dataHora)
    enderecoLoja=unquote(enderecoLoja)
    dataHora = "%s/%s/%s"%(dia,mes,dataHora)
    client = botmaker.Client()  # Will use the env var BOTMAKER_ACCESS_TOKEN

    # Send from '5215500000000' to '5215522222222'
    client.template_messages.create(
        '551123448400', telefone,
        'avaliacao_medica_presencial', nomeCliente=nomeCliente, dataHora=dataHora, enderecoLoja=enderecoLoja
    )
    return "<h1>OK! </h1>"

@app.route('/prevendas/consulta/online/<string:id>/<string:nomeCliente>/<string:dia>/<string:mes>/<string:dataHora>/<string:https>//<string:link>/<string:link2>', methods=['POST'])

def consultaOnlineTrigger(id, nomeCliente,dia,mes,dataHora,https,link, link2):
    telefone=unquote(id)
    if link2[-1::] == "_":
        link2=link2[:-1]
    
    nomeCliente=unquote(nomeCliente)
    dataHora=unquote(dataHora)
    link="%s//%s/%s"%(https,link,link2)
    dataHora = "%s/%s/%s"%(dia,mes,dataHora)
    client = botmaker.Client()  # Will use the env var BOTMAKER_ACCESS_TOKEN

    # Send from '5215500000000' to '5215522222222'
    client.template_messages.create(
        '551123448400', telefone,
        'avaliacao_medico_online', nomeCliente=nomeCliente, dataHora=dataHora, link=link
    )
    return "<h1>OK! </h1>"

@app.route('/contatar/iniciar/<string:id>/<string:nomeCliente>/<string:emailConsultor>/<string:nomeOperador>', methods=['POST'])

def msgContatarTrigger(id, nomeCliente,emailConsultor,nomeOperador):
    telefone=unquote(id)
    nomeCliente=unquote(nomeCliente)
    nomeOperador=unquote(nomeOperador)
    emailConsultor=unquote(emailConsultor)
   
    client = botmaker.Client()  # Will use the env var BOTMAKER_ACCESS_TOKEN

    # Send from '5215500000000' to '5215522222222'
    client.template_messages.create(
        '551123448400', telefone,
        'mensagem_inicial_contatar5', nomeCliente=nomeCliente, nomeOperador=nomeOperador, emailConsultor=emailConsultor
    )
    return "<h1>OK! </h1>"

if __name__ == "__main__":
    app.run(debug=False)
