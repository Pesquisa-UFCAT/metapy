---
layout: default
title: Structure Problem
parent: Applications
grand_parent: Learning
nav_order: 3
has_children: false
has_toc: false
---

<!--Don't delete this script-->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete this script-->

<h3>Problema estrutural</h3>
<br>

<p align="justify">
    Os problemas do portfólio envolvem a otimização estrutural, área amplamente utilizada na solução de problemas como benchmark, onde a eficácia dos algoritmos desenvolvidos deve ser posta à prova. É importante ressaltar que, em basicamente toda engenharia estrutural, a determinação dos melhores valores para cada um dos parâmetros é algo inerente. Dito isto, objetivos e restrições de projeto são não lineares, envolvendo assim diversas variáveis de projeto.
</p>

<p align="justify">
    Segundo Gandomi (2011) <a href="#ref1">[1]</a>, o campo da otimização estrutural é uma área que passa por rápidas mudanças em termos de metodologia e ferramentas de design. Assim, é altamente necessário resumir alguns problemas para otimização estrutural. Neste portfólio, foram resolvidos problemas de viga soldada, viga de concreto armado, mola de compressão, vaso de pressão, redutor de velocidade e viga cantilever escalonada.
</p>

<h4>Viga soldada</h4>

<p align="justify">
    Uma questão de engenharia estrutural muito importante é minimizar o custo total de projeto para uma viga soldada. Este é o intuito do problema a seguir. A Figura XX ilustra uma viga de aço de baixo carbono (C-1010) que foi soldada em um suporte rígido.
</p>

<p align="justify">
    As variáveis de projeto devem ser determinadas para suportar uma carga P, são elas:
</p>

<ul>
    <li>h: espessura da solda;</li>
    <li>l: comprimento da junta soldada;</li>
    <li>t: largura da viga;</li>
    <li>b: espessura da viga.</li>
</ul>

<p align="justify">
    A função objetivo deste problema é expressa na Equação <a href="#eq1">(1)</a>.
</p>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[OF=(1+C_{1})h^2\times l+C_{2}\times t\times b(L+l)\]</td>
        <td class="number"><p id="eq1">(1)</p></td>
    </tr>
</table>

<p align="justify">
    Assim como todos problemas de otimização estrutural, a determinação dos melhores valores de cada parâmetro está sujeita a restrições. Neste caso, há cinco delas:
</p>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[g_{1} = \tau_{d}\ - \tau\geq 0\]</td>
        <td class="number"><p id="eq2">(2)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{2} = \sigma_{d} - \sigma\geq 0\]</td>
        <td class="number"><p id="eq3">(3)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{3} = b - h\geq 0\]</td>
        <td class="number"><p id="eq4">(4)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{4} = P_{c} - P \geq 0\]</td>
        <td class="number"><p id="eq5">(5)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{5} = 0.25 - \delta\geq 0\]</td>
        <td class="number"><p id="eq6">(6)</p></td>
    </tr>
</table>

<p align="justify">
    Onde:
</p>

<table border="0">
    <tr>
        <td align="left">\[
        \tau = \sqrt{\frac{\tau_{1}^2 + \tau_{2}^2 + l\tau_{1}\tau_{2}}{\sqrt{0.25(l^2 + (h + t)^2)}}}
        \]</td>
        <td class="number"><p id="eq7">(7)</p></td>
    </tr>
    <tr>
        <td align="left">\[
        \tau_{d} = 13600 \, \text{psi}
        \]</td>
        <td class="number"><p id="eq8">(8)</p></td>
    </tr>
    <tr>
        <td align="left">\[
        \tau_{1} = \frac{6000}{\sqrt{2}hl}
        \]</td>
        <td class="number"><p id="eq9">(9)</p></td>
    </tr>
    <tr>
        <td align="left">\[
        \tau_{2} = \frac{6000(14 + 0.5l)\sqrt{0.25(l^2 + (h + t)^2)}}{2(0.707hl)\left(\frac{l^2}{12} + 0.25(h + t)^2\right)}
        \]</td>
        <td class="number"><p id="eq10">(10)</p></td>
    </tr>
    <tr>
        <td align="left">\[
        \delta = \frac{2.1952}{t^{3}b}
        \]</td>
        <td class="number"><p id="eq11">(11)</p></td>
    </tr>
    <tr>
        <td align="left">\[
        P_{c} = 64746(1-0.0282346t)tb^{3}
        \]</td>
        <td class="number"><p id="eq12">(12)</p></td>
    </tr>
