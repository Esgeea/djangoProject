from django.urls import path

from student import views

urlpatterns = [
    path('create_student/', views.StudentCreateView.as_view(), name='create-student'),
    path('list_students/', views.StudentListView.as_view(), name='list-students'),
    path('get_students/<int:pk>/', views.get_all_students_per_trainer, name='get-students'),
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update-student'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete-student'),
    path('details_student/<int:pk>/', views.StudentDetailView.as_view(), name='details-student'),
    path('history_student/', views.HistoryStudentListView.as_view(), name='history-student'),
]