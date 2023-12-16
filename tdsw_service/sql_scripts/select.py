select_med = """
SELECT name FROM organizations WHERE id = 50000;
"""

select_doctors = """SELECT people.id, people.name, lastname, surname, phone, shils, oms, email, category,
hiring_date, dismissal_date, diploma_number,
specialization_book.name
    FROM people, specializations, specialization_book, doctors WHERE 
    people.id = specializations.person_id AND specialization_book.id = specializations.profession_id
    AND people.id = doctors.person_id;
"""

select_workers = """SELECT people.id, people.name, lastname, surname, phone, shils, oms, email,
    workers.tid, organizations.name as org_name, workers.position, workers.profession FROM
    people, workers, organizations WHERE people.id = workers.person_id AND workers.organization_id = organizations.id;
    """

select_orgs = """
SELECT organizations.id, organizations.name, organizations.location, organizations.inn, 
organizations.ogrn, agreement.exp_date
    FROM organizations
    JOIN agreement ON organizations.id = agreement.hospital_id
    WHERE agreement.hospital_id = 50000;
"""

select_records = """SELECT prof_inspections.id, prof_inspections.appointment_date, prof_types.name, people.name, 
people.lastname, people.surname, workers.tid, workers.position, workers.profession 
    FROM prof_inspections, prof_types, 
    people, workers WHERE prof_inspections.type_id = prof_types.id AND prof_inspections.worker_id = workers.id AND 
    workers.person_id = people.id;
    """

select_inspections = """SELECT results.id, results.complaints, results.result, people.name, people.lastname, people.surname,
    workers.tid, workers.position, workers.profession
    FROM results, people, workers, prof_inspections WHERE
    results.prof_inspection_id = prof_inspections.id AND
    prof_inspections.worker_id = workers.id AND
    workers.person_id = people.id;
"""

select_insp_types = """SELECT * FROM prof_types;"""
select_spec_book = """SELECT * FROM specialization_book;"""

report_visit = """
SELECT name, COUNT(*) AS visit_count
FROM results
GROUP BY name
ORDER BY visit_count DESC
LIMIT 5;
"""

repost_health = """
SELECT result, COUNT(*) AS count
FROM results
GROUP BY result
ORDER BY count DESC;
"""
report_comps = """
SELECT complaints, COUNT(*) AS count
FROM results
GROUP BY complaints
ORDER BY count DESC;
"""


def get_user(login):
    query = f"""SELECT people.login, people.password, people.category 
    FROM people WHERE people.login = '{login}';"""
    return query
