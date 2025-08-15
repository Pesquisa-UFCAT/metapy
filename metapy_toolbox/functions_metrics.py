"""functions and metrics for metapy_toolbox"""
import numpy as np


def loss_function_mse(y_true, y_pred):
    """
    Loss function: Mean Square Error.

    See documentation in https://wmpjrufg.github.io/METAPY/STATS_LOSS_MSE.html

    Args:
        y_true (List): True values.
        y_pred (List): Predicted values.
    
    Returns:
        mse (Float): Mean Square Error.
    """

    res = [(tr-pr)**2 for tr, pr in zip(y_true, y_pred)]
    error = sum(res)

    return (1 / len(y_true)) * error


def loss_function_mae(y_true, y_pred):
    """
    Loss function: Mean Absolute Error.

    See documentation in https://wmpjrufg.github.io/METAPY/STATS_LOSS_MAE.html

    Args:
        y_true (List): True values.
        y_pred (List): Predicted values.
    
    Returns:
        mae (Float): Mean Absolute Error.
    """

    res = [np.abs(tr-pr) for tr, pr in zip(y_true, y_pred)]
    error = sum(res)

    return (1 / len(y_true)) * error


def loss_function_mape(y_true, y_pred):
    """
    Loss function: Mean Absolute Percentage Error.

    See documentation in https://wmpjrufg.github.io/METAPY/STATS_LOSS_MAPE.html

    Args:
        y_true (List): True values.
        y_pred (List): Predicted values.
    
    Returns:
        mape (Float): Mean Absolute Percentage Error.
    """

    res = [100 * np.abs(tr-pr) / tr  for tr, pr in zip(y_true, y_pred)]
    error = sum(res)

    return (1 / len(y_true)) * error


def loss_function_hubber(y_true, y_pred, delta):
    """
    Loss function: Smooth Mean Absolute Error or Hubber Loss.

    See documentation in https://wmpjrufg.github.io/METAPY/STATS_LOSS_HUBBER.html

    Args:
        y_true (List): True values.
        y_pred (List): Predicted values.
        delta (Float): Threshold.
    
    Returns:
        smae (Float): Hubber Loss.
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


def loss_function_rmse(y_true, y_pred):
    """
    Loss function: Root Mean Square Error.

    See documentation in https://wmpjrufg.github.io/METAPY/STATS_LOSS_RMSE.html
    
    Args:
        y_true (List): True values.
        y_pred (List): Predicted values.
    
    Returns:
        rmse (Float): Root Mean Square Error.
    """

    return np.sqrt(loss_function_mse(y_true, y_pred))


def loss_function_r2(y_true, y_pred):
    """
    Loss function: R2 Score (Coefficient of Determination).
    
    See documentation in https://wmpjrufg.github.io/METAPY/STATS_LOSS_R2.html

    Args:
        y_true (List): True values.
        y_pred (List): Predicted values.
    
    Returns:
        r2 (Float): R2 Score.
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


def loss_function_r2_adjusted(y_true, y_pred, num_params):
    """
    Loss function: R2 Adjusted Score.

    See documentation in https://wmpjrufg.github.io/METAPY/STATS_LOSS_R2_ADJUSTED.html

    Args:
        y_true (List): True values.
        y_pred (List): Predicted values.
        num_params (int): Number of parameters in the model.

    Returns:
        r2_adjusted (Float): R2 Adjusted Score.
    """
    
    import numpy as np
    
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
