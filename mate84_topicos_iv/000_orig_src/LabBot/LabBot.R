#* @get /classificador
function(){
	library("rjson")
	json_file <- "http://35.198.13.33:8080/api/datasensor"
	json_data <- fromJSON(file=json_file) #list
	dados = json_data$data

	dados$TIMESTAMP_ <- strptime(dados$TIMESTAMP_, format= "%Y-%m-%dT%H:%M:%S")
	df=data.frame(dados$TIMESTAMP_, dados$TEMPERATURA, dados$LUZ, dados$UMIDADE, dados$QUANT_PESSOAS)
	colnames(df) <- c("TIMESTAMP_", "TEMPERATURA","LUZ","UMIDADE","QUANT_PESSOAS")

	datas = unclass(dados$TIMESTAMP_)
	dfCompleto=data.frame(datas$wday,datas$hour,df$TEMPERATURA,df$LUZ, df$UMIDADE, df$QUANT_PESSOAS)
	colnames(dfCompleto) <- c("DIA_SEMANA","HORA","TEMPERATURA","LUZ","UMIDADE","QUANT_PESSOAS")

	#dfCompleto=data.frame(dados$DIA_SEMANA,dados$HORA,dados$TEMPERATURA,dados$LUZ, dados$UMIDADE, dados$QUANT_PESSOAS)
	#colnames(dfCompleto) <- c("DIA_SEMANA","HORA","TEMPERATURA","LUZ","UMIDADE","QUANT_PESSOAS")	

	objeto = list(DIA_SEMANA = 0, HORA = 0, TEMPERATURA = 0, LUZ = 0, UMIDADE = 0, QUANT_PESSOAS = 0);

	#switch(dfCompleto$DIA_SEMANA, '0'={objeto$DIA_SEMANA = "Domingo"}, '1'={objeto$DIA_SEMANA = "Segunda"},
	#	'2'={objeto$DIA_SEMANA = "Terca"}, '3'={objeto$DIA_SEMANA = "Quarta"}, '4'={objeto$DIA_SEMANA = "Quinta"},
	#	'5'={objeto$DIA_SEMANA = "Sexta"}, '6'={objeto$DIA_SEMANA = "Sabado"});

	if(dfCompleto$DIA_SEMANA == 1){
		objeto$DIA_SEMANA = "Segunda"
	}
	else{
		if(dfCompleto$DIA_SEMANA == 2){
			objeto$DIA_SEMANA = "Terca"
		}
		else{
			if(dfCompleto$DIA_SEMANA == 3){
				objeto$DIA_SEMANA = "Quarta"
			}
			else{
				if(dfCompleto$DIA_SEMANA == 4){
					objeto$DIA_SEMANA = "Quinta"
				}
				else{
					if(dfCompleto$DIA_SEMANA == 5){
						objeto$DIA_SEMANA = "Sexta"	
					}
					else{
						if(dfCompleto$DIA_SEMANA == 6){
							objeto$DIA_SEMANA = "Sabado"
						}
						else{
							objeto$DIA_SEMANA = "Domingo"	
						}	
					}	
	
				}		

			}
		}	
	}

	if(dfCompleto$HORA >= 0 && dfCompleto$HORA <= 7){
		objeto$HORA = "Manha";
	}
	if(dfCompleto$HORA >= 8 && dfCompleto$HORA <= 17){
		objeto$HORA = "Comercial";
	}
	if(dfCompleto$HORA >= 18 && dfCompleto$HORA <= 23){
		objeto$HORA = "Noite";
	}

	if(dfCompleto$TEMPERATURA < 23){
		objeto$TEMPERATURA = "Frio"
	}
	if(dfCompleto$TEMPERATURA > 26){
		objeto$TEMPERATURA = "Quente"
	}
	if(dfCompleto$TEMPERATURA >= 23 && dfCompleto$TEMPERATURA <= 26){
		objeto$TEMPERATURA = "Normal"
	}

	if(dfCompleto$UMIDADE <= 39){
		objeto$UMIDADE = "Seco"
	}
	if(dfCompleto$UMIDADE > 70){
		objeto$UMIDADE = "Umido"
	}
	if(dfCompleto$UMIDADE >= 23 && dfCompleto$UMIDADE <= 26){
		objeto$UMIDADE = "Normal"
	}	

	if(dfCompleto$LUZ <= 341){
		objeto$LUZ = "Claro"
	}
	if(dfCompleto$LUZ >= 683){
		objeto$LUZ = "Escuro"
	}
	if(dfCompleto$LUZ > 341 && dfCompleto$LUZ < 683){
		objeto$LUZ = "Normal"
	}

	if(dfCompleto$QUANT_PESSOAS == 0){
		objeto$QUANT_PESSOAS = "Vazio"
	}
	if(dfCompleto$QUANT_PESSOAS >= 21){
		objeto$QUANT_PESSOAS = "Cheio"
	}
	if(dfCompleto$QUANT_PESSOAS > 0 && dfCompleto$QUANT_PESSOAS < 21){
		objeto$QUANT_PESSOAS = "Normal"
	}

	caminho = paste("TEMPERATURA = ", objeto$TEMPERATURA, "- > ");

	#arvore
	if (objeto$TEMPERATURA != "Normal"){ #
		classe = "Razoavel"
		caminho = paste(caminho, classe)
	}
	else{
		caminho = paste(caminho, "HORA = ", objeto$HORA, "- > ")
		if (objeto$HORA == "Comercial"){ #
			caminho = paste(caminho, "DIA DA SEMANA = ", objeto$DIA_SEMANA, "- > ")
			if(objeto$DIA_SEMANA == "Sexta" || objeto$DIA_SEMANA == "Sabado" || objeto$DIA_SEMANA == "Domingo"){
				classe = "Agradavel"
			}
			else{
				classe = "Razoavel"
			}
			caminho = paste(caminho, classe)
		}else{
				caminho = paste(caminho, "QUANTIDADE DE PESSOAS = ", objeto$QUANT_PESSOAS, "- >")
				if(objeto$QUANT_PESSOAS == "Cheio"){
					classe = "Razoavel";
					caminho = paste(caminho, classe)
				}else{
						caminho = paste(caminho, "DIA DA SEMANA = ", objeto$DIA_SEMANA, "- >")
						if(objeto$DIA_SEMANA == "Segunda" || objeto$DIA_SEMANA == "Terça"){
							caminho = paste(caminho, "HORA = ", objeto$HORA, "- >")
								if(objeto$HORA == "Manha"){
									classe = "Agradavel"
									caminho = paste(caminho, classe)
								}else{
									caminho = paste(caminho, "LUZ = ", objeto$LUZ, "- >")
									if (objeto$LUZ == "Normal"){
										classe = "Agradavel"
										caminho = paste(caminho, classe)
									}else{
										classe = "Razoavel"
										caminho = paste(caminho, classe)
									}
								}
							
						}else{
							classe = "Agradavel";
							caminho = paste(caminho, classe)
						}
				}
			}
	}			
	
	return(caminho)

}

