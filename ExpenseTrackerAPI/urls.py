from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, ExpenseView, BudgetView

router = DefaultRouter()
router.register(r'expenses', ExpenseView, basename='expense')
router.register(r'budgets', BudgetView, basename='budget')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls))
]