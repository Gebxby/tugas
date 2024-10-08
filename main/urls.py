from django.urls import path
from main.views import show_main, create_menu,show_xml,show_json,show_xml_by_id, show_json_by_id,register,login_user,logout_user,edit_menu,delete_menu, add_menu_by_ajax



app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('create_menu', create_menu, name='create_menu'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-menu/<uuid:id>', edit_menu, name='edit_menu'),
    path('delete/<uuid:id>', delete_menu, name='delete_menu'),
    path('create-menu-by-ajax', add_menu_by_ajax, name='add_menu_by_ajax'),
    
    
]