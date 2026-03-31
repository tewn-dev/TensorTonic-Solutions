import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    Arguments:
    x: list or array - Numeric data
    q: list or array - Percentile values (0-100)
    
    Returns:
    NumPy array of percentile values
    """
    # Convert inputs to NumPy arrays (Hint 2)
    x = np.asarray(x)
    q = np.asarray(q)
    
    # method='linear' is the default, but we specify it explicitly per the hint
    return np.percentile(x, q, method='linear')
