import pytest
from django.urls import reverse
from conceptoFacturable.models import ConceptoFacturable


@pytest.mark.django_db
def test_view_home(client):
    url = reverse('conceptos_facturables_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_detail(client):

    concept = ConceptoFacturable.objects.create(
        concepto="Concepto Test",
        clase_concepto="Clase Concepto Test",
        operador="Operador Test",
        tipo_comunicacion="Tipo Comunicacion Test",
        concepto_operador="Concepto Operador Test",
        ambito="Ambito Test"
    )
    pk = concept.pk
    url = reverse('conceptos_facturables_detail', kwargs={'pk': pk})
    response = client.get(url)
    assert response.status_code == 200

    url = reverse('conceptos_facturables_detail', kwargs={'pk': pk+1})
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_view_nuevo(client):
    url = reverse('conceptos_facturables_nuevo')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_editar(client):

    concept = ConceptoFacturable.objects.create(
        concepto="Concepto Test",
        clase_concepto="Clase Concepto Test",
        operador="Operador Test",
        tipo_comunicacion="Tipo Comunicacion Test",
        concepto_operador="Concepto Operador Test",
        ambito="Ambito Test"
    )
    pk = concept.pk

    url = reverse('conceptos_facturables_editar', kwargs={'pk': pk})
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_editar_superuser(admin_client):

    concept = ConceptoFacturable.objects.create(
        concepto="Concepto Test",
        clase_concepto="Clase Concepto Test",
        operador="Operador Test",
        tipo_comunicacion="Tipo Comunicacion Test",
        concepto_operador="Concepto Operador Test",
        ambito="Ambito Test"
    )
    pk = concept.pk

    url = reverse('conceptos_facturables_editar', kwargs={'pk': pk})
    response = admin_client.get(url)
    assert response.status_code == 200

    url = reverse('conceptos_facturables_editar', kwargs={'pk': pk+1})
    response = admin_client.get(url)
    assert response.status_code == 404
