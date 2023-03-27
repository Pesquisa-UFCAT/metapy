<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h1>Benchmarks and other functions</h1>

<p align = "justify">
In the METApy environment you can use predefined functions to speed up your study.
</p>

<h2>Loss function</h2>

<p align = "justify">
The purpose of loss functions is to compute the quantity that a model should seek to minimize during optimization.
</p>


<h2><b><code>RESIDUALS</code></b></h2>
<p align = "justify">
This function determines the error between two values. Predict value (S) and Observed value (O).
</p>

<h4>Sintaxe</h4>

```python
ERROR = RESIDUALS(S_VALUE, O_VALUE)
```

<h4>Input variables</h4>

<table style = "width:100%">
    <tr>
        <td>S</td>
        <td>Numerical value (\(y_{pre}\))</td>
        <td>Float</td>
    </tr>
    <tr>
        <td>O</td>
        <td>Observed value (\(y_{obs}\))</td>
        <td>Float</td>
    </tr>
</table>

<h4>Output variables</h4>

<table style = "width:100%">
    <tr>
        <td>RESIDUAL</td>
        <td>Residual value</td>
        <td>Float</td>
    </tr>
</table>

<h4>Equation</h4>

<table style = "width:100%">
    <tr>
        <td>\[res = y_{pre} - y_{obs}\]</td>
        <td><p align = "right">(1)</p></td>
    </tr>
</table>

<h4>Numerical example</h4>

<table style = "width:100%">
    <tr>
        <td><p align = "left">\[y_{pre} = 2.0\]</p></td>
    </tr>
    <tr>
        <td><p align = "left">\[y_{obs} = 2.5\]</p></td>
    </tr>
    <tr>
        <td><p align = "left">\[residual = 2.0 - 2.5 = - 0.50\]</p></td>
    </tr>
</table>

<h4>Notebook example</h4>

<p align = "justify">
See link to <a href="https://wmpjrufg.github.io/META_TOOLBOX/001-VERSION.html" target="_blank">Notebook file</a>.
</p>

<h2><b><code>LOSS_FUNCTION_1</code></b></h2>
<p align = "justify">
This function determines the Loss function d-dimension. Mean Square Error. Predict vector (Y_NUM) and Observed vector (Y_EXP).
</p>

<h4>Sintaxe</h4>

```python
ERROR = LOSS_FUNCTION_1(Y_EXP, Y_NUM)
```

<h4>Input variables</h4>

<table style = "width:100%">
    <tr>
        <td>Y_EXP</td>
        <td>Observed dataset (\(\symbf{y}_{exp}\))</td>
        <td>Py list</td>
    </tr>
    <tr>
        <td>Y_NUM</td>
        <td>Numerical dataset (\(\symbf{y}_{num}\))</td>
        <td>Py list</td>
    </tr>
</table>

<h4>Output variables</h4>

<table style = "width:100%">
    <tr>
        <td>ERROR</td>
        <td>Total error</td>
        <td>Float</td>
    </tr>
</table>

<h4>Equation</h4>

<table style = "width:100%">
    <tr>
        <td>\[mse = \frac{1}{n}.\sum_{k=1}^{n} \left(\symbf{y}_{num,k} - \symbf{y}_{exp,k}\right)^2\]</td>
        <td><p align = "right">(2)</p></td>
    </tr>
</table>

<p align = "justify">
\(n\) dataset lenght.
</p>

<h4>Numerical example</h4>

<table style = "width:100%">
    <tr>
        <td><p align = "left">\[ y_{num} = \left[2.0, 3.0, 5.0 \right] \]</p></td>
    </tr>
    <tr>
        <td><p align = "left">\[ y_{exp} = \left[1.0, 2.0, 5.0 \right] \]</p></td>
    </tr>
    <tr>
        <td><p align = "left">\[mse_{k=0} = 2.00 - 1.00 = 1.00\]</p></td>
    </tr>
    <tr>
        <td><p align = "left">\[mse_{k=1} = 3.00 - 2.00 = 1.00\]</p></td>
    </tr>
    <tr>
        <td><p align = "left">\[mse_{k=2} = 5.00 - 5.00 = 0.00\]</p></td>
    </tr>
    <tr>
        <td><p align = "left">\[mse = \frac{1}{3}.\left(1^2 + 1^2 + 0^2 \right) = 0.67\]</p></td>
    </tr>
</table>

<h4>Notebook example</h4>

<p align = "justify">
See link to <a href="https://wmpjrufg.github.io/META_TOOLBOX/001-VERSION.html" target="_blank">Notebook file</a>.
</p>