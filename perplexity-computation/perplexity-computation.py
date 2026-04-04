import math

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here

    N = len(actual_tokens)
    
    log_probs = [math.log(prob_distributions[i][actual_tokens[i]]) for i in range(N)]
    
    cross_entropy = -sum(log_probs) / N
    
    return math.exp(cross_entropy)