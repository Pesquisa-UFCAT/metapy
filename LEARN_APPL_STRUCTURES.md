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


<h3>Finance problem</h3>

<br>

<p align = "justify">
O problema do portfólio envolve a alocação ideal de recursos em uma variedade de ativos que compõem uma carteira de investimentos. Em um contexto financeiro, o desafio reside na seleção ótima de investimentos para maximizar os retornos e minimizar os riscos <a href="#ref1">[1]</a>.
<br><br>
Baseado na premissa de que a diversificação de ativos pode reduzir os riscos, o renomado economista Harry Markowitz desenvolveu, em 1952, um dos modelos mais influentes para a gestão de portfólios financeiros: o Modelo de Média-Variância <a href="#ref2">[2]</a>. Este modelo busca construir uma carteira que ofereça o menor risco possível.
No modelo de Markowitz o retorno é determinado em função do histórico de preço dos ativos S<sub>1</sub>, S<sub>2</sub>, ..., S<sub>n</sub>. O retorno é representado pela equação <a href="#eq1">(1)</a>.
</p>

<table border = "0" style = "width:100%">
    <tr>
        <td style="width: 90%;">&sum;<sup>n</sup><sub>i=1</sub> X<sub>i</sub> &mu;<sub>i</sub></td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
</table>
<p align = "justify">
    Onde: <br>
    X<sub>i</sub> : peso dos ativos<br>
    &mu;<sub>i</sub> : média do retorno diário dos ativos<br> 
    <p>No modelo de Markowitz o risco é dado pela variância do portfólio conforme a equação <a href="#eq2">(2)</a>. </p>
</p>

<table border = "0" style = "width:100%">
    <tr>
        <td style="width: 90%;">&sum;<sup>n</sup><sub>i=1</sub>&sum;<sup>n</sup><sub>j=1 &#963</sub> X<sub>i</sub> X;<sub>j</sub></td>
        <td style="width: 10%;"><p align = "right" id = "eq2">(2)</p></td>
    </tr>
</table>

<p align = "justify">
    Onde: <br>
    &#963<sub>ij</sub>: covariância dos ativos i e j <br>      
    X<sub>i</sub> : peso do ativo i <br>
    X<sub>j</sub> : peso do ativo j<br>
</p>

<h3>Algorithm</h3>

<p align = "justify">
The section <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/STATS_LOSS.html">"loss"</a> shows some loss equations implemented in the METApy framework.
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
            <td><p align = "center" id = "ref1">[1]</p></td>
            <td><p align = "left"><a href= "https://ieeexplore.ieee.org/document/9043547" target="_blank" rel="noopener noreferrer">AH Khan et al ., "Optimal Portfolio Management for Engineering Problems Using Nonconvex Cardinality Constraint: A Computing Perspective," em IEEE Access , vol. 8, pp. 57437-57450, 2020.</a></p></td>
        </tr>
                <tr>
            <td><p align = "center" id = "ref1">[2]</p></td>
            <td><p align = "left"><a href="https://www.jstor.org/stable/2975974?origin=crossref" target="_blank" rel="noopener noreferrer"> Markowitz, Harry. “Portfolio Selection.” The Journal of Finance, vol. 7, no. 1, 1952, pp. 77–91. JSTOR. </a></p></td>
        </tr>
    </tbody>
</table>
