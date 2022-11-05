from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'depends_on_past': True,
    'retries': 3,
    'retry_delay': timedelta(seconds=30),
}

with DAG(
        dag_id="example_dag_3",
        start_date=datetime(2022, 6, 20),
        schedule_interval="*/1 * * * *",
        default_args=default_args,
        catchup=False
) as dag:
    command = """
    VAR=$(($RANDOM % 2))
    echo $VAR
    if [[ $VAR -eq 1 ]]
    then
      exit 1
    else
      exit 0
    fi
    """

    t1 = BashOperator(
        task_id='random',
        bash_command=command
    )