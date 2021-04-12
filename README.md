# Projetos-Mega
Projetos desenvolvidos durante meu estagio na Mega Isenções

### fromContacttoDeal.py – Aplicação em linguagem Python

Utilizando as bibliotecas python ‘bitrix24’ e ‘openpyxml’, desenvolvi uma aplicação cujo objetivo é copiar os campos ‘telefone’ e ‘email’ do Contato para o Negocio desse mesmo cliente, para isso foi extraída uma planilha com todos os Ids dos negócios que seria necessário fazer essa cópia. Para o programa conseguir ler os dados da planilha esse programa deve ser executado localmente.

###botmakerTrigger.py – Aplicação web em linguagem Python

Utilizando as bibliotecas python ‘requests’,’json’,’botmaker’,’os’,’flask’, desenvolvi uma aplicação cujo objetivo é disparar templates no Botmaker, por meio das regras de automação do CRM Bitrix24. Para isso, utilizando o microframework Flask, foram criadas rotas especificas para o disparo de cada template. 
Os templates que não possuem variáveis como o ‘pre_vendas_reagendamento’, recebe apenas a variável ‘id’ em sua rota, no qual é atribuído o telefone do cliente. Já os templates que possuem variáveis como o ‘mensagem_inicial_contatar5’, recebem na rota, além do ‘id’, todas as demais variáveis obrigatórias para o disparo no Botmaker.

###addCep.py – Aplicação web em linguagem Python

Utilizando as bibliotecas python ‘flask’, ‘bitrix24’, ’pycep_correios’, desenvolvi uma aplicação cujo objetivo é, com base no cep, preencher os campos referentes ao endereço desse cliente. Para isso, utilizando o microframework Flask, foi criado uma rota que recebe como parâmetro o id do Negócio. A partir do id é feita uma requisição utilizando o método da API do bitrix ‘crm.deal.get’ para extrair o cep e fazer o processamento adequado.
Paralelamente, é feito uma padronização do RG e do CPF do cliente utilizando o método ‘chr_remove’. Essa padronização é feia tanto no Negócio quanto no Contato.

###taskTrigger.py – Aplicação web em linguagem Python

Utilizando as bibliotecas python ‘flask’, ‘bitrix24’, desenvolvi uma aplicação cujo objetivo é criar uma tarefa para a pessoa responsável do lead. Para isso, utilizando o microframework Flask, foi criado uma rota que recebe como parâmetros: id do Negócio, id do responsável do lead e um título para a tarefa.

###copiarNegocio.py – Aplicação web em linguagem Python

Utilizando as bibliotecas python ‘flask’, ‘bitrix24’’, desenvolvi uma aplicação cujo objetivo é, com base no id de um ‘Negocio’, criar copias desse cliente em diferentes funis de vendas. Para isso, utilizando o microframework Flask, foram criadas rotas que recebem como parâmetro o id do Negócio (cada rota cria um uma cópia em um determinado funil). A partir do id é feita uma requisição utilizando o método da API do bitrix ‘crm.deal.get’ para extrair os dados do Negócio principal e criar as copias.

###produtoCpf.py – Aplicação web em linguagem Python

Utilizando as bibliotecas python ‘flask’, ‘bitrix24’’, desenvolvi uma aplicação cujo objetivo é, com base no id de um ‘Negocio’, preencher os produtos adquiridos por esse cliente em um campo em formato de texto. Para isso, utilizando o microframework Flask, foi criada uma rota que recebe como parâmetro o id do Negócio. A partir do id é feita uma requisição utilizando o método da API do bitrix ‘crm.deal.productrows.get’ para extrair os produtos do Negócio principal e preencher no campo designado.

###BotLaudos – Integração entre botmaker e bitrix24

Utilizando o tópico de código do Botmaker, vou desenvolver em linguagem de programação javascript uma integração entre o Botmaker e o CRM Bitrix24. O objetivo desse bot é captar as respostas dos clientes a determinadas perguntas e preencher os campos relacionados no Bitrix. A ativação será por meio das regras de automação do CRM Bitrix24.

###whatsapp-bot – Integração entre Twilio(Whatsapp) e bitrix24

Projeto com o mesmo objetivo do ‘BotLaudos’ porem desenvolvido unicamente com python e twilio.

###Botmaker/consultarProcesso.js - Integração entre botmaker e bitrix24

Utilizando o tópico de código do Botmaker, desenvolvi em linguagem de programação javascript uma integração entre o Botmaker e o CRM Bitrix24. O objetivo desse programa é, por meio do CPF do cliente, informar em qual fase esse cliente está. Para isso foi utilizada a biblioteca ‘rp’ do javascript, onde foram feitas algumas requisições à API do bitrix para identificar a fase que esse cliente está. A ativação será por meio das intenções de bot no Botmaker.
