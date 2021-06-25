from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

# EJERCICIO1

test = DAG(
    dag_id='test',
    default_args=defaults_args,
    start_date=datetime(2021, 6, 25, 3, 0, 0),
    schedule_interval=timedelta(1))
# EJERCICIO2

start = DummyOperator(
    task_id='start'
)

end = DummyOperator(
    task_id='end'
)



# NUNCA TRABAJE CON AIRFLOW Y ESTOY TENIENDO PROBLEMAS PARA INSTALAR EL DOCKER, HE REALIZADO LO QUE HE PODIDO EN CUANTO A CODIGO.

# EJERCICIO5
# Los hooks son interfaces para plataformas y bases de datos externas como Hive, S3, MySQL, PostgreS...
# El hook es que realiza el get_connection y para conseguir la conexion y la conexion como
# su palabra indica es la union a la plataforma o base de datos externa (con un numero de id).
