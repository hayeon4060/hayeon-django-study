# 1번

from django.contrib import admin
from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV
urlpatterns = [
    path('admin/', admin.site.urls),

    #Class-based views
    path('bookmark/', BookmarkLV.as_view(), name='index'),
    path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail')
]


# 2번

# from django.contrib import admin
# from django.urls import path
# from django.views.generic import ListView, DetailView
# from bookmark.models import Bookmark


# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # urls with view definition
#     path('bookmark/', ListView.as_view(model=Bookmark), name='index'),
#     path('bookmark/<int:pk>', DetailView.as_view(model=Bookmark), name='detail')
# ]
