from django.urls import path
from. import views

urlpatterns = [
    # path('',views.task,name='task'),
    # path('delete/<int:taskid>',views.delete,name='dlt'),
    # path('update/<int:id>',views.update,name='update'),

    # path('cbvtask/',views.TaskListView.as_view(),name='cbvtask'),

    path('', views.TaskListView.as_view(), name='cbvtask'),
    path('add',views.task,name='add'),

    path('cbvdetail/<int:pk>',views.TaskDetailView.as_view(),name='detail'),
    path('cbvupdate/<int:pk>',views.TaskUpdateView.as_view(),name='update'),
    path('cbvdelete/<int:pk>', views.TaskDeleteView.as_view(), name='dlt'),

]
