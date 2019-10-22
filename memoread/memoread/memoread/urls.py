"""memoread URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from record.views import Login, Create_account, RecordListView, RecordCreateView
from record.views import DetailAccount, RecordDetailView, RecordUpdateView, RecordDeleteView
from record.views import UpdateAccount
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RecordListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='record/login.html'), name='logout'),
    path('account/', Create_account.as_view(), name='create_account'),
    path('account_detail/<slug:username>/', DetailAccount.as_view(), name='account_info'),
    path('account_update/<slug:username>/', UpdateAccount.as_view(), name='account_update'),
    path('create/', RecordCreateView.as_view(), name="create"),
    path('<slug:username>/<int:pk>', RecordDetailView.as_view(), name="detail"),
    path('update/<int:pk>', RecordUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', RecordDeleteView.as_view(), name="delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
