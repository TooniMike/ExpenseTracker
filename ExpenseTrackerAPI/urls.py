from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, ExpenseView, BudgetView, AnalyticsView

router = DefaultRouter()
router.register(r'expenses', ExpenseView, basename='expense')
router.register(r'budgets', BudgetView, basename='budget')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
     path('analytics/detailed/', AnalyticsView.as_view(), name='detailed-analytics'),
]