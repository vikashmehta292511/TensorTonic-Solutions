import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    # Write code here
    rewards = np.asarray(rewards, dtype=float)
    states  = np.asarray(states,  dtype=int)
    V       = np.asarray(V,       dtype=float)
    T       = len(rewards)

    G = np.zeros(T)
    G[-1] = rewards[-1]
    for t in range(T - 2, -1, -1):
        G[t] = rewards[t] + gamma * G[t + 1]

    return G - V[states]
    pass
