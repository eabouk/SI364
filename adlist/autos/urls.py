from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.AutoListView.as_view(), name='autos'),
    #path('ads', views.AdListView.as_view(), name='ads'),
    path('autos/<int:pk>/detail', views.AutoDetailView.as_view(), name='auto_detail'),
    path('autos/create', 
        views.AutoFormView.as_view(success_url=reverse_lazy('autos')), name='auto_create'),
    path('autos/<int:pk>/update', 
        views.AutoFormView.as_view(success_url=reverse_lazy('autos')), name='auto_update'),
    path('autos/<int:pk>/delete', 
        views.AutoDeleteView.as_view(success_url=reverse_lazy('autos')), name='auto_delete'),
#    path('auto_picture/<int:pk>', views.stream_file, name='ad_picture'),
    path('autos/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='comment_create'),
    path('autos/comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('forums')), name='comment_delete')
#    path('ad/<int:pk>/favorite',
#    views.AddFavoriteView.as_view(), name='ad_favorite'),
#    path('ad/<int:pk>/unfavorite',
#    views.DeleteFavoriteView.as_view(), name='ad_unfavorite')
]
