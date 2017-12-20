# -*- coding: utf-8 -*-

from data_enums import DataSetType
from pandas_dataframe_wrapper import PandasDF


class DataSetWrapperFactory:
    def __init__(self, data_set, data_set_type=DataSetType.PANDAS_DF):
        if data_set_type == DataSetType.PANDAS_DF:
            self.internal_wrapper = PandasDF(data_set)
        else:
            pass  # TODO: Add other dataset/dataframe wrapper

        self.data_set_type = data_set_type

    def populate_metadata(self):
        return self.internal_wrapper.populate_metadata()



