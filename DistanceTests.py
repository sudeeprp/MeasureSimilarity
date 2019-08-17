import unittest
import math
import spacy
import NumericDistanceComputer as dc
import SentenceEncoder as se
import SentenceDistanceComputer as sentdist

class DistanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nlp = spacy.load('en_core_web_md')

    def test_thatAverageOfMinima_computes_averageOfSmallestQuarterOfSamples(self):
        self.assertEqual(dc.average_minimals([1, 2, 3, 4, 5, 6, 7, 8]), 1.5)
        self.assertEqual(dc.average_minimals([5]), 5)
        self.assertEqual(dc.average_minimals([3, 2]), 2)
        self.assertEqual(dc.average_minimals([5, 4, 2, 1, 3]), 1.5)

    def test_thatLenOfEmbeddingDistances_is_productOfEmbeddingSetSizes(self):
        embeddingset1 = [[1, 2], [3, 4]]
        embeddingset2 = [[1, 2], [1, 3]]
        distances = dc.compute_embedding_distances(embeddingset1, embeddingset2)
        self.assertEqual(len(distances), 4)
        self.assertLess(distances[0], distances[1])

    def test_thatSentenceEmbedding_has_oneOrMoreItems(self):
        embeddingset = se.sentence_embedding(self.nlp,
                                             "All FHIR fields must be extracted into a dictionary")
        self.assertGreater(len(embeddingset), 0)

    def test_thatSentenceEmbedding_doesnt_have_nonDictionaryWords(self):
        embeddingset = se.sentence_embedding(self.nlp, "FHIR fields")
        self.assertEqual(len(embeddingset), 1)

    def test_thatSentenceDistance_is_aNumber(self):
        distance = sentdist.compute_sentence_distance(self.nlp, "Hello there", "Hello world")
        self.assertFalse(math.isnan(distance))

    def test_thatDomainRelatedTest_has_lessDistanceThanGenericTest(self):
        requirement = "FHIR fields from repository must be reflected in the response of patient query"
        domain_testspec1 = "All FHIR fields are extracted into a dictionary"
        domain_testspec2 = "All primitive and general-purpose data are extracted into a dictionary"
        generic_testspec = "After extraction, dictionary has non-empty values"
        generic_distance = sentdist.compute_sentence_distance(self.nlp, requirement, generic_testspec)
        domain_distance1 = sentdist.compute_sentence_distance(self.nlp, requirement, domain_testspec1)
        self.assertLess(domain_distance1, generic_distance)
        domain_distance2 = sentdist.compute_sentence_distance(self.nlp, requirement, domain_testspec2)
        self.assertLess(domain_distance2, generic_distance)


if __name__ == '__main__':
    unittest.main()
