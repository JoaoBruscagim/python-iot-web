from django.db import models
import json
class Dispositivos(models.Model):
    nome = models.CharField(max_length=50, blank=False,null=False)
    endereco = models.CharField(max_length=15,blank=False,null=False)
    chave = models.CharField(max_length=50, blank=True,null=True)
    devId = models.CharField(max_length=50, blank=False,null=False,default='0')
    ativo = models. BooleanField(default=True)
    def __str__(obj):
        tmp = {
            "id": obj.id,
            "nome": obj.nome,
            "endereco": obj.endereco,
            "chave": obj.chave,
            "devId": obj.devId
        }
        
        return json.dumps(tmp)