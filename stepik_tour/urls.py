from django.contrib import admin
from django.urls import path
from tours.views import MainPageView, DepartureView, TourView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", MainPageView.as_view()),
    path("departure/<str:departure_id>/", DepartureView.as_view()),
    path("tour/<int:tour_id>/", TourView.as_view()),
]
