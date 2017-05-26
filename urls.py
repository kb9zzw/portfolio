"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from portfolio import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^contact/success/$', TemplateView.as_view(template_name="contact_success.html", content_type="text")),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),

    # Geospatial Projects
    url(r'^mn_climate/$', TemplateView.as_view(template_name="mn_climate.html"), name='mn_climate'),
    url(r'^svr_wx/$', TemplateView.as_view(template_name="svr_wx.html"), name='svr_wx'),
    url(r'^rsi/$', TemplateView.as_view(template_name="rsi.html"), name='rsi'),
    url(r'^lake_mead/$', TemplateView.as_view(template_name="lake_mead.html"), name='lake_mead'),

    # Geospatial Information Science
    url(r'^mapping/$', TemplateView.as_view(template_name="mapping.html"), name='mapping'),
    url(r'^interpolation/$', TemplateView.as_view(template_name="interpolation.html"), name='interpolation'),
    url(r'^suitability/$', TemplateView.as_view(template_name="suitability.html"), name='suitability'),
    url(r'^gps/$', TemplateView.as_view(template_name="gps.html"), name='gps'),
    url(r'^image_classification/$', TemplateView.as_view(template_name="image_classification.html"), name='image_classification'),
    url(r'^remote_sensing/$', TemplateView.as_view(template_name="remote_sensing.html"), name='remote_sensing'),

    # Geospatial Technologies
    url(r'^esri/$', TemplateView.as_view(template_name="esri.html"), name='esri'),
    url(r'^python/$', TemplateView.as_view(template_name="python.html"), name='python'),
    url(r'^open_source/$', TemplateView.as_view(template_name="open_source.html"), name='open_source'),
    url(r'^web_services/$', TemplateView.as_view(template_name="web_services.html"), name='web_services')
    
]
