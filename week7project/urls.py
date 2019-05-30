from django.contrib import admin
from django.urls import path
from write import views as write
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', write.home, name='home'),
    path('create/', write.create, name='create'),
    path('new/', write.new, name="new"),
    path('read/<int:blog_id>/', write.read, name="read"),
    path('read/<int:blog_id>/update/', write.update, name='update'),
    path('read/<int:blog_id>/renew/', write.renew, name='renew'),
    path('read/<int:blog_id>/delete', write.delete, name='delete'),
    path('accounts/signup/', accounts.signup, name='signup'),
    path('accounts/login/', accounts.login, name='login'),
    path('accounts/logout/', accounts.logout, name='logout'),
    path('<int:blog_id>/comment/create', write.create_c, name="comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
