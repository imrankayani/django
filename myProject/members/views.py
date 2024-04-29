from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
import requests

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # Redirect to a success page.    
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error logging in, please try again!"))
            return redirect('login')



    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        # Create a form instance with POST data
        form = UserCreationForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the user (create the user in the database)
            form.save()
            
            # Authenticate the user (log them in)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Registration was successful!")
                
                # Redirect to the home page
                return redirect('home')
        
        # If the form is not valid, render the form with errors
        else:
            messages.error(request, "There was an error with your form submission.")
    
    # Create a new, empty form if the request method is GET
    else:
        form = UserCreationForm()

    # Render the registration form template
    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })

def get_nutrition_data(request):
    ingredient =- request.GET.get('ingredient', 'chicken')

    api_url = "https://api.edamam.com/api/nutrition-data"
    app_id = "27665238"
    app_key = "7aa61cf1dce97ed88e604a9b57326064"
    params = {
        'app_id': app_id,
        'app_key': app_key,
        'nutrition-type': 'logging',
        'ingr': ingredient
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data from API'}, status=400)
    
