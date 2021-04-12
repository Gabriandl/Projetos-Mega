from flask import Flask
from bitrix24 import *

app = Flask(__name__)

@app.route('/<id>/<idResponsavel>/<title>', methods=['POST','GET'])

def taskTrigger(id,idResponsavel,title):
    
    descrição = '\n[URL = https://megaisencoes.bitrix24.com.br/crm/deal/details/'+id+'/]Ir para Negócio[/URL]'
    bx24 = Bitrix24('https://megaisencoes.bitrix24.com.br/rest/XXXX/XXXXXXX/')
    bx24.callMethod("task.item.add", fields={'TITLE':title,'RESPONSIBLE_ID':idResponsavel,'DESCRIPTION':descrição,'PRIORITY':2})
    
    #bx24.callMethod("crm.activity.add", fields={'OWNER_ID':Id,'OWNER_TYPE_ID':'2','TYPE_ID':'3','ASSOCIATED_ENTITY_ID':Id,'PROVIDER_ID':'TASKS','PROVIDER_TYPE_ID':'TASK','SUBJECT':'Contatar cliente imediatamente','COMMUNICATION':{'ENTITY_ID':Id},'RESPONSIBLE_ID':idResponsavel1,'DESCRIPTION':'Corpo da tarefa'})
    
    return "<h1>Ok!<\h1>"

if __name__ == '__main__':
    app.run(debug=True)
