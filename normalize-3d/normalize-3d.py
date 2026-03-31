import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Convert input to a numpy array of floats
    v_np = np.asarray(v, dtype=float)
    
    # Calculate the L2 norm along the last axis
    # keepdims=True ensures the output shape is (1,) or (N, 1) to allow broadcasting
    norms = np.linalg.norm(v_np, axis=-1, keepdims=True)
    
    # Avoid division by zero by replacing norms below the 1e-6 tolerance with 1.0
    safe_norms = np.where(norms < 1e-6, 1.0, norms)
    
    # Calculate the unit vectors
    unit_vectors = v_np / safe_norms
    
    # Enforce exact zeros for vectors that originally had a norm below the tolerance
    return np.where(norms < 1e-6, 0.0, unit_vectors)