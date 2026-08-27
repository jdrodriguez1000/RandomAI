# Necesidades — <NOMBRE DEL PROYECTO>

| | |
|---|---|
| **Artefacto** | `_discovery/005_needs.md` |
| **Fase que lo produce** | `005_discovery` |
| **Estado** | `BORRADOR` |
| **Abierto** | `<AAAA-MM-DD>` |
| **Cerrado** | `<AAAA-MM-DD, o — mientras siga en BORRADOR>` |
| **Escrito por** | terminal **ejecutora** |

> **Estado:** `BORRADOR` mientras la fase siga abierta · `CERRADO` cuando se cumpla la
> condición de salida de `005_discovery` §6.
>
> ⚠️ **Las fechas de arriba las lee la auditora y las cruza contra el historial de Git.**
> No se rellenan a posteriori: una fecha declarada que no cuadra con la del commit
> manda el Gate a `NO AUDITABLE`.

---

## 1. Las nueve preguntas

No se avanza hasta que las nueve tengan respuesta **o un «no se sabe» escrito**.

📌 Un **«no se sabe»** vale más que una respuesta inventada: se convierte en un
`SUP-xxx` en `025_constraints.md` y alguien tendrá que ir a verificarlo. Escríbelo así:
`No se sabe → SUP-003`.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Por qué existe la necesidad? | `<…>` |
| 2 | ¿Para qué se necesita la aplicación? | `<…>` |
| 3 | ¿Qué problema se quiere resolver? | `<…>` |
| 4 | ¿Quién tiene el problema? | `<…>` |
| 5 | ¿Quién usará la solución? | `<resumen en una línea → el detalle va en 010_actors.md>` |
| 6 | ¿Qué resultado espera obtener la empresa? | `<…>` |
| 7 | ¿Qué procesos existen actualmente? | `<…>` |
| 8 | ¿Qué restricciones existen? | `<resumen en una línea → el detalle va en 025_constraints.md>` |
| 9 | ¿Qué sistemas actuales participan? | `<…>` |

---

## 2. Necesidades registradas

Una ficha por necesidad. Se numeran `N-001`, `N-002`, … y **no se reutiliza un número**
aunque la necesidad se descarte después.

🚨 **Una necesidad solo se registra si se puede enunciar sin nombrar una pantalla.**
Si en el enunciado aparece «pantalla», «botón», «formulario», «dashboard», «app» o
«menú», todavía es una solución disfrazada. Vuelve a preguntar *«¿cómo haces esto hoy?»*.

### N-001 · `<título corto, 5 palabras máximo>`

| Campo | Contenido |
|---|---|
| **Enunciado** | `<la necesidad, sin nombrar ninguna pantalla>` |
| **Quién la tiene** | `<persona o rol concreto — no «la empresa», no «los usuarios»>` |
| **Cómo se hace hoy** | `<el proceso real de hoy, sin la aplicación>` |
| **Qué cuesta hoy** | `<tiempo, dinero, errores o trabajo perdido — con número si lo hay>` |
| **De dónde salió** | `<entrevista con X · observación del proceso · documento Y>` |
| **Fecha** | `<AAAA-MM-DD en que se recogió>` |
| **Petición original** | `<lo que el cliente pidió literalmente, antes de desvestirla>` |
| **Estado** | `REGISTRADA` |

**Relacionada con:** `<actores de 010_actors.md · RES-xxx / SUP-xxx de 025_constraints.md · —>`

<!-- Copia el bloque completo para N-002, N-003, … -->

---

## 3. Peticiones que NO eran necesidades

Aquí queda el rastro del trabajo de desvestir. **No se borra**: si dentro de tres meses
alguien vuelve a pedir lo mismo, esta tabla dice qué se preguntó y qué se encontró.

| Lo que se pidió | Qué se preguntó | Qué resultó ser | Resultado |
|---|---|---|---|
| `<«necesito un dashboard»>` | `<¿qué decisión tomarías con ese dato?>` | `<nadie sabe cuántas recogidas se cumplieron>` | `<→ N-002>` |
| `<…>` | `<…>` | `<…>` | `<descartada: no hay decisión detrás>` |

---

## 4. Comprobación antes de cerrar este archivo

Esto **no** es la condición de salida de la fase — esa está en `005_discovery.md` §6 y
abarca los cinco artefactos. Esto es solo lo que le toca a este archivo.

