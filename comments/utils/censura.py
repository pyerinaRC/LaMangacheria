import unicodedata
import re

PALABRAS_PROHIBIDAS = [
    "puta", "puto", "mierda", "cabron", "imbecil", "pendejo", "culero",
    "coño", "malparido", "gilipollas", "estupido", "perra", "zorra",
    "marica", "hpta", "gonorrea", "idiota", "verga", "joder", "hdp",
]

def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto.lower())
        if not unicodedata.combining(c)
    )

def censurar_lenguaje(texto):
    normalizado = normalizar(texto)
    censurado = list(texto)

    for palabra in PALABRAS_PROHIBIDAS:
        for match in re.finditer(rf'\b{palabra}\b', normalizado):
            inicio, fin = match.start(), match.end()
            for i in range(inicio + 1, fin):
                if i < len(censurado) and censurado[i].isalpha():
                    censurado[i] = '*'

    return ''.join(censurado)
