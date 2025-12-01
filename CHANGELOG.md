# Changelog
Todos los cambios importantes de este proyecto se documentarán en este archivo.

El formato está basado en **Keep a Changelog**
y este proyecto sigue **Semantic Versioning (SEMVER)**.

---

## [1.2.0] - 2025-01-12
### Added
- Nuevo módulo `datasets/loader.py` para gestión automática de datasets.
- Scripts en `notebooks/` para análisis exploratorio de datos.
- Integración con entorno `.env` usando `python-dotenv`.

### Changed
- Optimización del pipeline principal en `src/pipeline.py`.
- Refactorización de `models/model.py` para mayor claridad y mantenibilidad.

### Fixed
- Corrección de error al cargar rutas relativas en Windows.
- Arreglo en la función `train()` que no liberaba memoria correctamente.

---

## [1.1.0] - 2024-12-20
### Added
- Sistema de logging configurable mediante variables de entorno.
- Validaciones extra en el preprocesamiento de datos.

### Changed
- Reorganización del directorio `src/` para seguir una arquitectura más limpia.

### Deprecated
- El script `src/old_train.py` marcado como obsoleto.

---

## [1.0.1] - 2024-11-10
### Fixed
- Error tipográfico en el README.
- Inconsistencia en el `Makefile` al ejecutar `make train`.

---

## [1.0.0] - 2024-11-01
### Added
- Primera versión estable del proyecto.
- Estructura base de directorios (`src/`, `models/`, `datasets/`...).
- Implementación inicial del pipeline de entrenamiento.
- Archivo `.env.example` con variables necesarias para el entorno.
