---
layout: default
title: loss_function_mape
parent: Loss
grand_parent: Statistical
has_children: false
has_toc: false
nav_order: 3
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<p align="justify">
The Mean Absolute Percentage Error (MAPE) loss function is a \(d\)-dimensional loss function.

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
        <td>True values.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>y_pred</code></td>
        <td>Predicted values.</td>
        <td>List</td>
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
        <td><code>mape</code></td>
        <td>The function returns the value of the Mean Absolute Percentage Error (MAPE) calculated based on the true and predicted values.</td>
        <td>Float</td>
    </tr>
</table>
<h3>Problem</h3>
<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[f(\mathbf{y}) = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_{\text{true},i} - y_{\text{pred},i}}{y_{\text{true},i}} \right| \times 100\]</td>
        <td style="width: 10%;"><p align = "right">(1)</p></td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Considering the true values \(\mathbf{y}_{\text{true}} = [1, 2, 3, 4, 5]\) and predicted values \(\mathbf{y}_{\text{pred}} = [1.2, 2.3, 2.9, 4.2, 5.3]\), what is the resulting Mean Absolute Percentage Error (MAPE)?
  </i>
</p>

```python
# Example data
y_true_example = [1.0, 2.0, 3.0, 4.0, 5.0]
y_pred_example = [1.2, 2.3, 2.9, 4.2, 5.3]

# Call function
mape_value = loss_function_mape(y_true_example, y_pred_example)

# Output details
print("Mean Absolute Percentage Error (MAPE): {:.4f}".format(mape_value))
```

```bash
Mean Absolute Percentage Error (MAPE): 9.8667
```

