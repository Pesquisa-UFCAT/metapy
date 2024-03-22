---
layout: default
title: loss_function_r2
parent: Loss
grand_parent: Statistical
has_children: false
has_toc: false
nav_order: 6
---

<!-- Don't delete this script -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!-- Don't delete this script -->

<h3>loss_function_r2</h3>

<br>

<p align="justify">
Loss function: R2 Score (Coefficient of Determination).
</p>

```python
r2 = loss_function_r2(y_true, y_pred)
```

Input variables
{: .label .label-yellow }

<table style="width:100%">
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
</table>

Output variables
{: .label .label-yellow }

<table style="width:100%">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Type</th>
    </tr>
  </thead>
  <tr>
    <td><code>r2</code></td>
    <td>R2 Score</td>
    <td>Float</td>
  </tr>
</table>

<h3>Problem</h3>

<table style="width:100%">
  <tr>
    <td style="width: 90%;">
      \[R^2 = 1 - \frac{\text{RSS}}{\text{TSS}}\]
    </td>
    <td style="width: 10%;"><p align="right">(1)</p></td>
  </tr>
  <tr>
    <td style="width: 90%;">
      \[\text{RSS} = \sum_{i=1}^{n} (y_{\text{true},i} - y_{\text{pred},i})^2\]
    </td>
    <td style="width: 10%;"><p align="right">(2)</p></td>
  </tr>
  <tr>
    <td style="width: 90%;">
      \[\text{TSS} = \sum_{i=1}^{n} (y_{\text{true},i} - \bar{y}_{\text{true}})^2\]
    </td>
    <td style="width: 10%;"><p align="right">(3)</p></td>
  </tr>
</table>

<p align="justify">
    \(\text{RSS}\) is the sum of squares of residuals and \(\text{TSS}\) is the total sum of squares.
</p>

Example 1
{: .label .label-blue }

<p align="justify">
    <i>
        Considering the true values \(\mathbf{y}_{\text{true}} = [1.0, 2.0, 3.0, 4.0, 5.0]\) and predicted values \(\mathbf{y}_{\text{pred}} = [1.2, 2.3, 2.9, 4.2, 5.3]\), what is the resulting R2 Score?
    </i>
</p>

```python
# Data
y_true_example = [1.0, 2.0, 3.0, 4.0, 5.0]
y_pred_example = [1.2, 2.3, 2.9, 4.2, 5.3]

# Call function
r2_value = loss_function_r2(y_true_example, y_pred_example)

# Output details
print("R2 Score: {:.4f}".format(r2_value))
```

```bash
R2 Score: 0.9730
```