from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ExpenseForm, BudgetForm
from .models import *

# for downloading
from django.http import HttpResponse
import csv

def home(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'app.html', {'expenses': expenses})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('set_budget')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('expense_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# Budget
# def set_budget(request):
#     if request.method == 'POST':
#         amount = request.POST.get('amount')
#         request.user.budget.amount = amount
#         request.user.budget.save()
#         return redirect('expense_list')
#     return render(request, 'set_budget.html')
def set_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('expense_list')
    else:
        form = BudgetForm()
    return render(request, 'set_budget.html', {'form': form})

def update_budget(request):
    budget = Budget.objects.get(user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'update_budget.html', {'form': form})

def delete_budget(request):
    budget = Budget.objects.get(user=request.user)
    budget.delete()
    return redirect('expense_list')

# Expense
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')  # Redirect to the expense list after updating the expense
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'edit_expense.html', {'form': form})

def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    expense.delete()
    return redirect('expense_list')


def download_records(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="records.csv"'

    writer = csv.writer(response)
    writer.writerow(['User', 'Category', 'Name', 'Date', 'Amount'])
    expenses = Expense.objects.all()
    for expense in expenses:
        writer.writerow([
            expense.user.username,
            expense.category,
            expense.name,
            expense.date.strftime('%Y-%m-%d'),
            expense.amount
        ])

    return response