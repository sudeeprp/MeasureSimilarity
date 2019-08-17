import NumericDistanceComputer as dc
import SentenceEncoder as se


def compute_sentence_distance(nlp, sentence1, sentence2):
    return dc.average_minimals(
                     dc.compute_embedding_distances(se.sentence_embedding(nlp, sentence1),
                                                    se.sentence_embedding(nlp, sentence2)))
