from django.shortcuts import render, redirect
from .models import Transaction, Category
from .forms import TransactionForm, CategoryForm

def index(request):
    return render(request, 'index.html')
# def transaction_create(request):
#     if request.method == 'POST':
#         transaction_form = TransactionForm(request.POST)
#         category_form = CategoryForm(request.POST)
#         if transaction_form.is_valid():
#             transaction = transaction_form.save(commit=False)
#             # Check if a new category is being added
#             if category_form.is_valid() and category_form.cleaned_data.get('name'):
#                 category = category_form.save()
#                 transaction.category = category
#             transaction.user = request.user
#             transaction.save()
#             return redirect('transaction_list')  # Redirect to a page where you list transactions
#     else:
#         transaction_form = TransactionForm()
#         category_form = CategoryForm()
#     return render(request, 'transaction_form.html', {'transaction_form': transaction_form, 'category_form': category_form})
def transaction_create(request):
    if request.method == 'POST':
        transaction_form = TransactionForm(request.POST)
        if transaction_form.is_valid():
            transaction = transaction_form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')  # Redirect to a page where you list transactions
    else:
        transaction_form = TransactionForm()
    return render(request, 'transaction_form.html', {'transaction_form': transaction_form})

def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transaction_list.html', {'transactions': transactions})