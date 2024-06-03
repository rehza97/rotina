import django_filters
from accounts.models import Account

        
class PatientFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Account
        fields = ['username']

