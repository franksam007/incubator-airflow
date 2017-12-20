# -*- coding: utf-8 -*-
# Metadata container for dataframe container

from data_enums import BasicDatatype
from data_enums import ValueCategory
from data_enums import DatasetRole
from data_enums import DataStats
from data_enums import DataRole
from data_enums import MetadataStoreType


class ColumnMetadata:
    """
    Metadata of columns of a dataset/dataframe(table-like)
    """
    column_name = ''
    column_datatype = BasicDatatype.STRING
    column_value_category = ValueCategory.NUMERIC
    column_role = DataRole.FACTOR
    column_name_lc = ''
    column_desc = ''
    column_stat = {
        DataStats.MEAN: 0.0,
        DataStats.MEDIAN: 0.0,
        DataStats.MODE: 0.0,
        DataStats.CANDIDATE_COUNT: 1,
        DataStats.DEV: 0.0,
        DataStats.STD_DEV: 0.0,
        DataStats.QUARTILE: [],  # four values
        DataStats.DECILE: [],  # ten values
        DataStats.HISTOGRAM: [],  # member as tuple of (lower_bound, upper_bound, feq)
        DataStats.EMPTY_RATIO: 0.0,  # the ratio of rows with empty value to all rows
        DataStats.ABNORMAL_RATIO: 0.0  # ratio of rows with abnormal values to all rows
    }
    extra = {}  # user defined metadata

    def __init__(
        self,
        column_name,
        column_datatype,
        column_value_category=ValueCategory.NUMERIC,
        column_role=DataRole.FACTOR,
        column_name_lc='',
        column_desc='',
        column_stat={},
        extra={}
    ):
        """

        :param column_name: column name represented with ascii characters
        :type column_name: str
        :param column_datatype: basic datatype of the column, using Enumerate, such as int, string, etc
        :type column_datatype: data_enums.BasicDatatype
        :param column_value_category: semantic category of the values in the columns, using Enumerate, such as temporal,
            spatial, numeric, etc.
        :type column_value_category: data_enums.ValueCategory
        :param column_role: column role in model training/testing/validating, using Enumerate, such as factor value to
            describe the sample or response value (the class/category of the sample for classification problems, or a
            continuous value for prediction problems)
        :param column_name_lc: column name represented with localized characters
        :type column_name_lc: str encoded with Unicode(UTF-8)
        :param column_desc: column description
        :type column_desc: str
        :param column_stat: statistics of values in the column. there are different sets of statistics for different
            value categories, i.e., for numeric value, MEAN, MODE, MEDIAN, etc. are meaningful. This field is supposed
            to be populated by the outer container, i.e., DataContainer
        :type column_stat: dict(data_enums.DataStats, object), the value type depends on data_enums.DataStats
        :param extra: user defined metadata container, it contents TOTALLY depends user -- you produce, consume the
            contents, and you handle all possible situations associated with the contents
        :type extra: dict(str, obj)

        """
        self.column_name = column_name
        self.column_datatype = column_datatype
        self.column_value_category = column_value_category
        self.column_role = column_role
        self.column_name_lc = column_name_lc
        self.column_desc = column_desc
        self.column_stat = column_stat
        self.extra = extra

    def fill_up_stat(self, column_stat):
        """
        Fill up column statistics

        :param column_stat: dictionary of stat values
        :type column_stat: dict(DataStats, obj)
        :return:
        """
        if column_stat and isinstance(column_stat, dict):
            for key in column_stat.keys():
                self.column_stat[key] = column_stat[key]
        else:
            raise ValueError("Invalid column_stat value")

    def set_column_stat(self, stat_key, stat_value):
        if stat_key and isinstance(stat_key, DataStats) and stat_value:
            self.column_stat[stat_key] = stat_value
        else:
            raise ValueError("Invalid stat_key or stat_value!")

    def get_column_stat(self, stat_key):
        if stat_key and isinstance(stat_key, DataStats):
            if stat_key in self.column_stat:
                return self.column_stat[stat_key]
            else:
                return None
        else:
            raise ValueError("Invalid stat_key!")

    def clear_column_stat(self):
        self.column_stat.clear()

    def fill_up_extra(self, extra):
        if extra and isinstance(extra, dict):
            for key in extra.keys():
                self.extra[key] = extra[key]
        else:
            raise ValueError("Invalid extra value!")

    def set_extra(self, extra_key, extra_value):
        if extra_key and isinstance(extra_key, str) and extra_value:
            self.extra[extra_key] = extra_value
        else:
            raise ValueError("Invalid extra_key or extra_value!")

    def get_extra(self, extra_key):
        if extra_key and isinstance(extra_key, str):
            if extra_key in self.extra:
                return self.extra[extra_key]
            else:
                return None
        else:
            raise ValueError("Invalid extra_key!")

    def clear_extra(self):
        self.extra.clear()

    def load_column_metadata(
        self,
        metadata_store_type=MetadataStoreType.LOCAL_FILE,
        *args
    ):
        """
        Factory method to load column metadata from metadata store
        Concrete load action are delegated to methods behind the scene based on metadata_store_type

        :param metadata_store_type: type of the facility to store metadata store, i.e., a file on local file system,
            a file on some DFS, a table(or table-like entinty) in some RDBMS/NON-SQL DB
        :type metadata_store_type: data_enums.MetadataStoreType
        :param args: list of arguments to retrieve metadata. the type and count of arguments depend on
            metadata_store_type, i.e., for local file, args includes a string(containing path and file name), for remote
            file, args may include a string(containing protocol, domain name, path and file name), user_id/password(if
            necessary), for rdbms, args may include a connection string, user_id/password, or a connection object,
            table name
        :return:
        """
        pass

    # TODO: Define concrete load_column_metadata

    def save_column_metadata(
        self,
        metadata_store_type=MetadataStoreType.LOCAL_FILE,
        *args
    ):
        """
        Factory method to save column metadata to metadata store
        :param metadata_store_type:
        :param args:
        :return:
        """
        pass

    # TODO: Define concrete save_column_metadata


class DataSetMetadata:
    def __init__(
        self,
        data_set_name,
        data_set_type,
        data_set_role=DatasetRole.TRAINING,
        data_set_name_lc='',
        data_set_desc='',
        data_set_stat={},
        extra={},
        columns=[]
    ):
        self.data_set_name = data_set_name
        self.data_set_type = data_set_type
        self.data_set_role = data_set_role
        self.data_set_name_lc = data_set_name_lc
        self.data_set_desc = data_set_desc
        self.data_set_stat = data_set_stat
        self.extra = extra
        self.columns = columns

    def get_column_names(self):
        col_name = []
        if self.columns:
            for item in self.columns[:]:
                col_name.append(item.column_name)
        return col_name

    def get_column_names(self, pattern):
        
    # TODO: Define class methods, just like methods in ColumnMetadata

