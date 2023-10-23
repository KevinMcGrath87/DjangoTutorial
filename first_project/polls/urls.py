from django.urls import path

from . import views

app_name = "polls"
# the app name allows for namespaceing the urls. i.e. in the {% url 'polls:detail", question.id %} the namespace polls is used to diffentiate the detail view form others in other apps.
# naming urls allows their reference in templates without hardcoding them. this way if you change the literal URL you dont need to worry about changing it literally in the template
urlpatterns = [
    path('', views.IndexView.as_view(), name = "index"),
    path('<int:pk>/', views.DetailView.as_view(),name ='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(), name = 'results'),
    path('<int:question_id>/vote/',views.vote, name = 'vote'),

]