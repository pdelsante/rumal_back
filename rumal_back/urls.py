from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api
from main.api import *

v1_api = Api(api_name='v1')
v1_api.register(ProxyResource())
v1_api.register(TaskResource())
v1_api.register(AnalysisResource())
v1_api.register(UrlResource())
v1_api.register(PcapResource())
v1_api.register(BehaviorResource())
v1_api.register(ConnectionResource())
v1_api.register(LocationResource())
v1_api.register(CodeResource())
v1_api.register(SampleResource())
v1_api.register(CertificateResource())
v1_api.register(ExploitResource())
v1_api.register(GraphResource())
v1_api.register(ComboResource())
v1_api.register(StatusResource())

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # APIs
    url(r'^api/', include(v1_api.urls)),
]
