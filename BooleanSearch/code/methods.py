# The queries that were given in the instructions

# Query 1: aspect1 OR aspect2 OR opinion
def method1(index_table, aspect1, aspect2, opinion):
    """performs aspect1 OR aspect2 OR opinion using the global posting list."""
    results = set(index_table.get(aspect1.lower(), [])) | set(index_table.get(aspect2.lower(), [])) | set(index_table.get(opinion.lower(), []))
    return results

# Query 2: aspect1 AND aspect2 AND opinion
def method2(index_table, aspect1, aspect2, opinion):
    """performs aspect1 AND aspect2 AND opinion using the global posting list."""
    results_aspect1 = set(index_table.get(aspect1.lower(), []))
    results_aspect2 = set(index_table.get(aspect2.lower(), []))
    results_opinion = set(index_table.get(opinion.lower(), []))
    results = results_aspect1 & results_aspect2 & results_opinion
    return results

# Query 3: (aspect1 OR aspect2) AND opinion
def method3(index_table, aspect1, aspect2, opinion):
    """performs (aspect1 OR aspect2) AND opinion using the global posting list."""
    results_aspect = set(index_table.get(aspect1.lower(), [])) | set(index_table.get(aspect2.lower(), []))
    results_opinion = set(index_table.get(opinion.lower(), []))
    results = results_aspect & results_opinion
    return results

