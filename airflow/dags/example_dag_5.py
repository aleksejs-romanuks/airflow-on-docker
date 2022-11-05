# from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
# from airflow.contrib.sensors.file_sensor import FileSensor
# from airflow import DAG
# from datetime import datetime
# from airflow.models import Variable

# with DAG(
#     dag_id="example_dag_5",
#     start_date=datetime(2022, 6, 20),
#     schedule_interval=None,
#     catchup=True
# ) as dag:

#     # air_quality: {"source": "/home/ubuntu/airflow_workspace/resources/WHO_air_data_quality.csv", "target": "/home/ubuntu/airflow_workspace/target/air_quality"}
#     variable = Variable.get("air_quality", deserialize_json=True)
    
#     source = variable["source"]
#     target = variable["target"]

#     file_sensor = FileSensor(
#         task_id= "file_sensor_task", 
#         poke_interval= 30,  
#         filepath= source 
#     )

#     # spark_local: host = local
#     submit_job = SparkSubmitOperator(
#         application="/home/ubuntu/airflow_workspace/spark-apps/air_quality_data_partitioning.py", 
#         task_id="spark-airquality-partitioning",
#         conn_id="spark_local",
#         application_args=[source, target]
#     )

#     file_sensor >> submit_job