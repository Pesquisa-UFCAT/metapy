"""Objective function"""
from metapy_toolbox import loss_function_mse
from dimensionamento_celular import *
from diana import *
import numpy as np

def my_function_diana_inverse_problem(x, none_variable):

    # Aquisitando a interpolação do modelo
    temp = none_variable

    # Diana nonlinear problem
    sigma_t = [x[0], x[1], 0.0]
    eps_t = [0.0, x[2], x[3]]
    sigma_c = 68.74

    # Run Diana TNO
    input_data = './tenacidade.dat'
    construcao_modelo_nao_linear_tracao(input_data, sigma_t, sigma_c, eps_t)
    file_directory = 'cd C:\\Users\\wanderlei@eeca\\Desktop\\wanderLucas'
    run_diana_tno(file_directory, 'tenacidade')

    # Read output Diana TNO
    output_data = './tenacidade.tb'
    x_aux, y_predaux = leitura_saida_modelo_nao_linear(output_data, 'TDtY', 'FBY')

    # Loss
    x_num = []
    y_pred = []
    for i, valor in enumerate(x_aux):
        if valor > 3.0:
            break
        else:
            x_num.append(valor)
            y_pred.append(y_predaux[i])
    y_true = temp(x_num)
    of = loss_function_mse(y_true, y_pred)

    # Penalty function
    e_f = 2.32750E+04
    tetha_1 = np.abs(x[0]-x[1]/x[2])
    tetha_2 = np.abs((x[1]-0)/(x[2]-x[3]))
    g_0 = (x[1]-x[0]) / x[0]
    g_1 = (0.1*x[0]-x[1]) / x[1]
    g_2 = (tetha_1-e_f) / e_f
    g_3 = (tetha_2-tetha_1) / tetha_1
    g = [g_0, g_1, g_2, g_3]
    for j in g:
        of += 1E6 * max(0, j) ** 2

    return of


def my_function_diana_inverse_problem_2(x, none_variable):

    # Aquisitando a interpolação do modelo
    temp = none_variable

    # Diana nonlinear problem
    sigma_t = [x[0], x[1], 0.0]
    eps_t = [0.0, x[2], x[3]]
    sigma_c = 68.74

    # Run Diana TNO
    input_data = './tenacidade.dat'
    construcao_modelo_nao_linear_tracao(input_data, sigma_t, sigma_c, eps_t)
    file_directory = 'cd C:\\Users\\wanderlei@eeca\\Desktop\\wanderLucas'
    run_diana_tno(file_directory, 'tenacidade')

    # Read output Diana TNO
    output_data = './tenacidade.tb'
    x_aux, y_predaux = leitura_saida_modelo_nao_linear(output_data, 'TDtY', 'FBY')

    # Loss
    x_num = []
    y_pred = []
    for i, valor in enumerate(x_aux):
        if valor > 3.0:
            break
        else:
            x_num.append(valor)
            y_pred.append(y_predaux[i])
    y_true = temp(x_num)
    of = loss_function_mse(y_true, y_pred)

    # Penalty function
    e_f = 2.32750E+04
    tetha_1 = np.abs(x[0]-x[1]/x[2])
    tetha_2 = np.abs((x[1]-0)/(x[2]-x[3]))
    g_0 = (x[1]-x[0]) / x[0]
    g_1 = (0.1*x[0]-x[1]) / x[1]
    g_2 = (tetha_1-e_f) / e_f
    g_3 = (tetha_2-tetha_1) / tetha_1
    g = [g_0, g_1, g_2, g_3]
    for j in g:
        of += 1E6 * max(0, j) ** 2

    return of, x_aux, y_predaux


