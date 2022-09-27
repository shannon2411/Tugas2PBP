from django.urls import path
from todolist.views import register 
from todolist.views import login_user 
from todolist.views import logout_user
from todolist.views import show_todolist
from todolist.views import show_create_todo

app_name = 'todolist'

urlpatterns = [
    # path('', show_watchlist_main, name='show_watchlist_main'),
    # path('xml/', show_xml, name='show_xml'), 
    # path('json/', show_json, name='show_json'),
    # path('html/', show_watchlist, name='show_watchlist'),
    path('', show_todolist, name="show_todolist"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', show_create_todo, name='show_create_todo')
]