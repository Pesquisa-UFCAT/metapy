<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h1>Knapsack problem</h1>

<h2>Theory</h2>

<p align = "justify">
The Knapsack Problem is a combinatorial optimization problem that consists of choosing, from a set of objects, those that should be placed inside a knapsack considering that it has a limited capacity (\(c_{max}\)).
<br><br>
Thus, given a set of \(N\) objects, where object \(i\) has a monetary value \(V_i\) and a weight \(P_i\), what is the combination of objects that maximizes the total value of items contained in the knapsack given a maximum storage capacity of \(c_{max}\)? Mathematically, the knapsack problem can be written as equation (1):
</p>

<table style = "width:100%">
    <tr>
        <td>max \[\symbf{x}_{i,k}^{t+1} = \symbf{x}_{i,k}^{t} + \symbf{\beta}.(\symbf{x}_{j,k}^{t} - \symbf{x}_{i,k}^{t}) + \alpha.(\symbf{rand} - 0.50)\]</td>
        <td><p align = "right">(1)</p></td>
    </tr>
</table>

<p align = "justify">
Where \(\symbf{x}_{i}\) are nonnegative integer-valued decision variables.
</p>

<h2>Numerical example</h2>

<p align = "justify">
The Knapsack Problem is a combinatorial optimization problem that consists of choosing, from a set of objects, those that should be placed inside a knapsack considering that it has a limited capacity (\(C_{max}\)).
<br><br>
Thus, given a set of \(N\) objects, where object i has a monetary value \(V_i\) and a weight \(P_i\), what is the combination of objects that maximizes the total value of items contained in the knapsack given a maximum storage capacity of \(C_{max}\)? Mathematically, the knapsack problem can be written as equation (1):
</p>