</table>

<h4>Viga de concreto armado</h4>

<p align="justify">
    No caso de uma viga de concreto armado, o objetivo não é diferente, sendo o custo total o intuito a ser minimizado. A Figura XX ilustra a viga em questão. 
</p>

<p align="justify">
    As variáveis de projeto neste caso são:
</p>

<ul>
    <li>As: área de armadura;</li>
    <li>b: largura da viga;</li>
    <li>h: profundidade da viga;</li>
</ul>

<p align="justify">
    A função objetivo deste problema é expressa na Equação <a href="#eq1">(13)</a>.
</p>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[OF=29.4\times A_{s}+0.6bh\]</td>
        <td class="number"><p id="eq13">(13)</p></td>
    </tr>
</table>

<p align="justify">
    As restrições são:</a>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[g_{1} = \frac{h}{b}-4\leq 0\]</td>
        <td class="number"><p id="eq14">(14)</p></td>
    </tr>
    <tr>
        <td align="left">\[M_{u}=0.9A_{s}F_{y}(0.8h)(1.0-0.59\frac{A_{s}F_{y}}{0.8bh\sigma _{c}})\geq 1.4M_{d}+1.7M_{l}\]</td>
        <td class="number"><p id="eq15">(15)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{2} = 180+7.375\frac{A_{s}}{b}-A_{s}h\leq 0\]</td>
        <td class="number"><p id="eq16">(16)</p></td>
    </tr>
    <tr>
</table>

Onde:
</p>

<table border="0">
    <tr>
        <td align="left">\( M_{u} \) = Resistência à flexão;</td>
   </tr>
    <tr>
        <td align="left">\( M_{d} \) = Carga permanente;</td>
    </tr>
    <tr>
        <td align="left">\( M_{l} \) = Momentos de carga dinâmica;</td>
    </tr>
</table>

<h4>Mola de compressão</h4>

<p align="justify">
    Problemas que envolvem uma mola de compressão possuem muitas variações e são estudados por diversos pesquisadores. Neste caso, o objetivo de minimização é o peso da mola, a Figura XX demonstra uma mola de compressão com três variáveis de projeto, são elas:
</p>

<ul>
    <li>d: diâmetro do fio;</li>
    <li>D: diâmetro médio da bobina;</li>
    <li>N: número de bobinas ativas;</li>
</ul>

<p align="justify">
    A função objetivo deste problema é expressa na Equação <a href="#eq1">(17)</a>.
</p>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[OF=(N+2)\times Dd^{2}\]</td>
        <td class="number"><p id="eq1">(17)</p></td>
    </tr>
</table>

<p align="justify">
    As restrições deste problema são:</a>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[g_{1}=1 - \frac{D^3 N}{71785 d^4}\leq 0\]</td>
        <td class="number"><p id="eq18">(18)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{2}=\frac{4 D^2 - D d}{12566 (D d^3 - d^4)} + \frac{1}{510} d^2 - 1\leq 0\]</td>
        <td class="number"><p id="eq19">(19)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{3}=1 - \frac{140.45 d}{D^2 N}\leq 0\]</td>
        <td class="number"><p id="eq20">(20)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{4}=\frac{D + d}{1.5} - 1\leq 0\]</td>
        <td class="number"><p id="eq21">(21)</p></td>
    </tr>
    <tr>
</table>

<h4>Vaso de pressão</h4>

<p align="justify">
    Vasos de pressão podem ser definidos como um recipiente em que gases e líquidos estão presentes em seu interior. Normalmente, este conteúdo está sujeito a uma pressão significantemente maior em relaçao ao ambiente exterior. A Figura XX ilustra um vaso de pressão cilíndrico onde ambas as extremidades estão tampadas por cabeças esféricas.
</p>
<p align="justify">  
    Este tipo de recipiente é amplamente utilizado na engenharia e, além disso, apresenta um alto custo de fabricação, então o objetivo aqui é a minimização deste custo.
</p>
<p align="justify">  
    As variáveis de projeto neste caso são as seguintes:
</p>

