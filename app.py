import streamlit as st
import pandas as pd
from metapy_toolbox import hill_climbing_01
from my_example import my_obj_function  # Certifique-se de que esta função está definida

st.write("""
# METAPY - Algorithm Hill Climbing
Insira os dados abaixo para aplicação do algoritmo hill climbing
""")

# Número de iterações
iteration = st.number_input('Number Of Iterations', min_value=1, max_value=100, value=100)
population = st.number_input('Number Of Population', min_value=1, max_value=10, value=2)
dimension = st.number_input('Number Of Dimensions', min_value=1, max_value=10, value=2)
x_lower = st.number_input('X Pop Lower Limit', min_value=-100, max_value=100, value=-10)
x_upper = st.number_input('X Pop Upper Limit', min_value=-100, max_value=100, value=10)
cov = st.number_input('Covariance (%)', min_value=-100, max_value=100, value=20)

# Solicitar a população inicial ao usuário
st.write("### População Inicial")
init_pop = []
for i in range(population):
    st.write(f"#### Indivíduo {i + 1}")
    individual = []
    for j in range(dimension):
        value = st.number_input(
            f'Dimensão {j + 1} do Indivíduo {i + 1}',
            min_value=float(x_lower),
            max_value=float(x_upper),
            value=(x_lower + x_upper) / 2  # Sem o int(), agora é um float
        )
        individual.append(value)
    init_pop.append(individual)

# Botão para executar o algoritmo
if st.button('Run Algorithm'):
    # Configuração do algoritmo
    setup = {
        'number of iterations': iteration,
        'number of population': population,
        'number of dimensions': dimension,
        'x pop lower limit': [x_lower] * dimension,
        'x pop upper limit': [x_upper] * dimension,
        'none variable': None,
        'objective function': my_obj_function,
        'algorithm parameters': {
            'mutation': {
                'cov (%)': 20,
                'pdf': 'uniform'
            }
        },
    }

    seed = None  # Semente para reprodutibilidade

    # Executar o algoritmo
    settings = [setup, init_pop, seed]
    df_all_results, df_resume, time_cost, report = hill_climbing_01(settings)

    # Renomear colunas dinamicamente com base no número de dimensões
    best_columns = [f'X_{i}_BEST' for i in range(dimension)]
    worst_columns = [f'X_{i}_WORST' for i in range(dimension)]
    other_columns = ['OF BEST', 'FIT BET', 'ID BEST', 'OF WORST', 'FIT WORST', 'ID WORST', 'OF AVG', 'FIT AVG', 'ITERATION', 'neof']
    df_resume.columns = best_columns + worst_columns + other_columns

    # Exibir resultados
    st.write("### Resultados do Algoritmo")
    st.write(f"Tempo de execução: {time_cost} segundos")
    st.write("#### Melhor Resultado:")
    st.write(df_all_results.iloc[-1])  # Melhor resultado da última iteração
    st.write("#### Resumo das Iterações:")
    st.write(df_resume)  # Resumo das iterações com colunas renomeadas

    # Exibir o relatório completo
    st.write("### Relatório Completo")
    st.text(report)

    # Opção para baixar o relatório em formato .txt
    st.download_button(
        label="Baixar Relatório em TXT",
        data=report,
        file_name="report_hill_climbing.txt",
        mime="text/plain"
    )

    # Opção para baixar o resumo em formato .xlsx
    st.download_button(
        label="Baixar Resumo em Excel",
        data=df_resume.to_csv(index=False).encode('utf-8'),
        file_name="report_hill_climbing.csv",
        mime="text/csv"
    )
