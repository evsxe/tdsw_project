from ._names import __names_local, __names_global
import random
import json

# РОК
prof_types_data = {"id": [i for i in range(1, 11)],
                   "name": [random.choice(["Общего назначений",
                                           "Производства Класса A",
                                           "Производства Класса B",
                                           "Производства Класса C"]) for _ in range(1, 11)]}

# РОК
specialization_book_data = {"id": [i for i in range(1, 31)],
                            "name": [random.choice(["кардиолог",
                                                    "отоларинголог",
                                                    "терапевт",
                                                    "врач мануальной терапии",
                                                    "рефлексотерапевт-невролог",
                                                    "психиатр",
                                                    "психиатр-нарколог",
                                                    "гематолог",
                                                    "Рентгенолаборант",
                                                    "дерматовенеролог",
                                                    "уролог",
                                                    "офтальмолог",
                                                    "ревматолог",
                                                    "акушер-гинеколог"
                                                    ]) for _ in range(1, 31)]}
# РБОК
orgs_data = {"id": [i for i in range(50000, 50004)],
             "name": [
                 "Медучреждение1",
                 "ПАО МОСэнерго",
                 "ПАО РКС",
                 "ПАО Роснефть"],
             "location": ["г. Москва",
                          "г. Москва,",
                          "г. Москва,",
                          "г. Москва,"],
             "inn": ["564646454", "45345242", "4242424", "5213131"],
             "ogrn": ["43424242", "0039393", "3252529", "42423456"],
             }

# ЛТ, РКД
agreement_data = {"id": [i for i in range(50000, 50003)],
                  "hospital_id": [50000, 50000, 50000],
                  "factory_id": [50001, 50002, 50003],
                  "doc_path": [" " for _ in range(3)],
                  "exp_date": ["2025-01-01 00:00:00" for _ in range(3)]}

# РБОК
people_data = {"id": [i for i in range(50000, 50009)],
               "name": ["Ольга", "Антон", "Томара", "Дмитрий", "Борис", "Root", "Bob", "Alice", "Tim"],
               "lastname": ["Иванова", "Сергеев", "Сидоров", "Петров", "Борисыч", "Rootov", "Alice", "Tim", "Tim"],
               "surname": ["Олеговна", "Сергеевич", "Ивановна", "Борисович", "Tim", "Rootovich", "Bob", "Alice", "Tim"],
               "phone": ["+79152039832", "+79142039832", "+79252039432", "+79154032832", "+7945039832",
                         "+7900039832", "731342039832", "79452039832", "79452039832"],
               "shils": ["4758353853", "475844253853", "4345353853", "4758566853", "47580099853", "303029292",
                         "4098353853", "4424242321", "4049930300"],
               "oms": ["475800000253", "470282002253853", "434535232433853", "470942566853", "4758121230853", "303029292",
                       "303029292", "3029292033", "303029292"],
               "email": ["email" for _ in range(50000, 50009)],
               "is_superuser": [False, False, False, False, False, True, False, False, False],
               "category": ["med_admin", "doctor", "doctor", "doctor", "doctor", "superuser", "worker",
                            "worker", "worker"],
               "login": ["madmin", "test_d1", "test_d2", "test_d3", "test_d4", "root", "alic", "bob", "tim"],
               "password": ["1234", '1234', "1234", '1234', "1234", "root", "alic", "alic", "alic"]
               }

worker_data = {"id": [i for i in range(50000, 50003)],
               "person_id": [50006, 50007, 50008],
               "tid": ["1", "2", "3"],
               "organization_id": [50001, 50001, 50001],
               "position": ["мастер", "главный бухгалтер", "секретарь"],
               "hiring_date": ["2018-03-05 00:00:00",
                               "2016-01-10 00:00:00", "2019-04-03 00:00:00"],
               "dismissal_date": ["2027-01-10 00:00:00", "2027-01-10 00:00:00", "2027-01-10 00:00:00"],
               "profession": ["сварщик", "специалист по финансового отдела", "ведущий специалист"]
               }

