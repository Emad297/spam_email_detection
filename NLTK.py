import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

directory = r'C:\Users\Emado\Desktop\ProjectSpam\spam-mail-ml\data\kaggle\ham'

for filename in os.listdir(directory):
    with open(f'{directory}/{filename}', 'r') as fp:
        text = fp.read()

    # split into words
    tokens = word_tokenize(text)

    # convert to lower case
    tokens = [w.lower() for w in tokens]

    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]

    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]

    # filter out stop words
    stop_words = set(stopwords.words('english'))
    '''words = [w for w in words if w not in stop_words]'''
    words = [f"'{w}'" for w in words if w not in stop_words]

    # output file
    with open(f'C:/Users/Emado/Desktop/ProjectSpam/spam-mail-ml/cleaned_data/output_ham/{filename}', 'w') as fp:
        fp.write(', '.join(words))

