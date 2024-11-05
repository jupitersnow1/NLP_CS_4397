# tokenizer.py
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# removing any instance of stop words to reduce the size of the postings_list

# load English stop words
stop_words = set(stopwords.words('english'))


def tokenize(text):
    """
    Tokenize text and remove stop words.

    Args:
        text (str): The text to tokenize.

    Returns:
        list: List of tokens without stop words.
    """
    tokens = word_tokenize(text.lower())  # tokenize and lowercase the text
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    return filtered_tokens
