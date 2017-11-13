# -*- coding: utf-8 -*-
#
# Top level package of Data Factory by 3Golden.
# This package is expanded from Airflow basic facility, and uses its definitions of DAG, hook, operator, task, etc.
# In this package, the followings are defined:
# 1. Dataframe container, including abstract class and implementation with pandas, H2O, spark...
# 2. Piped operators, there are dataframes or their references transferred between these operators
# 3. Hooks, which handle some common interactions to some third party facilities, such as dfs, rdbms, non-sql db,
#    framework, service, etc.
