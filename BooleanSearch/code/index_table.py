import json
import os
from tqdm import tqdm
from collections import defaultdict, Counter
import pickle
from tokenizer import tokenize  # import tokenize function


def load_data(file_path):
    """load review data from a pickle file."""
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data


def create_index(data):
    """
    creates a global posting list for all unique words in the review data.

    args:
        data (DataFrame): The review data.

    returns:
        dict: a dictionary where each word is associated with a list of review IDs.
    """
    index_table = defaultdict(set)  # Use a set to avoid duplicate review IDs for each token

    for idx, row in tqdm(data.iterrows(), total=data.shape[0], desc="Creating global posting list"):
        review_id = row['review_id']
        tokens = tokenize(row['review_text'])  # Tokenize and remove stop words

        # Add each token to the posting list with the review ID
        for token in tokens:
            index_table[token].add(review_id)

    # convert sets to lists for JSON serialization
    index_table = {token: list(review_ids) for token, review_ids in index_table.items()}

    return index_table


def sort_index(index_table):
    """
    sort the index table by word frequency (most frequent to least frequent)
    and include the list of review IDs.

    args:
        index_table (dict): The unsorted posting list.

    returns:
        list: A sorted list of dictionaries, each containing (keyword, frequency, unique_review_count, review_ids).
    """
    # create a list of dictionaries for keyword details
    sorted_keywords = [
        {
            "keyword": token,
            "frequency": len(review_ids),
            "unique_review_count": len(set(review_ids)),
            "review_ids": list(review_ids)  # Include the review IDs
        }
        for token, review_ids in index_table.items()
    ]

    # sort by frequency and then by keyword (for ties)
    sorted_keywords.sort(key=lambda x: (-x['frequency'], x['keyword']))

    return sorted_keywords


def save_posting_list(index_table, output_dir):
    """save the global posting list as a JSON file in the output directory."""
    json_path = os.path.join(output_dir, 'posting_list.json')
    with open(json_path, 'w') as json_file:
        json.dump(index_table, json_file, indent=4)


# this is meant to sort the posting list keywords by frequency so its easier for the user distinguish the inverted index list
def save_sorted_keywords(sorted_keywords, output_dir):
    """save the sorted keywords with frequencies and unique review counts to a JSON file."""
    json_path = os.path.join(output_dir, 'sorted_keywords.json')
    with open(json_path, 'w') as json_file:
        json.dump(sorted_keywords, json_file, indent=4)


