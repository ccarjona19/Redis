import redis

# Función para conectarse a Redis
def conectar_redis():
    r = redis.Redis(host='localhost', port=6379)
    
    # Diccionario a insertar en Redis
    diccionario = [{"palabra": "tongo", "significado": "policia"},
            {"palabra": "gringo", "significado": "persona de origen anglo no habla espaniol"},
            {"palabra": "mopri", "significado": "primo"},
            {"palabra": "llesca", "significado": "calle"},
            {"palabra": "compa", "significado": "compadre"}]

    # Insertar cada par clave-valor en Redis
    for palabra in diccionario:
        r.set(palabra['palabra'], palabra['significado'])  
    return r

  