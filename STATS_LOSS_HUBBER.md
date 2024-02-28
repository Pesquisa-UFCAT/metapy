---
layout: default
title: loss_function_hubber
parent: Loss
grand_parent: Statistical
has_children: false
has_toc: false
nav_order: 4
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>loss_function_hubber</h3>

<br>

<p align="justify">
Loss function: Smooth Mean Absolute Error or Hubber Loss.
</p>

```python
smae = loss_function_hubber(y_true, y_pred, delta)
```

Input variables
{: .label .label-yellow}

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
        <td><code>delta</code></td>
        <td>Threshold</td>
        <td>Float</td>
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
        <td><code>hubber</code></td>
        <td>Smooth Mean Absolute Error or Hubber Loss</td>
        <td>Float</td>
    </tr>
</table>

<h3>Problem</h3>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[f(\mathbf{y}_{\text{true}}, \mathbf{y}_{\text{pred}}) = \frac{1}{n} \cdot \sum_{i=1}^{n} L_\delta(y_{\text{true},i}, y_{\text{pred},i})\]</td>
        <td style="width: 10%;"><p align = "right">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[L_\delta(a, b) = \begin{cases} 0.5 \cdot (a-b)^2 & \text{for } |a-b| \leq \delta, \\ \delta \cdot |a-b| - 0.5 \cdot \delta^2 & \text{otherwise.} \end{cases}\]</td>
        <td style="width: 10%;"><p align = "right">(2)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[a=y_{\text{true},i} \;\; b=y_{\text{pred},i}\]</td>
        <td style="width: 10%;"><p align = "right">(3)</p></td>
    </tr>
</table>

<p align="justify">
\(n\) is the number of samples.
</p>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Considering the true values \(\mathbf{y}_{\text{true}} = [1.0, 2.0, 3.0, 4.0, 5.0]\), predicted values \(\mathbf{y}_{\text{pred}} = [1.2, 2.3, 2.9, 4.2, 5.3]\), and a threshold \(\mathbf{\delta = 0.5}\), what is the resulting Hubber Loss?
  </i>
</p>

```python
# Data
y_true_example = [1.0, 2.0, 3.0, 4.0, 5.0]
y_pred_example = [1.2, 2.3, 2.9, 4.2, 5.3]
delta_example = 0.5

# Call the loss function
hubber_loss_value = loss_function_hubber(y_true_example, y_pred_example, delta_example)

# Print the result
print("Hubber Loss: {:.4f}".format(hubber_loss_value))
```

```bash
Hubber Loss: 0.1350
```