# Bloque 1: Problemas del caso y atributos ISO/IEC 25010:2023

Atributos: adecuación funcional, eficiencia de desempeño, compatibilidad, capacidad de interacción, fiabilidad, seguridad, mantenibilidad, flexibilidad, seguridad operacional (safety).

| Problema identificado en el caso | Atributo / Subcaracterística ISO 25010:2023 | Justificación técnica del impacto |
|---|---|---|
| Defectos escapados a producción | Adecuación Funcional (Exactitud / Corrección funcional) y Fiabilidad (Tolerancia a fallos) | La aplicación presenta comportamientos erróneos o fallos directos que impactan al usuario final al agendar citas, evidenciando brechas en la verificación antes de la entrega |
| Pruebas 100% manuales | Mantenibilidad (Capacidad de ser probado / Testabilidad) | Sin suites de pruebas automatizadas, verificar regresiones es lento, propenso al error humano y encarece la validación de cada incremento |
| Despliegues en viernes por la tarde | Fiabilidad (Madurez y Disponibilidad) y Operabilidad | Desplegar antes del fin de semana sin observabilidad ni rollback automatizado eleva el riesgo de tiempos de indisponibilidad prolongados durante días no laborables |
| Falta de puertas de calidad (Quality Gates) | Mantenibilidad (Modularidad y Reusabilidad) | El código se integra sin validación continua de estilo, cobertura de pruebas ni análisis estático, degradando progresivamente la base de código |
