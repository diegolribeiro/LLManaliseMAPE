from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.globals import set_debug
import pandas as pd
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from prompt_mape import prompt_analise_previsao


st.set_page_config(layout='wide')
st.title("Análise de MAPE de Categoria")


load_dotenv()
set_debug(False)
llm = ChatOpenAI(model="gpt-4.1-mini",
                    temperature=0.0,
                    api_key=os.getenv("OPENAI_API_KEY"),
                    verbose=True)

df_mape_categoria = pd.read_csv("./dados/MAPE_CATEGORIA.csv", sep=";", thousands=".", decimal=",", encoding="latin1")
df_mape_item = pd.read_csv("./dados/MAPE_ITEM.csv", sep=";", thousands=".", decimal=",", encoding="latin1")
df_faturamento_item = pd.read_csv("./dados/FARUAMENTO_ITEM.csv", sep=";", thousands=".", decimal=",", encoding="latin1")


lista_categoria = df_mape_categoria['CATEGORIA'].unique()
options = st.selectbox('Selecione uma categoria', df_mape_categoria['CATEGORIA'].unique(), placeholder='Escolha uma categoria para filtrar')


df_mape_categoria_filtrado = df_mape_categoria[df_mape_categoria['CATEGORIA'].isin([options])]
df_mape_item_filtrado = df_mape_item[df_mape_item['CATEGORIA'].isin([options])]
df_faturamento_item_filtrado = df_faturamento_item[df_faturamento_item['CATEGORIA'].isin([options])].nlargest(5,'FATURAMENTO MÉDIO ÚLTIMOS 3 MESES')

dados_mape_categoria =  df_mape_categoria_filtrado.to_markdown(index=False)
modelo_mape_categoria = prompt_analise_previsao.prompt_analise_mape_categoria(dados_mape_categoria)

parte1_mape = modelo_mape_categoria | llm | StrOutputParser()


if st.button("Analisar MAPE"):
    with st.spinner("Analisando os dados...", show_time=True):
        #cadeia = SimpleSequentialChain(chains=[cadeia_cidade, cadeia_restaurantes, cadeia_culturual], verbose=True)
        cadeia_analise = (parte1_mape)
        resultado = cadeia_analise.invoke({"dados" : dados_mape_categoria})
        with st.expander(str(options), expanded=False, icon=None, width="stretch"):
            st.markdown(resultado)

        with st.expander('Análise dos Itens da Categoria', expanded=False, icon=None, width="stretch"):
            lista_itens_analise = df_faturamento_item_filtrado['ITEM'].unique()
            for item in lista_itens_analise:
                dados = df_mape_item_filtrado[df_mape_item_filtrado['ITEM'] == item]
                if not dados.empty:
                    with st.expander(str(item), expanded=False, icon=None, width="stretch"):
                        modelo_mape_item = prompt_analise_previsao.prompt_analise_mape_item(dados.to_markdown(index=False),options)
                        parte1_mape_item = modelo_mape_item | llm | StrOutputParser()
                        cadeia_analise = (parte1_mape_item)
                        resultado = cadeia_analise.invoke({"dados" : dados, "categoria" : options})
                        st.markdown(resultado)
            


            