import nbformat
from nbconvert import PythonExporter
import pytest

def test_notebook():
    # Cargar el notebook
    with open("notebooks/Heart_Disease_EDA.ipynb") as f:
        nb = nbformat.read(f, as_version=4)

    # Convertir el notebook a código Python
    exporter = PythonExporter()
    body, resources = exporter.from_notebook_node(nb)

    # Ejecutar el código en un entorno aislado
    exec(body)  # Puedes agregar pruebas específicas aquí si lo deseas
    assert True  # Si el código corre sin errores, la prueba es exitosa
