def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    # Write code here

    n_states = len(values)
    new_values = []

    for s in range(n_states):
        best_q = float("-inf")
        n_actions = len(transitions[s])
        for a in range(n_actions):
            q = rewards[s][a]
            for s_next in range(n_states):
                q += gamma * transitions[s][a][s_next] * values[s_next]
            if q > best_q:
                best_q = q
        new_values.append(best_q)
    return new_values