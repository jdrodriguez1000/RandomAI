# tasks.md — Tareas del proyecto RandomAI

> Registro de tareas realizadas y por realizar. Toda tarea tiene **código** y **estado**.
> Cumple la regla de trazabilidad del método (`000_method.md` §47): *nada se construye sin
> una razón trazable*. Ninguna tarea existe sin origen.

**Última actualización:** 2026-08-26

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
| `80` | &nbsp;&nbsp;↳ Notas de alcance | [↓](#notas-de-alcance) |
| `95` | **Tablero — Tareas propias (T)** | [↓](#tablero--tareas-propias-t) |
| `137` | **Orden de trabajo** | [↓](#orden-de-trabajo) |

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
| `TA-0001` | Corregir atribución sobre «Actor Invitado» (§10 y Anexo A.1); retirar `➕` de §10 | Alta | Bloqueante | `No implementada` |
| `TA-0002` | Incorporar contenido normativo omitido de `015` §35–§48 | Alta | Bloqueante | `No implementada` |
| `TA-0007` | Añadir «decisión de alcance del prototipo» a las salidas del Descubrimiento (§14) | Alta | Bloqueante | `No implementada` |
| `TA-0003` | Declarar en el Anexo A las omisiones deliberadas de `015` §35–§51 | Alta | No bloqueante | `No implementada` |
| `TA-0004` | Añadir Anexo A.8: alcance del Prototipo de Evolución | Media | No bloqueante | `No implementada` |
| `TA-0005` | Corregir la fila «Cuándo» de la tabla §57 | Media | No bloqueante | `No implementada` |
| `TA-0006` | Reformular §32 de forma agnóstica a la infraestructura | Media | No bloqueante | `No implementada` |
| `TA-0008` | Registrar en el Anexo A la resolución sobre «Product Baseline» | Baja | No bloqueante | `No implementada` |
| `TA-0009` | Normalizar encabezados de `015_evolution.md` §35–§51 | Media | No bloqueante | `Cancelada` |

**`TA-0009` · Razón de cancelación:** decisión `D-01` del usuario — las fuentes se conservan
intactas (`000_method.md:6-7`). El defecto queda documentado en la auditoría y en `DT-001`.
**Pendiente:** el usuario debe trasladar este estado a la auditora, que en su tablero lo
registrará como `Descartada`.

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
| `T-022` | Decidir si igualar el modelo de `session-starter` (`haiku`) al de `session-closer` (`sonnet`) | `session-closer` | `No implementada` |

**`T-006` y `T-008` · Razón de cancelación:** decisión `D-04`. Ambas existían únicamente para
servir a `phases/`; sin ese directorio no tienen objeto. Ver `DT-002` y `DT-003`, ambas
`Descartada`.

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
TA-0001 → TA-0002 (+TA-0003) → TA-0007
   ↓
TA-0004 · TA-0005 · TA-0006 (T-007 ya hecha) · TA-0008
   ↓
Verificación por la auditora
   ↓
T-013  (decisión del usuario sobre DT-008)
   ↓
Fase 005_discovery
```
