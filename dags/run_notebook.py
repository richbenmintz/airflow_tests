from __future__ import annotations
from airflow import DAG
from apache_airflow_microsoft_fabric_plugin_rbm.operators.fabric import FabricRunItemOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
}

with DAG(
    dag_id="fabric_items_dag",
    default_args=default_args,
    schedule_interval="@daily",
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
                        "_inlineInstallationEnabled": {
                            "value": "True",
                            "type": "bool"
                        },
                        "Param_1": {
                            "value": "Value",
                            "type": "string"
                        }
                }
                
    )
    
    run_fabric_item
