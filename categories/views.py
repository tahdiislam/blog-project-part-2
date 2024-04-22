from django.shortcuts import render, redirect
from .forms import CategoryForm


# Create your views here.
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("add_category")
    else:
        form = CategoryForm()
    return render(request, "categories/add_category.html", {"form": form})
