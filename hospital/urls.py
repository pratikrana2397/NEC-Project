from django.urls import path
from . import views
app_name="hospital"
urlpatterns = [
	path('',views.index,name='index'),
	path('register/',views.UserFormView.as_view(),name='register'),
	path('doctor/add/',views.doctorcreate.as_view(),name='doctor-add'),
	path('patient/add',views.Patientcreate.as_view(),name='patient-add'),
	path('list/doctors',views.doctorListView.as_view(),name='doctor-list'),
	path('list/patients',views.PatientListView.as_view(),name='patient-list'),
	path('doctor/update/<int:pk>/',views.doctorupdate.as_view(),name='doctor-update'),
	path('doctor/<int:pk>/delete/',views.doctordelete.as_view(),name='doctor-delete'),
	path('patient/update/<int:pk>/',views.Patientupdate.as_view(),name='patient-update'),
	path('patient/<int:pk>/delete/',views.Patientdelete.as_view(),name='patient-delete'),
        
]
