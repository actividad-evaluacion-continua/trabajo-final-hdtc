name: Solicitud de funcionalidad
description: Sugiere una mejora o nueva característica
title: "[FEATURE] Breve descripción de la propuesta"
labels: enhancement
assignees: ''

body:
  - type: markdown
    attributes:
      value: |
        ¿Tienes una idea para mejorar el proyecto? ¡Cuéntanos!

  - type: input
    id: objetivo
    attributes:
      label: ¿Qué problema resuelve esta funcionalidad?
      description: Describe el objetivo o necesidad que cubre
      placeholder: "Ejemplo: Mejorar la experiencia de usuario al buscar datos"

  - type: textarea
    id: propuesta
    attributes:
      label: Descripción de la funcionalidad
      description: Explica qué propones y cómo debería funcionar
      placeholder: "Ejemplo: Añadir un botón de búsqueda con filtros por fecha"

  - type: textarea
    id: impacto
    attributes:
      label: Impacto esperado
      description: ¿Cómo beneficiaría al proyecto o a los usuarios?
      placeholder: "Ejemplo: Facilitar el acceso a datos específicos y ahorrar tiempo"
