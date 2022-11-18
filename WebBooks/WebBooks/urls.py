from django.contrib import admin
from django.urls import path
from catalog import views
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    url(r'^books/$', views.BookListView.as_view(), name="books"),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(),
        name="book-detail"),
    url(r'^authors/$', views.AuthorListView.as_view(), name="authors"),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(),
        name="author-detail"),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'mybooks/$', views.LoanedBooksByUserListView.as_view(), name="my-borrowed"),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('authors_add/edit1/<int:id>/', views.edit1, name='edit1'),
    path('authors_add/create/', views.create, name='create'),
    path('authors_add/delete/<int:id>/', views.delete, name='delete'),
    url(r'^book/create/$', views.BookCreate.as_view(),
                                      name='book_create'),
    url(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(),
                                      name='book_update'),
    url(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(),
                                      name='book_delete')
]
