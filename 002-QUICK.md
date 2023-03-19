<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h1>Quick Start</h1>

<p align = "justify">
Quick start guide.
</p>

<h2>Dependences</h2>

<ul>
    <li><a href="https://numpy.org/install/" target="_blank">Numpy</a></li>
    <li><a href="https://xlsxwriter.readthedocs.io/getting_started.html" target="_blank">Xlsxwriter</a></li>
</ul>

<h2>Version</h2>

<code>2022.1</code>

<p align = "justify">
See others versions. <a href="https://wmpjrufg.github.io/META_TOOLBOX/LOG.html" target="_blank">Log file</a>.
</p>

<h2>Install</h2>

<p align = "justify">
installation command-line: <a href="https://pypi.org/project/META-TOOLBOX/2023.1/#description" target="_blank">Pypi</a>.
</p>

```python
pip install META-TOOLBOX==2023.1
```

<h2>Run algorithm</h2>

<p align = "justify">
Hill Climbing example.
</p>

```python
from META_TOOLBOX import HILL_CLIMBING_001 # or from META_TOOLBOX import *

# Input
PARAMETERS = {'SIGMA': 10} # equal 10%

SETUP = {
        'N_REP': 10,
        'N_POP': 5,
        'N_ITER': 1000,
        'X_L': [-2, -2, -2],
        'X_U': [2, 2, 2],
        'D': 3,
        'NULL_DIC': None,
        'PARAMETERS': PARAMETERS
        }

# OF statement
def OF_FUNCTION(X, NULL_DIC):
    X_0 = X[0]
    X_1 = X[1]
    X_2 = X[2]
    OF = X_0 ** 2 + X_1 ** 2 + X_2 ** 2
    return OF

# Call function
RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE = HILL_CLIMBING_001(OF_FUNCTION, SETUP)
```

<h2>Analysis</h2>

<p align = "justify">
<b>1)</b> See best and worst repetition procedure.
</p>

```python
# Call function
RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE = HILL_CLIMBING_001(OF_FUNCTION, SETUP)

# Best ID procedure
STATUS[0]

# Worst ID procedure
STATUS[-1]
```

<p align = "justify">
<b>2)</b> See details best procedure.
</p>

```python
BEST_ID = STATUS[0]
BEST_REP[BEST_ID]
```