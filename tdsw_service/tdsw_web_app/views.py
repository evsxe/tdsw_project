from sql_scripts.load_data import insert_data, insert_slave_data, select_data, \
    insert_persons, select_user, select_report
from django.http import HttpResponse
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json
# Create your views here.

import cfg


# def on_start(request):
#     res = select_med_orgs()
#     return HttpResponse()

def parse_body(req):
    body = req.body
    js_body = body.decode("utf8")
    return json.loads(js_body)


@csrf_exempt
def init(request):
    d = parse_body(request)
    cfg.con.set_node(d.get("node"))
    return HttpResponse("GOT")


@csrf_exempt
def select_data_for_med_admin(request):
    d = parse_body(request)
    t = d.get("what")
    res = select_data(t)
    return JsonResponse({"data": res})


@csrf_exempt
def auth(request):
    d = parse_body(request)
    login, psw = d.get("login", ""), d.get("psw", "")
    res, status = select_user(login, psw)
    if status:
        res.update({"token": cfg.tokens[res["category"]],
                    "menu": cfg.menu[res["category"]]})
        return JsonResponse({"data": res, "status": "ok"})
    return JsonResponse({"data": {}, "status": "error"})


@csrf_exempt
def report(request):
    d = parse_body(request)
    w = d.get("what")
    rep = select_report(w)
    print(rep)
    return JsonResponse({"data": rep})


def index(request):
    try:
        insert_data()
        insert_slave_data()
        insert_persons()
        return HttpResponse("Loaded")
    except IntegrityError:
        return HttpResponse("Already loaded")
