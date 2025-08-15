"""Restrições do problema de otimização viga castelada"""

import numpy as np

def propriedades_perfil_alveolar_celular(eta, micro, d, b_f, t_f, t_w, h_c, r_y, modulo_e, modulo_g, impressao):
    """
    Avalia as propriedades geométricas do perfil castelado
    Args:
      d (Float): Altura do perfil original.
      b_f (Float): Largura da mesa do perfil original.
      t_f (Float): Espessura da mesa do perfil original.
      t_w (Float): Espessura da alma do perfil original.
      k (Float): Razão de expansão do perfil original.
      h_c (Float): Altura da chapa de expansão.
      impressao (Booleano): impressão do resultado.

    Returns:

    """

    b_w = micro * d * (eta - 1)
    d_0 = micro * d
    h_e0 = np.sqrt((d_0 / 2) ** 2 - (b_w / 2) ** 2)
    d_g = d + h_e0
    k = d_g / d
    passo = eta * d_0
    h_0 = d_0
    altura_a = d_0 / 2
    h_t = (d_g-d_0) / 2
    numerador_yavg = (b_f * t_f ** 2) + (h_t ** 2 * t_w) - (t_f ** 2 * t_w)
    denominador_yavg = 2 * (b_f * t_f + h_t * t_w - t_f * t_w)
    y_barra = numerador_yavg / denominador_yavg
    y_0 = h_0 / 2 + h_t - y_barra
    y_a = h_t - y_barra
    a_t = t_w * (h_t - t_f) + b_f * t_f
    a_a = 2 * a_t
    z_x0 = 2 * a_t * y_0
    i_t1 = (b_f * t_f **3) / 12
    i_t2 = b_f * t_f * (y_barra - t_f * 0.50) ** 2
    i_t3 = t_w * (h_t - t_f) ** 3 / 12
    i_t41 = t_w * (h_t - t_f)
    i_t42 = (y_barra - (h_t + t_f) / 2)**2
    i_t4 =  i_t41 * i_t42
    i_t = i_t1 + i_t2 + i_t3 + i_t4
    i_y1 =  t_f * b_f ** 3 / 12
    i_y2 = (h_t - t_f) * t_w ** 3 / 12
    i_y = 2 * (i_y1 + i_y2)
    j_1 = b_f * t_f ** 3
    j_2 = (h_t - t_f) * t_w ** 3
    j = 2 / 3 * (j_1 + j_2)
    w_x = 4 * y_0 ** 2 * a_t / d_g
    i_e1 = 2 * ((a_t * y_0 ** 2) + i_t)
    i_e2 = (t_w / 24) * ((6 * altura_a ** 3) + (8 * (altura_a ** 2) * h_c) + (3 * altura_a * (h_c ** 2)) + (((2 * b_w) / passo) * (altura_a + h_c) * ((altura_a ** 2) + (2 * altura_a * h_c) + (2 * h_c ** 2))))
    i_e = i_e1 + i_e2
    par_1 = 54 / ((y_0**2) * t_w * (passo**2))
    par_1_1 = modulo_g / modulo_e
    par_2 = (0.2 * (altura_a**3)) + (0.375 * altura_a * h_c * (altura_a + 0.75 * h_c)) + (0.125 * (h_c**3))
    par_3 = (0.6 / (t_w * y_0**2)) * (2.08 * altura_a + 1.5 * h_c)
    par_4 = passo**2 / (648 * i_t)
    par_5 = (2 * t_w * y_a**5) / (45 * i_t**2)
    a_e1 = (par_1 * par_1_1) * (par_2) + par_3 + (par_4 * par_1_1) + par_5
    a_e = 1 / a_e1
    a_aco = 2 * b_f * t_f + (d_g - t_f) * t_w + (4 - np.pi) * r_y ** 2

    if impressao:
        print('Propriedades geometricas do perfil alveolar castelado')
        print('b_w:', b_w, 'm')
        print('d_0:', d_0, 'm')
        print('h_e0:', h_e0, 'm')
        print('d_g:', d_g, 'm')
        print("passo:", passo, 'm')
        print('k:', k)
        print('h_0:', h_0, 'm')
        print('a:', altura_a, 'm')
        print('h_t:', h_t, 'm')
        print('y_barra:', y_barra, 'm')
        print('y_0:', y_0, 'm')
        print('y_a:', y_a, 'm')
        print('a_t:', a_t, 'm2')
        print('a_a:', a_a, 'm2')
        print('z_x0:', z_x0, 'm3')
        print('i_t:', i_t, 'm4')
        print('i_y:', i_y, 'm4')
        print('j:', j, "m4")
        print('w_x:', w_x, "m3")
        print('a_e:', a_e, "m2")
        print('i_e:', i_e, "m4")
        print('a_aco:', a_aco, "m2")
        print('\n\n')

    return h_e0, b_w, d_g, passo, h_0, altura_a, h_t, y_barra, y_0, y_a, a_t, a_a, z_x0, i_t, i_y, j, w_x, a_e, i_e, a_aco, d_0


