from ._names import __names_local, __names_global
import random

prof_types_data = {"id": [i for i in range(1, 11)],
                   "name": [random.choice(["Общего назначений",
                                           "Производства Класса A",
                                           "Производства Класса B",
                                           "Производства Класса C"]) for _ in range(1, 11)]}

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

orgs_data = {"id": [i for i in range(50000, 50004)],
             "name": [
                 "МУ",
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

agreement_data = {"id": [i for i in range(50000, 50003)],
                  "hospital_id": [50000, 50000, 50000],
                  "factory_id": [50001, 50002, 50003],
                  "doc_path": [" " for _ in range(3)],
                  "exp_date": ["2025-01-01 00:00:00" for _ in range(3)]}


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
