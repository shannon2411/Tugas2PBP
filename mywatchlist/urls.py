from django.urls import path
from mywatchlist.views import show_watchlist, show_watchlist_main
from mywatchlist.views import show_json
from mywatchlist.views import show_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist_main, name='show_watchlist_main'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('html/', show_watchlist, name='show_watchlist'),
]