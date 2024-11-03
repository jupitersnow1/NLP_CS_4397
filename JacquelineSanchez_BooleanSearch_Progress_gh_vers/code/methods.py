import pandas as pd
import json
import os

# postings list
def save_posting_list(index_table, output_dir):
    """Save the posting list as a JSON file."""
    with open(os.path.join(output_dir, 'posting_list.json'), 'w') as json_file:
        json.dump(index_table, json_file)

# query 1: aspect 1 or aspect 2 or opinion
def method1(index_table, aspect1, aspect2, opinion):
    """Perform aspect1 OR aspect2 OR opinion."""
    results = set(index_table.get(aspect1.lower(), [])) | set(index_table.get(aspect2.lower(), [])) | set(index_table.get(opinion.lower(), []))
    return results

# query 2: aspect 1 and aspect 2 and opinion
def method2(index_table, aspect1, aspect2, opinion):
    """Perform aspect1 AND aspect2 AND opinion."""
    results_aspect1 = set(index_table.get(aspect1.lower(), []))
    results_aspect2 = set(index_table.get(aspect2.lower(), []))
    results_opinion = set(index_table.get(opinion.lower(), []))
    results = results_aspect1 & results_aspect2 & results_opinion
    return results

# query 3: aspect 1 or aspect 2 and opinion
def method3(index_table, aspect1, aspect2, opinion):
    """Perform (aspect1 OR aspect2) AND opinion."""
    results_aspect = set(index_table.get(aspect1.lower(), [])) | set(index_table.get(aspect2.lower(), []))
    results_opinion = set(index_table.get(opinion.lower(), []))
    results = results_aspect & results_opinion
    return results
