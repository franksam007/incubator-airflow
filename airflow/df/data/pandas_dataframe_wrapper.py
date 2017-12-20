# -*- coding: utf-8 -*-

from pandas import DataFrame as df
from metadata import DataSetMetadata

class PandasDF:
    def __init__(self, data_set):
        if isinstance(data_set, df) and data_set:
            self.internal_data_set = df(data_set)
        else:
            raise ValueError("Invalid pandas dataframe!")

    def populate_metadata(self):
        ds_meta = DataSetMetadata()
        if self.internal_data_set:
            pass
        return ds_meta

