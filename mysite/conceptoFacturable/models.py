from django.db import models


class ConceptoFacturable(models.Model):
    concepto = models.CharField(max_length=100)
    clase_concepto = models.CharField(max_length=45)
    operador = models.CharField(max_length=45)
    tipo_comunicacion = models.CharField(max_length=45)
    concepto_operador = models.CharField(max_length=100)
    ambito = models.CharField(max_length=45)

    class Meta:
        verbose_name = "concepto_facturable"
        verbose_name_plural = "conceptos_facturables"
        ordering = ["pk"]

    def __str__(self):
        return self.concepto
