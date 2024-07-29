
from django.contrib import admin
from django.urls import path,include
from olcha.views import CategoryListView, GroupListView,ProductListView,ImagelistView
from olcha import views
from olcha.auth import UserLoginAPIView,UserRegisterAPIView, UserLogoutAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category',views.CategoryModelViewSet,basename='category'),

router.register('group',views.GroupModelViewSet,basename='group')
router.register('product',views.ProductModelViewSet,basename='product')

urlpatterns = [
    path('router',include(router.urls)),
    path('category/', CategoryListView.as_view(),name='index'),
    path('group/', GroupListView.as_view(),name='group'),
    path('product/', ProductListView.as_view(),name='product'),
    path('image/', ImagelistView.as_view(),name='image'),
    # path('atribut/', ProductAtributListView.as_view(),name='atribut'),
    # path('detail/<slug:slug>/',CategoryDetail.as_view(),name='detail'),
    path('delet/<int:pk>', views.CategoryDelete.as_view(),name='Delete'),
    #""" CRUD """
    path('CRUD_category/', views.CategitiyListCRUD.as_view(),name='CRUD_category'),
    path('CRUD_product/', views.ProductList_CRUD.as_view(),name='CRUD_product'),
    path('CRUD_group/', views.GroupList_CRUD.as_view(),name='CRUD_group'),
    path('CRUD_detail/<int:pk>', views.CategoryDetialCRUD.as_view(),name='CRUD_detail'),

    path('CRUD_Add_Category/', views.CategoryAddCRUD.as_view(),name='CRUD_Add_Category'),
    path('CRUD_Add_Group/', views.GroupAddCRUD.as_view(),name='CRUD_Add_Group'),
    path('CRUD_Add_Product/', views.ProductAddCRUD.as_view(),name='CRUD_Add_Product'),

    path('Categoty_Updata/<int:pk>',views.CategoryUpdata.as_view(),name='Categoty_Updata'),
    path('Group_Updata/<int:pk>',views.GroupUpdata.as_view(),name='Group_Updata'),
    path('Product_Updata/<int:pk>',views.ProductUpdata.as_view(),name='Product_Updata'),

    path('category_delete/<int:pk>',views.CategoryDelete.as_view(),name='category_delete'),
    path('group_delete/<int:pk>',views.GroupDelete.as_view(),name='group_delete'),
    path('product_delete/<int:pk>',views.ProductDelete.as_view(),name='product_delete'),


###LOGIN
    path('login/', UserLoginAPIView.as_view(),name='login'),
    path('register/',UserRegisterAPIView.as_view(),name='register'),
    path('logout/', UserLogoutAPIView.as_view(),name='logout'),

]