def formacao_mecanismo_veirendel(y_a, b_w, y_0, a_t, i_t, vao,z_x0, q_sd, f_yd, gamma_a1, impressao):
    """
    Verificação da restrição do mecanismo de vierendeel para forma castelada

    Args:
      y_a (Float): Distância entre o topo do perfil e o centro de gravidade do terço superior.
      b_w (Float): Largura da alma.
      y_0 (Float): Distância entre o centro de gravidade do cordão ao eixo da viga.
      a_t (Float): Área do T.
      i_t (Float): Inércia de um cordão em relação ao seu eixo baricentrico.
      vao (Float): Vão do perfil.
      z_x0 (Float): Módulo de resistência plástico da seção.
      q_sd (Float): Carga uniformemente distribuída de cálculo.
      f_yd (Float): Tensão de cálculo do escoamento do aço.
      gamma_a1 (Float): Coeficiente de ponderação da resistência.
      impressao (Booleano): impressão do resultado.
    
    Returns:
      g (Float): Restrição do mecanismo de vierendeel.
      m_rk (Float): Momento de plastificação caracteristico.
    """

    # Cálculo da seção crítica da viga castelada
    fator = (3 * y_a ** 2) / b_w ** 2
    if fator <= 1:
        p_1 = b_w * y_0 * y_a * a_t
        p_2 = 2 * i_t
    else:
        p_1 = np.sqrt(3) * y_0 * (y_a ** 2) * a_t
        p_2 = 2 * i_t
    c = p_1 / p_2
    x = vao / 2 - c

    # Esforços internos na seção critica
    m_sdc = 0.50 * q_sd * vao * x - 0.5 * q_sd * x ** 2
    v_sdc = 0.50 * q_sd * vao - q_sd * x

    # Restrição do mecanismo de Vierendeel
    m_rk = z_x0 * f_yd
    m_plastificacao = m_rk / gamma_a1
    m_vierendeel = m_sdc + c * v_sdc
    g = m_vierendeel / m_plastificacao - 1

    # Impressões
    if impressao:
      print('Verificacao da viga castelada para momento de vierendeel')
      print('c: ', c, 'm')
      print('x: ', x, 'm')
      print('m_sdc: ', m_sdc, 'kN.m')
      print('v_sdc: ', v_sdc, 'kN')
      print('m_sd: ', round(m_vierendeel, 3), 'kN.m')
      print('m_rk: ', round(m_rk, 3), 'kN.m')
      print('m_rd: ', round(m_plastificacao, 3), 'kN.m')
      print('Restricao: ', g)
      print('\n\n')

    return g, m_rk


