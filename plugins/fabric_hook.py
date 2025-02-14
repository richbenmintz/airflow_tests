from airflow.plugins_manager import AirflowPlugin
from apache_airflow_microsoft_fabric_plugin_rbm.hooks.fabric import FabricHook
from apache_airflow_microsoft_fabric_plugin_rbm.operators.fabric import FabricRunItemLink

class AirflowFabricPlugin(AirflowPlugin):
    name = "fabric_plugin"
    operator_extra_links = [FabricRunItemLink()]
    hooks = [
          FabricHook,
      ]