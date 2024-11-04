from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Category, Expense, Budget

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password':{'write_only': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email')
        )
        return user
    
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BudgetSerializer(ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
    
class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'