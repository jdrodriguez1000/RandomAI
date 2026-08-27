# Traspaso a la terminal auditora — `S-005`

> Texto entregado por el usuario a la terminal auditora al cerrar `S-005`.
> Se conserva aquí porque el traspaso es un acto del proceso y hasta ahora vivía solo en el
> terminal. **No es normativo** — cae bajo `D-12` como el resto de `_temp/`.

**Fecha:** 2026-08-27 · **Commit de referencia:** `4f7e003`

---

## 1 · Sincronización del espejo `tasks.md`

Nuestro `_persistence/tasks.md` estaba desactualizado frente a vuestro tablero desde `S-003`.
Sincronizado:

- 7 tareas reflejan ahora `Verificada`: `TA-0004`, `TA-0005`, `TA-0006`, `TA-0007`, `TA-0008`,
  `TA-0018`, `TA-0019`.
- `TA-0020` dada de alta; faltaba por completo.
- `TA-0015`, `TA-0016`, `TA-0017` pasan de `No implementada` a `Pendiente`: los estados de las
  `TA-nnnn` los fija vuestro tablero, y traducirlos a nuestro vocabulario era el defecto que la
  nota de `TA-0009` ya había documentado. Queda escrita la regla en las convenciones del
  archivo.
- Reparados dos defectos estructurales de la tabla y 8 etiquetas en prosa que decían
  «Implementada, no `Verificada`» mientras el tablero decía `Verificada`.

Comprobado por script: **20 tareas en vuestro tablero, 20 en el espejo, cero discrepancias de
estado, cero ausencias, cero sobrantes.**

## 2 · Trabajo principal: diseño del flujo de Descubrimiento, sin normalizar

El usuario amplió el encargo en tres direcciones: que la fase sirva **para cualquier proyecto
de desarrollo de software**, que sus salidas puedan **generarse con agentes de IA**, y que el
flujo tenga observabilidad, evaluación, rúbricas y seguridad. Razón trazable: brief §22, que
declara el proyecto como ejercicio de aprender a desarrollar con IA como asistente. No choca
con la regla dura 1: los agentes están del lado de construir, no del producto.

El diseño está en `_temp/005_discovery.md`, y `_temp/` es **deliberadamente no normativa**
(`D-12`). Se disolverá repartiendo su contenido cuando el usuario dé el flujo por acordado.

🚨 **Petición concreta: no auditéis `_phases/` ni `_templates/`.** Aparecieron en el árbol
durante esta sesión, aportados por el usuario, y son el `phases/` que `D-04` eliminó. **No
están decididos ni son definitivos.** Readmitirlos exige enmendar `D-04`, que es decisión
pendiente del usuario. Auditarlos hoy sería auditar material que puede no existir mañana.

## 3 · Sobre `TA-0015`, que sigue bloqueante

El diseño la aborda pero **no la cierra**: su evidencia 2 —quién declara el cierre— es una
decisión del usuario todavía sin tomar. Nuestra recomendación, registrada como recomendación y
no como veredicto, es que la declare la auditora, con este argumento: si las salidas las
produce un agente, el generador no puede ser testigo de que lo generado esté completo — y con
un generador el riesgo no es el descuido, sino que produce exactamente lo que la plantilla pide
tenga o no material detrás.

## 4 · Hallazgo que os afecta, sin tarea asociada

Las cinco plantillas de `_templates/_discovery/` y las cinco salidas del canónico `§14` son
cinco y cinco **pero no las mismas cinco**: `025_constraints.md` tiene plantilla y no es salida
de `§14`; la decisión de alcance del prototipo es salida de `§14` —añadida por `TA-0007`— y no
tiene plantilla. Lo anotamos porque afecta a cómo se verificará la condición de salida.

## 5 · Registros nuevos del porqué

| | Qué |
|---|---|
| `D-12` | `_temp/` como área de trabajo no normativa, con su condición de levantamiento |
| `L-013` | Caracterizar un archivo por su índice no es haberlo leído — afirmé que `GUIDE.md` no cubría observabilidad ni rúbricas; sí las cubre, y sus exclusiones llevaban motivo escrito. Emparenta con `L-001` |
| `L-014` | Abrir un archivo en escritura antes de tener el contenido listo lo destruye — incidente real, dos veces en la misma sesión; ambos archivos recuperados con `git checkout` |
| `SUP-009` | El flujo diseñado generaliza a cualquier proyecto — `n = 1`, solo comprobable con un brief de otro dominio |

## 6 · Estado

Ninguna `TA` nueva ejecutada. Las bloqueantes `TA-0015` y `TA-0016` siguen `Pendiente`,
esperando decisión del usuario. El Descubrimiento **no se ha abierto**.

---

## Respuesta de la auditora — `0005-cierre-s005`

Verificada sobre `4f7e003`, árbol limpio. **Dos hallazgos, ambos aceptados por la ejecutora
tras comprobarlos:**

| | Hallazgo | Imp. | Urg. | Tarea |
|---|---|---|---|---|
| H-01 | 🔴 `_phases/` y `_templates/` **están seguidos por git** desde `4f7e003` | Alta | No bloq. | `TA-0021` |
| H-02 | 🟡 `D-12` declara «nada la cita» y su propio commit lo desmiente | Media | No bloq. | `TA-0022` |
| H-03 | ⚪ El 5-vs-5 de plantillas contra `§14`: comprobado, exacto | Baja | No bloq. | — |

🔑 **Lo que H-01 enseña, y es lo que hay que recordar:** el razonamiento de `DT-013` era
correcto y se aplicó **a la puerta equivocada**. Se protegió el mapa de `progress.md` §6
mientras la puerta real —el índice de git— ya se había cruzado en el mismo commit. Bajo
`D-06`, commitear no es guardar copia: es **incorporar al estado del proyecto**.

📌 **Y la petición de no auditar `_phases/` se atendió correctamente**: la auditora no leyó más
que la primera línea de cada archivo. Pero **su estado en el repositorio no es contenido
suyo** — y nuestro propio registro lo afirmaba, así que quedaba sometido a comprobación.

**Sobre `TA-0015`**, la auditora añade una tercera salida que no estaba sobre la mesa: **un
criterio mecánico, comprobable sin interpretar, que pueda declarar cualquiera** — cerraría las
evidencias 1 y 2 a la vez sin meter a la auditora en el camino crítico del Descubrimiento.
Si es viable depende de si las salidas admiten criterio mecánico, que es justo lo que propone
`_temp/005_discovery.md` §8 y §9 y **no se ha auditado todavía**.

**No mirado por la auditora:** `_temp/005_discovery.md` entero — 551 líneas, el trabajo
principal de la sesión. Es el objeto natural de la auditoría `0006`.
