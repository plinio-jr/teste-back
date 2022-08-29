from pyexpat import model
from unicodedata import decimal
from django.db import models

class Lista(models.Model):
    nome_lista = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    cod_lista = models.CharField(max_length=10)
    
class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    categoria_produto = models.CharField(max_length=255)
    quantidade_produto = models.CharField(max_length=3)
    peso_produto = models.FloatField(max_length=5)
    preco_produto = models.FloatField(max_length=5)
    
class Mercado(models.Model):
    nome_mercado = models.CharField(max_length=255)
    rua_mercado = models.CharField(max_length=255)
    bairro_mercado = models.CharField(max_length=255)
    avaliacao_mercado= models.CharField(max_length=2)
    
