import os
from app import app

# Cargar configuración desde un archivo específico si es necesario
# app.config.from_object('config.Config')  # Ajusta esta línea si necesitas cargar configuraciones específicas

if __name__ == "__main__":
    app.run()
