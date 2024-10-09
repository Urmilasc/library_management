# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.book_list, name='book_list'),
#     path('add/', views.add_book, name='add_book'),
#     path('update/<int:pk>/', views.update_book, name='update_book'),
#     path('delete/<int:pk>/', views.delete_book, name='delete_book'),
#     path('borrow/<int:pk>/', views.borrow_book, name='borrow_book'),
#     path('return/<int:pk>/', views.return_book, name='return_book'),
#     path('history/', views.view_history, name='view_history'),
#     path('members/', views.view_members, name='view_members'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('books/return/<int:book_id>/', views.return_book, name='return_book'),
    path('books/add/', views.add_book, name='add_book'),
    path('available-books/', views.view_available_books, name='view_available_books'),
]

