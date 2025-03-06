from django.conf.urls.static import static
from django.urls import path
from Books import settings
from .views import HomeView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/", ProductView.as_view(), name="product"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="delete"),
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)