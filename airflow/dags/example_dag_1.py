from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="example_dag_1",
    start_date=datetime(2022, 6, 20),
    schedule_interval="*/1 * * * *"
) as dag:
    t1 = BashOperator(
        task_id='hello_world',
        bash_command='echo "Hello World!"'
    )