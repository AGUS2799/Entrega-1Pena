from django.urls import path

from app_1 import views

app_name='app_1'
urlpatterns = [
    path('', views.index, name='Home'),
    path('jugadores', views.players, name='Jugadores'),
    path('nuevos-jugadores', views.new_players, name='NuevosJugadores'),
    path('editar/<int:pk>/jugador', views.player_edit, name='EditPlayer'),
    path('eliminar/<int:pk>/jugador', views.delete_player, name='DeletePlayer'),
    path('categorias', views.category, name='Category'),
    path('nueva-categoria', views.new_category, name='NewCategory'),
    path('eliminar/<int:pk>/categoria', views.delete_category, name='DeleteCategory'),
    path('editar/<int:pk>/categoria', views.category_edit, name='EditCategory'),
    path('ganadores', views.winners, name='Winners'),
    path('nuevos-ganadores', views.new_winners, name='NewWinners'),
    path('eliminar/<int:pk>/ganadores', views.delete_winners, name='DeleteWinners'),
    path('editar/<int:pk>/ganadores', views.winners_edit, name='EditWinners'),
]
