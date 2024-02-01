from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

# Function or class
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "febuary": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    'april': "Focus on Tensorflow and Sklearn!",
    "may": "Woah!",
    "june": "Practice superv.ised Learning!",
    "july": "Revise React.js!",
    "august": "Celebrate Independence day!",
    "september": "Apply for internship!",
    "october": "Fix Engagement!",
    "november": "Go to honeymoon!",
    "december": None


}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month_challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{
    #         capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    dict_items = list(monthly_challenges.items())
    if 1 <= month <= len(dict_items):
        # Access the key-value pair at the specified index
        key, value = dict_items[month - 1]
        redirect_path = reverse("month_challenge", args=[
                                key])  # /challenge/january
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("Invalid month!")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {"text": challenge_text, "month": month.capitalize()})
        # render_to_string("",{})
        # response_data = render_to_string("")
        # return HttpResponse(response_data)
    except:
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)
