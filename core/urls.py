# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include, re_path  # add this
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path('api-auth/', include('rest_framework.urls')),  #  Usage: To add REST framework's login and logout views
    path("", include("apps.authentication.urls")),  # Auth routes - login / register
    path("", include("apps.app.urls")),             # UI Kits Html files

    # path('acctcust/', include('acctcust.urls')),
    # path('labordeliverytype/', include('labordeliverytype.urls')),
    # path('labordelivery/', include('labordelivery.urls')),
    # path('tntworksheet/', include('tntworksheet.urls')),
    # path('statusstate/', include('statusstate.urls')),
    path('prodvendor/prodvendor.html', include('prodvendor.urls')),
    # path('orderitem/', include('orderitem.urls')),
    # path('orderitem_mgr/', include('orderitem_mgr.urls')),
    # path('order_mgr/', include('order_mgr.urls')),

    path('product/', include('product.urls')),
    path('category', include('category.urls')),


]
