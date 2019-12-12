from django.contrib import admin
from django.urls import path, re_path

from bugtracker import views
from bugtracker.models import Ticket
from bugtracker.views import index, login_view, logout_view, signup_view, user_view, ticket_view, create_ticket_view, edit_ticket_view

from bugtracker.views import UserProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('home/', index),
    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', signup_view, name='signup'),
    path('ticket/<int:id>', ticket_view, name='ticket'),
    path('createticket/', create_ticket_view, name='createticket'),
    path('editticket/<int:id>', edit_ticket_view, name='editticket'),
    path('user/<int:id>', user_view, name='user'),

    
    # By user ID
    re_path(r'^profile/id/(?P<pk>\d+)/$', UserProfileView.as_view()),
    # By username
    re_path(r'^user/(?P<slug>[\w.@+-]+)/$', UserProfileView.as_view())
]