# Guía para Contribuir

¡Gracias por tu interés en contribuir a este proyecto!
Sigue estas instrucciones para mantener un flujo de trabajo ordenado y colaborativo.

---

## 🚀 Proceso de Contribución

### 1. Haz un Fork del repositorio
Crea tu copia y clónala localmente.

### 2. Crea una rama para tu trabajo
Usa un nombre descriptivo siguiendo la convención:


### 3. Realiza tus cambios
Puedes modificar código en `src/`, notebooks en `notebooks/`, o componentes de visualización en `streamlit_app/`.

Asegúrate de:
- Mantener un estilo de código limpio y consistente.
- Documentar las funciones si añades nuevo comportamiento.

### 4. Ejecuta comprobaciones antes de enviar cambios
Antes de crear un Pull Request:

- Ejecuta los tests si los hay (`pytest`, `make test`, etc.).
- Revisa los notebooks localmente para evitar celdas corruptas o outputs innecesarios.
- Asegúrate de que los mensajes de commit siguen las buenas prácticas.

### 5. Abre un Pull Request hacia `main`
Incluye en el PR:

- **Descripción clara del cambio**
- **Motivación del cambio** (por qué es necesario)
- **Checklist** como:
  - [ ] Código probado localmente
  - [ ] Documentación actualizada (si aplica)
  - [ ] No rompe compatibilidad previa

### 6. Etiqueta a los revisores del equipo
Asigna al menos a un revisor responsable del módulo que tocaste.

---

## 📌 Normas y Buenas Prácticas

### 📝 Mensajes de commit
Usar prefijos tipo *Conventional Commits*:


### 📚 Sobre los notebooks
- Si modificas un notebook grande, envía **un PR por notebook** para facilitar la revisión.
- Limpia salidas innecesarias antes de subirlo.
- Mantén celdas ejecutadas en orden.

### 🔧 Estilo de código
- Sigue PEP8 (si es Python).
- Usa tipado cuando sea posible.
- Evita funciones demasiado largas.

---

## 🤝 Preguntas o soporte
Si necesitas orientación antes de contribuir, puedes abrir una *issue* o contactar al equipo del proyecto.

¡Gracias por ayudar a mejorar este repositorio!
