from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator


def print_hello(value):
    print(f'hello {value}')

default_args = {
    'start_date': datetime(2023, 3, 1)
}

with DAG(
    dag_id='test',
    schedule_interval = '0 6 * * *',
    catchup=False,
    default_args = default_args
) as dag:

    run_start = EmptyOperator(
        task_id = 'run_start'
    )

    run_bash = BashOperator(
        task_id = 'run_bash',
        bash_command = 'start project'
    )
    
    run_bash2 = BashOperator(
        task_id = 'run_bash2',
        bash_command='start data processing'
    )

    run_python = PythonOperator(
        task_id = 'run_python',
        python_callable = print_hello,
        op_kwargs = {'value': 'data_test'},
        dag=dag
    )

    run_last = EmptyOperator(
        task_id = 'run_last'
    )

    run_start >> [run_bash, run_bash2, run_python] >> run_last