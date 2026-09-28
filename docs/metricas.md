# Bloque 5: Reporte y Análisis de Métricas DORA

Este informe consolida las cuatro métricas DORA calculadas a partir del registro histórico de entregas (`datos/despliegues.csv`), el cual documenta 20 eventos de despliegue ocurridos durante el mes de septiembre de 2026.

---

## 1. Tabla Resumen de Métricas DORA

| Métrica DORA | Fórmula Aplicada | Resultado Obtenido | Nivel de Rendimiento DORA |
| :--- | :--- | :---: | :---: |
| Deployment Frequency (DF) | $\frac{\text{Total Despliegues}}{\text{Periodo en Semanas}}$ | 4.9 despliegues / semana (~0.67 al día) | Medio - Alto |
| Lead Time for Changes (LTTC) | $\text{Promedio}(\text{Fecha Despliegue} - \text{Fecha Commit})$ | 24.75 horas (~1.03 días) | Alto |
| Change Failure Rate (CFR) | $\left(\frac{\text{Despliegues Fallidos}}{\text{Total Despliegues}}\right) \times 100$ | 20.0% (4 de 20 fallaron) | Medio |
| Failed Deployment Recovery Time (MTTR) | $\frac{\text{Suma Horas de Recuperación}}{\text{Número de Fallas}}$ | 4.5 horas | Medio |

---

## 2. Desarrollo y Detalle de Cálculos

### 2.1. Deployment Frequency (Frecuencia de Despliegues)
* **Datos:** 20 despliegues en una ventana de 28.6 días (4.09 semanas).
* **Cálculo:** 
  $$\text{DF} = \frac{20 \text{ despliegues}}{4.09 \text{ semanas}} \approx 4.89 \text{ despliegues por semana}$$
* **Diagnóstico:** El equipo tiene un ritmo de entrega frecuente (varias veces por semana), lo que supera la cadencia quincenal tradicional del caso de estudio inicial.

### 2.2. Lead Time for Changes (Tiempo de Entrega del Cambio)
* **Datos:** Tiempo transcurrido entre el commit del desarrollador y la puesta en producción.
* **Cálculo:** 
  * Suma total de tiempos de ciclo: $495 \text{ horas}$.
  * Promedio: $\frac{495}{20} = 24.75 \text{ horas}$.
* **Diagnóstico:** Los cambios tardan en promedio 1 día en llegar a producción. Los picos más altos (48 a 52 horas) se presentaron en los despliegues de fin de semana (IDs 5, 10, 18, 19 y 20).

### 2.3. Change Failure Rate (Tasa de Fallos en Cambios)
* **Datos:** 4 despliegues no exitosos (IDs 3, 8, 13 y 17) de 20 totales.
* **Cálculo:** 
  $$\text{CFR} = \left(\frac{4}{20}\right) \times 100 = 20\%$$
* **Diagnóstico:** 1 de cada 5 despliegues termina en incidente en producción. Esto confirma la presencia de defectos escapados provocados por la ausencia previa de pruebas automáticas.

### 2.4. Failed Deployment Recovery Time / MTTR (Tiempo Medio de Reparación)
* **Datos:** Incidentes registrados con tiempos de 5h (ID 3), 3h (ID 8), 2h (ID 13) y 8h (ID 17).
* **Cálculo:** 
  $$\text{MTTR} = \frac{5 + 3 + 2 + 8}{4} = \frac{18}{4} = 4.5 \text{ horas}$$
* **Diagnóstico:** Ante una falla, el servicio tarda en promedio 4 horas y media en restablecerse. El peor incidente (ID 17, 8 horas) ocurrió durante el despliegue del viernes 25 de septiembre por la tarde, evidenciando el riesgo de realizar liberaciones al cierre de la semana laboral.

---

## 3. Plan de Mejora con Quality Gates y Kanban

1. **Reducción de CFR (Meta: < 5%):** Con la introducción del workflow de GitHub Actions (`ci.yml`) que exige el 80% de cobertura de pruebas unitarias y linters, los defectos que originaron los fallos en los despliegues 3, 8, 13 y 17 serán detectados en la fase de Pull Request antes de fusionar a `main`.
2. **Reducción del MTTR (Meta: < 1 hora):** La política de prohibir despliegues los viernes por la tarde y estandarizar despliegues de lunes a jueves evitará que incidentes críticos queden desatendidos durante los fines de semana.