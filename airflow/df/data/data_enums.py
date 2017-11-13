# -*- coding: utf-8 -*-
# Data type enumerates

from enum import Enum


class BasicDatatype(Enum):
    INTEGER = 'int'
    LONG = 'long'
    FLOAT = 'float'
    DOUBLE = 'double'
    DECIMAL = 'decimal'
    STRING = 'string'


class DataSetType(Enum):
    PANDAS_DF = 'pandas_dataframe'
    H2O_DF = 'h2o_dataframe'
    SPARK_DF = 'spark_dataframe'
    SPARK_RDD = 'spark_rdd'


class ValueCategory(Enum):
    IDENTIFICATIONAL = 'identificational'
    TEMPORAL = 'temporal'
    SPATIAL = 'spatial'
    NUMERIC = 'numeric'
    CATEGORIAL = 'categorial'


class DimensionType(Enum):
    UNKNOWN = 'unknown'
    LENGTH = 'length'
    AREA = 'area'
    VOLUME = 'volume'
    TIME_INTERVAL = 'time_interval'
    CURRENCY = 'currency'


class DataStats(Enum):
    ROW_COUNT = 'row_count'
    COLUMN_COUNT = 'column_count'
    MEAN = 'mean'
    MEDIAN = 'median'
    MODE = 'mode'
    CANDIDATE_COUNT = 'candidate_count'
    DEV = 'deviation'
    STD_DEV = 'standard_deviation'
    QUARTILE = 'quartile'
    DECILE = 'decile'
    HISTOGRAM = 'histogram'
    EMPTY_RATIO = 'empty_ratio'
    ABNORMAL_RATIO = 'abnormal_ratio'


class DatasetRole(Enum):
    TRAINING = 'training'
    TESTING = 'testing'
    VALIDATING = 'validating'


class DataRole(Enum):
    NO_USE = 'no_use'
    FACTOR = 'factor_value'
    RESPONSE = 'response_value'


class MetadataStoreType(Enum):
    LOCAL_FILE = 'local_file'
    REMOTE_FILE = 'remote_file'
    DATABASE = 'database'




