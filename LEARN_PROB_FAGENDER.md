---
layout: default
title: Gender Firefly
parent: Probabilistic
grand_parent: Learning
nav_order: 6
has_children: true
has_toc: true
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>Theory</h3>

<br>

<p align = "justify">
O algoritmo de Firefly aprimorado com base nas diferenças de gênero e sua convergência é uma extensão do algoritmo de Firefly original, que introduz uma abordagem baseada em gênero para melhorar a exploração do espaço de busca e a convergência para soluções ótimas. Este algoritmo reflete o processo de interação entre fireflies, onde fireflies mais brilhantes (com soluções melhores) são atraídos para fireflies menos brilhantes (com soluções piores), resultando em um movimento em direção a soluções ótimas <a href="#ref1">[1]</a>.
<br><br>
Nesta versão aprimorada do algoritmo de firefly, a população é segmentada em dois subgrupos distintos: fireflies masculinos e femininos <a href="#ref1">[1]</a>.
<br><br>
Na dinâmica aprimorada do algoritmo de firefly, os fireflies masculinos selecionam de forma aleatória duas fireflies femininas para atualizar suas posições. Para isso, dois fatores discriminantes são empregados para orientar o movimento desses fireflies masculinos <a href="#ref1">[1]</a>.
<br><br>
 Já as fireflies femininas direcionam-se em direção à firefly masculina mais luminosa. Tal abordagem as conduz a explorar regiões da solução em busca de ótimas soluções, contribuindo para aprimorar a qualidade do resultado final <a href="#ref1">[1]</a>. 
<br><br>
Nesta versão, foram propostas duas fórmulas de busca distintas para os dois subgrupos. Uma dessas fórmulas prioriza a busca global, enquanto a outra foca na busca local <a href="#ref1">[1]</a>.
<br><br>
A fórmula de atualização é determinada pelo modo de movimento das fireflies. A intensidade luminosa de cada firefly é ajustada de acordo com a qualidade da solução que ela representa. Para os fireflies machos, eles selecionam aleatoriamente duas fireflies fêmeas para atualizar sua posição (equação <a href="#eq2">[2]</a>),enquanto as fireflies fêmeas ajustam suas posições movendo-se em direção ao melhor firefly macho, (equação <a href="#eq3">[3]</a>).  
</p>

<h3>Position update formula of male firefly</h3>

<p align = "justify">
A fórmula de atualização do firefly macho foi concebida para realizar uma busca global, explorando todo o espaço disponível. Cada firefly macho (representado por X<sub>i</sub>)  seleciona aleatoriamente duas fêmeas (Y<sub>k</sub>, Y<sub>j</sub>). Dois fatores discriminantes (d<sub>1</sub>,d<sub>2</sub>)  são calculados com base na comparação do brilho entre o firefly macho e as duas fêmeas, determinando se o movimento será em direção às fêmeas no espaço de busca ou para longe delas. Veja a equação  <a href="#eq1">[1]</a>.
<br><br>
 Ao comparar a intensidade luminosa entre os fireflies macho e fêmea, o fator discriminante é atribuído com valores distintos. Se o valor da função y<sub>k</sub> for menor que o valor de x<sub>i</sub>, o primeiro fator discriminante d<sub>1</sub> é estabelecido como 1; caso contrário, é definido como -1. A configuração de d<sub>2</sub> segue a mesma lógica do d<sub>1</sub> <a href="#ref1">[1]</a>.