def escoamento_montante_alma_cisalhamento(q_sd, vao, b_w, t_w, y_0, passo, f_yd, gamma_a1, impressao):
    """
    Verificação do escoamento do montante da alma por cisalhamento

    Args:
      q_sd (Float): Carga uniformemente distribuída de cálculo.
      vao (Float): Vão do perfil.
      b_w (Float): Largura da alma.
      t_w (Float): Espessura da alma.
      y_0 (Float): Distância entre o centro de gravidade do cordão ao eixo da viga.
      passo (Float): Passo do alvéolo.
      f_yd (Float): Tensão de cálculo do escoamento do aço.
      gamma_a1 (Float): Coeficiente de ponderação da resistência.
      impressao (Booleano): impressão do resultado.

    Returns:
      g (Float): Restrição do escoamento do montante da alma por cisalhamento.
      v_rk1 (Float): Resistência característica do escoamento do montante da alma por cisalhamento.
    """

    # Cortante de cálculo
    v_sd = 0.50 * q_sd * vao

    # Resistência característica do escoamento do montante da alma por cisalhamento
    p_1 = 4 * b_w * t_w * y_0 * f_yd
    p_2 = 3 * np.sqrt(3) * passo
    v_rk1 = p_1 / p_2
    v_rk = v_rk1
    v_rd = v_rk / gamma_a1

    # Resistência
    g = v_sd / v_rd - 1

    # Impressões
    if impressao:
      print('Verificacao da viga castelada para escoamento do montante da alma por cisalhamento')
      print('v_sd: ', v_sd, 'kN')
      print('v_rk: ', v_rk, 'kN')
      print('v_rd: ', v_rd, 'kN')
      print('Restricao: ', g)
      print('\n\n')

    return g, v_rk1


def escoamento_montante_alma_flexao(q_sd, vao, eta, y_0, t_w, f_yd, gamma_a1, impressao):
    """
    Verificação do escoamento do Montante da alma por flexão
    """

    # Resistência característica do escoamento do montante da alma por flexão
    qsi = np.sqrt(eta ** 2 + 8)
    p_1 = y_0 * t_w * f_yd / (3 * eta)
    p_2 = (3 * eta - qsi) ** 2
    p_3 = np.sqrt(4 - (eta - qsi) ** 2)
    v_rk2 = p_1 * p_2 / p_3
    v_rk = v_rk2
    v_rd = v_rk / gamma_a1

    # Cortante de cálculo
    v_sd = 0.50 * q_sd * vao

    # Resistência
    g = v_sd / v_rd - 1

    # Impressões
    if impressao:
      print('Verificacao da viga castelada para escoamento do montante da alma por flexao')
      print('v_sd: ', v_sd, 'kN')
      print('v_rk: ', v_rk, 'kN')
      print('v_rd: ', v_rd, 'kN')
      print('Restricao: ', g)
      print('\n\n')

    return g, v_rk2


def flambagem_lateral_montante_alma(q_sd, vao, b_w, t_w, y_0, altura_a, eta, modulo_e, v_rk2, impressao):
    """
    Verificação da flambagem lateral do montante da alma
    """

    # Cortante critico
    p_1 = (modulo_e * t_w ** 3) / (0.59 * eta * y_0 ** 2)
    p_2 = y_0 - 0.40 * (2 - eta) * altura_a
    v_cr = p_1 * p_2
    fator = v_cr / v_rk2

    # Cortante de cálculo
    v_sd = 0.50 * q_sd * vao

    # Restrição da flambagem lateral do montante da alma
    if fator < 1:
        v_max = 2 / 3 * v_cr
    elif 1 <= fator < 2:
      v_max = (v_rk2 + v_cr) / 3
    elif fator >= 2:
      v_max = v_rk2
    g = v_sd / v_max - 1

    # Impressões
    if impressao:
      print('Verificacao da flambagem lateral do montante da alma')
      print('v_sd: ', v_sd, 'kN')
      print('v_cr: ', v_cr, 'kN')
      print('v_rk2: ', v_rk2, 'kN')
      print('fator: ', fator)
      print('v_max: ', v_max, 'kN')
      print('Restricao: ', g)
      print('\n\n')

    return g, v_cr, v_max


