# -*- coding: utf-8 -*-

from data_enums import DataSetType
from metadata import ColumnMetadata
from metadata import DataContainerMetadata


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
        else:
            self.data_set_metadata = DataContainerMetadata(
                data_set_name, data_set_type, data_set_name_lc, data_set_desc)

        self.data_set = data_set


