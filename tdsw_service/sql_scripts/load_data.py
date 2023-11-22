from . import init
from . import data
from django.db import connections


def with_connection(t):
    def wrapper(func):
        def inner(*args, **kwargs):
            conn = connections[t].cursor()
            print(t)
            with conn as curr:
                kwargs["curr"] = curr
                return func(*args, **kwargs)

        return inner

    return wrapper


@with_connection("default")
def create_tables(**kwargs):
    curr = kwargs["curr"]
    master = init.create_master
    for m in master:
        curr.execute(m)


@with_connection("slave")
def alter_slave(**kwargs):
    curr = kwargs["curr"]
    slave = init.alter_slave
    for s in slave:
        curr.execute(s)


@with_connection("default")
def insert_data(**kwargs):
    curr = kwargs["curr"]
    all_data = data.all_data
    for d in all_data:
        curr.execute(d)
    return


@with_connection("slave")
def insert_slave_data(**kwargs):
    curr = kwargs["curr"]
    d = data.slaves_data
    for i in d:
        curr.execute(i)
    return
