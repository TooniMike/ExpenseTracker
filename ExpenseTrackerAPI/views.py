from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from .serializers import RegisterSerializer, ExpenseSerializer, BudgetSerializer
from .models import Expense, Budget

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
