import streamlit as st
import pytest

def test_app():
    # Este es un ejemplo muy básico. Puedes agregar más pruebas en función de tu aplicación.
    st.write("Test")
    assert "Test" in st.session_state
