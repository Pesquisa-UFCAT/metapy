from metapy_toolbox import genetic_algorithm_01, hill_climbing_01, initial_population_01
from io import BytesIO

import streamlit as st
import pandas as pd

import base64
import textwrap


def generate_function(text_function):
    function_code = f"""
    def obj_function(x, none_variable):
        obj_fun = {objective_funcion}

        return obj_fun
    """
    
    with open("obj_functions.py", "w") as f:
        f.write(textwrap.dedent(function_code))
    
    return function_code

st.title("Learning with METApy")

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = image_to_base64("assets/images/logo.png")
img_html = f'<img src="data:image/png;base64,{img_base64}" width="150"/>'


st.markdown(rf""" 
<table>
  <tr>
    <td style="width:70%;">
      <p align="justify">
        The METApy optimization toolbox is an easy-to-use environment for applying metaheuristic optimization methods. The platform has several optimization methods and functions for generating charts and statistical analysis of the results.
      </p>
    </td>
    <td style="width:100%; text-align: center;">{img_html}</td>  
  </tr>
</table>  
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .suggestions-box1 {
        border: 2px solid #00008B;
        background-color: #ADD8E6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    
    ::-webkit-scrollbar {
     width: 18px;
    }

    /* Estiliza o fundo da barra de rolagem */
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }

    /* Estiliza o "thumb" da barra de rolagem */
    ::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 10px;
    }

    /* Muda a cor quando hover */
    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
    </style>
    
    <div class="suggestions-box1">
        <h4>Suggestions</h4>
        <p>If you have any suggestions or error reports regarding the algorithm's functioning, 
        please email us at <a href="mailto:wanderlei_junior@ufcat.edu.br">wanderlei_junior@ufcat.edu.br</a>. 
        We will be happy to improve the framework.</p>
    </div>
    """,
    unsafe_allow_html=True)

# st.write("")

# st.markdown(
#     """    
#     <style>
#     .suggestions-box {
#         border: 2px solid #FFA500;
#         background-color: #FFF3CD;
#         padding: 15px;
#         border-radius: 10px;
#         box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
#     }
#     .suggestions-box p {
#         margin: 5px 0;
#     }
#     .suggestions-box a {
#         text-decoration: none;
#         color: #007BFF;
#         font-weight: bold;
#     }
#     </style>

#     <div class="suggestions-box">
#         <h4>Team</h4>
#         <p><a href="http://lattes.cnpq.br/2268506213083114" target="_blank">Prof. PhD Wanderlei Malaquias Pereira Junior</a></p>
#         <p><a href="http://lattes.cnpq.br/8801080897723883" target="_blank">Prof. PhD Daniel de Lima Araújo</a></p>
#         <p><a href="http://lattes.cnpq.br/4319075758352865" target="_blank">Prof. PhD André Teófilo Beck</a></p>
#         <p><a href="http://lattes.cnpq.br/7623383075429186" target="_blank">Prof. PhD André Luis Christoforo</a></p>
#         <p><a href="http://lattes.cnpq.br/3180484792983028" target="_blank">Prof. PhD Iuri Fazolin Fraga</a></p>
#         <p><a href="http://lattes.cnpq.br/0067281135180613" target="_blank">Prof. PhD Marcos Napoleão Rabelo</a></p>
#         <p><a href="http://lattes.cnpq.br/3103828419121683" target="_blank">Prof. PhD Marcos Luiz Henrique</a></p>
#         <p><a href="https://cse.umn.edu/dsi/ketson-r-m-dos-santos" target="_blank">Prof. PhD Ketson Roberto Maximiano dos Santos</a></p>
#         <p><a href="http://lattes.cnpq.br/6429652195589650" target="_blank">Msc. Murilo Carneiro Rodrigues</a></p>
#         <p><a href="http://lattes.cnpq.br/8465474056220474" target="_blank">Msc. Matheus Henrique Morato Moraes</a></p>
#         <p><a href="http://orcid.org/0009-0008-4084-2137" target="_blank">Academic Luiz Henrique Ferreira Rezio</a></p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# st.write("")
# st.subheader("How to use")
# st.markdown("""
# To use PAREpy, you need to define a state limit function. In this case, fill the boxes with your capacity and demand functions. 
# This framework uses Python, so you need to start declaring your variables as x[0], x[1], and so on, depending on the number of variables in your problem. See an example:

