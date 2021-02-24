<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script> 
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

## DETERMINAÇÃO DO DIAGRAMA MOMENTO CURVATURA

<p style="text-align: justify;">O diagrama momento-curvatura reflete as leis tensão-deformação não lineares do aço e do concreto. Para cálculo do diagrama momento-curvatura admite-se a hipótese de Bernoulli. Com isto a curvatura é igual ao gradiente de deformações na seção transversal, e também igual a variação da rotação por unidade de comprimento da barra [1].</p> 

Para o cálculo desse diagrama deverá ser admitido o seguintes hipóteses [1]:  
1. Seções planas antes e após das deformações;  
2. Na compressão e na tração antes da fissuraão há aderência rígida (sem deslizamento) entre armadura e o concreto circundante;  
3. Consideração de carregamento monotônicos quase-estáticos, sem qualquer alterância ou repetição $$(\dfrac{d(\epsilon)}{dt} \approx 10^{-5} /s)$$;  
4. Efeito de fluência é desconsiderado;  
5. Após a fissuração despreza-se, na seção transversal fissurada, a resistência à tração do concreto.  

<p style="text-align: justify;">Para obtenção do diagrama de momento-curvatura de uma viga é necessário primeiramente definir os pontos notáveis de mudança de estádio da peça. A seguir são descritos os passos para obtenção desse diagrama.</p>

### Passo 1: Determinação do limite entre o Estádio I e Estádio II

<p style="text-align: justify;">Primeiramente deve-se estabelecer o ponto de início do processo de fissuração na viga de concreto, que corresponde ao fim do Estádio I e início do Estádio II. Esse ponto de interesse é definido pelo cálculo do Momento Resistente conforme eq. 1. Considerando seções planas e as relações lineares entre as deformações pode obter a curvatura da barra conforme eq. 2.</p>

    
$$
(1)    M_{1} = M_{r} = \frac{\alpha.f_{ct,inf}.I_{I}}{y_{t}}
$$          
   
$$
(2)    \epsilon_{c} = \frac{f_{ct,inf}}{E_{ci}}
$$        
    
$$
(3)    \phi_{1} = \frac{\epsilon_{c}}{x_{I}}
$$        

