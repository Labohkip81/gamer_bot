from django.urls import path


from .views import home_page_view,HomePage,AboutPage


urlpatterns = [
    #class based views have to call an as view function.
    path('', HomePage.as_view(), name='home'),
    path("about", AboutPage.as_view(), name='about'),
    
]
