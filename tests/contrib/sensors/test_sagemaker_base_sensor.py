# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import unittest

from airflow import configuration
from airflow.contrib.sensors.sagemaker_base_sensor import SageMakerBaseSensor
from airflow.exceptions import AirflowException


class TestSagemakerBaseSensor(unittest.TestCase):
    def setUp(self):
        configuration.load_test_config()

    def test_subclasses_succeed_when_response_is_good(self):
        class SageMakerBaseSensorSubclass(SageMakerBaseSensor):
            def non_terminal_states(self):
                return ['PENDING', 'RUNNING', 'CONTINUE']

            def failed_states(self):
                return ['FAILED']

            def get_sagemaker_response(self):
                return {
                    'SomeKey': {'State': 'COMPLETED'},
                    'ResponseMetadata': {'HTTPStatusCode': 200}
                }

            def state_from_response(self, response):
                return response['SomeKey']['State']

        sensor = SageMakerBaseSensorSubclass(
            task_id='test_task',
            poke_interval=2,
            aws_conn_id='aws_test'
        )

        sensor.execute(None)

    def test_poke_returns_false_when_state_is_a_non_terminal_state(self):
        class SageMakerBaseSensorSubclass(SageMakerBaseSensor):
            def non_terminal_states(self):
                return ['PENDING', 'RUNNING', 'CONTINUE']

            def failed_states(self):
                return ['FAILED']

            def get_sagemaker_response(self):
                return {
                    'SomeKey': {'State': 'PENDING'},
                    'ResponseMetadata': {'HTTPStatusCode': 200}
                }

            def state_from_response(self, response):
                return response['SomeKey']['State']

        sensor = SageMakerBaseSensorSubclass(
            task_id='test_task',
            poke_interval=2,
            aws_conn_id='aws_test'
        )

        self.assertEqual(sensor.poke(None), False)

    def test_poke_raise_exception_when_method_not_implemented(self):
        class SageMakerBaseSensorSubclass(SageMakerBaseSensor):
            def non_terminal_states(self):
                return ['PENDING', 'RUNNING', 'CONTINUE']

            def failed_states(self):
                return ['FAILED']

        sensor = SageMakerBaseSensorSubclass(
            task_id='test_task',
            poke_interval=2,
            aws_conn_id='aws_test'
        )

        self.assertRaises(AirflowException, sensor.poke, None)

    def test_poke_returns_false_when_http_response_is_bad(self):
        class SageMakerBaseSensorSubclass(SageMakerBaseSensor):
            def non_terminal_states(self):
                return ['PENDING', 'RUNNING', 'CONTINUE']

            def failed_states(self):
                return ['FAILED']

            def get_sagemaker_response(self):
                return {
                    'SomeKey': {'State': 'COMPLETED'},
                    'ResponseMetadata': {'HTTPStatusCode': 400}
                }

            def state_from_response(self, response):
                return response['SomeKey']['State']

        sensor = SageMakerBaseSensorSubclass(
            task_id='test_task',
            poke_interval=2,
            aws_conn_id='aws_test'
        )

        self.assertEqual(sensor.poke(None), False)

    def test_poke_raises_error_when_job_has_failed(self):
        class SageMakerBaseSensorSubclass(SageMakerBaseSensor):
            def non_terminal_states(self):
                return ['PENDING', 'RUNNING', 'CONTINUE']

            def failed_states(self):
                return ['FAILED']

            def get_sagemaker_response(self):
                return {
                    'SomeKey': {'State': 'FAILED'},
                    'ResponseMetadata': {'HTTPStatusCode': 200}
                }

            def state_from_response(self, response):
                return response['SomeKey']['State']

        sensor = SageMakerBaseSensorSubclass(
            task_id='test_task',
            poke_interval=2,
            aws_conn_id='aws_test'
        )

        self.assertRaises(AirflowException, sensor.poke, None)


if __name__ == '__main__':
    unittest.main()
