
from django.http import HttpResponse

from .models import User, Expense, ExpensePaidBy, ExpenseOwedBy

from .serializers import (
    UserSerializer,
    ExpenseSerializer,
    ExpensePaidBySerializer,
    ExpenseOwedBySerializer,
)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status

from django.db import IntegrityError
from django.db.models import Sum
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def user_profile(request):
    return render(request, 'profile.html')



def homePage(request):
    
    # return HttpResponse("Welcome to my Django Project")
    return render(request, "index.html")


def allUser(request):
    data = User.objects.all().values()
    return HttpResponse(data)


class UserListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = User.objects.all()
    
    serializer_class = UserSerializer


def validate_exp_type(exp_type):
    if exp_type not in ["EQUAL", "EXACT", "PERCENT"]:
        
        raise ValueError("Expense type must be one of: EQUAL, EXACT, PERCENT.")


def validate_desc(desc):
    if not isinstance(desc, str):
        raise ValueError("Description must be a string.")


def validate_total_amt(amt):
    if not isinstance(amt, int):
        raise ValueError("Total amount must be an integer.")


def validate_user_ids(user_ids, user_id_list, field_name):
    for uid, amt in user_ids.items():
        if int(uid) not in user_id_list:
            raise ValueError(f"Invalid user ID '{uid}' in '{field_name}'.")
        if not isinstance(amt, (int, float)):
            raise ValueError("Amount must be a number.")


def validate_total(total_dict, expected_total):
    if sum(total_dict.values()) != expected_total:
        raise ValueError(
            f"Total amount does not match the specified total amount of {expected_total}."
        )


def validate_created_by(created_by_id, user_id_list):
    if created_by_id not in user_id_list:
        raise ValueError(f"Invalid created by user ID '{created_by_id}'.")

