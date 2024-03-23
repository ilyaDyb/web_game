from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from user.models import User


@login_required
def index(request):
    user = User.objects.get(pk=request.user.id)
    context = {
        "user": user,
    }

    return render(request, "boosts/index.html", context=context)


@login_required
def buy_ability(request):
    if request.method == "POST":
        if request.POST.get("booster") == "tap_ability":
            user = request.user
            if user.score >= int(request.POST.get("price")):
                user.tap_ability = user.tap_ability + 1
                user.score = user.score - int(request.POST.get("price"))
                user.save()
                messages.success(request, "Successul")
                return redirect(reverse("boosts:index"))
            else:
                messages.warning(request, "Not enough points")
                return redirect(reverse("boosts:index"))
 
        if request.POST.get("booster") == "auto_click":
            user = request.user
            if user.score >= int(request.POST.get("price")):
                user.auto_click = user.auto_click + 1
                user.score = user.score - int(request.POST.get("price"))
                user.save()
                messages.success(request, "Successul")
                return redirect(reverse("boosts:index"))     
            else:
                messages.warning(request, "Not enough points")
                return redirect(reverse("boosts:index"))
    else:
        return HttpResponse(status=404)