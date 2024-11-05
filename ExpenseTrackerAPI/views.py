from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets, status
from .serializers import RegisterSerializer, ExpenseSerializer, BudgetSerializer
from .models import Expense, Budget
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.utils.dateparse import parse_date
from django.db.models import Sum
from rest_framework.response import Response

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    pagination_class = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    
class ExpenseView(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
        
        
class BudgetView(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class AnalyticsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Parse query parameters for date filtering
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        # Filter expenses by user and date range (if provided)
        
        expenses = Expense.objects.filter(user=request.user)
        if start_date:
            expenses = expenses.filter(date__gte=parse_date(start_date))
        if end_date:
            expenses = expenses.filter(date__lte=parse_date(end_date))
            
        # Calculate total expenses in the time period
        total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
        
        # Calculate category-wise expenses
        category_expenses = (
            expenses.values('category__name')
            .annotate(total=Sum('amount'))
            .order_by('category__name')
        )
        
        # Calculate remaining budget for each category
        remaining_budgets = []
        budgets = Budget.objects.filter(user=request.user)
        for budget in budgets:
            category_expenses_total = expenses.filter(category=budget.category).aggregate(total=Sum('amount'))['total'] or 0
            remaining_amount = budget.amount - category_expenses_total
            remaining_budgets.append({
                'category': budget.category.name,
                'budgeted_amount': budget.amount,
                'spent_amount': category_expenses_total,
                'remaining_amount': remaining_amount
            })
            
             # Prepare the response data
            data = {
            'total_expenses': total_expenses,
            'category_expenses': list(category_expenses),
            'remaining_budgets': remaining_budgets,
        }
            
        return Response(data, status=status.HTTP_200_OK)
