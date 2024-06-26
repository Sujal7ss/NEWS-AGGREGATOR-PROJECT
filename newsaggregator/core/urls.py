from django.urls import path
from core import views

app_name='core'

urlpatterns=[
    path('',views.news_list,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('advertise/',views.advertise,name='advertise'),
    path('privacy/',views.privacy,name='privacy'),
    path('scrape/<str:name>', views.scrape, name="scrape"),

    # bookmarking
    path('bookmark/<int:headline_id>/', views.bookmark_article, name='bookmark_article'),
    path('bookmarks/', views.view_bookmarks, name='view_bookmarks'),
    path('remove_bookmark/<int:headline_id>/', views.remove_bookmark, name='remove_bookmark'),
]