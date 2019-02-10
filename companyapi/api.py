from rest_framework import routers
from company import views as myapp_views

router = routers.DefaultRouter()
router.register(r'company', myapp_views.ComapnyViewSet, basename='companies')
router.register(r'^(?P<pk>\d+)/$', myapp_views.ComapnyViewSet,name='create_events'),)