- [ ] Las nueve preguntas tienen respuesta o un «no se sabe» **con su `SUP-xxx`**.
- [ ] Hay **al menos una** `N-xxx` registrada.
- [ ] **Ninguna** `N-xxx` nombra una pantalla, un botón ni un formulario.
- [ ] Cada `N-xxx` dice **quién la tiene**, con nombre de rol o de persona.
- [ ] Cada `N-xxx` dice **cómo se hace hoy**.
- [ ] Las peticiones descartadas están en §3, no borradas.
- [ ] **No queda ni un solo `<` en el archivo** — ningún hueco sin rellenar.
- [ ] La sección «Guía de llenado» de abajo **está borrada**.
- [ ] La cabecera dice `CERRADO` y tiene fecha de cierre.

Las dos últimas y la del `<` se comprueban desde fuera, sin leer el archivo entero:

```bash
grep -n "<" _discovery/005_needs.md          # debe no devolver nada
grep -n "Guía de llenado" _discovery/005_needs.md   # debe no devolver nada
```

---
---

## Guía de llenado — ⚠️ BORRAR esta sección al cerrar el artefacto

> Existe para escribir el archivo. **No sobrevive al cierre de la fase.** Si se queda,
> el que lea mañana no puede distinguir lo que decidió el proyecto de lo que traía la
> plantilla — y lo tratará como decisión.

### La pregunta que hace todo el trabajo

> **¿Cómo haces esto hoy?**

Se repite en toda la fase. Lo primero que dice el cliente es casi siempre una solución,
no una necesidad.

| Lo que dijo | La necesidad detrás | La pregunta que la destapa |
|---|---|---|
| «Necesito una app para pedir recogidas» | los clientes no tienen forma de pedir una recogida sin llamar por teléfono | *¿qué pasa hoy cuando alguien quiere una recogida?* |
| «Necesito un dashboard» | nadie sabe cuántas recogidas se cumplieron | *¿qué decisión tomarías con ese dato?* |

### Ejemplo de una ficha completa

### N-001 · Pedir recogida sin llamar

| Campo | Contenido |
|---|---|
| **Enunciado** | Un cliente no tiene forma de solicitar una recogida sin llamar por teléfono en horario de oficina. |
| **Quién la tiene** | El cliente que genera el residuo — contacto operativo de la empresa recolectada. |
| **Cómo se hace hoy** | Llama al fijo. Si no contestan, vuelve a llamar. La analista lo anota en una hoja de cálculo. |
| **Qué cuesta hoy** | ~40 llamadas al mes; 6 quedaron sin registrar en julio. |
| **De dónde salió** | Entrevista con la analista de logística + revisión de la hoja de cálculo de julio. |
| **Fecha** | 2026-07-14 |
| **Petición original** | «Necesito una app para pedir recogidas.» |
| **Estado** | `REGISTRADA` |

**Relacionada con:** Actor Generador (`010_actors.md`) · `RES-002` (solo horario hábil)

### Errores que esta plantilla existe para evitar

| Error | Cómo se ve | Qué hacer |
|---|---|---|
| Necesidad que es una solución | «que haya un botón para agendar» | preguntar *«¿cómo lo haces hoy?»* hasta que desaparezca el botón |
| Dueño en plural | «lo tienen los usuarios» | un rol o una persona; si son varios, son varias `N-xxx` |
| Supuesto disfrazado de hecho | «los clientes tienen celular» | pasarlo a `SUP-xxx` en `025_constraints.md` |
| Rellenar el «Qué cuesta hoy» con adjetivos | «es muy ineficiente» | un número, o «no se sabe → SUP-xxx» |
| Descartar una petición sin dejar rastro | §3 vacía y §2 con menos fichas | toda petición desvestida deja fila en §3 |

### Lo que esta fase tiene PROHIBIDO, y aquí se cuela solo

Diseñar pantallas · elegir tecnología · escribir código · escribir PRD/SPEC/ARCHIT ·
prometer alcance o fechas. Si al llenar este archivo aparece un nombre de librería o un
plazo, va fuera: no hay evidencia todavía para prometer nada.

📌 Definiciones: `methodology/000_method.md` §13–§14 y §46.
📌 Procedimiento: `phases/005_discovery.md` §4, pasos 1, 2 y 6.
