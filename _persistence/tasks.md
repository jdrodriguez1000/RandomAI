# tasks.md — Tareas del proyecto RandomAI

> Registro de tareas realizadas y por realizar. Toda tarea tiene **código** y **estado**.
> Cumple la regla de trazabilidad del método (`000_method.md` §47): *nada se construye sin
> una razón trazable*. Ninguna tarea existe sin origen.

**Última actualización:** 2026-08-26 (S-003)

<!--INDEX-->

## Índice

> **Búsqueda rápida.** Salta con el enlace, o ve directo a la línea indicada (exacta, ya contando este índice).
> Por código: `grep -n 'TA-0002' tasks.md`

| Línea | Sección | Ir a |
|---|---|---|
| `30` | **Convenciones** | [↓](#convenciones) |
| `32` | &nbsp;&nbsp;↳ Códigos | [↓](#códigos) |
| `42` | &nbsp;&nbsp;↳ Estados | [↓](#estados) |
| `59` | **Tablero — Tareas de auditoría (TA)** | [↓](#tablero--tareas-de-auditoría-ta) |
| `216` | &nbsp;&nbsp;↳ Notas de alcance | [↓](#notas-de-alcance) |
| `231` | **Tablero — Tareas propias (T)** | [↓](#tablero--tareas-propias-t) |
| `280` | **Orden de trabajo** | [↓](#orden-de-trabajo) |

<!--/INDEX-->

---

## Convenciones

### Códigos

| Prefijo | Familia | Quién la emite |
|---|---|---|
| `TA-NNNN` | Tarea de auditoría — **espejo** del tablero de la auditora | terminal auditora |
| `T-NNN` | Tarea propia de la ejecutora | terminal ejecutora / usuario |

Los códigos son correlativos dentro de su familia, **nunca se reutilizan ni se renumeran**.
Cuando exista construcción, las `T-NNN` deberán ser trazables a una Vertical Slice `VS-NNN`.

### Estados

| Estado | Significado |
|---|---|
| `No implementada` | registrada, sin empezar |
| `En curso` | se está trabajando en ella |
| `Implementada` | terminada por la ejecutora |
| `Cancelada` | no se hará. **Requiere razón registrada** |
| `Suspendida` | se detuvo temporalmente. **Requiere razón y condición de reanudación** |

> ⚠️ **Para las `TA-NNNN`, `Implementada` no es el cierre.** El único estado de cierre es
> `Verificada`, y **solo lo asigna la auditora** tras comprobar la evidencia con sus propios
> ojos (`tasks_audit.md`, regla de verificación). Que aquí figure `Implementada` significa
> que está lista para verificación, no que esté cerrada.

---

## Tablero — Tareas de auditoría (`TA`)

Origen: [`0001-method`](../../RandomAi_Auditor/audits/0001-method.md)

| Código | Tarea | Imp. | Urg. | Estado |
|---|---|---|---|---|
| `TA-0001` | Corregir atribución sobre «Actor Invitado» (§10 y Anexo A.1); retirar `➕` de §10 | Alta | Bloqueante | `Verificada` |
| `TA-0002` | Incorporar contenido normativo omitido de `015` §35–§48 | Alta | Bloqueante | `Verificada` |
| `TA-0007` | Añadir «decisión de alcance del prototipo» a las salidas del Descubrimiento (§14) | Alta | Bloqueante | `Implementada` |
| `TA-0003` | Declarar en el Anexo A las omisiones deliberadas de `015` §35–§51 | Alta | No bloqueante | `Verificada` |
| `TA-0004` | Añadir Anexo A.8: alcance del Prototipo de Evolución | Media | No bloqueante | `No implementada` |
| `TA-0005` | Corregir la fila «Cuándo» de la tabla §57 | Media | No bloqueante | `No implementada` |
| `TA-0006` | Reformular §32 de forma agnóstica a la infraestructura | Media | No bloqueante | `No implementada` |
| `TA-0008` | Registrar en el Anexo A la resolución sobre «Product Baseline» | Baja | No bloqueante | `No implementada` |
| `TA-0009` | Normalizar encabezados de `015_evolution.md` §35–§51 | Media | No bloqueante | `Descartada` |
| `TA-0010` | Frases normativas propias entregadas bajo un `↳` sin `➕` ni entrada en Anexo A | Media | No bloqueante | `Verificada` |
| `TA-0011` | `§17-bis` remite a «Ver Anexo A» para la convención `bis`; el Anexo no la contenía | Media | No bloqueante | `Verificada` |
| `TA-0012` | La fila «§42 → completa §47» de `D-03` sigue escrita y contradice al canónico | Media | No bloqueante | `Verificada` |
| `TA-0013` | Doble `↳` consecutivo en cuatro puntos del canónico | Baja | No bloqueante | `Verificada` |
| `TA-0014` | Marcas `↳` ampliadas que cubren texto anterior no procedente de la fuente nueva | Media | No bloqueante | `En discusión` |

**`TA-0009` · Razón del descarte:** decisión `D-01` del usuario — las fuentes se conservan
intactas (`000_method.md:6-7`). El defecto queda documentado en la auditoría y en `DT-001`.
El traslado a la auditora ya se hizo: su tablero registra `Descartada`
(`tasks_audit.md:66`, comprobado en `S-004`). ⚠️ **Nota de nomenclatura:** aquí figuró como
`Cancelada` —estado de tareas propias `T-nnn`— hasta `S-004`. Los estados de las `TA-nnnn`
los fija el tablero de la auditora; este archivo es espejo, no fuente.

**`TA-0001` · `Verificada` por la auditora.** Corregidos §10 y el Anexo A.1 de
`000_method.md` (evidencia: `git diff` de `S-003`). Se añadió además la justificación de por
qué `A.1` sigue en la lista de ADR pendientes del Anexo A, registrada como `D-10`. La
auditora asignó el estado de cierre `Verificada` (`tasks_audit.md:59`, comprobado en `S-004`).

**`TA-0002` · Implementada, no `Verificada`.** Ejecutada en `S-004` sobre
`000_method.md` (1012 → 1212 líneas). Las 13 secciones de `015` §36–§48 tienen
contrapartida localizable, más la fusión de `015` §50 en el §4:

| `015` | Destino en el canónico |
|---|---|
| §36, §37 | `§37.1` — No construir no significa no diseñar (Parte VI, junto a ARCHIT) |
| §38 | `§50.1` — La viabilidad se evalúa periódicamente |
| §39 | `§29.1` — Qué NO valida el prototipo (Parte V) |
| §40 | `§30` — ampliado: éxito de prototipo ≠ adopción |
| §41 | `§41.1` — GRTH no puede degenerar en Waterfall (Parte VII) |
| §42, §43 | `§17-bis.3` — Los dos riesgos simétricos |
| §44 | `§17-bis.5` — Límites del método |
| §45 | `§17-bis.1` — Cuándo debe extenderse el prototipo |
| §46 | `§17-bis.2` — **Los seis criterios**, enumerados completos |
| §47 | `§17-bis.4` — Aplicaciones que requieren adaptación |
| §48 | `§17-bis.6` — Principio de excepción |
| §50 | `§4` — de 3 a 6 preguntas (se añaden WSLT, GRTH, RELEASE OBJETIVO) |

`§17` y `§48` referencian `§17-bis`: ninguno de los dos se lee ya como regla absoluta.
Cada bloque incorporado lleva su marca `↳`. No hubo renumeración: `§18`, `§30`, `§47`,
`§61` y `§62` conservan su número (`RES-007`).

**Pendiente de la ejecutora:** ninguna. `TA-0003` quedó implementada en la misma sesión
`S-004`. El único estado de cierre es `Verificada` y lo asigna la auditora.

**`TA-0010`, `TA-0011`, `TA-0013` · Implementadas, no `Verificadas`.** Origen:
auditoría `0002-metodo-ampliado`. Las tres son defectos introducidos por `TA-0002` en la
misma sesión `S-004`, y se corrigieron en ella:

- **`TA-0013`** — fusionadas las cuatro marcas `↳` dobles (`§29`, `§37`, `§41`, `§50`).
  Cada sección vuelve a tener una sola marca, con las fuentes acumuladas.
- **`TA-0011`** — creada la entrada **Anexo A.9**, que enuncia la convención `bis` con su
  porqué. `§17-bis` ya no remite a un Anexo que no la contenía. **`A.8` queda reservada**
  para `TA-0004`, para que las dos tareas no colisionen en el mismo número.
- **`TA-0010`** — seis frases marcadas `➕` con remisión a `A.9`, y **dos retiradas por
  endurecer la fuente**: `015 §41` dice que cada iteración *debería* entregar capacidad
  demostrable, y el cierre que escribí lo convertía en definición absoluta; `015 §39` dice
  que el límite del prototipo *debe quedar explícito*, no que sea criterio de aprobación.
  Ese es el hallazgo real: no era decoración, era regla desplazada.

**`TA-0012` · Implementada, no `Verificada`.** El usuario autorizó la enmienda el
2026-08-27. La fila de `§42` en `D-03` pasa a «Incorporar → `§17-bis`, emparejada con
§43», con nota de enmienda fechada bajo la tabla (`decisions.md:214, 225`). Se enmienda
`D-03` en lugar de abrir una `D-11`: una decisión nueva no borra la anterior, y `D-03` es
la que se cita desde aquí y desde el tablero de la auditora. `D-03` conserva código, fecha
y estado `Vigente`; el alcance decidido no cambia.

**`TA-0003` · Implementada, no `Verificada`.** Creada la entrada **Anexo A.10** en
`000_method.md`: qué se omitió de `015` §35–§51 y por qué. Cierra el rango completo —14
secciones incorporadas al cuerpo + 3 omitidas = §35–§51—, comprobado por script: ninguna
sección sin resolver, ninguna en dos sitios a la vez.

Las tres omisiones, con la razón que consta en el canónico:

| `015` | Razón |
|---|---|
| §35 Ventajas | Argumentativa, no normativa. Justifica por qué conviene el método; no enuncia reglas. Lo normativo ya está en `§2`, `§3` y `§4` |
| §49 Principios (28 ítems) | Recapitulación. Los 28 están distribuidos por el cuerpo (`§16`, `§40`, `§51`, `§37.1`, `§17-bis`, `§60`…). Repetirlos crearía un segundo sitio donde la misma regla puede divergir |
| §51 Filosofía final | Duplica material presente en tres piezas: `§62`, el diagrama de `§5` y `§4` |

⚠️ **Hallazgo propio, registrado dentro de la propia entrada A.10.** `D-03` justificaba
omitir §49 y §51 diciendo que «duplican §61 y §62». **Comprobado, y es impreciso:** `§61`
son diez principios cuya fuente es `005 §41`, no los 28 de `015 §49`; y `§62` procede de
`005 §43`. La omisión sigue siendo correcta, pero por recapitulación distribuida, no por
duplicación con esas dos secciones. **No se modifica `D-03`**: la decisión no cambia, solo
su justificación, y la razón precisa queda escrita donde el lector del canónico la va a
buscar.

**`TA-0014` · En discusión — la ejecutora disputa la premisa, con evidencia.**

La auditora observa que el `↳` de `§4` pasó a `015 §2, §50` y que dos filas de la tabla
—MVP y EVOL— no dicen lo que dice `015 §50`. **Es cierto que no vienen de §50. Vienen de
§2, que sigue citado en la misma marca.** `015_evolution.md:45-53`:

| | `015 §2` (fuente) | Canónico `§4` |
|---|---|---|
| MVP | «¿La solución construida realmente es adoptada y utilizada por el **Actor Generador**?» | «¿El Actor Generador realmente adopta y usa la solución construida?» |
| EVOL | «¿Cómo aumentamos el valor de una solución que ya demostró adopción?» | «¿Cómo aumentamos el valor de algo que ya demostró adopción?» |

La segunda es casi literal. La marca `↳ *015 §2, §50*` es un **conjunto**, no una
atribución fila a fila: cada afirmación de `§4` está cubierta por uno de los dos. No hay
defecto que corregir en `§4`.

**El método que propone la auditora sí es correcto, y se aplicó.** Barridas las otras cinco
marcas ampliadas por `TA-0002`, preguntando —como pide— si el conjunto citado cubre **cada
afirmación** del bloque, no si la fuente nueva aporta algo:

| Marca | Cubre |
|---|---|
| `§29` `:636` — `005 §12 · 010 §29 · 015 §39` | cuerpo de §29 ← `005 §12`, `010 §29`; §29.1 ← `015 §39` ✅ |
| `§30` `:655` — `005 §12 · 015 §15, §24, §40` | cuerpo ← `005 §12`, `015 §15, §24`; párrafo nuevo ← `015 §40` ✅ |
| `§37` `:765` — `005 §17 · 015 §36, §37` | ARCHIT ← `005 §17`; §37.1 ← `015 §36, §37` ✅ |
| `§41` `:832` — `005 §21 · 015 §18, §19, §41` | GRTH ← `005 §21`, `015 §18, §19`; §41.1 ← `015 §41` ✅ |
| `§50` `:997` — `015 §23, §38` | cuerpo ← `015 §23`; §50.1 ← `015 §38` ✅ |

Lo que en cada bloque **no** procede de ninguna fuente ya lleva su `➕` con remisión a
`A.9`, por `TA-0010`. **Ninguna de las seis marcas cubre texto huérfano.**

📌 **Lo que sí queda en pie del hallazgo, y merece anotarse:** ampliar una marca es una
operación que puede introducir un defecto sin tocar una sola línea de texto. `TA-0010` y
`TA-0014` son la misma comprobación en dos direcciones: allí se añadió texto bajo una
marca; aquí se amplió una marca sobre texto. Que esta vez saliera limpia no la hace
prescindible — **hay que hacerla cada vez que una marca se amplía**, y sobre el conjunto
citado, no sobre la fuente añadida.

**Devuelto a la auditora** para que resuelva: la ejecutora no cierra sus propias tareas.

**`TA-0007` · Implementada, no `Verificada`.** Última bloqueante del Paso 1. Añadida a
`§14` la quinta salida —**decisión de alcance del prototipo**— y creada `§14.1` con su
desarrollo. Las tres evidencias:

1. `§14:291-292` la lista como salida.
2. `§14.1:309-317` exige la justificación, no solo la decisión, **y también cuando se
   decide el alcance por defecto**: decidir «solo el Generador» sin haber mirado `§17-bis`
   no es aplicar la regla general, es no haber decidido.
3. `§14.1` remite a `§17-bis.1`, `§17-bis.4` y `§17-bis.6`, creadas por `TA-0002`.

📌 **Marcada `➕` con entrada `A.11`, aplicando `L-010` por adelantado.** `015 §45` y `§47`
establecen **que** la decisión debe tomarse; ninguna fuente dice **cuándo** ni **dónde se
registra**. Situarla como salida del Descubrimiento es adición del canónico, y se declara
como tal en vez de entregarla bajo el `↳` de `005 §39 · 015 §45, §47`. Es el defecto que
la auditoría `0002` encontró en `TA-0002`; esta vez se evitó al escribir, no al corregir.

### Notas de alcance

- **`TA-0002` se ejecutará con alcance ampliado** respecto a su enunciado, por decisión `D-03`:
  13 secciones (§36–§48) en lugar de las 6 del mínimo, más la fusión de `015` §50 en el §4 del
  canónico. La auditora encontrará **más** de lo pedido, no menos.
- **`TA-0002` y `TA-0007` se ejecutan bajo la restricción `RES-007`:** el canónico se amplía
  **sin renumerar** (`§17-bis`). El motivo original eran las 62 referencias de `phases/`;
  tras `D-04` el motivo son las **43 referencias del repo de la auditora**, que no podemos
  editar (`RES-009`). Ver la revisión en `D-02`.
- **`TA-0007` vuelve a un solo frente.** Se había ampliado a `phases/005_discovery.md` además
  del canónico §14; con `phases/` eliminado por `D-04`, **su alcance es únicamente el canónico
  §14**, tal y como la auditoría lo enunció. Esta ampliación queda sin efecto.

---

## Tablero — Tareas propias (`T`)

| Código | Tarea | Origen | Estado |
|---|---|---|---|
| `T-001` | Leer y comprender `_brief/Client_brief.txt` | usuario | `Implementada` |
| `T-002` | Leer y comprender `_methodology/000_method.md` y las 3 fuentes | usuario | `Implementada` |
| `T-003` | Analizar la auditoría `0001-method` y verificar sus hallazgos de forma independiente | usuario | `Implementada` |
| `T-004` | Paso 0 — preparar y registrar las 3 decisiones previas (`D-01`…`D-03`) | usuario | `Implementada` |
| `T-005` | Crear la capa de persistencia `_persistence/` con sus 7 archivos | usuario | `Implementada` |
| `T-009` | Añadir índice de búsqueda rápida a los 7 archivos de `_persistence/` | usuario | `Implementada` |
| `T-010` | Consolidar `decisions/0001-method-decisions.md` en `decisions.md` y eliminar la carpeta | usuario | `Implementada` |
| `T-011` | Renombrar `brief/` y `methodology/` a `_brief/` y `_methodology/` | `D-05` | `Implementada` |
| `T-012` | Ajustar los registros por la eliminación de `phases/` | `D-04` | `Implementada` |
| `T-006` | Reconciliar la divergencia `_persistence/` vs `_memory/` en `phases/` | `DT-003` | `Cancelada` |
| `T-007` | Crear `CLAUDE.md` con el esquema de dos terminales | `TA-0006` | `Implementada` |
| `T-008` | Crear `templates/` con las plantillas que `phases/` referencia | `DT-002` | `Cancelada` |
| `T-013` | Resolver el hueco operativo del método tras eliminar `phases/` | `DT-008` | `No implementada` |
| `T-014` | Confirmar la eliminación de `phases/` y dejar el repo coherente | `D-04` | `Implementada` |
| `T-015` | Inicializar git y enlazar el remoto de GitHub | `D-06` | `Implementada` |
| `T-016` | Mover el generador de índices del scratchpad a `tools/mkindex.py` | `D-07` | `Implementada` |
| `T-017` | Adaptar el skill `protocol-close` a este proyecto | `D-07` | `Implementada` |
| `T-018` | Reestructurar `progress.md` con entradas de sesión `S-nnn` | `D-07` | `Implementada` |
| `T-019` | Adaptar el agente `session-closer` al skill ya adaptado | `DT-009` | `Implementada` |
| `T-020` | Adaptar el skill `protocol-start` a este proyecto | `D-07` | `Implementada` |
| `T-021` | Adaptar el agente `session-starter` al skill ya adaptado | `DT-010` | `Implementada` |
| `T-023` | Construir la capa del «cómo se trabaja con IA»: `_guide/GUIDE.md` | brief §22 · `D-09` | `Implementada` |
| `T-024` | Escribir las plantillas ejecutables de prueba | `D-09` | `Suspendida` |
| `T-025` | Pedir a la auditora que corra la auditoría del historial público | `D-09` | `No implementada` |
| `T-022` | Decidir si igualar el modelo de `session-starter` (`haiku`) al de `session-closer` (`sonnet`) | `session-closer` | `No implementada` |

**`T-006` y `T-008` · Razón de cancelación:** decisión `D-04`. Ambas existían únicamente para
servir a `phases/`; sin ese directorio no tienen objeto. Ver `DT-002` y `DT-003`, ambas
`Descartada`.

**`T-024` · Razón de suspensión:** no hay stack decidido (brief §23.1). **Condición de
reanudación:** que se decida la tecnología. Ese día se escriben las plantillas del capítulo 5
de la guía en el lenguaje elegido, y se amplía la tabla de «qué nunca sube a Git».

**`T-013`** no bloquea las tareas de auditoría en curso, pero **sí bloqueará la apertura de la
fase de Descubrimiento**. Requiere decisión del usuario entre las tres opciones de `DT-008`.

**`T-022`** — detectada al cierre de `S-001`: `session-starter.md` declara `model: haiku` y
`session-closer.md` declara `model: sonnet` (`.claude/agents/`, línea 5 de cada uno). El
arranque ahora hace comparaciones finas (cruzar tableros propio y de la auditora, cotejar el
id `S-nnn` más alto), lo que sugiere igualarlos — pero es una decisión del usuario, no una
lectura automática del diff. Sin decisión registrada.

---

## Orden de trabajo

Primero las **bloqueantes** por importancia, después las **no bloqueantes** por importancia:

```text
TA-0001 (Verificada) → TA-0002 (+TA-0003) → TA-0007
   ↓
TA-0004 · TA-0005 · TA-0006 (T-007 ya hecha) · TA-0008
   ↓
Verificación por la auditora
   ↓
T-013  (decisión del usuario sobre DT-008)
   ↓
Fase 005_discovery
```
