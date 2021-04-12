var cpf = user.get('cpf');
//var cpf = 47530994824;
var url = "https://megaisencoes.bitrix24.com.br/rest/XXXX/XXXXXXX/crm.deal.list.json?FILTER[UF_CRM_5DF0204BA9076]="+cpf+"&SELECT[]=*";
var contact, fase, fase1, arrayDeal, nome,  url2,url3, category, stage = '', array, faseStr;
var cont = 0 ;
var i ;

     rp({uri: url, json: true}) 
        .then(json => {
       
       		 arrayDeal = json.result[0]; 
       		 category = arrayDeal.CATEGORY_ID;
       		 fase = arrayDeal.STAGE_ID;
             contact = arrayDeal.CONTACT_ID;
       
             url2 = "https://megaisencoes.bitrix24.com.br/rest/XXXX/XXXXXXX/crm.contact.get.json?id="+ contact +"";
       		 url3 = "https://megaisencoes.bitrix24.com.br/rest/XXXX/XXXXXXX/crm.dealcategory.stage.list.json?id="+ category + "";
                   
       			rp({uri: url3, json: true}) 
                            .then(json => {
                  			
                  				for (cont=0; stage != fase;cont++)
                                {
                                   array = json.result[cont];
                                   stage = array.STATUS_ID;
                                    faseStr = array.NAME;  	
                                 }
                                   

                            rp({uri: url2, json: true}) 
                            .then(json => {
                                nome = json.result.NAME;
                                result.text('Olá '+nome+', você está na fase '+faseStr);
                                result.done();
                            })	.catch(err => {
                                result.text( "Por favor, prossiga com o SAC.");
                                //context.userData.digitouErrado=true;
                                //result.gotoRule('Consultar Processo');
                                result.done(); 
                            });
       
                            })	.catch(err => {
                                result.text( "Por favor, prossiga com o SAC.");
                                //context.userData.digitouErrado=true;
                                //result.gotoRule('Consultar Processo');
                                result.done(); 
                            });		

        })	.catch(err => {
            result.text( "Por favor, prossiga com o SAC.");
       		//context.userData.digitouErrado=true;
            result.done(); 
        });