<ul>
    <li>\( T_{s} \): espessura da casca;</li>
    <li>\( T_{h} \): espessura da cabeça;</li>
    <li>R: raio interno;</li>
    <li>L: comprimento da seção cilíndrica;</li>
</ul>

<p align="justify">
    A função objetivo deste problema é expressa na Equação <a href="#eq1">(22)</a>.
</p>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[OF=(0.6224 T_s R L) + (1.7781 T_h R^2) + (3.1661 T_s^2 L) + (19.84 T_h^2 L)\]</td>
        <td class="number"><p id="eq22">(22)</p></td>
    </tr>
</table>

<p align="justify">
    As restrições deste problema são:</a>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[g_{1}=-T_s + 0.0193 R\leq 0\]</td>
        <td class="number"><p id="eq23">(23)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{2}=-T_h + 0.0095 R \leq 0\]</td>
        <td class="number"><p id="eq24">(24)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{3}=-\pi R^2 L - \frac{4}{3} \pi R^3 + 1296000\leq 0\]</td>
        <td class="number"><p id="eq25">(25)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{4}=L - 240\leq 0\]</td>
        <td class="number"><p id="eq26">(26)</p></td>
    </tr>
    <tr>
</table>

<h4>Redutor de velocidade</h4>

<p align="justify">
  Redutores de velocidade são utilizados em diversos tipos de aplicações e, portanto, é bastante útil trabalhar em uma otimização. Aqui, o objetivo de minimização é o peso total do redutor de velocidade, no entanto, esta não é uma tarefa simples, pois para tal, é necessário trabalhar com sete variáveis de projeto. São elas: 
</p>

<ul>
    <li>b: largura da face;</li>
    <li>m: módulo dos dentes;</li>
    <li>z: número de dentes no pinhão;</li>
    <li>l1: comprimento do primeiro eixo entre os rolamentos;</li>
    <li>l2: comprimento do segundo eixo entre os rolamentos;</li>
    <li>d1: diâmetro do primeiro eixo;</li>
    <li>d2: diâmetro do segundo eixo;</li>
</ul>

<p align="justify">
    A função objetivo deste problema é expressa na Equação <a href="#eq1">(27)</a>.
</p>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[OF=0.7854 b m^2 (3.3333 z^2 + 14.9334 z - 43.0934) - 1.508 b (d_1^2 + d_2^2) + 7.477 (d_1^3 + d_2^3) + 0.7854 (l_1 d_1^2 + l_2 d_2^2)\]</td>
        <td class="number"><p id="eq27">(27)</p></td>
    </tr>
</table>

<p align="justify">
    As restrições deste problema são:</a>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[g_{1}=\frac{27}{b m^2 z} - 1\leq 0\]</td>
        <td class="number"><p id="eq28">(28)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{2}=\frac{397.5}{b m^2 z^2} - 1\leq 0\]</td>
        <td class="number"><p id="eq29">(29)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{3}=\frac{1.93 l_1^3}{m z d_1^4} - 1\leq 0\]</td>
        <td class="number"><p id="eq30">(30)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{4}=\frac{1.93 l_2^3}{m z d_2^4} - 1\leq 0\]</td>
        <td class="number"><p id="eq31">(31)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{5}=\frac{\sqrt{\left(\frac{745 l_1}{m z}\right)^2 + 16.9 \times 10^6}}{110 d_1^3} - 1\leq 0\]</td>
        <td class="number"><p id="eq32">(32)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{6}=\frac{\sqrt{\left(\frac{745 l_2}{m z}\right)^2 + 157.5 \times 10^6}}{85 d_2^3} - 1\leq 0\]</td>
        <td class="number"><p id="eq33">(33)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{7}=\frac{m z}{40} - 1\leq 0\]</td>
        <td class="number"><p id="eq34">(34)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{8}=\frac{5 m}{b} - 1\leq 0\]</td>
        <td class="number"><p id="eq35">(35)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{9}=\frac{b}{12 m} - 1\leq 0\]</td>
        <td class="number"><p id="eq36">(36)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{10}=\frac{1.5 d_1 + 1.9}{l_1} - 1\leq 0\]</td>
        <td class="number"><p id="eq37">(37)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{11}=\frac{1.1 d_2 + 1.9}{l_2} - 1\leq 0\]</td>
        <td class="number"><p id="eq38">(38)</p></td>
    </tr>
    <tr>
      
