from .models import User, Expense, ExpensePaidBy, ExpenseOwedBy
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'name', 'email', 'mobileNumber']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['expenseId', 'desc', 'amount', 'createdById', 'createdAt']

class ExpensePaidBySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensePaidBy
        fields = ['userId', 'expenseId', 'amount']

class ExpenseOwedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseOwedBy
        fields = ['userId', 'expenseId', 'amount']