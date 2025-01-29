from airflow.plugins_manager import AirflowPlugin

from apache_airflow_microsoft_fabric_plugin.hooks.fabric import FabricHook
from apache_airflow_microsoft_fabric_plugin.operators.fabric import FabricRunItemLink

class AirflowFabricPlugin(AirflowPlugin):
    """
    Microsoft Fabric plugin.
    """

    name = "fabric_plugin"
    operator_extra_links = [FabricRunItemLink()]
    hooks = [
        FabricHook,
    ]