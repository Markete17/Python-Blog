from django.test import TestCase
from conceptoFacturable.models import ConceptoFacturable


# Create your tests here.
class test_concepto_facturable(TestCase):

    # python manage.py test conceptoFacturable.tests.test_concepto_facturable
    # test_concepto_facturable_create
    def test_concepto_facturable_create(self):
        concepto = ConceptoFacturable.objects.create(
            concepto="Concepto Test",
            clase_concepto="Clase Concepto Test",
            operador="Operador Test",
            tipo_comunicacion="Tipo Comunicacion Test",
            concepto_operador="Concepto Operador Test",
            ambito="Ambito Test"
        )
        conceptoAssert = ConceptoFacturable.objects.get(pk=concepto.pk)
        self.assertEqual(concepto, conceptoAssert)

    # python manage.py test conceptoFacturable.tests.test_concepto_facturable
    # test_concepto_facturable_list
    def test_concepto_facturable_list(self):

        conceptsAssert = []
        concepto1 = ConceptoFacturable.objects.create(
            concepto="Concepto Test1",
            clase_concepto="Clase concepto Test1",
            operador="Operador Test1",
            tipo_comunicacion="Tipo Comunicacion Test1",
            concepto_operador="Concepto Operador Test1",
            ambito="Ambito Test1"
        )
        concepto2 = ConceptoFacturable.objects.create(
            concepto="Concepto Test2",
            clase_concepto="Clase concepto Test2",
            operador="Operador Test2",
            tipo_comunicacion="Tipo Comunicacion Test2",
            concepto_operador="Concepto Operador Test2",
            ambito="Ambito Test2"
        )
        conceptsAssert.append(concepto1)
        conceptsAssert.append(concepto2)

        conceptos = ConceptoFacturable.objects.all()
        self.assertEqual(conceptos[0], concepto1)
        self.assertEqual(conceptos[1], concepto2)

    # python manage.py test conceptoFacturable.tests.test_concepto_facturable
    # test_concepto_facturable_detalle
    def test_concepto_facturable_detalle(self):
        concepto = ConceptoFacturable.objects.create(
            concepto="CreateTest00",
            clase_concepto="Clase concepto Test",
            operador="Operador Test",
            tipo_comunicacion="Tipo Comunicacion Test",
            concepto_operador="Concepto Operador Test",
            ambito="Ambito Test"
        )
        conceptoAssert = ConceptoFacturable.objects.get(pk=concepto.pk)
        self.assertEqual(concepto, conceptoAssert)

    # python manage.py test conceptoFacturable.tests.test_concepto_facturable
    # test_concepto_facturable_editar
    def test_concepto_facturable_editar(self):

        concepto = ConceptoFacturable.objects.create(
            concepto="CreateTest00",
            clase_concepto="Clase concepto Test",
            operador="Operador Test",
            tipo_comunicacion="Tipo Comunicacion Test",
            concepto_operador="Concepto Operador Test",
            ambito="Ambito Test"
        )
        concepto.concepto = "Edit Test"
        concepto.save()

        conceptoAssert = ConceptoFacturable.objects.get(pk=concepto.pk)
        self.assertEqual(conceptoAssert.concepto, "Edit Test")
