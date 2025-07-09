from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import TypingResult
from .utils import get_random_text
import json
from django.shortcuts import get_object_or_404

# Typing Test View (requires login)
@login_required
def my_results_view(request):
    results = TypingResult.objects.filter(username=request.user.username).order_by('-id')[:10]

    # Convert seconds to minutes and attach as `.minutes` attribute
    for result in results:
        result.minutes = round(result.time_taken / 60, 2)

    return render(request, "my_results.html", {"results": results})

def test_selection_view(request):
    if request.method == "POST":
        duration = int(request.POST.get("duration"))
        request.session["duration"] = duration
        return redirect("typing-test")
    return render(request, "home.html")

@login_required
def typing_test_view(request):
    text = get_random_text()
    duration = request.session.get("duration", 60)  # default to 60 seconds
    return render(request, "test.html", {"text": text, "duration": duration})

# Save Result
@login_required
def save_result(request):
    if request.method == "POST":
        data = json.loads(request.body)
        TypingResult.objects.create(
            username=request.user.username,
            wpm=data["wpm"],
            accuracy=data["accuracy"],
            time_taken=data["time_taken"],
            test_type=data.get("test_type", "unknown")  # get test type from request
        )
        return JsonResponse({"status": "ok"})
    return JsonResponse({"error": "Invalid method"}, status=400)


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already taken."})
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("test")
    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

# Logout
def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def print_certificate(request, pk):
    result = get_object_or_404(TypingResult, pk=pk, username=request.user.username)
    return render(request, "certificate.html", {"result": result})