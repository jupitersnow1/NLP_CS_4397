from nltk.tokenize import word_tokenize

# Tokenization function
"""Split the input text into individual words

    Args:
        text (str): The text string you want to tokenize.

    Returns:
        list: A list of words extracted from the input text.
        
"""
def tokenize(text):
    return word_tokenize(text.lower())
