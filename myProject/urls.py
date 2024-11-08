from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',signupPage,name="signupPage"),
    path("signInPage/", signInPage, name="signInPage"),
    path("HomePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("ProfilePage/", profilePage, name="profilePage"),


    path("AddJob/", AddJob, name="AddJob"),
    path("JobFeed/", JobFeed, name="JobFeed"),
    path("createdJob/", createdJob, name="createdJob"),
    path("DeleteJob/<str:id>", DeleteJob, name="DeleteJob"),
    path("EditJob/<str:id>", EditJob, name="EditJob"),
    path("ApplyJob/<str:id>", ApplyJob, name="ApplyJob"),
    path("searchPage/", searchPage, name="searchPage"),
    path("SkillMatchingPage/", SkillMatchingPage, name="SkillMatchingPage"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
