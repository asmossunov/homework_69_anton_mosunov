import json
from django.http.response import JsonResponse


def add(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            number_a = float(numbers['A'])
            number_b = float(numbers['B'])
            result = number_a + number_b
            answer['result'] = result
        except ValueError as te:
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
        except ValueError as te:
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
        except ValueError as te:
            answer['error'] = 'There is a non-numeric value among the entered values'
            return JsonResponse(answer, status=400)
    answer['result'] = result
    return JsonResponse(answer)


def divide(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            number_a = float(numbers['A'])
            number_b = float(numbers['B'])
        except ValueError as te:
            answer['error'] = 'There is a non-numeric value among the entered values'
        try:
            result = number_a / number_b
            answer['result'] = result
            return JsonResponse(answer)
        except ZeroDivisionError:
            answer['error'] = "Can't divide by zero"
            return JsonResponse(answer, status=400)
