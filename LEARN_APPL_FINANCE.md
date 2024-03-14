---
layout: default
title: Finance problem
parent: Applications
grand_parent: Learning
nav_order: 2
has_children: false
has_toc: false
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>Inverse problem</h3>

<br>

<p align = "justify">
In this application, the optimization technique is used to minimize the deviation between the numerical results and the ones observed experimentally <a href="#ref1">[1]</a>, where the Objective Function (OF) is given by equation <a href="#eq1">(1)</a>.
</p>

<table border = "0" style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ min \left| \mathbf{y}_{\text{true}} - \mathbf{y}_{\text{pred}} \right| \]</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
</table>

<p align = "justify">
The section <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/STATS_LOSS.html">"loss"</a> shows some loss equations implemented in the METApy framework.
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
            <td><p align = "left"><a href="https://link.springer.com/article/10.1007/s13369-022-07132-6" target="_blank" rel="noopener noreferrer">Pereira Junior, W.M.; Borges, R.A.; Araújo, D.L; Fernandes, G. R.; Pituba, J. J. C. (2023). Parametric Identification and Sensitivity Analysis Combined with a Damage Model for Reinforced Concrete Structures. Arab J Sci Eng 48, 4751–4767</a></p></td>
        </tr>
    </tbody>
</table>