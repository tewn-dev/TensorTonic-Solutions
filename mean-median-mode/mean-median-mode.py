import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Convert input to a NumPy array
    x_arr = np.asarray(x)
    
    # Calculate Mean and Median using NumPy (Hint 1)
    mean_val = float(np.mean(x_arr))
    median_val = float(np.median(x_arr))
    
    # Calculate Mode using Counter (Hint 2)
    # Count frequencies of each element
    freqs = Counter(x_arr)
    
    # Find the highest frequency count
    max_freq = max(freqs.values())
    
    # Extract all elements that share this highest frequency
    mode_candidates = [val for val, count in freqs.items() if count == max_freq]
    
    # Get the smallest value among the most frequent elements and convert to float
    mode_val = float(min(mode_candidates))
    
    # Return as a tuple of floats (Hint 3)
    return mean_val, median_val, mode_val