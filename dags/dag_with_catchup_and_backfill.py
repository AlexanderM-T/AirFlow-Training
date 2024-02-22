"""
Aqui se ejecuta un dag con dos diferencias:

catchup=True -> permite que el dag se ejecute para las fechas anteriores
a la fecha de inicio especificada.

catchup=False -> hace que el dag solo se ejecute para la fecha de inicio
especificada y las fechas futuras, las pasadas no se ejecutaran automaticamente.

Ahora, para hacer un backfill se utilizan los comandos

Para ver la ID del container de apache (el scheduler) -> docker ps
Para entrar al bash del contenedor -> docker exec -it id_del_container bash
Para ejecutar el backfill -> airflow dags backfill -s year-month-day -e year-month-day dag_id

Las flags -s y -e significan start y end para las fechas, se debe reemplazar con las que se desean

"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'diego',
    'retries':5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id = 'dag_with_catchup_backfill_v02',
    default_args=default_args,
    start_date=datetime(2024,2,1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command='echo This is a simple bash command!'
    )