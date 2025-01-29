from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from apache_airflow_microsoft_fabric_plugin.operators.fabric import FabricRunItemOperator

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

# Instantiate the DAG object
with DAG(
     dag_id="Run_Fabric_Item",
     schedule_interval="@daily",
     start_date=datetime(2023, 8, 7),
     catchup=False,
 ) as dag:

     run_fabric_item = FabricRunItemOperator(
         task_id="run_fabric_item",
         fabric_conn_id="fabric-conn",
         workspace_id="7157d32b-5d50-4125-bb55-8c60f27cccbd",
         item_id="2e2a1f50-8e2e-4419-b7e6-121865897ef1",
         job_type="RunNotebook",
         wait_for_termination=True,
         deferrable=True,
         job_params={
                            "executionData": {
                                "parameters": {
                                "_inlineInstallationEnabled": {
                                    "value": "True",
                                    "type": "bool"
                                },
                                "Param_1": {
                                    "value": "Value",
                                    "type": "string"
                                }
                            }
                            }
                            }
     )

     run_fabric_item
