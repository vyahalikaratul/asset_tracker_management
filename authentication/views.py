# # asset_tracker/views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import CustomAuthenticationForm
# from django.contrib.auth import authenticate, login
#
#
# def login_view(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request, request.POST)
#         if form.is_valid():
#             remember_me = form.cleaned_data['remember_me']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 print("Authentication successful")  # Debugging statement
#                 login(request, user)
#                 if not remember_me:
#                     request.session.set_expiry(0)  # Set session expiry to browser close
#                 return redirect('/home/')  # Redirect to home page
#             else:
#                 print("Authentication failed")  # Debugging statement
#                 form.add_error(None, "Invalid email or password. Please try again.")  # Add non-field error
#     else:
#         form = CustomAuthenticationForm()
#     return render(request, 'login.html', {'form': form})
#
#
# def home_view(request):
#     return render(request, 'home.html')
#