</table>

<h4>Viga cantilever escalonada</h4>

<p align="justify">
  Este é um problema em que há a presença de várias variáveis de projeto, dentre os problemas apresentados é o mais desafiador em quesitos de benchmark. Aqui, o objetivo de minimização é o volume de uma viga cantilever escalonada.
</p>

<p align="justify">
  As variáveis de projeto aqui são as larguras, alturas e comprimentos da viga em todas as cinco etapas, como demonstrado na Figura XX
</p>

<p align="justify">
    A função objetivo deste problema é expressa na Equação <a href="#eq39">(39)</a>.
</p>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[OF=(b_{1} h_{1} l_{1}) + (b_{2} h_{2} l_{2}) + (b_{3} h_{3} l_{3}) + (b_{4} h_{4} l_{4}) + (b_{5} h_{5} l_{5})\]</td>
        <td class="number"><p id="eq39">(39)</p></td>
    </tr>
</table>

<p align="justify">
    As restrições neste caso são dadas por:</a>

<table border="0" style="width:100%">
    <tr>
        <td align="left">\[g_{1}=\left(\frac{6 P l_5}{b_5 h_5^2}\right) - \sigma_d\leq 0\]</td>
        <td class="number"><p id="eq40">(40)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{2}=\left(\frac{6 P (l_5 + l_4)}{b_4 h_4^2}\right) - \sigma_d\leq 0\]</td>
        <td class="number"><p id="eq41">(41)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{3}=\left(\frac{6 P (l_5 + l_4 + l_3)}{b_3 h_3^2}\right) - \sigma_d\leq 0\]</td>
        <td class="number"><p id="eq42">(42)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{4}=\left(\frac{6 P (l_5 + l_4 + l_3 + l_2)}{b_3 h_2^2}\right) - \sigma_d\leq 0\]</td>
        <td class="number"><p id="eq43">(43)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{5}=\left(\frac{6 P (l_5 + l_4 + l_3 + l_2 + l_1)}{b_1 h_1^2}\right) - \sigma_d\leq 0\]</td>
        <td class="number"><p id="eq44">(44)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{6}=\frac{PL^{3}}{3E}(\frac{1}{l_5} + \frac{7}{l_4} + \frac{19}{l_3} + \frac{37}{l_2} + \frac{61}{l_1}) - \Delta _m\leq 0\]</td>
        <td class="number"><p id="eq45">(45)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{7}=\frac{h_5}{b_5} - 20\leq 0\]</td>
        <td class="number"><p id="eq46">(46)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{8}=\frac{h_4}{b_4} - 20\leq 0\]</td>
        <td class="number"><p id="eq47">(47)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{9}=\frac{h_3}{b_3} - 20\leq 0\]</td>
        <td class="number"><p id="eq48">(48)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{10}=\frac{h_2}{b_2} - 20\leq 0\]</td>
        <td class="number"><p id="eq49">(49)</p></td>
    </tr>
    <tr>
        <td align="left">\[g_{11}=\frac{h_1}{b_1} - 20\leq 0\]</td>
        <td class="number"><p id="eq50">(50)</p></td>
    </tr>
    <tr>
       
</table>

Onde:
</p>

<table border="0">
    <tr>
        <td align="left">P = Carga aplicada na ponta da viga;</td>
   </tr>
    <tr>
        <td align="left">E = Módulo de elasticidade do concreto;</td>
    </tr>
    <tr>
        <td align="left">L = Comprimento total da viga;</td>
    </tr>
    <tr>
       <td align="left">\( \sigma \) = Tensão de flexão admissível;</td>
    </tr>
    <tr>
       <td align="left">\( \Delta _m \) = Deslocamento admissível;</td>
    </tr>
</table>

</p>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Reference</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><p align="center" id="ref1">[1]</p></td>
            <td><p align="left"><a href="https://link.springer.com/chapter/10.1007/978-3-642-20859-1_12" target="_blank" rel="noopener noreferrer">Gandomi, A. H., & Yang, X.-S. (2011). Benchmark Problems in Structural Optimization. Studies in Computational Intelligence, 259–281. doi:10.1007/978-3-642-20859-1_12.</a></p></td>
        </tr>
    </tbody>
</table>