def my_obj_function_rafael(x, none_variable):
    # Dados do perfil original
    d = none_variable['d (m) - perfil original']
    b_f = none_variable['b_f (m) - perfil original']
    t_f = none_variable['t_f (m) - perfil original']
    t_w = none_variable['t_w (m) - perfil original']
    h_c = none_variable['h_c (m) - perfil original']
    r_y = none_variable['r_y (m) - perfil original']
    rho = none_variable['rho (kN/m3) - peso específico']
    vao = none_variable['vão da viga (m)']
    g_k = none_variable['g_k (kN) - carga permanente']
    q_k1 = none_variable['q_k1 (kN) - carga variável principal']
    q_k2 = none_variable['q_k2 (kN) - carga variável secundária']
    f_yd = none_variable['f_yd (kN/m²) - resistência ao escoamento do aço']
    gamma_a1 = none_variable['gamma_a1 - coeficiente de ponderação da resistência do aço']
    gamma_g = none_variable['gamma_g - coeficiente de ponderação das ações permanentes']
    gamma_q1 = none_variable['gamma_q1 - coeficiente de ponderação das ações var. princ.']
    gamma_q2 = none_variable['gamma_q2 - coeficiente de ponderação das ações var. secun.']
    psi_0 = none_variable['psi_0']
    psi_2 = none_variable['psi_2']
    modulo_e = none_variable['modulo E (kPa)']
    modulo_g = none_variable['modulo G (kPa)']
    impressao = none_variable['impressao']

    # Variáveis de projeto
    eta = x[0]
    micro = x[1]

    # Propriedades geométricas
    h_e0, b_w, d_g, passo, h_0,\
        altura_a, h_t, y_barra, y_0,\
        y_a, a_t, a_a, z_x0, i_t, i_y,\
        j, w_x, a_e, i_e, a_aco, d_0 = propriedades_perfil_alveolar_celular(eta, micro, d, b_f,
                                                                       t_f, t_w, h_c, r_y,
                                                                       modulo_e, modulo_g,
                                                                       impressao)

    # Peso do perfil
    of = 1 / passo * (a_aco * passo - np.pi * (d_0 ** 2) * t_w / 4) * rho
    if impressao:
        print("valor da carga gerada pelo perfil: ", of, "kN/m", "\n\n")

    # Carregamentos
    q_sdelu = 1.25 * of + g_k * gamma_g + q_k1 * gamma_q1 + q_k2 * gamma_q2 * psi_0
    q_sdels = of + g_k + q_k1 * psi_2 + q_k2 * psi_2
    if impressao:
        print("Carregamento q_sdelu: ", q_sdelu, "kN/m")
        print("Carregamento q_sdelu: ", q_sdels, "kN/m")
        print("\n\n")

    # Mecaninismo de Vierendeel
    g_0, m_plastificacao = formacao_mecanismo_veirendel(y_a, b_w, y_0, a_t, i_t, vao,z_x0, q_sdelu, f_yd, gamma_a1, impressao)

    # Escoamento do montante de alma por cisalhamento
    g_1, v_rk1 = escoamento_montante_alma_cisalhamento(q_sdelu, vao, b_w, t_w, y_0, passo, f_yd, gamma_a1, impressao)

    # Escoamento do montante de alma por flexão
    g_2, v_rk2 = escoamento_montante_alma_flexao(q_sdelu, vao, eta, y_0, t_w, f_yd, gamma_a1, impressao)

    # Flambagem lateral do montante de alma
    g_3, v_cr, v_max = flambagem_lateral_montante_alma(q_sdelu, vao, b_w, t_w, y_0, altura_a, eta, modulo_e, v_rk2, impressao)

    # Flambagem lateral a torção
    g_4, m_rd = flambagem_lateral_torcao(q_sdelu, m_plastificacao, vao, d_g, t_f, i_y, a_a, w_x, j, 0, f_yd, modulo_e, gamma_a1, impressao)

    # Estado Limite de serviço
    g_5, f_sd = deslocamento_excessivo(q_sdels, vao, modulo_e, modulo_g, a_e, i_e, impressao)

    # Método de penalidade
    g = [g_0, g_1, g_2, g_3, g_4, g_5]
    for i in g:
        of += 1E6 * max(0, i) ** 2

    return of


