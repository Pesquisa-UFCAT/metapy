"""functions and metrics for metapy_toolbox"""
import numpy as np

from typing import List

def loss_function_mse(y_true: List[float], y_pred: List[float]) -> float:
    """
    Loss function: Mean Square Error.

    See documentation `here <https://wmpjrufg.github.io/METAPY/STATS_LOSS_MSE.html>`_.

    :param y_true: True values.
    :param y_pred: Predicted values.

    :return: Mean Square Error.
    """

    res = [(tr-pr)**2 for tr, pr in zip(y_true, y_pred)]
    error = sum(res)

    return (1 / len(y_true)) * error


def loss_function_mae(y_true: List[float], y_pred: List[float]) -> float:
    """
    Loss function: Mean Absolute Error.

    See documentation `here <https://wmpjrufg.github.io/METAPY/STATS_LOSS_MAE.html>`_.

    :param y_true: True values.
    :param y_pred: Predicted values.

    :return: Mean Absolute Error.
    """

    res = [np.abs(tr-pr) for tr, pr in zip(y_true, y_pred)]
    error = sum(res)

    return (1 / len(y_true)) * error


def loss_function_mape(y_true: List[float], y_pred: List[float]) -> float:
    """
    Loss function: Mean Absolute Percentage Error.

    See documentation `here <https://wmpjrufg.github.io/METAPY/STATS_LOSS_MAPE.html>`_.	

    :param y_true: True values.
    :param y_pred: Predicted values.

    :return: Mean Absolute Percentage Error
    """

    res = [100 * np.abs(tr-pr) / tr  for tr, pr in zip(y_true, y_pred)]
    error = sum(res)

    return (1 / len(y_true)) * error


def loss_function_hubber(y_true: List[float], y_pred: List[float], delta: float) -> float:
    """
    Loss function: Smooth Mean Absolute Error or Hubber Loss.

    See documentation `here <https://wmpjrufg.github.io/METAPY/STATS_LOSS_HUBBER.html>`_.

    :param y_true: True values.
    :param y_pred: Predicted values.
    :param delta: Threshold that controls the switch between L2 and L1 loss.

    :return: Hubber Loss value.
    """

    error = 0
    for i in range(len(y_true)):
        res = y_true[i] - y_pred[i]
        value = np.abs(res)
        if value <= delta:
            error += 0.5 * (res)**2
        else:
            error += delta*np.abs(res) - 0.5*delta**2

    return (1 / len(y_true)) * error


def loss_function_rmse(y_true: List[float], y_pred: List[float]) -> float:
    """
    Loss function: Root Mean Square Error.

    See documentation `here <https://wmpjrufg.github.io/METAPY/STATS_LOSS_RMSE.html>`_. 
    
    :param y_true: True values.
    :param y_pred: Predicted values.

    :return: Root Mean Square Error.
    """

    return np.sqrt(loss_function_mse(y_true, y_pred))


def loss_function_r2(y_true: List[float], y_pred: List[float]) -> float:
    """
    Loss function: R2 Score (Coefficient of Determination).
    
    See documentation `here <https://wmpjrufg.github.io/METAPY/STATS_LOSS_R2.html>`_. 

    :param y_true: True values.
    :param y_pred: Predicted values.

    :return: R² Score.
    """
    
    # Convert lists to arrays
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # Calculate the mean of true values
    y_mean = np.mean(y_true)
    
    # Calculate residual sum of squares (RSS)
    rss = sum((y_true - y_pred) ** 2)
    
    # Calculate total sum of squares (TSS)
    tss = sum((y_true - y_mean) ** 2)
    
    # Calculate R2 score
    r2 = 1 - (rss / tss)
    
    return r2


def loss_function_r2_adjusted(y_true: List[float], y_pred: List[float], num_params: int) -> float:
    """
    Loss function: R2 Adjusted Score.

    See documentation `here <https://wmpjrufg.github.io/METAPY/STATS_LOSS_R2_ADJUSTED.html`_.

    :param y_true: True values.
    :param y_pred: Predicted values.
    :param num_params: Number of parameters in the model.

    :return: Adjusted R² Score.
    """
    # Convert lists to arrays
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # Calculate the mean of true values
    y_mean = np.mean(y_true)
    
    n = len(y_true)
    
    # Calculate residual sum of squares (RSS)
    rss = sum((y_true - y_pred) ** 2)
    
    # Calculate total sum of squares (TSS)
    tss = sum((y_true - y_mean) ** 2)
    
    # Calculate R2 adjusted score
    r2_adjusted = 1 - ((rss / (n - num_params - 1)) / (tss / (n - 1)))

    return r2_adjusted

# https://www.datacamp.com/tutorial/loss-function-in-machine-learning
# https://medium.com/@amanatulla1606/demystifying-loss-functions-in-deep-learning-understanding-the-key-metrics-for-model-optimization-a81ce65e7315
# https://towardsdatascience.com/importance-of-loss-function-in-machine-learning-eddaaec69519
# https://www.analyticsvidhya.com/blog/2021/10/evaluation-metric-for-regression-models/#:~:text=Relative%20Root%20Mean%20Square%20Error,to%20compare%20different%20measurement%20techniques.
# https://medium.com/@evertongomede/understanding-loss-functions-in-deep-learning-9f06e5090f20
# https://www.analyticsvidhya.com/blog/2019/08/detailed-guide-7-loss-functions-machine-learning-python-code/
# https://medium.com/nerd-for-tech/what-loss-function-to-use-for-machine-learning-project-b5c5bd4a151e
# https://eyeonplanning.com/blog/the-heart-of-machine-learning-understanding-the-importance-of-loss-functions/
# https://github.com/christianversloot/machine-learning-articles/blob/main/about-loss-and-loss-functions.md
# https://arxiv.org/pdf/2301.05579.pdf
