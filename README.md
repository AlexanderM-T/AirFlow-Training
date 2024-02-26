# Airflow Module

## Airflow basics and core concepts

### **What is Airflow?**

- Starts in Airbnb 2014
- Manage complex workflows
- Top-level apache project 2019
- Workflow management platform
- Written in python

### **What is a workflow?**

Is a sequence of tasks, in airflow is defined as DAG.

Directed Acyclic Graph.

DAG is a collection of all the tasks you want to run, organized in
a way that reflects their relationships and dependencies.

### **What is the task?**

A task defines an unit of work within a DAG.

It is represented as a node in the DAG graph and it is written in python. 

The task implements an operator.

The goal of the task is to achieve a specific thing, the method it
uses is called operator.

### **What is an operator?**

Operators determine what actually gets done by a task. What is
going to be done.

In Airflow, there are many kinds of operators, like BashOperator,
PythonOperator, and also customized operators.

Each task is an implementation of an operator, for example a
PythonOperator to execute some Python code, or a BashOperator to
run a bash command.

### **Execution Date**

The execution date is the logical date and time which the DAG run, and its tasks instances are running for.

### **Task Instance**

A task instance is a run of a task at a specific point of time (execution date).

### **Dag Run**

A dag run is an instantiation of a dag, containing task instances that run for a specific execution date.

![Untitled](Airflow%20Module%207f7ec01e4c5a4cae88001215dcf4cb62/Untitled.png)

## Airflow Task Lifecycle

When a DAG run is triggered. Its tasks are going to be executed one after another according to their dependencies.

Each task will go through different stages from start to completion. 

Every stage indicates a specific status of the task instance. For example, when the task is in progress, its status is running, when the task has been finished, it has a success status and so on.

A task is usually starting with ‘No Status’ which means the scheduler created an empty task instance.

After that there are 4 different stages that the task can be moved to; **scheduled**, **removed**, **upstream failed** or **skipped**.

![Untitled](Airflow%20Module%207f7ec01e4c5a4cae88001215dcf4cb62/Untitled%201.png)

## Basic Architecture

![Untitled](Airflow%20Module%207f7ec01e4c5a4cae88001215dcf4cb62/Untitled%202.png)

## Postgres connection (generally any service)

We have to add the port range at services section in our yaml file

![Untitled](Airflow%20Module%207f7ec01e4c5a4cae88001215dcf4cb62/Untitled%203.png)

Then we can re create the container with: `docker-compose up -d --no-deps --build postgres`

**Important! → When you installed postgres if you defined an user and a password, then you have to put those credentials here in the environment section OR you can create a new user called airflow with password airflow and give it the necessary access.**

Then we create a connection in Airflow before we already have the database and the connection in our system established.

![Untitled](Airflow%20Module%207f7ec01e4c5a4cae88001215dcf4cb62/Untitled%204.png)

Templates reference in → [https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html)

## Ways to install python packages to airflow docker containers

Basically there are two different ways to do it, extending and customizing. Here are some pros and cons of each:

![Untitled](Airflow%20Module%207f7ec01e4c5a4cae88001215dcf4cb62/Untitled%205.png)

To extend we have to copy in a requirements.txt the libraries we need to use and then create a Dockerfile with the following content:

![Untitled](Airflow%20Module%207f7ec01e4c5a4cae88001215dcf4cb62/Untitled%206.png)

And then, extend the container with: `docker build . --tag extending_airflow:latest`

Do not forget to change the image name in the yaml file: `image:${AIRFLOW_IMAGE_NAME:-extending_airflow:latest}`

Finally, when the dag is ready, we have to restart the webserver and the scheduler as we changed the image, it is done with: `docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler`

The other way is to literally cloning into your machine the entire airflow repository from GitHub, making a requirements.txt file and launching it (personally i think that is not quite clean and no that easy to use).

Anyway if you want to do it, the requirements.txt goes in the docker-context-files directory and to build the container run → `docker build . --build-arg AIRFLOW_VERSION='2.0.1' --tag customising_airflow:latest`

## Unknown terms

**Cron Expression →** is a string comprising five fields separated by a white space that represents a set of times normally as a schedule to execute some routine

![Untitled](Airflow%20Module%207f7ec01e4c5a4cae88001215dcf4cb62/Untitled%207.png)

![Untitled](Airflow%20Module%207f7ec01e4c5a4cae88001215dcf4cb62/Untitled%208.png)

Useful website for making cron expressions → [https://crontab.guru/](https://crontab.guru/)

## Bash Commands

**To run airflow containers:** `docker-compose up -d`

**To shutdown the airflow and remove the volumes:** `docker-compose down -v`

**To create a new user:** `docker-compose run airflow-worker airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin`

**To eliminate an user:** `airflow users delete --username nombre_de_usuario`

**To see if airflow is running:** `docker ps`

## Code examples in:

[https://github.com/AlexanderM-T/AirFlow-Training](https://github.com/AlexanderM-T/AirFlow-Training)

## Caption

All the material was took and adapted from: [https://www.youtube.com/watch?v=K9AnJ9_ZAXE](https://www.youtube.com/watch?v=K9AnJ9_ZAXE)