Onde:
+ $$f_{ct,inf}$$: Resistência à tração inferior do concreto;
+ $$\alpha$$: Fator majorador da resistência à tração para seções. No caso de seção retangular $$\alpha = 1,50$$;
+ $$E_{ci}$$: Módulo de elasticidade tangente conforme Tabela 8.1 da NBR 6118 [2];
+ $$I_{I}$$ e $${y_{t}$$: Inércia da peça no Estádio I e distância da linha neutra ($$x_{I}$$) ao bordo mais tracionado.

<p style="text-align: justify;">As equações de determinação de inércia e linha neutra no Estádio I, com e sem consideração da armadura tracionada e/ou comprimida, podem ser encontradas em Carvalho e Figueiredo Filho [3] cap. 4.</p>

### Passo 2: Determinação da nova linha neutra para seção fissurada

<p style="text-align: justify;">Após o aumento da curvatura na peça de concreto começará a fissurar, logo deverá ser calculada uma nova posição da linha neutra conforme proposto em Carvalho e Figueiredo Filho [3] cap. 4, considerando agora as propriedades geométricas para uma seção fissurada.</p>

<p style="text-align: justify;">Determinada as propriedades geométricas de linha neutra e inércia para a nova condição (estado de fissuração) acontece uma singularidade instantânea no diagrama momento-curvatura. O diagrama de forças resistentes da seção passa a ser composto pelo concreto comprimido e o aço tracionado, lembrando aqui que a seção inferior de concreto passa a ser desprezada a partir desse ponto. Portanto o momento e a curvatura da seção são dadas pelas eq's. 4 e 5:</p>

$$
(4)   M_{2} = M_{r}
$$ 

$$
(5)  \phi_{2} = \frac{M_{r}}{E_{ci}.I_{II}}
$$  

### Passo 3: Aumento da curvatura e mudança no módulo de elasticidade do concreto

<p style="text-align: justify;">Uma outra seção de interesse é quando o concreto atinge cerca de 45% da sua resistência mecânica à compressão. Nesse ponto a linha neutra se manteve estável não alterando sua posição. Portanto é necessário avaliar a relação momento-curvatura para esta situação considerando a inércia fissurada da seção e mudança do módulo de elasticidade do concreto. As eq's. 6 a 8 apresentam o cálculo da curvatura e momento correspondente:</p>

$$
(6)  \epsilon_{c} = \frac{0,45.f_{ck}}{E_{cs}}
$$

$$
(7)   \phi_{3} = \frac{\epsilon_{c}}{x_{II}}
$$

$$
(8)    M_{3} = M_{r}.\frac{\phi_{3}}{\phi_{2}}
$$

<p style="text-align: justify;">Nessa fase é necessário checar se a tensão na armadura tracionada está em uma zona linear elástica para esse material. Para isso utiliza-se a relações entre deformação da seção, conforme eq. 9.</p>

$$
(9)     \epsilon_{s} = \epsilon_{c}.\frac{d-x_{II}}{x_{II}} \leq \epsilon_{y}
$$

### Passo 4: O escoamento da armadura

<p style="text-align: justify;">Com o sucessivo aumento da curvatura da peça é admitido que as armaduras entrem em processo de escoamento. Portanto nesse trecho a linha neutra da peça sofrerá uma nova alteração e para isso é necessário avaliar o equilíbrio de forças novamente, porém deve-se assumir que nesse estágio o concreto também possuirá um diagrama de comportamento não linear conforme descrito na seção 8.2.10.1 da NBR 6118 [2] e pela eq. 10.</p>

$$
(10)    \sigma_{c} = f_{ck}.[1-(1-\frac{\epsilon_{c,i}}{\epsilon_{c2}})^{2}]
$$ 

<p style="text-align: justify;">Para concreto do grupo 1 de resistência os valores das deformações da eq. 10 são:</p>  

+ $$\epsilon_{c2} = 0,002$$ e $$\epsilon_{cu} = 0,0035$$  

<p style="text-align: justify;">Portanto para obter as forças no concreto e o equilibrio da seção deverá ser considerado o diagrama apresentado na seção 8.2.10.1 relativo a curva tensão-deformação do concreto. No caso desse trabalho será utilizado a aproximação do diagrama parabola-retângulo permitida pela NBR 6118. Fazendo então as devidas aproximações, têm-se a equação de equilíbrio de forças normais é dado pela eq. 11:</p>

$$
(11)     \sigma_{c} = E_{cs}.\epsilon_{c,i}  
A_{s}.f_{y} = b_{w}.\int_{0}^{x}\sigma_{c} = b_{w}.0,80.x_{\epsilon y}.\sigma_{c}dy         
$$  

No caso a variável $$\epsilon_{c,i}$$ da eq. 10 será dada pela eq. 12. Na eq. 12 o valor de $$\epsilon_{y}$$ é igual a $$0,207%$$:

$$  
(12)      \epsilon_{c,i} = \epsilon_{y}.\frac{x_{\epsilon y}}{d-x_{\epsilon y}}  
$$  

<p style="text-align: justify;">Com as devidas manipulações algébricas consegue obter a nova posição da linha neutra considerando que as armaduras estão em processo de escoamento. Tal dado permite também obter a curvatura da peça.</p>

<p style="text-align: justify;">Com a posição da linha neutra é possível fazer o somatório de momentos na seção, conforme eq. 13.</p>

$$
(13)      M_{4} = A_{s}.f_{y}.(d-0.40.x_{\epsilon y})
$$

### Passo 5: Considerando que o concreto atinge o valor de $$f_{ck}$$ e plastifica completamente a seção comprimida

<p style="text-align: justify;">A partir desse ponto admite-se que o concreto atingiu o valor da resistência a compressão e então efetua-se o cálculo da nova posição da linha neutra da seção. Tomando como referência a eq. 11 obtém-se a eq. 14.</p>

$$
(14)      A_{s}.f_{y} = b_{w}.0,80.x_{\epsilon cu}.f_{ck}dy
$$  

Portanto determina-se o par momento-curvatura conforme eq's. 15 e 16:

$$
(15)      \phi_{5} = \frac{\epsilon_{cu}}{x_{\epsilon cu}}
$$  

$$
(16)      M_{5} = A_{s}.f_{y}.(d-0.40.x_{\epsilon cu})
$$

### Passo 6: Plotagem do diagrama Momento-Curvatura

<p style="text-align: justify;">Após a determinação de todos os pares ordenados nos 5 passos é possível obter o diagrama momento curvatura da viga analisada.</p>

### Viga 2$$\phi$$12.5 mm

[notebook Jupyter - Solução viga 1](https://nbviewer.jupyter.org/github/wmpjrufg/SET5963-EESC/blob/gh-pages/Trabalho3-viga1.ipynb)

### Viga 5$$\phi$$32.00 mm

[notebook Jupyter - Solução viga 2](https://nbviewer.jupyter.org/github/wmpjrufg/SET5963-EESC/blob/gh-pages/Trabalho3-viga2.ipynb)

### Referências

1. <p style="text-align: justify;">BUCHAIM, R. A influência da não-linearidade física do concreto armado na rigidez à flexão e na capacidade de rotação plástica. Tese de Doutorado em Engenharia de Estruturas. Universidade de São Paulo (USP), 2001.</p>

2. <p style="text-align: justify;">ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS (ABNT). NBR 6118 Projeto de Estruturas de Concreto - Procedimento, Rio de Janeiro, 2014.</p>

3. <p style="text-align: justify;">CARVALHO, R. C. FIGUEIREDO FILHO, J R. Cálculo e Detalhamento de Estruturas Usuais de Concreto Armado: Segundo a NBR 6118:2014. Editora EduFSCar, 4º edição, São Carlos, 2014.</p>
