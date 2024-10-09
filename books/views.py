from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book

# View to list all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# View to borrow a book
@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.status == 'available':
        book.status = 'borrowed'
        book.borrowed_by = request.user  # Assign the current user to borrowed_by
        book.save()
    return redirect('view_available_books')

# View to return a book
@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.status == 'borrowed' and book.borrowed_by == request.user:  # Only the borrower can return it
        book.status = 'available'
        book.borrowed_by = None
        book.save()
    return redirect('book_list')

# View to add a new book (for librarians)
@login_required
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author, status='available')
        return redirect('book_list')
    return render(request, 'books/book_form.html')  # Update to use the correct template path


def view_available_books(request):
    # Retrieve all available books from the database
    available_books = Book.objects.filter(available=True)

    # Create a context dictionary to pass to the template
    context = {
        'available_books': available_books
    }

    # Render the available_books.html template with the context
    return render(request, 'available_books.html', context)