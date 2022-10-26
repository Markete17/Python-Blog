import pytest
from conceptoFacturable.models import ConceptoFacturable
from django.urls import reverse


@pytest.mark.django_db
def test_concepto_detail(client):

    concept = ConceptoFacturable.objects.create(
        concepto="CreateTest00",
        clase_concepto="Clase concepto Test",
        operador="Operador Test",
        tipo_comunicacion="Tipo Comunicacion Test",
        concepto_operador="Concepto Operador Test",
        ambito="Ambito Test"
    )

    url = reverse('conceptos_facturables_detail', kwargs={'pk': concept.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert concept.concepto in str(response.content)
    assert concept.clase_concepto in str(response.content)
    assert concept.tipo_comunicacion in str(response.content)
    assert concept.concepto_operador in str(response.content)
    assert concept.concepto in str(response.content)
    assert concept.ambito in str(response.content)