def my_obj_function(x, none_variable):
    x_0 = x[0]
    x_1 = x[1]
    obj_fun = x_0 ** 2 + x_1 ** 2
    return obj_fun


def idf(a, b, c, k, t_r, t_c):
    return (k * t_r ** a) / (t_c + b) ** c


def my_obj_function2(x, none_variable):

    # External IDF dataset
    df = none_variable

    # Design variables
    a = x[0]
    b = x[1]
    c = x[2]
    k = x[3]

    # Start internal variables
    y_true = []
    y_pred = []

    # Read dataset and idf evaluation
    for _, row in df.iterrows():
        t_r = row['T_R']
        t_c = row['T_C']
        y_true.append(row['Y_EXP'])
        y_pred.append(idf(a, b, c, k, t_r, t_c))

    mse = loss_function_mse(y_true, y_pred)
    of = mse

    return of
# # Derivatives of the objective function
# def MY_FUNCTION_DERIVATIVE(X, NULL_DIC):
#     X_0 = X[0]
#     X_1 = X[1]
#     OF_DIFF_0 = 24 * X_0 - 12 * X_1 + 2
#     OF_DIFF_1 = 8 * X_1 - 12 * X_0
#     OF_DIFF = [OF_DIFF_0, OF_DIFF_1]
#     return OF_DIFF


# def MY_FUNCTION_TSP(X, NULL_DIC):
#     """
#     https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html
#     """
#     COST = [[0.0, 3.0, 4.0, 2.0, 7.0],
#             [3.0, 0.0, 4.0, 6.0, 3.0],
#             [4.0, 4.0, 0.0, 5.0, 8.0],
#             [2.0, 6.0, 5.0, 0.0, 6.0],
#             [7.0, 3.0, 8.0, 6.0, 0.0]]
#     ROUTE = list(X.copy())
#     OF = 0
#     for NODE in range(len(ROUTE)):
#         I = int(ROUTE[NODE])
#         if NODE == len(ROUTE) - 1:
#             J = int(ROUTE[0])
#         else:
#             J = int(ROUTE[NODE + 1])
#         OF += COST[I][J]
#     return OF


# def KNAPSACK(X, INSTANCE):
#     """
#     Input:
#     X
#     INSTANCE  |  Instance tag      |     | String
#     X         |  Design variables  |     | Py List
    
#     Output
#     G         |  Constraints       |  $  | Float
#     OF        |  Profit            |  $  | Float
#     """
    
#     if INSTANCE == 'LETS':
#         PROFIT = [5.0, 5.5, 7.5, 4.0, 4.5, 3.0, 6.0, 5.8, 6.2, 3.5, 1.0, 4.2, 6.5]
#         COST =   [5.0, 4.5, 2.5, 6.0, 5.5, 7.0, 4.0, 4.2, 3.8, 6.5, 9.0, 5.8, 3.5]
#         COST_MAX = 25.0
#         D = 13

#     OF = 0
#     G = 0
    
#     for I in range(len(PROFIT)):
#         OF += X[I] * PROFIT[I]
#         G += X[I] * COST[I]

#     OF *= -1
#     COST_VALUE = G
#     G -= COST_MAX
    
#     return COST_VALUE, G, OF

# def LETS_MAKE(X, NULL_DIC):
#     DISCRETE_DATA = NULL_DIC['X']
#     D = len(DISCRETE_DATA)
#     X_NEW = CONVERT_CONTINUOUS_DISCRETE(X, DISCRETE_DATA)
#     _, G_0, OF = KNAPSACK(X_NEW, NULL_DIC['INSTANCE'])
#     PSEUDO_OF = OF + (np.maximum(0, G_0)) * NULL_DIC['R_P']
    
#     return PSEUDO_OF

def tensao_max(x, none_variable):
    theta = x[0]*(np.pi/180.0)
    sigma_x = 50
    sigma_y = -10
    tal_xy = 40
    of = 0.5*(sigma_x + sigma_y) + 0.5*(sigma_x - sigma_y)*np.cos(2*theta) + tal_xy*np.sin(2*theta)
    
    return of