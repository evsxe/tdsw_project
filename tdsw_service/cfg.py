# NODE = None


class Connection:
    def __init__(self, NODE: str = None):
        self.NODE = NODE

    def set_node(self, node: str):
        self.NODE = node

    def get_node(self):
        return self.NODE


con = Connection()

tokens = {"med_admin": "med_admin_token",
          "doctor": "doctor_token",
          "superuser": "superuser_token",
          "worker_admin": "org_worker_token"}

menu = {"med_admin": [{"text": "Врачи", "href": "/auth/doctors"},
                      {"text": "Рабочие", "href": "/auth/workers"},
                      {"text": "Организации", "href": "/auth/orgs"},
                      {"text": "Записи", "href": "/auth/records"},
                      {"text": "Осмотры", "href": "/auth/inspections"},
                      {"text": "Общее", "href": "/auth/content"}],

        "superuser": [{"text": "Врачи", "href": "/auth/doctors"},
                      {"text": "Рабочие", "href": "/auth/workers"},
                      {"text": "Осмотры", "href": "/auth/inspections"},
                      {"text": "Справочник профессий", "href": "/auth/types"},
                      {"text": "Типы профосомтров", "href": "/auth/insp_types"},
                      {"text": "Записи", "href": "/auth/records"},
                      {"text": "Общее", "href": "/auth/content"},
                      {"text": "Отчеты", "href": "/auth/report"},
                      {"text": "Организации", "href": "/auth/orgs"}]}
