"""
URL configuration for metanit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from hello import views

product_patterns = [
    path('', views.products),
    path('new', views.new),
    path('top', views.top),
    path('comments', views.comments),
    path('questions', views.questions)
]

urlpatterns = [
    path('user/<str:name>', views.user),
    path('user/<str:name>/<int:age>', views.user),
    re_path('^contact', views.contact),
    re_path('^main', views.main),
    # path('', views.index, name='home'),
    path('products/', include(product_patterns)),
    path('products/<int:id>/', include(product_patterns)),
    path('aboutuser/', views.aboutuser),
    # path("index/<int:id>", views.index),
    path("age/<int:age>", views.age),
    path('set/', views.set),
    path('get', views.get),
    # path('', views.index),
    path('', views.static)
]
