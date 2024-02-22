"""
Aqui se ejecuta un dag con el operador de postgres y se hacen
queries a la base de datos en las tasks,
hay que tener en cuenta que se debe cambiar la seccion de
services en el archivo yaml para especificar las credenciales
de la conexion.
"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'diego',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    default_args = default_args,
    dag_id = 'dag_with_postgres_operator_v3',
    start_date = datetime(2024,2,20),
    schedule_interval = '0 0 * * *'
) as dag:
    
    # aqui se podria quitar la query de drop table y cambiar a
    # create table if not exists
    # para evitar perder registros que se tengan de antes
    task1 = PostgresOperator(
        task_id = 'create_postgres_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            drop table if exists dag_runs;

            create table dag_runs (
                dt date,
                dag_id character varying,
                primary key (dt, dag_id)
            )
        """
    )

    # Aqui dt y dag_id los provee nativamente airflow y se puede
    # acceder a ellos con las dobles llaves
    task2 = PostgresOperator(
        task_id = 'insert_into_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            insert into dag_runs (dt, dag_id) values('{{ ds }}', '{{ dag.dag_id }}')
        """
    )

    task3 = PostgresOperator(
        task_id = 'delete_data_from_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            delete from dag_runs where dt = '{{ ds }}' and dag_id = '{{ dag.dag_id }}';
        """
    )

    # Es importante tener un task que elimine registros porque
    # puede que al limpiar un dag airflow intente meter registros
    # que ya existen

    task1 >> task3 >> task2
    