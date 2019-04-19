from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.CatListView.as_view(), name='cats'),
    path('cats/<int:pk>/detail', views.CatDetailView.as_view(), name='cat_detail'),
    path('cats/create', 
        views.CatFormView.as_view(success_url=reverse_lazy('cats')), name='cat_create'),
    path('cats/<int:pk>/update', 
        views.CatFormView.as_view(success_url=reverse_lazy('cats')), name='cat_update'),
    path('cats/<int:pk>/delete', 
        views.CatDeleteView.as_view(success_url=reverse_lazy('cats')), name='cat_delete'),
#    path('auto_picture/<int:pk>', views.stream_file, name='ad_picture'),
    path('cats/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='comment_create'),
    path('cats/comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('forums')), name='comment_delete')
]