from django.urls import include, path
from rest_framework import routers

from myproject.core import views as v

app_name = 'core'


router = routers.DefaultRouter()
router.register('users', v.UserViewSet)
router.register('groups', v.GroupViewSet)
router.register('funcionarios', v.FuncionarioViewSet)
router.register('departamentos', v.DepartamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
