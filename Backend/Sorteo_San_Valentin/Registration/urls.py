from django.urls import path
from .views import RegistrationView, VerifyView , LoginView, ParticipantListView

urlpatterns = [
    path("register/",RegistrationView.as_view(), name="register"),
    path("verify/<str:token>",VerifyView.as_view(), name="verify-email"),
    path("login/",LoginView.as_view(), name="login"),
    path("select-winner/",LoginView.as_view(), name="select-winner"),
    path("participants/",ParticipantListView.as_view(), name="participants"),

]

