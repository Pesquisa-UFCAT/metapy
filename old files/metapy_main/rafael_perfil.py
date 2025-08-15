"""Objective function"""
from metapy_toolbox import convert_continuous_discrete
from dimensionamento_celular import *


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
    x_new = convert_continuous_discrete(x, data)
    x_new
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
