
from django.urls import path
from CSE import views
from CSE.views import StuList, Forms, StudentDetail, StudentUpdate, StudentDelete
from CSE.views import EmpList, Forms12, EmployeDetail, EmployeUpdate, EmployeDelete

app_name = 'CSE'

urlpatterns = [
    path('index', views.index, name='home'),
    path('index', views.index, name='index'),
    path('products', views.products, name='products'),
    path('service', views.service, name='service'),
    path('contacts', views.contacts, name='contacts'),
    path('basic', views.basic, name='basic'),

    # CBV- employees
    path('', EmpList.as_view(), name='list'),
    path('forms', Forms12.as_view(), name='forms'),
    path('<pk>/detail', EmployeDetail.as_view(), name='detail'),
    path('<pk>/update', EmployeUpdate.as_view(), name='update'),
    path('<pk>/delete', EmployeDelete.as_view(), name='delete'),

     # CBV-students
     path('list1', StuList.as_view(), name='list1'),
    path('forms1', Forms.as_view(), name='forms1'),
    path('<pk>/detail1', StudentDetail.as_view(), name='detail1'),
    path('<pk>/update1',StudentUpdate.as_view(), name='update1'),
    path('<pk>/delete1', StudentDelete.as_view(), name='delete1'),

    # FBV
    path('student', views.student, name='student'),  # Only keep one
    path('form', views.form, name='form'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

    ###GET and POST

    path('nie',views.nie, name = 'nie'),
    path('add', views.add, name = 'add'),
    path('add1', views.add1, name = 'add1'),

    # login, logout, user registration
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login'),
    path('logout', views.logoutuser, name = 'logout'),

]
