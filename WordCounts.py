import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import bigrams
from nltk import FreqDist


def text_to_tokens(text):
    return word_tokenize(text.lower())


def remove_punctuations(tokens):
    return [t for t in tokens if t not in string.punctuation]


def remove_stopwords(words):
    stop_words = set(stopwords.words('english'))
    return [w for w in words if w not in stop_words]


def text_to_words_without_stopwords(text):
    return remove_stopwords(remove_punctuations(text_to_tokens(text)))


def count_words(words):
    return Counter(words).most_common()


def count_bigrams(words):
    bigram_counts = []
    wordFreq = FreqDist(bigrams(words))
    for bigram, count in wordFreq.items():
        printable_bigram = (str(bigram[0]) + " " + str(bigram[1])).replace(',', ' ')
        bigram_counts.append((printable_bigram, count))
    return bigram_counts


def write_as_csv(filename, word_count_pairs):
    word_count_pairs.sort(key=lambda x: x[1], reverse=True)
    with open(filename, 'w') as output_file:
        for word_count_pair in word_count_pairs:
            output_file.write(str(word_count_pair[0]) + ',' + str(word_count_pair[1]) + '\n')


def write_counts():
    with open('c:\\workarea-out\\defect and cause.csv') as input_file:
        non_stopwords_nopunct = text_to_words_without_stopwords(input_file.read())
        word_counts = count_words(non_stopwords_nopunct)
        bigram_counts = count_bigrams(non_stopwords_nopunct)
    write_as_csv('c:\\workarea-out\\word counts.csv', word_counts)
    write_as_csv('c:\\workarea-out\\bigram counts.csv', bigram_counts)


if __name__ == '__main__':
    write_counts()
