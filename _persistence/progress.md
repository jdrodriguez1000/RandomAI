# progress.md — Estado y avance del proyecto RandomAI

> Archivo general del proyecto. Responde en todo momento a tres preguntas:
> **dónde estamos**, **qué acabamos de hacer** y **qué sigue**.
> Es el primer archivo que se lee al retomar el proyecto.
>
> **Lo escribe `session-closer` al cerrar cada sesión**, desde la evidencia del repositorio.
> La sección `Dónde estamos` puede actualizarla la sesión principal durante el trabajo.

**Última actualización:** 2026-08-27 (S-005)

<!--INDEX-->

## Índice

> **Búsqueda rápida.** Salta con el enlace, o ve directo a la línea indicada (exacta, ya contando este índice).
> Por código: `grep -n 'Que sigue' progress.md`

| Línea | Sección | Ir a |
|---|---|---|
| `34` | **1. Dónde estamos** | [↓](#1-dónde-estamos) |
| `57` | **2. Por qué no hemos empezado a construir** | [↓](#2-por-qué-no-hemos-empezado-a-construir) |
| `69` | **3. Sesiones** | [↓](#3-sesiones) |
| `79` | &nbsp;&nbsp;↳ Tablero de sesiones | [↓](#tablero-de-sesiones) |
| `89` | &nbsp;&nbsp;↳ Detalle de sesiones | [↓](#detalle-de-sesiones) |
| `260` | **4. Qué sigue** | [↓](#4-qué-sigue) |
| `287` | **5. Lo que bloqueará el arranque real del Descubrimiento** | [↓](#5-lo-que-bloqueará-el-arranque-real-del-descubrimiento) |
| `303` | **6. Mapa de archivos de persistencia** | [↓](#6-mapa-de-archivos-de-persistencia) |

<!--/INDEX-->

---

## 1. Dónde estamos

| | |
|---|---|
| **Fase del método** | *Ninguna todavía* — pre-Descubrimiento |
| **Etapa real** | Diseño (no normativo) del flujo de Descubrimiento, en paralelo a la auditoría |
| **Producto** | Sin construir. Cero líneas de código de aplicación |
| **Bloqueo activo** | Espejo de tareas ya sincronizado con la auditora (7 `TA` a `Verificada`, `TA-0020` de alta). Quedan **dos decisiones del usuario** bloqueando el paso siguiente: (1) quién declara el cierre del Descubrimiento — `TA-0015` —, y (2) si se enmienda `D-04` para readmitir `_phases/` y `_templates/` — `T-013` |

**Situación en una frase:** el espejo `tasks.md` quedó sincronizado con el tablero de la
auditora (20 tareas de cada lado, cero discrepancias, comprobado por script): `TA-0004`,
`TA-0005`, `TA-0006`, `TA-0007`, `TA-0008`, `TA-0018`, `TA-0019` pasan a `Verificada`, se da de
alta `TA-0020` y `TA-0015`–`TA-0017` pasan a `Pendiente`. En paralelo, se diseñó en
conversación —sin normalizar— el flujo completo del Descubrimiento (`_temp/005_discovery.md`,
`D-12`): bucle de extracción por agente ×4, bloque de criterio humano, cierre por la auditora,
trazabilidad al origen y la capa de observabilidad/evaluación/rúbricas del extractor.
Aparecieron sin seguimiento en git dos directorios que aportó el usuario —`_phases/` y
`_templates/`— que resultaron ser el `phases/` que `D-04` eliminó; **no están decididos**:
readmitirlos exige enmendar `D-04`. Sigue pendiente el traslado a la auditora del desfase de
`TA-0009` (`RES-009`).

---

## 2. Por qué no hemos empezado a construir

No es demora: es el propio método. `000_method.md` §2 —«no se construye aquello que todavía
no se entiende suficientemente bien»— y la auditoría `0001-method` H-02 demostró que el
canónico **invierte una regla de la fuente**: enuncia «solo Generador» como regla absoluta
cuando `015` §46 la define como regla con seis excepciones tasadas.

Arrancar el Descubrimiento con esa regla invertida haría que la fase 005 saliera mal
formada. Por eso se corrige primero el método.

---

## 3. Sesiones

> 🚨 **Una sesión es un bloque de tiempo, no un día** (`D-08`). Puede haber varias sesiones
> el mismo día, así que **la última es la del `S-nnn` más alto, nunca la de la fecha más
> reciente.** Ordenar por fecha mezcla sesiones y presenta como última una que no lo es.

**Convenciones.** Código `S-nnn`, correlativo, nunca se reutiliza. Cada sesión tiene **una
fila en el tablero y una entrada en el detalle**, y las dos se escriben juntas. La escribe
`session-closer` al cerrar, desde la evidencia.

### Tablero de sesiones

| Código | Fecha | Qué se hizo |
|---|---|---|
| `S-001` | 2026-08-26 | Primera sesión: brief + método leídos, auditoría `0001-method` verificada, `_persistence/` creada, `phases/` eliminado, git inicializado, skills y agentes adaptados |
| `S-002` | 2026-08-26 | Capa del «cómo»: `_guide/GUIDE.md` creado, reglas duras 8-9 en `CLAUDE.md`, corrección de `tools/mkindex.py` |
| `S-003` | 2026-08-26 | `TA-0001` ejecutada: corregida la atribución de fuentes sobre el Actor Invitado en `000_method.md` (§10 y Anexo A.1), con justificación añadida sobre por qué `A.1` sigue como ADR pendiente (`D-10`) |
| `S-004` | 2026-08-27 | Paso 1 de la auditoría cerrado: `TA-0002`, `TA-0003`, `TA-0007` implementadas. Ejecutadas además `TA-0004`–`TA-0006`, `TA-0008`, `TA-0010`–`TA-0013`, `TA-0018`, `TA-0019`. `TA-0014` descartada por la auditora. `DT-008` corregida (no saldada). Emiten `TA-0015`, `TA-0016` (bloqueantes) y `TA-0017` |
| `S-005` | 2026-08-27 | Espejo `tasks.md` sincronizado con el tablero de la auditora (7 `TA` a `Verificada`, alta de `TA-0020`, `TA-0015`–`17` a `Pendiente`). Diseñado en `_temp/005_discovery.md` (no normativo) el flujo completo del Descubrimiento (`D-12`). Aparecieron sin seguimiento `_phases/` y `_templates/`, el `phases/` de `D-04`, sin decidir su readmisión |

### Detalle de sesiones

#### `S-001` — 2026-08-26

**Fase del método:** ninguna todavía — pre-Descubrimiento. El proyecto está corrigiendo el
método antes de aplicarlo (ver sección 2).

**Qué quedó hecho.** Primer commit del repositorio (no existía historia previa):

- `_brief/` y `_methodology/` (con `sources/`) creados y leídos.
- La auditoría `0001-method` de la terminal auditora, analizada, con sus 6 hallazgos
  verificados de forma independiente.
- Tres decisiones previas del usuario (`D-01`, `D-02`, `D-03`) que condicionan la ejecución de
  las tareas de auditoría.
- `_persistence/` creada con sus 7 archivos, más el índice de búsqueda rápida con números de
  línea en los 7.
- `phases/` eliminado (`D-04`); carpetas de insumo renombradas a `_brief/` y `_methodology/`
  (`D-05`); registros ajustados en consecuencia.
- `CLAUDE.md` creado en la raíz.
- Git inicializado y remoto de GitHub enlazado (`D-06`).
- Skills `protocol-close` y `protocol-start`, y agentes `session-closer` y `session-starter`,
  adaptados a este proyecto (venían escritos contra otro).
- Definición de que una sesión es un bloque de tiempo, no un día (`D-08`).
- `progress.md` reestructurado con entradas de sesión `S-nnn` (`T-018`).

**Siguiente paso concreto.** Empezar el Paso 1 de la auditoría: `TA-0001` — corregir la
atribución de fuentes sobre «Actor Invitado» en `000_method.md` §10 y Anexo A.1.

---

#### `S-002` — 2026-08-26

**Fase del método:** ninguna todavía — pre-Descubrimiento. Sigue sin abrirse. Lo de hoy fue
infraestructura de proceso, no producto ni método.

**Qué quedó hecho** (según el diff):

- `_guide/GUIDE.md` creado (569 líneas): la capa del «cómo se ejecuta el trabajo con IA como
  asistente», trazable al brief §22. Traducida y recortada de la guía de un proyecto anterior
  fuera de este repo, con sus exclusiones declaradas en la propia sección 0 del archivo
  (`D-09`).
- `CLAUDE.md`: reglas duras 8 y 9 añadidas (ante prueba roja se arregla el código; el refactor
  se pide explícitamente al usuario), más una fila nueva en «Dónde está lo demás» apuntando a
  `_guide/`.
- `tools/mkindex.py` corregido: `headings()` ahora salta los bloques de código cercados, para
  no indexar encabezados de ejemplo como si fueran secciones reales (segunda aparición de
  `L-005`).
- `_persistence/decisions.md` — `D-09` añadida (ya escrita por la sesión principal).
- `_persistence/lessons.md` — segunda aparición de `L-005` registrada (ya escrita por la
  sesión principal).
- `_persistence/tasks.md` — `T-023` `Implementada`, `T-024` `Suspendida` (sin stack decidido),
  `T-025` `No implementada` (ya escrito por la sesión principal).

**Siguiente paso concreto.** `TA-0001` — corregir la atribución de fuentes sobre «Actor
Invitado» en `_methodology/000_method.md` §10 y Anexo A.1. Sigue siendo el primer paso
bloqueante; nada de hoy lo adelantó.

---

#### `S-003` — 2026-08-26

**Fase del método:** ninguna todavía — pre-Descubrimiento. Sigue sin abrirse.

**Qué quedó hecho** (según el diff):

- `_methodology/000_method.md` corregido para `TA-0001` (H-01): en §10 se retira la marca `➕`
  y la frase «005 y 015 lo incluían», y la cita queda `↳ *010 §12 · 015 §5*`. En el Anexo A.1 la
  columna «Fuentes en conflicto» se reescribe: solo `005 §5.6` incluye al Actor Invitado;
  `010 §12` y `015 §5` lo excluyen. Se añade al cierre del Anexo A un párrafo que justifica por
  qué `A.1` sigue en la lista de ADR pendientes pese a que el conflicto de fuentes ya no existe
  (consecuencia sobre el modelo de autorización, no taxonomía).
- `_persistence/decisions.md` — `D-10` añadida (ya escrita por la sesión principal): por qué
  `A.1` se queda en la lista de ADR pendientes.
- `_persistence/lessons.md` — `L-008` (un dato repetido en dos capas diverge, y miente la que
  menos se lee) y `L-009` (escribir en el sitio destruye el original antes de saber si va a
  funcionar) añadidas, ya escritas por la sesión principal.
- `_persistence/debt_tec.md` — `DT-004` actualizada (A.1 resuelta por `D-10`, sigue pendiente
  el ADR), `DT-011` (cita de A.3 sin verificar del todo) y `DT-012` (`tools/mkindex.py` no
  escribe de forma atómica) añadidas, ya escritas por la sesión principal.

**No se tocó hoy:** `TA-0002`+`TA-0003` (incorporar `015` §36–§48 con el alcance ampliado de
`D-03`) — el usuario pidió expresamente no trabajar en ella esta sesión.

**Desfase sin resolver:** `TA-0009` figura `Cancelada` en `tasks.md` pero `Pendiente` en el
tablero de la auditora. No se puede escribir en `RandomAi_Auditor/` (`RES-009`); el traslado lo
hace el usuario.

**Siguiente paso concreto.** `TA-0002` + `TA-0003` — incorporar `015` §36–§48 en el canónico
con el alcance ampliado de `D-03` (crear `§17-bis`, fusionar §50 en §4).

---

#### `S-004` — 2026-08-27

**Fase del método:** ninguna todavía — pre-Descubrimiento. Sigue sin abrirse.

**Qué quedó hecho** (según el diff, commits `5244145`…`9fc105c`):

- `_methodology/000_method.md` (1012 → ~1258 líneas): `TA-0002` incorpora `015` §36–§48 con el
  alcance ampliado de `D-03` — `§17-bis` nuevo (los seis criterios de `015` §46), `§29.1`,
  `§30`, `§37.1`, `§41.1`, `§50.1`, y `§4` ampliado de 3 a 6 preguntas. `TA-0003` cierra el
  Anexo A con las entradas `A.9` y `A.10` (omisiones deliberadas de `015` §35, §49, §51).
  `TA-0007` añade la quinta salida del Descubrimiento (decisión de alcance del prototipo, §14
  y §14.1). `TA-0004` (Anexo A.8, resuelve conflicto GRTH/EVOL entre `005` y `015`), `TA-0005`
  (celda «Cuándo» de §57), `TA-0006` (§32 reescrito agnóstico a infraestructura), `TA-0008`
  (Anexo A.12, «Product Baseline»), `TA-0010` (seis frases propias remarcadas), `TA-0011`
  (Anexo A.9 con la convención `bis`), `TA-0012` (enmienda a `D-03`), `TA-0013` (cuatro marcas
  `↳` dobles fusionadas), y la remisión de la última `+` del cuerpo a `A.6`.
- `TA-0014` — disputada por la ejecutora con evidencia (L-011) y **descartada por la
  auditora**.
- `TA-0018` y `TA-0019` cerradas: `debt_tec.md` pierde el campo `Estado` duplicado en las
  entradas de detalle (queda solo en el tablero); revisadas `A.8`–`A.12`, ninguna requiere ADR,
  con el criterio que lo decide escrito en el canónico.
- `DT-008` **corregida, no saldada**: cinco de sus ocho puntos ya estaban cubiertos y su
  premisa sobre el Gate 1 era falsa (§29–§32, §19–§27 dan más nivel operativo del que
  `phases/` daba). El hueco real es de tres puntos —entradas exigidas, condición de salida,
  entrega al Gate—, no de ocho. Emitida `TA-0015` (condición de salida del Descubrimiento,
  bloqueante) y `TA-0016` (Gate 1 sin umbral, bloqueante); `TA-0017` (frenos de agentes solo en
  prosa, no bloqueante).
- `_persistence/decisions.md` — `D-11` (por qué `TA-0018` se salda retirando el campo, no
  sincronizándolo) y la autorización del usuario a la enmienda de `D-03` (`TA-0012`), ya
  escritas por la sesión principal.
- `_persistence/lessons.md` — `L-010`, `L-011`, `L-012`, ya escritas por la sesión principal.
- `CLAUDE.md` — afinado el puntero de la asignación de Gates para citar el §32 reescrito.

**Siguiente paso concreto.** Decisión del usuario sobre `TA-0015` y `TA-0016` (bloqueantes
para abrir el Descubrimiento) y sobre las tres opciones de `DT-008` (`T-013`).

---

#### `S-005` — 2026-08-27

**Fase del método:** ninguna todavía — pre-Descubrimiento. Sigue sin abrirse; lo de hoy es
diseño previo, explícitamente no normativo.

**Qué quedó hecho** (según el diff):

- **Sincronización del espejo `_persistence/tasks.md`** contra
  `../RandomAi_Auditor/audits/tasks_audit.md`: `TA-0004`, `TA-0005`, `TA-0006`, `TA-0007`,
  `TA-0008`, `TA-0018`, `TA-0019` pasan a `Verificada`; alta de `TA-0020` (`Pendiente`);
  `TA-0015`–`TA-0017` pasan de `No implementada` a `Pendiente` (vocabulario del tablero de la
  auditora, no del propio). Reparados dos defectos estructurales de la tabla y ocho etiquetas
  en prosa que seguían diciendo «Implementada, no `Verificada`» sobre tareas ya verificadas.
  Añadida una nota de convención: el vocabulario de las `TA` es el de la auditora, este
  archivo es espejo.
- **`_temp/005_discovery.md` (nuevo, 551 líneas, sin seguimiento previo en git)**: diseño
  completo del flujo de Descubrimiento — los cuatro «quienes», entradas y salidas, bucle de
  extracción por agente (×4), bloque de criterio humano, cierre por la auditora, trazabilidad
  al origen con tres valores, y la capa de observabilidad/evaluación/rúbrica del extractor.
  Marcado explícitamente como archivo de trabajo, no normativo (`D-12`).
- **Aparecieron sin seguimiento en git dos directorios que aportó el usuario**: `_phases/`
  (con `005_discovery.md`, 210 líneas) y `_templates/_discovery/` (5 archivos). Son el
  `phases/` que `D-04` eliminó — el propio `_temp/005_discovery.md` §10 lo constata: citan
  `_memory/` y `tech-debt.md`, que reviven literalmente `DT-003` si se readmiten así. **No
  están decididos.**
- `_persistence/decisions.md` — `D-12` (por qué el diseño vive en `_temp/`, no normativo,
  antes de repartirlo), ya escrita por la sesión principal.
- `_persistence/assumptions.md` — `SUP-009` (el flujo de Descubrimiento generaliza a
  cualquier proyecto, no solo RandomAI), ya escrita por la sesión principal.
- `_persistence/lessons.md` — `L-013` (caracterizar un archivo por su índice no es haberlo
  leído) y `L-014` (abrir un archivo en escritura antes de tener el contenido listo lo
  destruye; incidente real, dos archivos truncados y recuperados con `git checkout --`), ya
  escritas por la sesión principal.

**Siguiente paso concreto.** Seguir trabajando en la definición de la fase de Descubrimiento
según el orden de `_temp/005_discovery.md` §12, empezando por las dos decisiones del usuario
que lo bloquean: quién declara el cierre del Descubrimiento (`TA-0015`) y si se enmienda
`D-04` para readmitir `_phases/` y `_templates/` (`T-013`).

---

## 4. Qué sigue

**Paso 1 de la auditoría — cerrado:** `TA-0001`, `TA-0002`, `TA-0003`, `TA-0007` `Verificada`.

**Paso 2, no bloqueantes — cerrado:** `TA-0004`–`TA-0006`, `TA-0008`, `TA-0010`–`TA-0013`,
`TA-0018`, `TA-0019` `Verificada`. `TA-0014` `Descartada` por la auditora.

**Pendiente, bloqueante para el Descubrimiento — dos decisiones del usuario, según el orden
de `_temp/005_discovery.md` §12:**

1. **Quién declara el cierre del Descubrimiento** (`TA-0015`; recomendación del documento de
   trabajo: la auditora, por §6 del canónico).
2. **Si se enmienda `D-04`** para readmitir `_phases/` y `_templates/` (`T-013`) — sin esto no
   se puede avanzar en el reparto del diseño hacia sus archivos definitivos.

`TA-0016` (umbral del Gate 1) queda como bloqueante aparte, más adelante en el orden.
`TA-0017` y `TA-0020` (no bloqueantes) siguen `Pendiente`.

**Después de esas dos decisiones:** repartir `_temp/005_discovery.md` según su §11 —
`GUIDE.md` (§9 + tres exclusiones de §0 caducadas), `_phases/005_discovery.md`,
`_templates/_discovery/`—, resolver `TA-0016`, y solo entonces correr el flujo completo sobre
el brief de RandomAI como primer caso de referencia.

**Solo entonces:** abrir la fase `005_discovery` del producto RandomAI.

---

## 5. Lo que bloqueará el arranque real del Descubrimiento

**`DT-008` — corregida en `S-004`, no saldada.** El hueco medido ya no son ocho puntos: son
tres — **entradas exigidas**, **condición de salida** y **entrega al Gate** —, que es lo que
emite `TA-0015` y `TA-0016`. Su premisa original (el Gate 1 se declararía sin criterio
operativo) quedó comprobada como falsa: §29, §29.1, §30, §31, §32 y §19–§27 dan a esa fase más
nivel operativo del que `phases/` daba.

Requiere decisión del usuario entre las tres opciones de [`debt_tec.md`](debt_tec.md) →
`DT-008`, registrada como `T-013`, ya redimensionadas contra el hueco real.

**Lo que dejó de bloquear:** `DT-002`, `DT-003` y `DT-006` quedaron `Descartada` — existían
solo por `phases/`.

---

## 6. Mapa de archivos de persistencia

**Estructura del repo tras `D-04` y `D-05`:**

```text
RandomAI/
├── .claude/         agente y skill de cierre
├── .gitignore
├── CLAUDE.md        cómo se trabaja aquí
├── tools/           mkindex.py — mantiene los índices
├── _brief/          el encargo del cliente
├── _methodology/    000_method.md + sources/
└── _persistence/    los 7 registros
```

Los 7 archivos abren con un **`## Índice`** de búsqueda rápida: línea exacta de cada
sección y enlace de salto, para no tener que leer el archivo entero.

| Archivo | Qué contiene |
|---|---|
| [`progress.md`](progress.md) | este archivo — estado general |
| [`tasks.md`](tasks.md) | tareas con código y estado |
| [`decisions.md`](decisions.md) | decisiones tomadas — **fuente única, no hay otra** |
| [`assumptions.md`](assumptions.md) | supuestos por validar |
| [`constraints.md`](constraints.md) | límites y restricciones |
| [`lessons.md`](lessons.md) | lecciones aprendidas |
| [`debt_tec.md`](debt_tec.md) | deuda técnica con estado |