# Consider the simply supported beam show in example 5.1 Nowak and Collins. The beam is subjected to a concentrated live load $p$ and a uniformly distributed dead load $w$. 
# Assume $P$ (concentrated live load), $W$ (uniformly distributed dead load) and the yield stress, $F_y$, are random quantities; the length $l$ and the plastic setion modulus $z$ are assumed to be precisely know (deterministic). 
# The distribution parameters for $P$, $W$ and $F_y$ are given bellow:
# """, unsafe_allow_html=True)

# st.table({
#     'Variable': ['Yield stress $F_y$', 'Live load $(P)$', 'Dead load $(W)$'],
#     'Distribution': ['Normal', 'Gumbel max.', 'Log-normal'],
#     'Location': [40.3, 10.2, 0.25],
#     'Coefficient of Variation (COV)': [0.115, 0.110, 0.100],
#     'Scale': [4.63, 1.12, 0.025]
#         })

# st.write("")

# st.markdown(r"""
#     The limit state function for beam bending can be expressed as:
#     $$
#     \begin{align*}
#     R &= 80 \cdot F_y \tag{1} \\
#     S &= 54 \cdot P + 5832 \cdot W \tag{2} \\
#     G &= R - S \begin{cases}
#                     \leq 0, \text{failure} \\
#                     > 0, \text{safe}
#                 \end{cases} \tag{3}
#     \end{align*}
#     $$
# """, unsafe_allow_html=True) 

st.write("")
st.subheader("Objective Function parameters")
objective_funcion = st.text_area("Objective Function", value="x[0] ** 2 + x[1] ** 2")

st.write("")
st.subheader("Setup")
col1, col2 = st.columns(2)
with col1:
    model_type = st.selectbox('Model Type', ['genetic algorithm','hill climbing'])
    population = st.number_input("Number of Population", min_value=1, max_value=100, value=2)
    x1_lower = st.number_input('X[0] Pop Lower Limit', min_value=-100, max_value=100, value=-10)
    x1_upper = st.number_input('X[0] Pop Upper Limit', min_value=-100, max_value=100, value=10)
    pdf = st.selectbox('Probability Density Function', ['uniform', 'gaussian'])
    
with col2:
    iteration = st.number_input('Number Of Iterations', min_value=1, max_value=100, value=100)
    dimension = st.number_input('Number Of Dimensions', min_value=1, max_value=10, value=2)
    x2_lower = st.number_input('X[1] Pop Lower Limit', min_value=-100, max_value=100, value=-10)
    x2_upper = st.number_input('X[1] Pop Upper Limit', min_value=-100, max_value=100, value=10)
    crossover = st.number_input('Covariance (%)', min_value=0, max_value=100, value=20)

if model_type == 'genetic algorithm':
    st.header("Genetic Algorithm Parameters")
    col1, col2 = st.columns(2)
    with col1:
        selection = st.selectbox('Selection', ['roulette'])
        crossover_type = st.selectbox('Crossover Type', ['linear', 'blx-alpha', 'single point', 'multi point', 'uniform', 'heuristic', 'arithmetic', 'sbc', 'laplace'])
        crossover = st.number_input('Crossover rate (%)', min_value=0, max_value=100, value=80)

    with col2:
        mutation_rate = st.number_input('Mutation rate (%)', min_value=0, max_value=100, value=12)
        mutation_type = st.selectbox('Mutation Type', ['hill climbing'])
        mutation_cov = st.number_input('Mutation Cov (%)', min_value=0, max_value=100, value=20)
        
    cross = ['arithmetic','sbc', 'laplace']

    if crossover_type in cross:
        st.header("Crossover Parameters")
        if crossover_type == 'arithmetic':
            alpha = st.number_input('Alpha', value=0.86)
            setup_cross = {'crossover rate (%)': crossover,'type': crossover_type, 'alpha': alpha}
        elif crossover_type == 'sbc':
            eta_c = st.number_input('eta_c', value=2)
            setup_cross = {'crossover rate (%)': crossover,'type': crossover_type, 'eta_c': eta_c}
        elif crossover_type == 'laplace':
            col1, col2 = st.columns(2)
            with col1:
                loc = st.number_input('Loc', value=0)
            with col2:
                scale = st.number_input('Scale', value=0.5)
            setup_cross = {'crossover rate (%)': crossover,'type': crossover_type, 'loc': loc, 'scale': scale}
    else:
        setup_cross = {'crossover rate (%)': crossover,'type': crossover_type}


