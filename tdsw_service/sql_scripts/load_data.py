from . import init
from . import data
from . import select
from django.db import connections
from cfg import con
import time

ty = con.get_node()


def with_connection(t):
    def wrapper(func):
        def inner(*args, **kwargs):
            new_t = t if t is not None else con.get_node()
            conn = connections[new_t].cursor()
            with conn as curr:
                kwargs["curr"] = curr
                return func(*args, **kwargs)

        return inner

    return wrapper


sel = {"Врачи": select.select_doctors, "Организации": select.select_orgs, "Рабочие": select.select_workers,
       "Записи": select.select_records, "Осмотры": select.select_inspections,
       "Справочник профессий": select.select_spec_book, "Типы профосомтров": select.select_insp_types}

reps = {"Отчеты": [select.report_visit, select.repost_health, select.report_comps]}
report_fields = {"visit": ["name", "count"],
                 "health": ["result", "count"],
                 "comps": ["complaints", "count"]}
fields = {"Организации": ["id", "name", "location", "inn", "ogrn", "exp_date"],
          "Врачи": ["id", "name", "lastname", "surname", "phone", "shils", "oms", "email", "category", "hiring_date",
                    "dismissal_date", "diploma_number", "specialisation"],
          "users": ["login", "password", "category"],
          "Рабочие": ["id", "name", "lastname", "surname", "phone", "shils", "oms", "email",
                      "tid", "organization", "position", "profession"],
          "Записи": ["id", "appointment_date", "prof_type_name", "worker_name", "worker_lastname",
                     "worker_surname", "tid", "position", "profession"],
          "Осмотры": ["id", "complaints", "result", "worker_name", "worker_lastname", "worker_surname", "tid",
                      "position", "profession"],
          "Справочник профессий": ["id", "name"],
          "Типы профосомтров": ["id", "name"]}
keys = {"Организации": "organizations"}


@with_connection("default")
def create_tables(**kwargs):
    curr = kwargs["curr"]
    master = init.create_master
    for m in master:
        curr.execute(m)


@with_connection("default")
def alter_master(**kwargs):
    curr = kwargs["curr"]
    master = init.alter_master
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


@with_connection("slave")
def select_med_orgs(**kwargs):
    curr = kwargs["curr"]
    data = select.select_med
    curr.execute(data)
    res = curr.fetchall()
    return res


@with_connection("slave")
def insert_persons(**kwargs):
    curr = kwargs["curr"]
    d = data.persons_data
    p = data.another_persons
    for i in d:
        # time.sleep(0.6)
        curr.execute(i)
    for j in p:
        time.sleep(0.6)
        curr.execute(j)
    return


@with_connection(ty)
def select_data(t, **kwargs):
    curr = kwargs["curr"]
    data = sel[t]
    curr.execute(data)
    res = curr.fetchall()
    result = [{fields[t][i]: row[i] for i in range(len(row))} for row in res]
    return result


def def_t(j: int):
    if j == 0:
        return "visit"
    elif j == 1:
        return "health"
    return "comps"


@with_connection("default")
def select_report(w, **kwargs):
    data = {}
    curr = kwargs["curr"]
    r = reps[w]
    for j, q in enumerate(r):
        curr.execute(q)
        res = curr.fetchall()
        t = def_t(j)
        result = [{report_fields["visit"][i]: row[i] for i in range(len(row))} for row in res]
        data.update({t: result, f"ids_{t}": [l for l in range(1, len(result) + 1)]})
    return data


@with_connection(ty)
def select_user(login, psw, **kwargs):
    curr = kwargs["curr"]
    user = select.get_user(login)
    curr.execute(user)
    res = curr.fetchall()
    if not res:
        return {}, False
    result = [{fields["users"][i]: row[i] for i in range(len(row))} for row in res]
    if psw != result[0]["password"]:
        return {}, False

    return result[0], True
