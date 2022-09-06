from django.urls import path     

from users.views import (
    # account_view,
    # crop_image,
    # edit_account,
    dashboard_view,
)

app_name = 'users'

urlpatterns = [
    # path('<user_id>/', account_view, name="view"),
    path('dashboard/<user_id>/', dashboard_view, name="dashboard"),
    # path('<user_id>/edit_account/', edit_account, name="edit"),
    # path('<user_id>/edit_account/crop_image', crop_image, name="crop_image"),
]
