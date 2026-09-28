# Definition of Done (DoD)

| # | Criterio | Atributo ISO 25010 | Evidencia |
| :---: | :--- | :--- | :--- |
| 1 | Pruebas unitarias completas: Cobertura de código superior al 80% y 100% de las pruebas pasando en verde. | Mantenibilidad (Capacidad de ser probado / Testabilidad) y Fiabilidad (Tolerancia a fallos) | Reporte de cobertura generado por `pytest-cov` en consola o artefacto de CI (mínimo 80% sin fallos). |
| 2 | Revisión de pares (Peer Review): Pull Request aprobado formalmente por al menos un desarrollador del equipo antes de fusionar a `main`. | Mantenibilidad (Modularidad y Modificabilidad) | Aprobación formal registrada en el historial del Pull Request en GitHub con comentarios de revisión cerrados. |
| 3 | Validación CI/CD: El pipeline automatizado de integración continua pasa sin errores ni alertas críticas de linters. | Mantenibilida (Analizabilidad) y Fiabilidad (Madurez) | Badge o check verde de GitHub Actions en la rama con la ejecución limpia de Flake8 y Pytest. |
| 4 | Criterios de aceptación cumplidos: Verificación funcional explícita de todos los escenarios de la historia de usuario. | Adecuación Funcional (Completitud funcional y Corrección) | Casos de prueba funcionales verificados y marcados como exitosos en la issue/tarjeta correspondiente. |
| 5 | Documentación al día: Endpoints actualizados en Swagger/OpenAPI o `README.md` documentado según corresponda. | Usabilidad (Capacidad de aprendizaje / Aprendibilidad) | Commit que incluye la actualización en el `README.md`, docstrings de métodos o archivo de especificación de la API. |
| 6 | Despliegue verificado en ambiente Staging: La funcionalidad está desplegada y probada en el entorno previo a producción. | Fiabilidad (Disponibilidad) y Compatibilidad | Registro de despliegue exitoso en el entorno de pruebas/staging y validación de humo (smoke test) sin errores. |
