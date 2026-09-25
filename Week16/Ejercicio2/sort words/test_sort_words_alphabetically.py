import pytest

from sort_words_alphabetically import sort_sentence

def test_sort_sentence_works_correctly():
    input_sentence = "python-variable-funcion-computadora-monitor"
    result = sort_sentence(input_sentence)
    assert result == "computadora-funcion-monitor-python-variable"


def test_sort_sentence_only_works_wiht_Str():
    input_sentence = [1245]
    with pytest.raises(AttributeError):
        sort_sentence(input_sentence) 


def test_sort_sentence_works_with_big_sentences():
    input_sentence = " luz - montaña - reloj - esfera - café - mapa - tinta - cristal - sombra - fuego - llave - papel - camino - sol - trueno - libro - puente - cielo - roca - ola - silencio - puerta - estrella - nube - raíz - espejo - tierra - viento - flor - luna - nieve - caja - sombra - faro - pluma - sendero - hielo - campana - murmullo - jardín - piedra - arbol - humo - río - ventana - isla - noche - palabra - corazón - horizonte"
    result = sort_sentence(input_sentence)
    assert result == " arbol - café - caja - camino - campana - cielo - corazón - cristal - esfera - espejo - estrella - faro - flor - fuego - hielo - horizonte- humo - isla - jardín - libro - llave - luna - luz - mapa - montaña - murmullo - nieve - noche - nube - ola - palabra - papel - piedra - pluma - puente - puerta - raíz - reloj - roca - río - sendero - silencio - sol - sombra - sombra - tierra - tinta - trueno - ventana - viento "