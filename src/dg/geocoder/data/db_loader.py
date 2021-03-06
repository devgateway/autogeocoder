import numpy
from numpy import random
from pandas.core.frame import DataFrame

from dg.geocoder.db.corpora import get_sentences


def get_geography_rows(limit=2000):
    return get_sentences(category='geography', limit=limit)['rows']


def get_none_rows(limit=2000):
    return get_sentences(category='none', limit=limit)['rows']


class DbDataLoader:
    @staticmethod
    def read_rows():
        geography_records = get_geography_rows()
        # get same amount of none records
        none_records = get_none_rows(limit=len(geography_records))
        all_records = geography_records + none_records
        random.shuffle(all_records)
        return all_records

    def build_data_frame(self):
        records = self.read_rows()
        rows = []
        index = []
        data_frame = None
        if len(records) > 0:
            for id, text, classification, file_name in records:
                index.append(id)
                rows.append({'text': text, 'class': classification})

            data_frame = DataFrame(rows, index=index)
            data_frame = data_frame.reindex(numpy.random.permutation(data_frame.index))

        return data_frame
