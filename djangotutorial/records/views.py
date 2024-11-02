import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Record

@csrf_exempt
def records_list(request):
    if request.method == "GET":
        records = list(Record.objects.values())
        return JsonResponse(records, safe=False)  

    elif request.method == "POST":
        data = json.loads(request.body)
        new_record = Record.objects.create(enregistre=data.get("enregistre"))
        return JsonResponse({"id": new_record.id, "enregistre": new_record.enregistre}, status=201)

@csrf_exempt
def record_detail(request, id):
    try:
        record = Record.objects.get(id=id)
    except Record.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=404)

    if request.method == "GET":
        return JsonResponse({"id": record.id, "enregistre": record.enregistre})

    elif request.method == "PUT":
        data = json.loads(request.body)
        record.enregistre = data.get("enregistre", record.enregistre)
        record.save()
        print('dddd')
        return JsonResponse({"id": record.id, "enregistre": record.enregistre})

    elif request.method == "DELETE":
        record.delete()
        return HttpResponse(status=204)
