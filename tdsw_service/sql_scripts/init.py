from ._names import __names_local, __names_global

create_prof_types = """
CREATE TABLE IF NOT EXISTS prof_types (
    id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL); 
"""

create_specialization_book = """
CREATE TABLE IF NOT EXISTS specialization_book (
    id INT PRIMARY KEY,
    name VARCHAR(40) NOT NULL);
"""

create_people = """
CREATE TABLE IF NOT EXISTS people (
    id INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    lastname VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    shils VARCHAR(40) NOT NULL,
    oms VARCHAR(30) NOT NULL,
    email VARCHAR(20),
    login VARCHAR(10) UNIQUE,
    is_superuser tinyint(1) NOT NULL,
    category VARCHAR(20),
    password VARCHAR(70));  
"""

create_organizations = """
CREATE TABLE IF NOT EXISTS organizations (
    id INT PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    location VARCHAR(40) NOT NULL,
    inn VARCHAR(30) NOT NULL,
    ogrn VARCHAR(30) NOT NULL);
"""

create_agreement = """
CREATE TABLE IF NOT EXISTS agreement (
    id INT PRIMARY KEY,
    hospital_id INT,
    factory_id INT,
    doc_path VARCHAR(40) NOT NULL,
    exp_date DATETIME NOT NULL,
    
    FOREIGN KEY (hospital_id) REFERENCES organizations(id),
    FOREIGN KEY (factory_id) REFERENCES organizations(id));
"""

create_doctors = """
CREATE TABLE IF NOT EXISTS doctors (
    id INT PRIMARY KEY,
    person_id INT,
    hospital_id INT,
    hiring_date DATETIME NOT NULL,
    dismissal_date DATETIME,
    
    FOREIGN KEY (hospital_id) REFERENCES organizations(id),
    FOREIGN KEY (person_id) REFERENCES people(id));
"""

create_specializations = """
CREATE TABLE IF NOT EXISTS specializations (
    id INT PRIMARY KEY,
    person_id INT,
    profession_id INT,
    diploma_date DATETIME NOT NULL,
    diploma_number VARCHAR(40) NOT NULL,
    
    FOREIGN KEY (profession_id) REFERENCES specialization_book(id),
    FOREIGN KEY (person_id) REFERENCES people(id));
"""

create_workers = """
CREATE TABLE IF NOT EXISTS workers (
    id INT PRIMARY KEY,
    person_id INT,
    tid VARCHAR(40) NOT NULL,
    organization_id INT,
    position VARCHAR(50) NOT NULL,
    hiring_date DATETIME NOT NULL,
    dismissal_date DATETIME,
    profession VARCHAR(100) NOT NULL,
    
    FOREIGN KEY (person_id) REFERENCES people(id),
    FOREIGN KEY (organization_id) REFERENCES organizations(id));
"""

create_prof_inspections = """
CREATE TABLE IF NOT EXISTS prof_inspections (
    id INT PRIMARY KEY,
    appointment_date TIMESTAMP NOT NULL,
    type_id INT,
    worker_id INT,
    
    FOREIGN KEY (type_id) REFERENCES prof_types(id),
    FOREIGN KEY (worker_id) REFERENCES workers(id));
"""

create_results = """
CREATE TABLE IF NOT EXISTS results (
    id INT PRIMARY KEY,
    data JSON NOT NULL,
    complaints VARCHAR(70) NOT NULL,
    prof_inspection_id INT,
    result VARCHAR(60) NOT NULL,
    doctor_id INT,
    name VARCHAR(65) NOT NULL,
    
    FOREIGN KEY (prof_inspection_id) REFERENCES prof_inspections(id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(id));
"""

create_files = """
CREATE TABLE IF NOT EXISTS files (
    id INT PRIMARY KEY,
    file_path VARCHAR(40) NOT NULL,
    inspection_id INT,
        
    FOREIGN KEY (inspection_id) REFERENCES results(id));
"""


def alter(Id, tables):
    return [f"""ALTER TABLE {tables[k]} AUTO_INCREMENT = {Id};""" for k, _ in tables.items()]


alter_master = alter(1, __names_global)

create_master = [create_prof_types, create_specialization_book, create_people, create_organizations,
                 create_agreement, create_doctors, create_specializations, create_workers, create_prof_inspections,
                 create_results, create_files, *alter_master]

alter_slave = alter(50000, __names_local)