# РБОК
specialization_data = {"id": [i for i in range(50000, 50004)],
                       "person_id": [i for i in range(50001, 50005)],
                       "profession_id": [1, 3, 10, 12],
                       "diploma_date": ["2012-11-01 00:00:00", "2013-03-05 00:00:00",
                                        "2014-01-10 00:00:00", "2015-04-03 00:00:00"],
                       "diploma_number": ["00991232", "267271", "334354", "282828"]}

# ЛТ, РКД
doctors_data = {"id": [i for i in range(50000, 50004)],
                "person_id": [i for i in range(50001, 50005)],
                "hospital_id": [50000, 50000, 50000, 50000],
                "hiring_date": ["2017-11-11 00:00:00", "2018-03-05 00:00:00",
                                "2016-01-10 00:00:00", "2019-04-03 00:00:00"],
                "dismissal_date": ["2027-01-10 00:00:00", "2027-01-10 00:00:00", "2027-01-10 00:00:00", "2027-01-10 00:00:00"]}

inspection_record_data = {"id": [50000, 50001, 50002],
                          "appointment_date": ["2023-03-05 00:00:00",
                                               "2023-01-10 00:00:00", "2023-04-03 00:00:00"],
                          "type_id": [1, 4, 6],
                          "worker_id": [50000, 50001, 50002]}

inspections_data = {"id": [i for i in range(50000, 50012)],
                    "data": [json.dumps({}) for _ in range(50000, 50012)],
                    "complaints": ["колющая боль в сердце", "колющая боль в сердце", "жалоб нет", "жалоб нет",
                                   "жалоб нет", "раздражения кожи на руке", "раздражения кожи на руке", "жалоб нет",
                                   "жалоб нет", "жалоб нет", "жалоб нет", "жалоб нет"],
                    "prof_inspection_id": [50000, 50000, 50000, 50000, 50001, 50001, 50001, 50001, 50002, 50002, 50002,
                                           50002],
                    "result": ["требует дополнительного исследования", "проблемы с сердцем", "здоров", "здоров",
                               "здоров", "проблемы с кожей", "проблемы с кожей", "здоров",
                               "здоров", "здоров", "здоров", "здоров"],
                    "doctor_id": [50000, 50001, 50002, 50003, 50000, 50001, 50002, 50003, 50000, 50001, 50002, 50003],
                    "name": ["прием у кардиолога", "прием у тепапевта", "прием у дерматолога", "прием у офтальмолога",
                             "прием у кардиолога", "прием у тепапевта", "прием у дерматолога", "прием у офтальмолога",
                             "прием у кардиолога", "прием у тепапевта", "прием у дерматолога", "прием у офтальмолога"]}


def insert(table_name, data):
    res = []
    for i in range(len(data["id"])):
        q1 = f"""INSERT INTO {table_name} {tuple(data.keys())}"""
        q2 = f"""VALUES {tuple([data[k][i] for k, _ in data.items()])};"""
        q1 = q1.replace("'", "`")
        q = q1 + " " + q2
        res.append(q)
    return res


prof_types = insert(__names_global["prof_types"], prof_types_data)
specialization_book = insert(__names_global["specialization_book"], specialization_book_data)

orgs = insert(__names_local["organizations"], orgs_data)
argem = insert(__names_local["agreement"], agreement_data)

all_data = prof_types + specialization_book
slaves_data = orgs + argem

persons_data = insert(__names_local["people"], people_data) + \
               insert(__names_local["specializations"], specialization_data) + \
               insert(__names_local["doctors"], doctors_data)
another_persons = insert(__names_local["workers"], worker_data) + \
               insert(__names_local["prof_inspections"], inspection_record_data) + \
               insert(__names_local["results"], inspections_data)
