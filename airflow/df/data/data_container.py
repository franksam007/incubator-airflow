# -*- coding: utf-8 -*-

from data_enums import DataSetType
from metadata import ColumnMetadata
from metadata import DataSetMetadata
from dataset_wrapper_factory import DataSetWrapperFactory


class DataContainer:
    def __init__(
        self,
        data_set_name,
        data_set_type,
        data_set,
        data_set_name_lc='',
        data_set_desc='',
        data_set_metadata=None
    ):
        if data_set_metadata:
            self.data_set_metadata = data_set_metadata
            self.data_set_metadata.data_set_name = data_set_name
            self.data_set_metadata.data_set_type = data_set_type
            self.data_set_metadata.data_set_name_lc = data_set_name_lc
            self.data_set_metadata.data_set_desc = data_set_desc
        else:
            self.data_set_metadata = DataSetMetadata(
                data_set_name, data_set_type, data_set_name_lc, data_set_desc)

        self.data_set_wrapper = DataSetWrapperFactory(data_set, data_set_type)
        self.populate_metadata()

    def populate_metadata(self):
        if self.data_set_wrapper:
            self.data_set_metadata = self.data_set_wrapper.populate_metadata()
