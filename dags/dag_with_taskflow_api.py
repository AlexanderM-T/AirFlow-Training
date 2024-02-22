"""
Aqui se ejecuta un dag con la api taskflow
lo mismo que en el fichero create_dag_with_python_operator
pero de una manera mas sencilla y utilizando los
decoradores @dag y @task

"""

from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    'owner':'diego',
    'retries':5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='dag_with_taskflow_api_v02',
     default_args = default_args,
     start_date=datetime(2024,2,20),
     schedule_interval='@daily')
def hello_world_etl():
    
    # Si no quiero los multiple outputs
    # simplemente quito el argumento
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name':'Diego',
            'last_name': 'Munera'
        }
    
    @task()
    def get_age():
        return 21
    
    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World! My name is {first_name} {last_name} and I am {age} years old!")

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'],
          last_name=name_dict['last_name'], 
          age=age)

greet_dag = hello_world_etl()