if st.button("Run Simulation"):
    function_str = generate_function(objective_funcion)

    from obj_functions import obj_function
    
    if model_type == 'genetic algorithm':
        setup = {
            'number of iterations': iteration,
            'number of population': population,
            'number of dimensions': dimension,
            'x pop lower limit': [x1_lower, x1_lower],
            'x pop upper limit': [x1_upper, x2_upper],
            'none variable': None,
            'objective function': obj_function,
            'algorithm parameters': {
                'selection': {'type': selection},
                'crossover': setup_cross,
                'mutation': {
                    'mutation rate (%)': mutation_rate,
                    'type': mutation_type,
                    'cov (%)': mutation_cov,
                    'pdf': pdf
                    }
            }
        }
        
        seed = None 

        init_pop = initial_population_01(setup['number of population'], setup['number of dimensions'], setup['x pop lower limit'], setup['x pop upper limit'])

        settings = [setup, init_pop, seed]
        df_all_results, df_resume, time_cost, report = genetic_algorithm_01(settings)


    elif model_type == 'hill climbing':
        setup = {
            'number of iterations': iteration,
            'number of population': population,
            'number of dimensions': dimension,
            'x pop lower limit': [x1_lower, x1_lower],
            'x pop upper limit': [x1_upper, x2_upper],
            'none variable': None,
            'objective function': obj_function,
            'algorithm parameters': {
                'mutation': {
                    'cov (%)': crossover,
                    'pdf': pdf
                }
            },
        }

        seed = None 

        init_pop = initial_population_01(setup['number of population'], setup['number of dimensions'], setup['x pop lower limit'], setup['x pop upper limit'])
        
        settings = [setup, init_pop, seed]
        df_all_results, df_resume, time_cost, report = hill_climbing_01(settings)

    best_columns = [f'X_{i}_BEST' for i in range(dimension)] + ['OF BEST', 'FIT BET', 'ID BEST']
    worst_columns = [f'X_{i}_WORST' for i in range(dimension)] + ['OF WORST', 'FIT WORST', 'ID WORST']
    avg_columns = ['OF AVG', 'FIT AVG', 'ITERATION', 'neof']
    df_resume.columns = best_columns + worst_columns + avg_columns

    st.session_state.text_results = "Results"
    st.session_state.text_time = f"Time of execution: {time_cost} seconds"
    st.session_state.text_resume = "Resume of Iterations"

    st.session_state.df_resume = df_resume
    st.session_state.report = report


if "text_results" in st.session_state:
    st.subheader(st.session_state.text_results)
    selected_columns = [f'X_{i}_BEST' for i in range(dimension)] + ['OF BEST', 'FIT BET', 'ID BEST']
    st.write(st.session_state.df_resume[selected_columns].iloc[-1]) 
    st.write(st.session_state.text_time)
    st.header(st.session_state.text_resume)
    st.write(st.session_state.df_resume)  

if "df_resume" in st.session_state:
    results = st.session_state.df_resume  
    final_results = BytesIO()
    with pd.ExcelWriter(final_results, engine="xlsxwriter") as writer:
        results.to_excel(writer, index=False, sheet_name="Results")
    final_results.seek(0)
    st.download_button("Download samples", final_results, file_name="results.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")