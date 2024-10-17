from django.shortcuts import render
from django.http import JsonResponse
from .models import Registration, Worker, Card

def card_list_json(request):
    cards = Card.objects.all()

    card_list = []
    for card in cards:
        card_list.append({
            'id': card.id,
            'rfid': card.rfid,
            'card_nr': card.card_nr,
            'id_worker': card.id_worker.id
        })

    return JsonResponse(card_list, safe=False)

def worker_list_json(request):
    workers = Worker.objects.all()

    worker_list = []
    for worker in workers:
        worker_list.append({
            'id': worker.id,
            'first_name': worker.first_name,
            'last_name': worker.last_name,
            'work_type': worker.work_type,
            'act': worker.act,
            'section': worker.section,
            'teta_nr': worker.teta_nr
        })

    return JsonResponse(worker_list, safe=False)

def registration_list_json(request):
    registrations = Registration.objects.all()

    reg_list = []
    for registration in registrations:
        reg_list.append({
            'id': registration.id,
            'datetime': registration.datetime,
            'id_worker': registration.id_worker.id,
            'id_card': registration.id_card.id,
        })

    return JsonResponse(reg_list, safe=False)