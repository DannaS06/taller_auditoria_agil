# Tablero Kanban: políticas por columna

Enlace o captura del tablero: [Tablero Kanban](https://github.com/users/DannaS06/projects/1/views/1)

| Columna | Límite WIP | Política de entrada | Política de salida |
|---|:---:|---|---|
| Por hacer | 4 | Historia de usuario refinada con criterios de aceptación claros, estimada y sin dependencias técnicas bloqueantes (cumple Definition of Ready) | Un desarrollador toma la tarjeta solo si hay cupo disponible en En desarrollo |
| En desarrollo | 3 | La tarjeta pasa desde Por hacer respetando el límite WIP. Se crea una rama dedicada para la funcionalidad (`feature/...`) | Código implementado, pruebas unitarias locales ejecutándose en verde y cumplimiento del estándar de codificación |
| En revisión / pruebas | 2 | Pull Request abierto hacia la rama de integración con el pipeline de CI en ejecución y pruebas automatizadas pasando | Aprobación formal obligatoria de revisión por pares (Peer Review) y suite de pruebas en verde en GitHub Actions[cite: 1] |
| Listo para desplegar | 2 | PR fusionado y artefacto desplegado en el ambiente previo (Staging) | Pruebas de humo (smoke tests) exitosas y ventana segura confirmada (despliegues únicamente de lunes a jueves) |
| Hecho | $\infty$ | Funcionalidad desplegada en producción que cumple el 100% de la Definition of Done (DoD) | Monitoreo en producción sin alertas durante las primeras 2 horas y cierre formal de la tarjeta/issue |
