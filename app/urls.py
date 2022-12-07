from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("bloglist/", views.bloglist, name="bloglist"),
    path("viewblog/", views.viewBlogs, name="viewBlogs"),
    path("logout/", views.logout, name="logout"),
    # url for Patients
    path("signupPatient/", views.signupPatient, name="signupPatient"),
    path("loginPatient/", views.loginPatient, name="loginPatient"),
    path("patientDashboard/", views.patientDashboard, name="patientDashboard"),
    path("appointment/", views.appointment, name="appointment"),
    path("confirmAppointment/", views.confirmAppointment, name="confirmAppointment"),
    # url for Doctors
    path("signupDoctor/", views.signupDoctor, name="signupDoctor"),
    path("loginDoctor/", views.loginDoctor, name="loginDoctor"),
    path("doctorDashboard/", views.doctorDashboard, name="doctorDashboard"),
    path("createblog/", views.createBlogs, name="createBlogs"),
    path("draft/", views.draft, name="draft"),
    path("events/", views.events, name="events"),
]


urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)