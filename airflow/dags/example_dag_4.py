from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator

default_args = {
    'depends_on_past': True,
    'retries': 3,
    'retry_delay': timedelta(seconds=30),
}

with DAG(
        dag_id="example_dag_4",
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

    random_operator = BashOperator(
        task_id='random',
        bash_command=command
    )

    def branching_condition(**kwargs):
        task_instance = kwargs['ti']
        exit_code = task_instance.xcom_pull(task_ids='random')
        return "all_good" if exit_code == "0" else "issue_found"


    branch_operator = BranchPythonOperator(
        task_id='branch',
        python_callable=branching_condition,
        provide_context=True,
        trigger_rule='all_done'
    )

    all_good_operator = DummyOperator(task_id="all_good")
    issue_found_operator = DummyOperator(task_id="issue_found")

    random_operator >> branch_operator
    branch_operator >> all_good_operator
    branch_operator >> issue_found_operator