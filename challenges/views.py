from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect

# Create your views here.

mothly_challenges = {
    "january" : "Welome to January",
    "february": "Welcome to February",
    "march": "Welcome to March"
}

def monthly_challenge_by_number(request,month):
    try:
        months = list(mothly_challenges.keys())
        redirect_month = months[month-1]
    except:
        return HttpResponse ("This is an Invalid Month")
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request,month):
    try:
        challange_text = mothly_challenges[month]
    except:
        return HttpResponseNotFound ("This is an invalid Month!!")
    return HttpResponse(challange_text)