from rest_framework import routers,serializers,viewsets
from webpage.models import employees
class employeesSerializers(serializers.ModelSerializer):
    class Meta:
        model=employees
        fields='__all__'