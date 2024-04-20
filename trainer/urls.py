from django.urls import path

from trainer import views

urlpatterns=[
    path('create_trainer/', views.TrainerCreateView.as_view(), name='create-trainer'),
    path('list_trainers/', views.TrainerListView.as_view(), name='list-trainers'),
    path('update_trainer/<int:pk>/', views.TrainerUpdateView.as_view(), name='update-trainer'),
    path('delete_trainer/<int:pk>/', views.TrainerDeleteView.as_view(), name='delete-trainer'),
    path('details_trainer/<int:pk>', views.TrainerDetailView.as_view(), name='details-trainer')
]