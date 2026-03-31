import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Hint 2: Convert input to a numpy array for vectorized operations
    k_array = np.array(k)
    
    # Hint 1: Calculate the PMF element-wise
    # (1 - p)^(k - 1) represents getting (k-1) failures before finally getting 1 success (p)
    pmf = ((1.0 - p) ** (k_array - 1)) * p
    
    # Hint 3: The mean is simply 1 / p
    # Convert to float to satisfy the return type requirement
    mean = float(1.0 / p)
    
    # Return as a tuple
    return pmf, mean