from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'diego',
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_sklearn():
    import sklearn
    print(f'Hi! Scikit-learn with version: {sklearn.__version__}')

def get_matplotlib():
    import matplotlib
    print(f'Hi! Matplitlib with version: {matplotlib.__version__}')


with DAG(
    default_args = default_args,
    dag_id = 'dag_with_python_dependencies_v02',
    start_date = datetime(2024,2,21),
    schedule_interval = '@daily'
) as dag:
    
    get_sklearn = PythonOperator(
        task_id = 'get_sklearn',
        python_callable = get_sklearn
    )
    get_sklearn

    get_matplotlib = PythonOperator(
        task_id = 'get_matplotlib',
        python_callable = get_matplotlib
    )


