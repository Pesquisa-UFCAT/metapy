---
layout: default
title: loss_function_r2_adjusted
parent: Loss
grand_parent: Statistical
has_children: false
has_toc: false
nav_order: 7
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>loss_function_r2_adjusted</h3>

<br>

<p align="justify">
Loss function: R2 Adjusted Score.
</p>

```python
r2_adjusted = loss_function_r2_adjusted(y_true, y_pred, num_params)
```

Input variables
{: .label .label-yellow }

<table style = "width:100%">
  <thead>
    <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
    </tr>
  </thead>
  <tr>
    <td><code>y_true</code></td>
    <td>True values</td>
    <td>List</td>
  </tr>
  <tr>
    <td><code>y_pred</code></td>
    <td>Predicted values</td>
    <td>List</td>
  </tr>
  <tr>
    <td><code>num_params</code></td>
    <td>Number of parameters in the model</td>
    <td>Integer</td>
  </tr>
</table>

Output variables
{: .label .label-yellow }

<table style = "width:100%">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Type</th>
    </tr>
  </thead>
  <tr>
    <td><code>r2_adjusted</code></td>
    <td>R2 Adjusted Score</td>
    <td>Float</td>
  </tr>
</table>

<h3>Problem</h3>

<table style = "width:100%">
<tr>
    <td style="width: 90%;">\[R^2_{\text{adjusted}} = 1 - \frac{\frac{RSS}{(n - p - 1)}}{\frac{TSS}{(n - 1)}}\]</td>
    <td style="width: 10%;"><p align = "right">(1)</p></td>
</tr>

  <tr>
    <td style="width: 90%;">\[RSS = \sum_{i=1}^{n} (y_{\text{true},i} - y_{\text{pred},i})^2\]</td>
    <td style="width: 10%;"><p align = "right">(2)</p></td>
  </tr>
  <tr>
    <td style="width: 90%;">\[TSS = \sum_{i=1}^{n} (y_{\text{true},i} - \bar{y}_{\text{true}})^2\]</td>
    <td style="width: 10%;"><p align = "right">(3)</p></td>
  </tr>
</table>

<p align="justify">
\(\text{RSS}\) is the residual sum of squares, \(\text{TSS}\) is the total sum of squares and \( p \) is the number of parameters in the model.
</p>

Example
{: .label .label-blue }

<p align = "justify">
  <i>
    Suppose you have a model with 3 parameters and you want to calculate the R2 Adjusted Score for it. Given the true values \(\mathbf{y}_{\text{true}}\) and predicted values \(\mathbf{y}_{\text{pred}}\), what would be the resulting R2 Adjusted Score?
  </i>
</p>

```python
# Data
y_true_example = [1.0, 2.0, 3.0, 4.0, 5.0]
y_pred_example = [1.2, 2.3, 2.9, 4.2, 5.3]
num_params_example = 3

# Call function
r2_adjusted = loss_function_r2_adjusted(y_true_example, y_pred_example, num_params_example)

# Print the result
print("R2 Adjusted Score: {:.4f}".format(r2_adjusted_value))
```

```bash
R2 Adjusted Score: 0.8920
```