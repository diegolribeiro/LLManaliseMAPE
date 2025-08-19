
from langchain.prompts import ChatPromptTemplate

def prompt_analise_mape_categoria(dados):
 return ChatPromptTemplate.from_template("""
Você irá fazer o papel de um analista de planejamento de demanda de um varejo. 
Você receberá uma tabela com os dados de MAPE (Erro Percentual Absoluto Médio) de uma categoria de produtos específico.

Primeiramente, analise os valores informados na coluna MAPE em cada mês, o mês está informado através da coluna DATA;

Em segundo lugar, avalie se a categoria demonstra uma tendência de aumento ou redução do erro percentual Absoluto Médio e explique os passos da análise antes de dar a resposta;

Em terceiro lugar, Informe o mês que teve pior MAPE, para isso analise todos os meses e os respectivos valores;                                         

Em quarto lugar, avalie todos dados da coluna "VIÉS DO ERRO DA PREVISÃO" e identifique quantas vezes a previsão de vendas foi MAIOR que as vendas realizadas, e quantas vezes a previsão de vendas foi menor que as vendas realizadas, a partir da análise de viés do erro da previsão feito no passo anteior, gere uma tabela que contenha a frequência em que a previsão de demanda foi maior que as vendas realizadas, e quando a previsão  foi menor que as vendas realizadas, utilize a coluna "VIÉS DP ERRO DA PREVISÃO".  Apresente os resultados em uma tabela, seguindo o exemplo abaixo:
| Viés do Erro da Previsão                              | Frequência |
|-------------------------------------------------------|------------|
| Previsão de Vendas foi MAIOR que as vendas realizadas | 3 vezes    |
| Previsão de Vendas foi MENOR que as vendas realizadas | 2 vezes    |


Em quinto lugar, a partir dos dados informados, identifique se há impacto no aumento cobertura de estoque da categoria quando o Viés do Erro da Previsão é positivo, isto é, quando o planejamento previsto de Vendas foi MAIOR que as vendas realizadas, siga os passos abaixo para a análise:

	1-) Para esta análise Utilize as colunas "Data", "Viés do Erro da Previsão" e "Cobertura de estoque em dias"
	2-) Identifique todos os meses em que houve viés positivo de previsão: isto é, quando o planejamento previsto de Vendas foi MAIOR que as vendas realizadas.
	3-) Para cada mês identificado:
		a-) Informe o valor da Cobertura de Estoque no mês analisado e no mês passado;
		b-) Avalie se a Cobertura de Estoque aumentou ou diminuiu nesses dois meses;
		c-) Apresente os resultados em uma tabela, seguindo o exemplo abaixo:
| Mês       | Viés da Previsão                             | Cobertura Estoque | Cobertura Estoque (Mês Passado)  | Variação na Cobertura de Estoque  |
|-----------|----------------------------------------------|-------------------|----------------------------------|-----------------------------------|
| Janeiro   | Previsão de Vendas foi MAIOR que as vendas   | 50                |                                  |							          |
| Fevereiro | Previsão de Vendas foi MAIOR que as vendas   | 30                | 50                               | Diminuição de 20 dias             |


Em sexto lugar, a partir dos dados informados, identifique se há impacto no aumento ruptura de estoque da categoria quando o Viés do Erro da Previsão é negativo, isto é, quando o planejamento previsto de Vendas foi MENOR que as vendas realizadas, siga os passos abaixo para a análise:

  1-) Para esta análise Utilize as colunas "Data", "Viés do Erro da Previsão" e "RUPTURA DO ESTOQUE"
	2-) Identifique todos os meses em que houve viés negativo de previsão: isto é, quando o planejamento previsto de Vendas foi MENOR que as vendas realizadas.
	3-) Para cada mês identificado:
		a-) Informe o valor da Ruptura de Estoque no mês analisado e no mês passado;
		b-) Avalie se a Ruptura de Estoque aumentou ou diminuiu nesses dois meses;
		c-) Apresente os resultados em uma tabela, seguindo o exemplo abaixo:
| Mês       | Viés da Previsão                             | Ruptura Estoque   | Ruptura Estoque (Mês Passado)    | Variação na Cobertura de Estoque  |
|-----------|----------------------------------------------|-------------------|----------------------------------|-----------------------------------|
| Janeiro   | Previsão de Vendas foi MENOR que as vendas   | 5%                |                                  |							          |
| Fevereiro | Previsão de Vendas foi MENOR que as vendas   | 6%                | 5%                               | Aumento de 1%             		  |

                                         
Os dados para sua análise estão detalhados na tabela abaixo:

	{dados} 

Retorne todas as respostas no formato markdown.
""")





