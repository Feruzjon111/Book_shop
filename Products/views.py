from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Book
from .forms import BookForm

class HomeView(View):
    def get(self, request):
        books = Book.objects.all()[:3]
        return render(request, 'home.html', {'books': books})

class ProductView(View):
    def get(self, request):
        books = Book.objects.all()
        q = request.GET.get('search')
        books = books.filter(Q(title__icontains=q) | Q(author__icontains=q)) if q else books
        return render(request, 'products.html', {'books': books})

class ProductDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'product_detail.html', {'book': book})

class ProductCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'product_create.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
        return render(request, 'product_create.html', {'form': form})

class ProductUpdateView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, 'product_update.html', {'form': form, 'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, request.FILES, instance=book)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('detail', pk=book.pk)
        return render(request, 'product_update.html', {'form': form, 'book': book})


class ProductDeleteView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'product_delete.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('product')
