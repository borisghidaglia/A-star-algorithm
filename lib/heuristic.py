def null_heuristic(a_star, node):
    return 0

def sum_min_in_lines(a_star, node):
    available_agents = a_star.agents - node.attributed_agents
    job = node.job
    val_heuristic = 0
    for job in range(job+1, a_star.cost_matrix.shape[0]):
        val_min = float('inf')
        for agent in available_agents:
            val_min = min(val_min, a_star.cost_matrix[agent][job])
        val_heuristic += val_min
    return val_heuristic
