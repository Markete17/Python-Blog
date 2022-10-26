import pytest

from django.contrib.auth.models import User
from conceptoFacturable.models import ConceptoFacturable


# transaction = Para solicitar acceso a la base de datos
# (al marcar django_db se pone True por defecto)
# reset_sequences =  reinicio de secuencias de incremento automático

@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_user_create():

    User.objects.create_user('marcos', 'marcos@gmail.com', 'password')
    assert User.objects.count() == 1


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_concepto_facturable_create():
    concepto = ConceptoFacturable.objects.create(
        concepto="Concepto Test",
        clase_concepto="Clase Concepto Test",
        operador="Operador Test",
        tipo_comunicacion="Tipo Comunicacion Test",
        concepto_operador="Concepto Operador Test",
        ambito="Ambito Test"
    )
    conceptoAssert = ConceptoFacturable.objects.get(pk=concepto.pk)
    assert concepto == conceptoAssert


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_concepto_facturable_list():
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
    assert conceptos[0] == concepto1
    assert conceptos[1] == concepto2


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_concepto_facturable_detalle():
    concepto = ConceptoFacturable.objects.create(
        concepto="CreateTest00",
        clase_concepto="Clase concepto Test",
        operador="Operador Test",
        tipo_comunicacion="Tipo Comunicacion Test",
        concepto_operador="Concepto Operador Test",
        ambito="Ambito Test"
    )
    conceptoAssert = ConceptoFacturable.objects.get(pk=concepto.pk)
    assert concepto == conceptoAssert


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_concepto_facturable_editar():

    text_test = "Edit Test"

    concepto = ConceptoFacturable.objects.create(
        concepto="CreateTest00",
        clase_concepto="Clase concepto Test",
        operador="Operador Test",
        tipo_comunicacion="Tipo Comunicacion Test",
        concepto_operador="Concepto Operador Test",
        ambito="Ambito Test"
    )
    concepto.concepto = text_test
    concepto.save()

    concepto_assert = ConceptoFacturable.objects.get(pk=concepto.pk)
    assert concepto_assert.concepto == text_test
