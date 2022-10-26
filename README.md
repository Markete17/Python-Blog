# Pytest

1. Primero instalar Pytest con: <b>pip install pytest-django</b>
2. Crear un fichero en el directorio raíz del proyecto para configurar Pytest llamado: <b>pytest.ini</b>

<pre><code>
[pytest]
DJANGO_SETTINGS_MODULE = yourproject.settings
python_files = tests.py test_*.py *_tests.py
</code></pre>

3. Las pruebas en pytest se ejecutan con estos índices:

<p>
pytest a_directory                     # directory
pytest test_something.py               # tests file
pytest test_something.py::single_test  # single test function
</p>

4. Database Helpers
<p>
Son anotaciones que empiezan: <b>@pytest.mark.django_db</b> y singifica que se va a crear la base de datos para el test y luego se destruirá
</p>
https://pytest-django.readthedocs.io/en/latest/helpers.html

- Probar la base de datos

<pre><code>
@pytest.mark.django_db(transaction=True)
def test_user_create():

    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() == 1
</code></pre>

- Probar Vistas

Con el método <b>reverse</b> pasando como argumento el name de las rutas del archivo <b>urls.py</b> se obtendrá la respuesta de la petición http.

<pre><code>
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
</code></pre>

- Probar Vistas protegidas.

Primero, crear una ruta protegida, para ello modificar el views.py y usar el import: <b>from django.contrib.auth.decorators import login_required</b>

Luego, para hacer que una vista esté protegida, en el views.py, arriba del método, establecer la anotación <b>@login_required</b>

Para que solo sea accedido por admins, incluir la anotacion <b>@staff_member_required</b> del import: <b>from django.contrib.admin.views.decorators import staff_member_required</b>

Después, es necesario especificar a Django  la ruta de Login. Para ello, editar el settings.py y añadir una constante llamada: <b>LOGIN_URL = '/admin/'</b>

- Fixtures