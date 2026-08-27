# progress.md — Estado y avance del proyecto RandomAI

> Archivo general del proyecto. Responde en todo momento a tres preguntas:
> **dónde estamos**, **qué acabamos de hacer** y **qué sigue**.
> Es el primer archivo que se lee al retomar el proyecto.
>
> **Lo escribe `session-closer` al cerrar cada sesión**, desde la evidencia del repositorio.
> La sección `Dónde estamos` puede actualizarla la sesión principal durante el trabajo.

**Última actualización:** 2026-08-26 (S-003)

<!--INDEX-->

## Índice

> **Búsqueda rápida.** Salta con el enlace, o ve directo a la línea indicada (exacta, ya contando este índice).
> Por código: `grep -n 'Que sigue' progress.md`

| Línea | Sección | Ir a |
|---|---|---|
| `34` | **1. Dónde estamos** | [↓](#1-dónde-estamos) |
| `52` | **2. Por qué no hemos empezado a construir** | [↓](#2-por-qué-no-hemos-empezado-a-construir) |
| `64` | **3. Sesiones** | [↓](#3-sesiones) |
| `74` | &nbsp;&nbsp;↳ Tablero de sesiones | [↓](#tablero-de-sesiones) |
| `82` | &nbsp;&nbsp;↳ Detalle de sesiones | [↓](#detalle-de-sesiones) |
| `174` | **4. Qué sigue** | [↓](#4-qué-sigue) |
| `190` | **5. Lo que bloqueará el arranque real del Descubrimiento** | [↓](#5-lo-que-bloqueará-el-arranque-real-del-descubrimiento) |
| `206` | **6. Mapa de archivos de persistencia** | [↓](#6-mapa-de-archivos-de-persistencia) |

<!--/INDEX-->

---

## 1. Dónde estamos

| | |
|---|---|
| **Fase del método** | *Ninguna todavía* — pre-Descubrimiento |
| **Etapa real** | Corrección del método antes de aplicarlo |
| **Producto** | Sin construir. Cero líneas de código de aplicación |
| **Bloqueo activo** | 2 tareas bloqueantes de auditoría abiertas: `TA-0002`, `TA-0007`. `TA-0001` está `Verificada` por la auditora (`tasks_audit.md:59`) |

**Situación en una frase:** `TA-0001` está resuelta en el canónico —§10 y Anexo A.1 corregidos,
más la justificación de por qué `A.1` sigue como ADR pendiente (`D-10`)— y ya `Verificada` por
la auditora; `TA-0002`+`TA-0003` (alcance ampliado por `D-03`) es el siguiente
paso bloqueante y **no se empezó a petición expresa del usuario**. Sigue pendiente el traslado
a la auditora del desfase de estado en `TA-0009` (`Cancelada` aquí, `Pendiente` en su tablero;
no podemos escribirlo nosotros, `RES-009`).

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

## 4. Qué sigue

**Inmediato — Paso 1, tareas bloqueantes de la auditoría:**

1. `TA-0001` — **`Verificada`** por la auditora (2026-08-26)
2. `TA-0002` + `TA-0003` — crear `§17-bis`, incorporar `015` §36–§48, fusionar §50 en §4
3. `TA-0007` — decisión de alcance del prototipo, en el canónico §14 (un solo frente tras `D-04`)

**Después — Paso 2, no bloqueantes:** `TA-0004`, `TA-0005`, `TA-0006`, `TA-0008`.

**Después — Paso 3:** devolver a la auditora para verificación.

**Solo entonces:** abrir la fase `005_discovery` del producto RandomAI.

---

## 5. Lo que bloqueará el arranque real del Descubrimiento

**`DT-008` — el método se quedó sin nivel operativo.** Al eliminar `phases/` (`D-04`),
`000_method.md` conserva el **qué** de cada fase y el proyecto pierde el **cómo**:
procedimiento, qué está prohibido en cada fase, checklist de condición de salida y qué se
entrega a cada Gate.

No bloquea las tareas de auditoría en curso. **Sí bloquea abrir el Descubrimiento**, porque el
Gate 1 se declararía sin criterio operativo escrito. Requiere decisión del usuario entre las
tres opciones de [`debt_tec.md`](debt_tec.md) → `DT-008`, registrada como `T-013`.

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