def flambagem_lateral_torcao(q_sd, m_plastificacao, vao, d_g, t_f, i_y, a_a, w_x, j, c_l, f_yd, modulo_e, gamma_a1, impressao):
    """
    Verificação da flambagem lateral à torçao
    """

    # Propriedades das equações
    c_w = ((d_g - t_f) ** 2 * i_y) / 4
    r_y = np.sqrt(i_y / a_a)
    beta_1 = (0.7 * f_yd * w_x) / (modulo_e * j)
    #beta_1 = 4
    l_p = 1.76 * r_y * np.sqrt(modulo_e / f_yd)
    l_b = vao / (c_l + 1)
    p_1 = (1.66 * np.sqrt (i_y * j)) / (j * beta_1)
    p_2 = np.sqrt(1 + (27 * c_w * beta_1 ** 2) / i_y)
    l_rcor = p_1 * np.sqrt(1 + p_2)

    # Esforços seção critica
    p_a = vao/4
    p_b = vao/2
    p_c = 3*vao/4
    m_a = ((q_sd * vao * p_a) / 2) - ((q_sd * p_a ** 2) / 2)
    m_b = ((q_sd * vao * p_b) / 2) - ((q_sd * p_b ** 2) / 2)
    m_c = ((q_sd * vao * p_c) / 2) - ((q_sd * p_c ** 2) / 2)
    m_max = q_sd * vao ** 2 / 8
    c_b = 12.5 * m_max / (2.5 * m_max + 3 * m_a + 4 * m_b + m_c)
    m_sd = m_max

    # Restrição da flambagem lateral a torção
    if l_b > l_rcor:
        condicao = 'l_b > l_rcor'
        m_rk1 = (c_b * np.pi ** 2 * modulo_e * i_y) / l_b ** 2
        m_rk2 = c_w / i_y
        m_rk3 = 1 + (0.039 * j * l_b ** 2) / c_w
        m_rk = m_rk1 * np.sqrt(m_rk2 * m_rk3)
        m_rcor = None
    elif l_p <= l_b <= l_rcor:
        condicao = 'l_p <= l_b <= l_rcor'
        m_rcor = ((0.31 * modulo_e) / l_rcor ** 2) * np.sqrt(i_y * (1000 * c_w + 39 * j * l_b ** 2))
        inter = (l_b - l_p) / (l_rcor - l_p)
        m_rk = c_b * (0.9 * m_plastificacao - (0.9 * m_plastificacao - m_rcor) * inter)
    elif l_b < l_p:
        condicao = 'l_b < l_p'
        m_rcor = None
        m_rk = 0.9 * m_plastificacao
    m_rd = m_rk / gamma_a1
    g = m_sd / m_rd - 1

    # Impressões
    if impressao:
      print('Verificacao da flambagem lateral a torcao')
      print("c_w:", c_w, 'm^6')
      print("r_y:", r_y, 'm')
      print("beta_1:", beta_1, 'm^-1')
      print("l_p:", l_p, 'm')
      print("l_b:", l_b, 'm')
      print("l_rcor:", l_rcor, 'm')
      print("m_a:", m_a, 'kNm')
      print("m_b:", m_b, 'kNm')
      print("m_c:", m_c, 'kNm')
      print('m_sd', m_max, 'kNm')
      print('c_b:', c_b)
      print('condicao:', condicao)
      print('m_rcor:', m_rcor, 'kNm')
      print('m_rk:', m_rk, 'kNm')
      print('m_rd:', m_rd, 'kNm')
      print('Restricao: ', g)
      print("\n\n")

    return g, m_rd


def deslocamento_excessivo(q_sd, vao, modulo_e, modulo_g, a_e, i_e, impressao):
    """
    Verificaçao da flecha por deformação excessiva
    """
    
    # Flechas isoladas
    f_m = (5 * q_sd * vao ** 4) / (384 * modulo_e * i_e)
    f_v = (q_sd * vao ** 2) / (8 * modulo_g * a_e)
    f_sd = (f_m + f_v)
    f_max = (vao / 350)
    
    # Verificação do estado limite
    g = f_sd / f_max - 1

    # Impressões
    if impressao:
      print('Verificacao da deformacao excessiva')
      print('Deslocamento f_m', f_m)
      print('Deslocamento f_v', f_v)
      print('Deslocamento total', f_sd)
      print('Deslocamento admissivel f_sd:', f_max)
      print('Restricao: ', g)

    return g, f_sd
