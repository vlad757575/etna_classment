from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
import requests

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def api_test(request):
    url = 'https://prepintra-api.etna-alternance.net/terms/819/students/lavren_v/marks'
    cookie = dict(authenticator="eyJpZGVudGl0eSI6ImV5SnBaQ0k2TkRFeE16UXNJbXh2WjJsdUlqb2liR0YyY21WdVgzWWlMQ0psYldGcGJDSTZJbXhoZG5KbGJsOTJRR1YwYm1FdFlXeDBaWEp1WVc1alpTNXVaWFFpTENKc2IyZGhjeUk2Wm1Gc2MyVXNJbWR5YjNWd2N5STZXeUp6ZEhWa1pXNTBJbDBzSW14dloybHVYMlJoZEdVaU9pSXlNREkwTFRBeExUSTFJREE1T2pBNU9qRTFJbjA9Iiwic2lnbmF0dXJlIjoib3NGT0FHOEJhNHZEWmlrRGU5Q0FKZDRHakZBbEhLQ2JWZk52XC9jczJYNjZTQ0xVaVcxdW9VaFZKZzJxY2huTGplXC84eVBseEJ6TnpjOFAwUlpSU1lIeWhMQmdROHZOOTFcL0NqV2JGSG9cL3pvdGdWQUdiNWtLREdzbG1wQVwvQ3liK25YNDJWN2hUeTZ3VXVEQ3FwVXNcL1ZSWmlSRzIzZjBTSE9HbGErR25ZYytVSlc1eVwvTFJ2K1wvNVo2TmxOeG1udVE1aTJpSWdudllNUWpXRmF4cFRvMzZqNVIrck9kY1hmQXlaeTBpdFkwZ1FMOERDTHllVmRjam1JMXQ1TVY0XC8yM1A4SHJhYktqaElGZG5RVklHMmlRRWswR1Izb215dXREbFBDTTM3ODRzSkVvc1d6WmlKK1wvWWZUYWt3dGlEb2RVdVJDRStub1duQ1VPZk5ZR01pSHlzMlwvUmJwUHBSaTZuN0JXOHpUWlpiVWgwcUppU29vV09Sa2FZenpGamw3Y054bnlkcHlYclAxWkJoc2MzNHhoNVhPdFwvdW1ZXC9renh6RzJLR0lRb3gyYlwvUEdLaW9SWWxpSjQydnVWTnBqZktISXIyQ3VFZUpBbWZScHY2THRveTVcL1wvbTAyQ1NkaDNqQTBQb1BVUjVjYXB3YkJkcGQyRFwvbjRIWHQ3TEZkOVBTWUNqYjE4STh2OXdkNzAyYjF5TkhSbDZ4a1VxeDJRbXVtVUJzdmZYeWt3Wm9wa3RsWXdXMTIrR29HaVArUlJyeVdiMDltUXMyNWpZZTdYZVZJdDJjd3UrNUNEb2VkZGM4eUdrbVpnWkFMK21DWlVid0lPNTFKdnZmS2RcL0prM0cwWVk2WWhSSkhMNmdVUzROVE8wRmZtNzI4eGFYM3JVekZST3hlSk1VbUhpRVk9In0%3D")
    response = requests.get(url,cookies=cookie)
    data = response.json()
    add = 0
    for note in data:
        add += (note['student_mark'])
        print(add)
    return JsonResponse(response.json(), safe=False)