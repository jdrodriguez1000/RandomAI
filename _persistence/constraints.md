# constraints.md — Limitaciones y restricciones del proyecto RandomAI

> Los límites dentro de los que hay que construir. Una restricción **no se negocia desde la
> ejecutora**: o viene del cliente, o del método, o de la realidad técnica.
>
> Distinción importante: una **restricción** (`RES`) es un límite firme y verificado; algo que
> creemos limitante pero no hemos comprobado es un **supuesto** (`SUP`) y vive en
> [`assumptions.md`](assumptions.md).

**Última actualización:** 2026-08-26

<!--INDEX-->

## Índice

> **Búsqueda rápida.** Salta con el enlace, o ve directo a la línea indicada (exacta, ya contando este índice).
> Por código: `grep -n 'RES-001' constraints.md`

| Línea | Sección | Ir a |
|---|---|---|
| `39` | **Convenciones** | [↓](#convenciones) |
| `50` | **Tablero** | [↓](#tablero) |
| `69` | **Detalle** | [↓](#detalle) |
| `71` | &nbsp;&nbsp;↳ RES-001 · Sin IA generativa en el producto | [↓](#res-001--sin-ia-generativa-en-el-producto) |
| `88` | &nbsp;&nbsp;↳ RES-002 · Despliegue en Vercel | [↓](#res-002--despliegue-en-vercel) |
| `101` | &nbsp;&nbsp;↳ RES-003 · Fuente de datos oficial | [↓](#res-003--fuente-de-datos-oficial) |
| `114` | &nbsp;&nbsp;↳ RES-004 · Alcance MVP estricto | [↓](#res-004--alcance-mvp-estricto) |
| `126` | &nbsp;&nbsp;↳ RES-005 · Actualización incremental | [↓](#res-005--actualización-incremental) |
| `135` | &nbsp;&nbsp;↳ RES-006 · Fuentes inmutables | [↓](#res-006--fuentes-inmutables) |
| `147` | &nbsp;&nbsp;↳ RES-007 · El canónico no se renumera | [↓](#res-007--el-canónico-no-se-renumera) |
| `175` | &nbsp;&nbsp;↳ RES-008 · La ejecutora no declara sus propios Gates | [↓](#res-008--la-ejecutora-no-declara-sus-propios-gates) |
| `187` | &nbsp;&nbsp;↳ RES-009 · La ejecutora no escribe en el repo de la auditora | [↓](#res-009--la-ejecutora-no-escribe-en-el-repo-de-la-auditora) |
| `197` | &nbsp;&nbsp;↳ RES-012 · El operativo de una fase no se escribe antes de abrir esa fase | [↓](#res-012--el-operativo-de-una-fase-no-se-escribe-antes-de-abrir-esa-fase) |

<!--/INDEX-->

---

## Convenciones

**Código:** `RES-NNN`, correlativo, nunca se reutiliza. Nomenclatura heredada de `phases/`,
eliminada por `D-04`; la convención se conserva.

**Origen:** `Cliente` · `Método` · `Técnica` · `Proceso`

**Estado:** `Vigente` · `Levantada` · `Modificada`

---

## Tablero

| Código | Restricción | Origen | Estado |
|---|---|---|---|
| `RES-001` | El producto final **no** usa IA generativa ni llama a APIs de LLM | Cliente | `Vigente` |
| `RES-002` | La aplicación debe desplegarse en **Vercel** | Cliente | `Vigente` |
| `RES-003` | Los datos provienen de la **página oficial de Baloto** | Cliente | `Vigente` |
| `RES-004` | Alcance MVP estricto: nada fuera del flujo definido sin definirlo antes | Cliente | `Vigente` |
| `RES-005` | Actualización **incremental** del histórico: no re-descargar todo | Cliente | `Vigente` |
| `RES-006` | Las fuentes de `_methodology/sources/` **no se editan** | Proceso | `Vigente` |
| `RES-007` | El canónico **se amplía pero no se renumera** | Proceso | `Vigente` |
| `RES-008` | La ejecutora **no declara sus propios Gates** | Método | `Vigente` |
| `RES-009` | La ejecutora **no escribe** en el repo de la auditora | Proceso | `Vigente` |
| `RES-010` | El repositorio de GitHub es **público** | Técnica | `Vigente` |
| `RES-011` | Con git **solo se añade historia**, nunca se reescribe | Proceso | `Vigente` |
| `RES-012` | El operativo de una fase no se escribe antes de abrir esa fase | Método | `Vigente` |

---

## Detalle

### `RES-001` · Sin IA generativa en el producto

**Origen:** brief §21 y §19. **Vigente.**

Prohibidas las llamadas a OpenAI/ChatGPT, Anthropic/Claude, Google Gemini u otros LLM. La
generación de números, el análisis estadístico y la comparación de resultados se ejecutan con
**código convencional y algoritmos determinísticos/aleatorios**.

**Matiz que no debe confundirse:** el producto puede ser *desarrollado* con asistencia de IA
—de hecho lo está siendo, brief §22— pero **no puede depender de una API de IA para
funcionar**. La restricción es sobre el producto, no sobre el proceso.

**Además, restricción de comunicación** (brief §9 y §19): el indicador estadístico no puede
presentarse como predicción, garantía, recomendación de apuesta ni predicción por IA.

---

### `RES-002` · Despliegue en Vercel

**Origen:** brief §24. **Vigente.**

Condiciona frontend, backend/API, ejecución de la actualización del histórico, almacenamiento
persistente, variables de entorno y tareas programadas. La arquitectura debe mantenerse
mínima, **sin infraestructura adicional innecesaria para el MVP**.

**Riesgo asociado:** `SUP-004` — que Vercel sostenga persistencia + cron en el plan disponible
está asumido, no verificado.

---

### `RES-003` · Fuente de datos oficial

**Origen:** brief §3. **Vigente.**

El histórico se obtiene de la página oficial de Baloto. El **método exacto** de obtención es
decisión pendiente (brief §23.3), así que la restricción es sobre *de dónde*, no sobre *cómo*.

**Riesgo asociado:** `SUP-001`, `SUP-002`, `SUP-003`. También brief §23.11 y §23.12: el manejo
de errores cuando la fuente no esté disponible y de resultados aún no publicados sigue sin
definir.

---

### `RES-004` · Alcance MVP estricto

**Origen:** brief §20. **Vigente.**

«No se deberán agregar funcionalidades adicionales que no sean necesarias para este flujo sin
definirlas previamente.»

Coincide con el método (`000_method.md` §47, regla de trazabilidad). **Doble candado: el
cliente lo pide y el método lo exige.**

---

### `RES-005` · Actualización incremental

**Origen:** brief §3. **Vigente.**

Tras la carga inicial, cada actualización identifica la última fecha almacenada e incorpora
**únicamente** los sorteos faltantes.

---

### `RES-006` · Fuentes inmutables

**Origen:** `000_method.md:6-7` + decisión `D-01`. **Vigente.**

Las fuentes se conservan intactas como registro de cómo se diseñó el método, incluso para
correcciones que no alteran contenido.

**Efecto colateral aceptado:** el defecto de encabezados de `015:896–1147` persiste. Ver
`DT-001` y `L-001`.

---

### `RES-007` · El canónico no se renumera

**Origen:** decisión `D-02`. **Vigente.**

Las ampliaciones del canónico entran con numeración sufijada (`§17-bis`) en lugar de
desplazar las secciones existentes.

⚠️ **Fundamento revisado el 2026-08-26 (`D-04`).** Esta restricción nació para proteger las 62
referencias cruzadas de `phases/`. Al eliminarse `phases/`, esas 62 desaparecieron — pero la
restricción **sigue vigente por un motivo distinto y más fuerte**: el repo de la auditora
contiene **43 referencias inequívocas al canónico en secciones ≥ §18**
(`0001-method.md`: 31 · `tasks_audit.md`: 12), y `RES-009` nos prohíbe editarlas.

| Dónde | Refs ≥ §18 | ¿Podemos corregirlas? |
|---|---|---|
| `phases/` | 41 | eliminado por `D-04` |
| `RandomAi_Auditor/audits/0001-method.md` | 31 | **No** (`RES-009`) |
| `RandomAi_Auditor/audits/tasks_audit.md` | 12 | **No** (`RES-009`) |

Renumerar hoy invalidaría silenciosamente el tablero de tareas **vivo** que dirige nuestro
trabajo — `§29`(x10), `§32`(x7) y `§57`(x10) son las más citadas.

**Condición de levantamiento:** que ningún consumidor externo referencie el canónico por
número. Hoy no se cumple, y **el consumidor que queda es precisamente el que no podemos
editar**.

---

### `RES-008` · La ejecutora no declara sus propios Gates

**Origen:** `000_method.md` §32. **Vigente.**

*Quien construye no puede ser su propio testigo: un sistema que se revisa a sí mismo comprueba
que es coherente, no que sea cierto.* El veredicto de un Gate lo emite la terminal auditora.

**Nota:** `TA-0006` reformulará §32 de forma agnóstica y moverá la asignación concreta a
`CLAUDE.md`. La restricción sobrevive al cambio de redacción; solo cambia dónde vive.

---

### `RES-009` · La ejecutora no escribe en el repo de la auditora

**Origen:** proceso de dos terminales. **Vigente.**

`RandomAi_Auditor/` es artefacto de la auditora. Los estados de `tasks_audit.md` —en particular
`Verificada` y `Descartada`— los asigna ella. La ejecutora **lee** la auditoría, refleja los
estados en su propio [`tasks.md`](tasks.md), y el usuario traslada los cambios.

---

### `RES-012` · El operativo de una fase no se escribe antes de abrir esa fase

**Origen:** Método (`D-13`, decisión del usuario). **Vigente.**

`_phases/` y `_templates/` contienen **únicamente** el operativo de la fase que se está
ejecutando o de las ya alcanzadas. Hoy: el Descubrimiento, y nada más.

**Qué prohíbe, en concreto.** Crear, adelantar o «dejar preparado» el archivo de fase o las
plantillas de una fase que aún no se ha abierto — Arquitectura, Implementación, Evolución o
cualquier otra. Tampoco por conveniencia («ya que estoy»), ni como borrador, ni en `_temp/`.

**Qué no prohíbe.** Que el canónico `000_method.md` describa **qué** es cada fase: eso ya
existe, es su trabajo, y no es operativo. La restricción es sobre el **cómo**, no sobre el
**qué**.

🔑 **El porqué, que vale más que la regla.** Un documento operativo escrito antes de abrir su
fase se convierte en norma sin que nadie haya decidido que lo fuera: cuando llega el turno de
esa fase, ya está escrito, y lo escrito se ejecuta en vez de discutirse. Es el defecto que
`D-12` evita con `_temp/`, un escalón más arriba. Y choca de frente con `000_method.md` §2 —**no
se construye aquello que todavía no se entiende suficientemente bien**—: el operativo de una
fase se entiende **al llegar a ella**, con lo aprendido en las anteriores, no antes.

⚠️ **Y hay un coste que esta restricción acepta a sabiendas.** Al abrir cada fase habrá que
escribir su operativo, y eso es trabajo que no está hecho. Se prefiere ese coste al de heredar
ocho documentos que nadie ha revisado y que nadie va a revisar hasta que sea tarde.

**Cómo se comprueba.** `find _phases _templates -type f` no devuelve ningún archivo de una fase
que no esté abierta. Comprobado el 2026-08-27: 6 archivos, todos de Descubrimiento.

**Condición de levantamiento.** No se levanta entera: **se levanta por fase y de una en una.**
Cada fase sale de la restricción en el momento en que se abre. La restricción como tal muere
cuando se haya alcanzado la última fase del método.

**Trazas:** `D-13` · `D-04` · `DT-008` · `D-12` · `000_method.md` §2