def prompt_analise_mape_item(dados, cateogoria):

	print("""

Você irá fazer o papel de um analista de planejamento de demanda de um varejo. 
Você receberá uma tabela com os dados de MAPE (Erro Percentual Absoluto Médio) de um produto específico da categoria: {categoria}.

Primeiramente, analise os valores informados na coluna MAPE em cada mês, o mês está informado através da coluna DATA;

Em segundo lugar, avalie se o produto demonstra uma tendência de aumento ou redução do erro percentual Absoluto Médio, utilize a coluna MAPE e a coluna DATA para avalia a tendência, e explique os passos da análise antes de dar a resposta;

Em terceiro lugar, Informe o mês que teve pior MAPE, para isso analise todos os meses e os respectivos valores;

Em quarto lugar, avalie todos dados da coluna "VIÉS DO ERRO DA PREVISÃO" e identifique quantas vezes a previsão de vendas foi MAIOR que as vendas realizadas, e quantas vezes a previsão de vendas foi menor que as vendas realizadas, a partir da análise de viés do erro da previsão feito no passo anteior, gere uma tabela que contenha a frequência em que a previsão de demanda foi maior que as vendas realizadas, e quando a previsão  foi menor que as vendas realizadas, utilize a coluna "VIÉS DP ERRO DA PREVISÃO".  Apresente os resultados em uma tabela, seguindo o exemplo abaixo:

| Viés do Erro da Previsão                              | Frequência |
|-------------------------------------------------------|------------|
| Previsão de Vendas foi MAIOR que as vendas realizadas | 3 vezes    |
| Previsão de Vendas foi MENOR que as vendas realizadas | 2 vezes    |


Em quinto lugar, a partir dos dados informados, identifique se há impacto no aumento cobertura de estoque do produto quando o Viés do Erro da Previsão positivo, isto é, quando o planejamento previsto de Vendas foi MAIOR que as vendas realizadas, siga os passos abaixo para a análise:

	1-) Para esta análise Utilize SOMENTE as colunas "DATA", "VIÉS DO ERRO DA PREVISÃO" e "COBERTURA DE ESTOQUE EM DIAS"
	2-) Identifique todos os meses em que houve viés positivo de previsão: isto é, quando o planejamento previsto de Vendas foi MAIOR que as vendas realizadas.
	3-) Para cada mês identificado:
      a-) Informe o valor da Cobertura de Estoque no mês analisado e no mês passado;
      b-) Avalie se a COBERTURA DE ESTOQUE EM DIAS aumentou ou diminuiu nesses dois meses;
      c-) Apresente os resultados em uma tabela, seguindo o exemplo abaixo:
| Mês       | Viés da Previsão                             | Cobertura Estoque | Cobertura Estoque (Mês Passado)  | Variação na Cobertura de Estoque  |
|-----------|----------------------------------------------|-------------------|----------------------------------|-----------------------------------|
| Janeiro   | Previsão de Vendas foi MAIOR que as vendas   | 50                |                                  |							                      |
| Fevereiro | Previsão de Vendas foi MAIOR que as vendas   | 30                | 50                               | Diminuição de 20 dias             |


Em sexto lugar, a partir dos dados informados, identifique se há impacto no aumento ruptura de estoque da categoria quando o Viés do Erro da Previsão é negativo, isto é, quando o planejamento previsto de Vendas foi MENOR que as vendas realizadas, siga os passos abaixo para a análise:

  1-) Para esta análise Utilize as colunas "Data", "Viés do Erro da Previsão" e "RUPTURA DO ESTOQUE"
	2-) Identifique todos os meses em que houve viés negativo de previsão: isto é, quando o planejamento previsto de Vendas foi MENOR que as vendas realizadas.
	3-) Para cada mês identificado:
		a-) Informe o valor da Ruptura de Estoque no mês analisado e no mês passado;
		b-) Avalie se a Ruptura de Estoque aumentou ou diminuiu nesses dois meses;
		c-) Apresente os resultados em uma tabela, seguindo o exemplo abaixo:
| Mês       | Viés da Previsão                             | Ruptura Estoque   | Ruptura Estoque (Mês Passado)    | Variação na Cobertura de Estoque  |
|-----------|----------------------------------------------|-------------------|----------------------------------|-----------------------------------|
| Janeiro   | Previsão de Vendas foi MENOR que as vendas   | 5%                |                                  |							          |
| Fevereiro | Previsão de Vendas foi MENOR que as vendas   | 6%                | 5%                               | Aumento de 1%             		  |

Os dados do produto para sua análise estão detalhados na tabela abaixo:

{dados} 

Retorne todas as respostas no formato markdown, coloque como título "Análise do Produto do item:" o código do item se encontra no campo ITEM da tabela de dados, também informe no título a categoria analisada. 

""")
  
	return ChatPromptTemplate.from_template("""

	Você irá fazer o papel de um analista de planejamento de demanda de um varejo. 
	Você receberá uma tabela com os dados de MAPE (Erro Percentual Absoluto Médio) de um produto específico da categoria: {categoria}.

	Primeiramente, analise os valores informados na coluna MAPE em cada mês, o mês está informado através da coluna DATA;

	Em segundo lugar, avalie se o produto demonstra uma tendência de aumento ou redução do erro percentual Absoluto Médio, utilize a coluna MAPE e a coluna DATA para avalia a tendência, e explique os passos da análise antes de dar a resposta;

	Em terceiro lugar, Informe o mês que teve pior MAPE, para isso analise todos os meses e os respectivos valores;

	Em quarto lugar, avalie todos dados da coluna "VIÉS DO ERRO DA PREVISÃO" e identifique quantas vezes a previsão de vendas foi MAIOR que as vendas realizadas, e quantas vezes a previsão de vendas foi menor que as vendas realizadas, a partir da análise de viés do erro da previsão feito no passo anteior, gere uma tabela que contenha a frequência em que a previsão de demanda foi maior que as vendas realizadas, e quando a previsão  foi menor que as vendas realizadas, utilize a coluna "VIÉS DP ERRO DA PREVISÃO".  Apresente os resultados em uma tabela, seguindo o exemplo abaixo:

	| Viés do Erro da Previsão                              | Frequência |
	|-------------------------------------------------------|------------|
	| Previsão de Vendas foi MAIOR que as vendas realizadas | 3 vezes    |
	| Previsão de Vendas foi MENOR que as vendas realizadas | 2 vezes    |


	Em quinto lugar, a partir dos dados informados, identifique se há impacto no aumento cobertura de estoque do produto quando o Viés do Erro da Previsão positivo, isto é, quando o planejamento previsto de Vendas foi MAIOR que as vendas realizadas, siga os passos abaixo para a análise:

		1-) Para esta análise Utilize SOMENTE as colunas "DATA", "VIÉS DP ERRO DA PREVISÃO" e "COBERTURA DE ESTOQUE EM DIAS"
		2-) Identifique todos os meses em que houve viés positivo de previsão: isto é, quando o planejamento previsto de Vendas foi MAIOR que as vendas realizadas.
		3-) Para cada mês identificado:
		a-) Informe o valor da Cobertura de Estoque no mês analisado e no mês passado;
		b-) Avalie se a COBERTURA DE ESTOQUE EM DIAS aumentou ou diminuiu nesses dois meses;
		c-) Apresente os resultados em uma tabela, seguindo o exemplo abaixo:
	| Mês       | Viés da Previsão                             | Cobertura Estoque | Cobertura Estoque (Mês Passado)  | Variação na Cobertura de Estoque  |
	|-----------|----------------------------------------------|-------------------|----------------------------------|-----------------------------------|
	| Janeiro   | Previsão de Vendas foi MAIOR que as vendas   | 50                |                                  |							                      |
	| Fevereiro | Previsão de Vendas foi MAIOR que as vendas   | 30                | 50                               | Diminuição de 20 dias             |


	Em sexto lugar, a partir dos dados informados, identifique se há impacto no aumento ruptura de estoque da categoria quando o Viés do Erro da Previsão é negativo, isto é, quando o planejamento previsto de Vendas foi MENOR que as vendas realizadas, siga os passos abaixo para a análise:

	1-) Para esta análise Utilize as colunas "Data", "Viés do Erro da Previsão" e "RUPTURA DO ESTOQUE"
		2-) Identifique todos os meses em que houve viés negativo de previsão: isto é, quando o planejamento previsto de Vendas foi MENOR que as vendas realizadas.
		3-) Para cada mês identificado:
			a-) Informe o valor da Ruptura de Estoque no mês analisado e no mês passado;
			b-) Avalie se a Ruptura de Estoque aumentou ou diminuiu nesses dois meses;
			c-) Apresente os resultados em uma tabela, seguindo o exemplo abaixo:
	| Mês       | Viés da Previsão                             | Ruptura Estoque   | Ruptura Estoque (Mês Passado)    | Variação na Cobertura de Estoque  |
	|-----------|----------------------------------------------|-------------------|----------------------------------|-----------------------------------|
	| Janeiro   | Previsão de Vendas foi MENOR que as vendas   | 5%                |                                  |							          |
	| Fevereiro | Previsão de Vendas foi MENOR que as vendas   | 6%                | 5%                               | Aumento de 1%             		  |

	Os dados do produto para sua análise estão detalhados na tabela abaixo:

	{dados} 

	Retorne todas as respostas no formato markdown, coloque como título "Análise do Produto do item:" o código do item se encontra no campo ITEM da tabela de dados, também informe no título a categoria analisada. 

	"""
											)