from django.db import models
import json

from dispositivos.models import Dispositivos

class Acoes(models.Model):
    acao = models.CharField(max_length=45,blank=False,null=False)
    dispositivo = models.ForeignKey(Dispositivos, on_delete=models.CASCADE)
    def __str__(obj):
        tmp = {
            "id": obj.id,
            "acao": obj.acao,
            "dispositivo": obj.dispositivo,
        }
        
        return json.dumps(tmp)