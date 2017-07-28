import numpy as np
from sner import Ner

from dg.geocoder.classification.classifier import load_classifier
from dg.geocoder.config import get_ner_host, get_ner_port
from dg.geocoder.readers.factory import get_reader


def process_activity(activity):
    print(activity)


def bulk_process(xml, path_to_docs='docs'):
    if xml is None:
        print('xml file should be provide')
    else:
        print('Process list of activities')


def classify(sentences, cls_name='default_classifier'):
    classifier = load_classifier(cls_name)
    results = classifier.predict(sentences)
    return np.where(results == 'geography')[0]


def classify_document(file, **kwargs):
    reader = get_reader(file)
    # split document in stences
    sentences = reader.split()
    indexes = classify(sentences, **kwargs)
    geo_sentences = [(sentences[i]) for i in indexes]
    return geo_sentences


def tag_sentences(sentences):
    tagger = Ner(host=get_ner_host(), port=get_ner_port())
    tagged_sentences = []
    for s in sentences:
        tagged = tagger.get_entities(s)
        locs = [(word) for word, tag in tagged if tag in ['LOCATION']]
        tagged_sentences.append((s, locs))
    return tagged_sentences


if __name__ == '__main__':
    texts = classify_document(
        'docs/GN-2005-009-EN-ADF-BD-WP-APPROVED-GUINEA-PPF-RURAL-DEVT-SUPPORT-PROJECT-FOR-THE-NORTH-WEST-FOUTA-DJALLON-AREA-LOTB-APPROVED.PDF',
        cls_name='default_classifier_1')
    tagged = tag_sentences(texts)
    print(tagged)
