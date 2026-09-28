# Cinco reglas de codificación del equipo (XP)

Para garantizar un código limpio, mantenible y libre de defectos en la app de citas médicas, se establecen las siguientes 5 reglas de obligatorio cumplimiento:

1. **Adherencia estricta a PEP 8:**
   * Indentación obligatoria de 4 espacios (sin tabuladores).
   * Variables y funciones en `snake_case`, constantes en `UPPER_CASE` y clases en `PascalCase`.
   * Longitud máxima de línea fijada en 100 caracteres (validada por Flake8).

2. **Tipado Estático Obligatorio (Type Hints):**
   * Toda función o método debe declarar explícitamente el tipo de datos de sus parámetros de entrada y su valor de retorno (ej. `def agendar(...) -> CitaMedica:`).

3. **Documentación descriptiva con Docstrings:**
   * Todas las funciones públicas y clases deben incluir un docstring que explique su propósito de negocio, los argumentos esperados y las excepciones que puede lanzar.

4. **Manejo defensivo y excepciones específicas:**
   * Queda prohibido el uso de bloques genéricos `except: pass` o `except Exception:`.
   * Se deben validar precondiciones en capas tempranas lanzando excepciones semánticas (como `ValueError` ante fechas pasadas o solapamientos).

5. **Límites de Complejidad y Modularidad:**
   * Ninguna función debe exceder los 25 renglones de lógica efectiva ni anidar más de 3 niveles de condicionales o bucles (`complexity limit`). Si supera este umbral, debe refactorizarse en funciones auxiliares.
