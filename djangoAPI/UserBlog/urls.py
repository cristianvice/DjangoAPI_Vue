from django.urls import re_path
from UserBlog import views

urlpatterns=[
    re_path(r'^user$',views.userApi),
    re_path(r'^user/([0-9]+)$', views.userApi),

    re_path(r'^blog$',views.BlogApi),
    re_path(r'^blog/([0-9]+)$', views.BlogApi)
]