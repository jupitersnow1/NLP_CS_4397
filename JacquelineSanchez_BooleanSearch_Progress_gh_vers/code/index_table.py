import json
import os
from tqdm import tqdm
from collections import defaultdict
import pickle

# import it from the `tokenizer.py`
from tokenizer import tokenize

def load_data(file_path):
    """load review data from a pickle file."""
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def create_index(data):
    """creates an index table for the review data using tokenization."""
    index_table = defaultdict(list)
    for idx, row in tqdm(data.iterrows(), total=data.shape[0], desc="Creating index"):
        review_id = row['review_id']
        tokens = tokenize(row['review_text'])  # tokenize function
        for token in tokens:
            index_table[token].append(review_id)
    return index_table

def save_posting_list(index_table, output_dir):
    """save the posting list as a JSON file in the output directory."""
    json_path = os.path.join(output_dir, 'posting_list.json')
    with open(json_path, 'w') as json_file:
        json.dump(index_table, json_file)