<table border = "0" style = "width:100%">
    <tr>
        <td style="width: 90%;">d = {<sup>1</sup><sub>-1</sub> f (y) < f (x)
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
</table>

<p align = "justify">
Observando a equação <a href="#eq1">[1]</a> é evidente que a firefly macho voará em direção à firefly fêmea selecionada quando a qualidade da solução feminina exceder a do macho. Caso contrário, eles se afastarão em busca de outro espaço. Com base nessa análise, a fórmula de atualização das fireflies machos é derivada da seguinte maneira:  &lambda; e &mu; representam números aleatórios no intervalo [0, 1], enquanto a atratividade entre duas fireflies é calculada pela equação <a href="#eq4">[4]</a>. &beta;<sub>1</sub> denota a atratividade entre x<sub>i</sub> e y<sub>k</sub>, e &beta;<sub>2</sub> é a atratividade entre x<sub>i</sub> e y<sub>j</sub> <a href="#ref1">[1]</a>. Consulte a fórmula de atualização da firefly macho na equação <a href="#eq2">[2]</a>. 
</p>

<table border = "0" style = "width:100%">
    <tr>
        <td style="width: 90%;">x<sub>i</sub><sup>t+1</sup> = x<sub>i</sub><sup>t</sup> + d<sub>1</sub>&beta;<sub>1</sub>&lambda; (y<sub>k</sub><sup>t</sup> - x<sub>i</sub><sup>t</sup>) +d<sub>2</sub>&beta;<sub>2</sub>&mu; (y<sub>j</sub><sup>t</sup> - x<sub>i</sub><sup>t</sup>) 
        <td style="width: 10%;"><p align = "right" id = "eq2">(2)</p></td>
    </tr>
</table>

<h3>Position update formula of male firefly</h3>
<p align = "justify">
A firefly fêmea é direcionada pelo firefly macho mais brilhante, para atualizar sua posição no espaço de busca <a href="#ref1">[1]</a>. Essa dinâmica permite que as fireflies fêmeas se desloquem estrategicamente em direção às regiões mais promissoras do espaço de solução, colaborando assim para o aprimoramento do processo de busca. Consulte a fórmula de atualização da firefly fêmea na equação <a href="#eq3">[3]</a>.
</p>
<table border = "0" style = "width:100%">
    <tr>
        <td style="width: 90%;">y<sub>i</sub><sup>t+1</sup> = y<sub>i</sub><sup>t</sup> + &beta;&phi; (X<sub>best</sub><sup>t</sup> - y<sub>i</sub><sup>t</sup>)  
        <td style="width: 10%;"><p align = "right" id = "eq3">(3)</p></td>
    </tr>
</table>

<p align = "justify">
Na equação <a href="#eq3">[3]</a> x<sub>best</sub> representa o firefly macho mais luminoso, &beta;  é o fator de atração entre y<sub>i</sub> e x<sub>best</sub>, e &phi; é um número aleatório em [0, 1]. Durante o processo de atualização, ambos os subgrupos desempenham papéis específicos: os fireflies machos se dedicam à busca global, enquanto as fêmeas de vaga-lume focam na busca local. No entanto, nenhum deles pode, por si só, alcançar soluções altamente precisas de maneira eficiente. Assim, através da cooperação entre fireflies machos e fêmeas, o algoritmo aprimorado é capaz de equilibrar melhor a exploração e a explotação, resultando em uma estratégia de busca mais eficaz <a href="#ref1">[1]</a>.
</p>


<h3>The attractiveness of each firefly </h3>

<p align = "justify">
A atratividade de cada firefly é determinada da seguinte maneira:
</p>
<table border = "0" style = "width:100%">
    <tr>
        <td style="width: 90%;">&beta;<sub>(r)</sub> = &beta;<sub>0</sub> e <sup>&gamma; r</sup><sup><sup>2</sup></sup>   
        <td style="width: 10%;"><p align = "right" id = "eq4">(4)</p></td>
    </tr>
</table>
<h3>Algorithm</h3>

```python
1:  Input initial parameters (p_c, p_m, n_population,n_iteration, x_lower, x_upper, fit_function, obj_function, n_dimensions)
2:  Input initial guess (x_pop)
3:  Calculate of and fit (initial population)
4:  for iter in range(n_iterations):
5:      Apply selection operator
6:      r = random number [0,1]
7:      if r <=p_c: 
8:         Apply crossover operator
9:      r = random number [0,1]
10:     if r <= p_m:              
11:        Apply mutation operator
12:     if fit(x_temp) > fit(x_pop):
13:        x_pop(iter+1) = x_temp
14:     else:
15:        x_pop(iter+1) = x_pop(iter)
```

<p align = "justify">
See <a href="https://wmpjrufg.github.io/METAPY/FRA_GA_GA.html" target="_blank">GA algorithm</a> in METApy Framework.
</p>


<h3>Reference list</h3>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Reference</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><p align = "center" id = "ref1">[1]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1016/j.asoc.2019.03.010" target="_blank" rel="noopener noreferrer">Chun-Feng Wang, Wen-Xin Song, A novel firefly algorithm based on gender difference and its convergence,Applied Soft Computing, Volume 80, 2019, Pages 107-124, ISSN 1568-4946,/a></p></td>
        </tr>
    </tbody>
</table>


# Logistic chaos map: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8977567