from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import configuracao.settings
from api.views import AlunoViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
