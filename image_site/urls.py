from django.conf.urls import url, include
from django.contrib import admin
from notgur.views import ImageListView, ImageCreateView, UserCreateView, ProfileView, ImageUpdateView, \
                        ImageDetailView, CommentFormView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', ImageListView.as_view(), name="image_list_view"),
    url(r'^comment_form/(?P<pk>\d+)/$',CommentFormView.as_view(), name='comment_form_view'),
    url(r'^profile/$', ProfileView.as_view(), name="profile_view"),
    url(r'^create/$', ImageCreateView.as_view(), name="image_create_view"),
    url(r'^update/(?P<pk>\d+)/$', ImageUpdateView.as_view(), name="image_update_view"),
    url(r'^image/(?P<pk>\d+)/$', ImageDetailView.as_view(), name="image_detail_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
