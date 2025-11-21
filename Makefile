# Makefile

# Acción por defecto
help:
	@echo "Acciones disponibles:"
	@echo "  install   -> Instala dependencias del proyecto"
	@echo "  run       -> Ejecuta el script principal training.py"
	@echo "  clean     -> Elimina archivos temporales y caché de Python"

# Instalar dependencias
install:
	pip3 install -r requirements.txt

# Ejecutar el script principal
run:
	python3 training.py

# Limpiar archivos temporales
clean:
	rm -rf __pycache__ *.pyc *.pyo
