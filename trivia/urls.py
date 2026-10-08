from django.urls import path
from .views import CategoriaListView, PreguntaPorCategoriaListView

urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('preguntas/<int:categoria_id>/', PreguntaPorCategoriaListView.as_view(), name='pregunta-list-por-categoria'),
]
