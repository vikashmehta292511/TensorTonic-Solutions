import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here

    real_scores = np.asarray(real_scores, dtype=float)
    fake_scores = np.asarray(fake_scores, dtype=float)

    mean_real = np.mean(real_scores)
    mean_fake = np.mean(fake_scores)

    return float(mean_fake - mean_real)
    
    pass