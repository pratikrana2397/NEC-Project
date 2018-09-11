from django.urls import path
from . import views
app_name="hospital"
urlpatterns = [
	path('',views.index,name='index'),
        path('register/',views.UserFormView.as_view(),name='register'),
	path('doctor/add/',views.doctorcreate.as_view(),name='doctor-add'),
	path('doctor/update/<int:pk>/',views.doctorupdate.as_view(),name='doctor-update'),
	path('doctor/<int:pk>/delete/',views.doctordelete.as_view(),name='doctor-delete'),
]
