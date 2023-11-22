
from sql_scripts.load_data import insert_data, insert_slave_data
from django.http import HttpResponse
from django.db.utils import IntegrityError

# Create your views here.


def index(request):
    try:
        insert_data()
        insert_slave_data()
        return HttpResponse("Loaded")
    except IntegrityError:
        return HttpResponse("Already loaded")