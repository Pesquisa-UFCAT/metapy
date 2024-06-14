---
layout: default
title: Structure Problem
parent: Applications
grand_parent: Learning
nav_order: 3
has_children: false
has_toc: false
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->


<h3>Problema Estrutural</h3>

<br>

<p align = "justify">
Os problemas do portfólio envolvem a otimização estrutural, área amplamente utilizada na solução de problemas como benchmark, onde a eficácia dos algoritmos desenvolvidos devem ser postos à prova. É importante resaltar que, em basicamente toda engenharia estrutural, a determinação dos melhores valores para cada um dos parâmetros é algo inerente, dito isto, objetivos e restrições de projeto são não lineares, envolvendo assim diversas variáveis de projeto</a>.
<br><br>
Segundo Gandomi (2011) <a href="#ref1">[1]</a>, o campo da otimização estrutural é uma área que passa por rápidas mudanças em termos de metodologia e ferramentas de design. Assim, é altamente necessário resumir alguns problemas para otimização estrutural. Neste portfólio, foram resolvidos problemas de viga soldada, viga de concreto armado, mola de compressão, vaso de pressão, redutor de velocidade e viga cantilever escalonada.

<h4>Viga soldada</h4>

Um questão de engenharia estrutural muito importante é minimizar o custo total de projeto para uma viga soldada. Este é o intuito do problema a seguir. A Figura XX ilustra uma viga de aço de baixo carbono (C-1010) que foi soldada em um suporte rígido.

Figura XX

As variáveis de projeto devem ser determinadas para suportar uma carga P, são elas:

h: espessura da solda; </p> 
l: comprimento da junta soldada; </p> 
t: largura da viga; e </p> 
b: espessura da viga.

A função objetivo deste problema é expressa na Equação <a href="#eq1">(1)</a>.

<table border = "0" style = "width:100%">
    <tr>
        <td class="equation">OF = (1 + c<sub>1</sub>)h<sup>2</sup>l + c<sub>2</sub>t b (L + l)</td>
        <td class="number"><p id="eq1">(1)</p></td>
    </tr>
</table>

Assim como todos problemas de otimização estrutural, a determinação dos melhores valores de cada parâmetro estão sujeitos a restrições, neste caso, há cinco delas:

<table border = "0" style = "width:100%">
   <tr>
        <td class="equation">G<sub>1</sub> = &tau; - &tau;<sub>d</sub></td>
        <td class="number"><p id="eq2">(2)</p></td>
    </tr>
    <tr>
        <td class="equation">G<sub>2</sub> = &sigma; - &sigma;<sub>d</sub></td>
        <td class="number"><p id="eq3">(3)</p></td>
    </tr>
    <tr>
        <td class="equation">G<sub>3</sub> = h - b</td>
        <td class="number"><p id="eq4">(4)</p></td>
    </tr>
    <tr>
        <td class="equation">G<sub>4</sub> = P - P<sub>c</sub></td>
        <td class="number"><p id="eq5">(5)</p></td>
    </tr>
    <tr>
        <td class="equation">G<sub>5</sub> = &delta; - 0.25</td>
        <td class="number"><p id="eq6">(6)</p></td>
    </tr>
</table>
<p align = "justify">
   Onde:
<table border="0">
    <tr>
        <td class="equation">
            τ = √(((τ<sub>1</sub>)<sup>2</sup> + (τ<sub>2</sub>)<sup>2</sup> + l &times; τ<sub>1</sub> &times; τ<sub>2</sub>) /
            (√(0.25 &times; (l<sup>2</sup> + (h + t)<sup>2</sup>))))
        </td>
        <td class="number"><p id="eq9">(9)</p></td>
    </tr>
    <tr>
        <td class="equation">
            τ<sub>d</sub> = 13600 psi
        </td>
        <td class="number"><p id="eq10">(10)</p></td>
    </tr>
    <tr>
        <td class="equation">
            τ<sub>1</sub> = 6000 / (√(2) &times; h &times; l)
        </td>
        <td class="number"><p id="eq7">(7)</p></td>
    </tr>
    <tr>
        <td class="equation">
            τ<sub>2</sub> = (6000 &times; (14 + 0.5 &times; l) &times; √(0.25 &times; (l<sup>2</sup> + (h + t)<sup>2</sup>))) /
            (2 &times; (0.707 &times; h &times; l) &times; (l<sup>2</sup> / 12 + 0.25 &times; (h + t)<sup>2</sup>))
        </td>
        <td class="number"><p id="eq8">(8)</p></td>
    </tr>
</table>

<h4>Viga de concreto armado</h4>







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
            <td><p align = "left"><a href= "https://link.springer.com/chapter/10.1007/978-3-642-20859-1_12" target="_blank" rel="noopener noreferrer">Gandomi, A. H., & Yang, X.-S. (2011). Benchmark Problems in Structural Optimization. Studies in Computational Intelligence, 259–281. doi:10.1007/978-3-642-20859-1_12.</a></p></td>
        </tr>
