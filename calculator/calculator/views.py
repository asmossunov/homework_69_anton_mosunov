import json
from django.http.response import JsonResponse


def add(request, *args, **kwargs):
    print(f'Распечатка входящего запроса! {request.body}')
    print(request.POST)
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            number_a = float(numbers['A'])
            number_b = float(numbers['B'])
            result = number_a + number_b
            answer['result'] = result
        except TypeError:
            answer['error'] = 'There is a non-numeric value among the entered values'
            return JsonResponse(answer, status=400)
    return JsonResponse(answer)


def subtract(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            number_a = float(numbers['A'])
            number_b = float(numbers['B'])
            result = number_a - number_b
        except TypeError:
            answer['error'] = 'There is a non-numeric value among the entered values'
            return JsonResponse(answer, status=400)
    answer['result'] = result
    return JsonResponse(answer)


def multiply(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            number_a = float(numbers['A'])
            number_b = float(numbers['B'])
            result = number_a * number_b
        except TypeError:
            answer['error'] = 'There is a non-numeric value among the entered values'
            return JsonResponse(answer, status=400)
    answer['result'] = result
    return JsonResponse(answer)
