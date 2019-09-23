import unittest
import WordCounts as wc

SHORT_WORD = "Hi"
NAME_WORD = "Maarvelus"
APOST_WORD = "I'm"
SAMPLE_STOP_WORDS = ['the', 'to', 'and']
PUNCTUATION = ','


class WordCountTest(unittest.TestCase):
    def test_words_are_split(self):
        token_list = wc.text_to_tokens(SHORT_WORD + PUNCTUATION + APOST_WORD + ' ' + NAME_WORD)
        self.assertTrue(NAME_WORD.lower() in token_list)
        self.assertTrue(SHORT_WORD.lower() in token_list)
        # we don't care for apostrophes, so it isn't asserted here

    def test_punctuations_are_removed(self):
        tokens_with_punctuation = [NAME_WORD, PUNCTUATION, APOST_WORD]
        word_list = wc.remove_punctuations(tokens_with_punctuation)
        self.assertTrue(PUNCTUATION not in word_list,
                        msg=PUNCTUATION + " should not be there!")

    def test_stopwords_are_removed(self):
        words_with_stopwords = [NAME_WORD, APOST_WORD] + SAMPLE_STOP_WORDS
        filtered_word_list = wc.remove_stopwords(words_with_stopwords)
        self.assertTrue(NAME_WORD in filtered_word_list)
        for stopword in SAMPLE_STOP_WORDS:
            self.assertTrue(stopword not in filtered_word_list,
                            msg=stopword + " should not be there!")

    def test_text_is_converted_to_words_without_stopwords(self):
        sample_text = '''Configuration,F5 firmware + Certificate strategy wasn't configured.
         > We did not know the required strategy and configurations >  No documentation.'''
        words = wc.text_to_words_without_stopwords(sample_text)
        self.assertTrue(',' not in words, msg="Comma shouldn't be there")
        self.assertTrue('+' not in words, msg="Plus shouldn't be there")
        self.assertTrue('did' not in words, msg="did shouldn't be there")


if __name__ == "__main__":
    unittest.main()
