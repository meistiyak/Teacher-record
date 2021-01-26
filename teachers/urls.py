from django.urls import path

from . import views

urlpatterns = [
  path('list', views.teacher_list, name='teacher-list'),
  path('<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
  path('create/', views.TeacherCreateView.as_view(), name='teacher-create'),
  path('<int:pk>/update/', views.TeacherUpdateView.as_view(), name='teacher-update'),
  path('delete/<int:pk>/', views.TeacherDeleteView.as_view(), name='teacher-delete'),
  path('upload/', views.TeacherBulkUploadView.as_view(), name='teacher-upload'),
  path('download-csv/', views.download_csv, name='download-csv'),

]
