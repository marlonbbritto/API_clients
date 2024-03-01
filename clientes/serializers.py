from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_valido, nome_valido,rg_valido,celular_valido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self,data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 digitos'})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome deve conter apenas caracteres alfabeticos'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"o RG deve ter 9 digitos"})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O celular deve seguir o padrão (dd) 00000-0000"})
        return data
    
        
    
   
    
    