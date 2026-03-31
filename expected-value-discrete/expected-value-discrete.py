import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Convert inputs to numpy arrays to easily check shapes and perform vectorized operations
    x = np.asarray(x)
    p = np.asarray(p)
    
    # Requirement: Ensure shapes of x and p match
    if x.shape != p.shape:
        raise ValueError(f"Shape mismatch: x has shape {x.shape} but p has shape {p.shape}.")
    
    # Requirement: Raise a ValueError if probabilities don't sum to 1 (within tolerance 10^-6)
    if not np.allclose(np.sum(p), 1.0, atol=1e-6):
        raise ValueError("The probabilities in p must sum to exactly 1.")
    
    # Compute the expected value: element-wise product of x and p, then sum
    expected_value = np.sum(x * p)
    
    # Return as a single float
    return float(expected_value)
