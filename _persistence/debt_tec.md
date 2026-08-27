# debt_tec.md — Deuda técnica del proyecto RandomAI

> Todo lo que se dejó a medias, se aplazó conscientemente o quedó peor de lo que debería,
> **con su estado**, para que al implementarlo podamos cerrarlo.
>
> Una deuda registrada es una decisión; una deuda no registrada es un accidente esperando.
> Registrar no es saldar: mientras el estado no sea `Implementada` o `Aceptada`, sigue viva.

**Última actualización:** 2026-08-27 (S-005)

<!--INDEX-->

## Índice

> **Búsqueda rápida.** Salta con el enlace, o ve directo a la línea indicada (exacta, ya contando este índice).
> Por código: `grep -n 'DT-003' debt_tec.md`

| Línea | Sección | Ir a |
|---|---|---|
| `41` | **Convenciones** | [↓](#convenciones) |
| `72` | **Tablero** | [↓](#tablero) |
| `92` | **Detalle** | [↓](#detalle) |
| `94` | &nbsp;&nbsp;↳ DT-001 · Encabezados de 015_evolution.md sin normalizar | [↓](#dt-001--encabezados-de-015_evolutionmd-sin-normalizar) |
| `112` | &nbsp;&nbsp;↳ DT-002 · Rutas referenciadas por phases/ que no existen | [↓](#dt-002--rutas-referenciadas-por-phases-que-no-existen) |
| `132` | &nbsp;&nbsp;↳ DT-003 · Divergencia de nombres en la capa de persistencia | [↓](#dt-003--divergencia-de-nombres-en-la-capa-de-persistencia) |
| `166` | &nbsp;&nbsp;↳ DT-004 · ADRs pendientes del Anexo A | [↓](#dt-004--adrs-pendientes-del-anexo-a) |
| `190` | &nbsp;&nbsp;↳ DT-005 · Numeración no correlativa del canónico | [↓](#dt-005--numeración-no-correlativa-del-canónico) |
| `205` | &nbsp;&nbsp;↳ DT-006 · phases/ sin auditar | [↓](#dt-006--phases-sin-auditar) |
| `221` | &nbsp;&nbsp;↳ DT-010 · El agente session-starter sigue sin adaptar | [↓](#dt-010--el-agente-session-starter-sigue-sin-adaptar) |
| `246` | &nbsp;&nbsp;↳ DT-009 · El agente session-closer contradice al skill | [↓](#dt-009--el-agente-session-closer-contradice-al-skill) |
| `281` | &nbsp;&nbsp;↳ DT-008 · El método pierde su nivel operativo | [↓](#dt-008--el-método-pierde-su-nivel-operativo) |
| `338` | &nbsp;&nbsp;↳ DT-007 · CLAUDE.md no existe | [↓](#dt-007--claudemd-no-existe) |
| `355` | &nbsp;&nbsp;↳ DT-011 · La cita de A.3 no está verificada del todo | [↓](#dt-011--la-cita-de-a3-no-está-verificada-del-todo) |
| `387` | &nbsp;&nbsp;↳ DT-012 · tools/mkindex.py puede no escribir de forma atómica | [↓](#dt-012--toolsmkindexpy-puede-no-escribir-de-forma-atómica) |
| `415` | &nbsp;&nbsp;↳ DT-013 · progress.md §6 («Mapa de archivos») no incluye _temp/, _phases/ ni _templates/ | [↓](#dt-013--progressmd-6-mapa-de-archivos-no-incluye-_temp-_phases-ni-_templates) |

<!--/INDEX-->

---

## Convenciones

**Código:** `DT-NNN`, correlativo, nunca se reutiliza.

**Estados:**

| Estado | Significado |
|---|---|
| `Abierta` | registrada, sin saldar |
| `En curso` | se está saldando |
| `Implementada` | saldada. **Estado de cierre** |
| `Aceptada` | se decide convivir con ella indefinidamente. **Requiere decisión `D-NNN`** |
| `Descartada` | dejó de ser deuda (el código o documento desapareció, o el problema se disolvió) |

**Severidad:** `Alta` (bloqueará algo) · `Media` (costará más caro después) · `Baja` (molestia)

**Cada deuda declara:** qué se debe · por qué se aplazó · **qué la salda** · qué pasa si no se salda.

🚨 **La severidad y el estado viven en el tablero, y solo ahí.** Las entradas no los repiten:
un dato en dos capas diverge, y miente la capa que menos se lee (`L-008`). Hasta `S-004`,
tres entradas llevaban su propio campo `Estado:`; dos de las tres ya contradecían al tablero
—`DT-009` y `DT-010` decían `Abierta` estando `Implementada`—. Se retiró el campo en vez de
sincronizarlo: sincronizar deja el defecto listo para repetirse.

> ⚠️ Mientras no exista código de aplicación, la deuda es **documental y de proceso**. Cuando
> empiece la construcción, esta será la fuente principal de deuda de implementación.
> La obligación de revisarla en cada Gate vivía en `phases/`, eliminado por `D-04`: hoy no
> está escrita en ninguna parte. Ver `DT-008`.

---

## Tablero

| Código | Deuda | Severidad | Estado |
|---|---|---|---|
| `DT-001` | Encabezados de `015_evolution.md` §35–§51 sin normalizar | Media | `Aceptada` |
| `DT-002` | `phases/` referencia `templates/`, `_memory/` y `_discovery/`, que no existen | Alta | `Descartada` |
| `DT-003` | Divergencia de nombres: `_persistence/` vs `_memory/`, `debt_tec.md` vs `tech-debt.md` | Alta | `Descartada` |
| `DT-004` | ADRs pendientes del Anexo A del canónico (A.1, A.2, A.5, A.6) | Media | `Abierta` |
| `DT-005` | La numeración del canónico dejará de ser correlativa (`§17-bis`) | Baja | `Aceptada` |
| `DT-006` | `phases/` sin auditar — 8 archivos, ~88 KB | Media | `Descartada` |
| `DT-008` | El método pierde su nivel operativo al eliminar `phases/` | Alta | `Abierta` |
| `DT-009` | El agente `session-closer` contradice al skill que dice invocar | Alta | `Implementada` |
| `DT-010` | El agente `session-starter` sigue escrito contra el proyecto de origen | Alta | `Implementada` |
| `DT-007` | `CLAUDE.md` no existe; el esquema de dos terminales no está escrito en ninguna parte | Media | `Implementada` |
| `DT-011` | La cita de `A.3` del Anexo A no está verificada del todo | Baja | `Abierta` |
| `DT-012` | `tools/mkindex.py` puede no escribir de forma atómica | Media | `Abierta` |
| `DT-013` | `progress.md` §6 («Mapa de archivos») no incluye `_temp/`, `_phases/` ni `_templates/` | Baja | `Abierta` |

---

## Detalle

### `DT-001` · Encabezados de `015_evolution.md` sin normalizar

**Qué se debe.** Las secciones §35–§51 (líneas 896–1147) son texto plano sin prefijo `#`.

**Por qué se aplazó.** Decisión `D-01`: las fuentes se conservan intactas (`RES-006`). Se
prefirió la regla de inmutabilidad sobre la comodidad de navegación.

**Estado: `Aceptada`.** Convivimos con ella indefinidamente, respaldada por `D-01`.

**Mitigación en vigor.** El defecto está documentado en la auditoría `0001-method` (H-02, causa
raíz), en `L-001` y aquí. **Toda lectura de esa fuente se hace por rango de líneas.**

**Qué pasa si no se mitiga.** Ya pasó una vez: se perdieron ~200 líneas normativas y se
invirtió una regla del método. Puede volver a pasar con cualquier lector futuro que no lea
`L-001`.

---

### `DT-002` · Rutas referenciadas por `phases/` que no existen

> **`Descartada` el 2026-08-26 por `D-04`.** `templates/`, `_memory/` y `_discovery/` solo
> eran necesarias porque `phases/` las citaba. Eliminado `phases/`, el problema se disolvió:
> no hay nada que apunte a esas rutas. Se conserva el registro como historia.

**Qué se debe.** `phases/` referencia `templates/` (plantillas de los cinco artefactos de
Descubrimiento), `_memory/` y `_discovery/`. Ninguna existe.

**Por qué se aplazó.** No bloquea la corrección del método, que es el trabajo actual.

**Qué la salda.** `T-008` (crear `templates/`) y la resolución de `DT-003` (que decide si
`_memory/` debe existir o renombrarse).

**Qué pasa si no se salda.** **Bloqueará el arranque real de la fase `005_discovery`:**
`phases/005_discovery.md` §5 dice literalmente «Las plantillas de estos cinco archivos aún no
están escritas → `templates/`».

---

### `DT-003` · Divergencia de nombres en la capa de persistencia

> **`Descartada` el 2026-08-26 por `D-04`.** La divergencia existía entre `_persistence/` y
> lo que `phases/` esperaba encontrar. Sin `phases/` no hay dos partes que reconciliar:
> `_persistence/` es ahora la única capa de registro. `T-006` queda `Cancelada`.

**Qué se debe.** El usuario pidió `_persistence/` con `debt_tec.md`. `phases/` referencia
`_memory/` con `tech-debt.md`, en 8 puntos distintos y en 6 de los 8 archivos de fase.

**Los nombres en conflicto:**

| Este repo (`_persistence/`) | `phases/` (`_memory/`) |
|---|---|
| `progress.md` | `progress.md` ✅ coincide |
| `lessons.md` | `lessons.md` ✅ coincide |
| `assumptions.md` | `assumptions.md` ✅ coincide |
| `constraints.md` | `constraints.md` ✅ coincide |
| `debt_tec.md` | `tech-debt.md` ❌ difiere |
| `decisions.md` | *no existe en `phases/`* |
| `tasks.md` | *no existe en `phases/`* |

**Por qué se aplazó.** Se construyó lo que el usuario pidió; reconciliar `phases/` es una
decisión suya, no de la ejecutora.

**Qué la salda.** `T-006`. Dos caminos posibles: **(a)** actualizar las referencias de
`phases/` a `_persistence/` y `debt_tec.md`; **(b)** renombrar esta carpeta a `_memory/`.
**Recomendación: (a)** — `_persistence/` es más descriptivo, y `decisions.md` y `tasks.md`
enriquecen lo que `phases/` contemplaba.

**Qué pasa si no se salda.** Las fases apuntarán a una carpeta inexistente y la ejecutora
escribirá en dos sitios distintos, o en ninguno.

---

### `DT-004` · ADRs pendientes del Anexo A

**Qué se debe.** `000_method.md:1002` declara: «**Pendiente:** A.1, A.2, A.5 y A.6 merecen un
ADR propio con contexto, alternativas y consecuencias. Aún no se han escrito.»

**Estado tras la auditoría.** A.5 requerirá reescritura si se ejecuta `TA-0006`.

✅ **A.1 resuelta por `D-10`** (2026-08-26). `TA-0001` obligó a decidir si seguía necesitando
ADR, y la respuesta fue **sí, pero por otro motivo**: no porque el conflicto entre fuentes siga
abierto —no lo está— sino porque la regla restringe el **modelo de autorización del producto**.
La justificación está escrita en el cierre del Anexo A del canónico. Sigue contando como ADR
pendiente; ya no como ADR **por revisar**.

**Qué la salda.** Escribir los cuatro ADR —A.1, A.2, A.5 y A.6— al tocar la **Baseline**, que
es donde viven los `ADR-NNN` (`000_method.md` §38). Antes no: hoy no hay diseño que restringir.

📌 **Revisada en `S-004` (`TA-0019`).** Al pasar el Anexo A de 7 a 12 entradas, la lista de
ADR pendientes no se revisó. Hecho: **`A.8`–`A.12` no requieren ADR**, y el criterio que lo
decide —¿la decisión restringe el diseño del producto, o solo este documento?— quedó escrito
en el propio canónico, que es donde hace falta al añadir la siguiente entrada. La deuda sigue
`Abierta`: la componen `A.1`, `A.2`, `A.5` y `A.6`, sin cambios.

---

### `DT-005` · Numeración no correlativa del canónico

**Qué se debe.** Tras `TA-0002`, el canónico tendrá `§17-bis` entre §17 y §18.

**Por qué se aceptó.** Decisión `D-02`. El motivo original —41 de 62 referencias en
`phases/`— desapareció con `D-04`, pero la deuda **sigue `Aceptada`**: ahora la sostienen las
43 referencias del repo de la auditora, que `RES-009` nos impide corregir.

**Estado: `Aceptada`.** Es el precio consciente de `RES-007`.

**Condición de cierre.** Que ningún consumidor externo referencie el canónico por número.
Ver la revisión de `D-02` y `RES-007`.

---

### `DT-006` · `phases/` sin auditar

> **`Descartada` el 2026-08-26 por `D-04`.** No queda objeto que auditar. La lección que
> produjo —`L-004`, el alcance declarado de una auditoría es su límite— **sigue vigente** y
> es lo que hay que conservar de aquí.

**Qué se debe.** Los 8 archivos de fase operacionalizan el método y nunca han sido auditados;
la auditoría `0001-method` declaró como objeto solo `000_method.md`.

**Evidencia de que importa.** Sin auditar, ya aparecieron dos problemas reales: el riesgo de
las 62 referencias y el segundo frente de `TA-0007` en `005_discovery.md`.

**Qué la salda.** Ya no aplica.

---

### `DT-010` · El agente `session-starter` sigue sin adaptar

> **`Implementada` el 2026-08-26 (`T-021`).** El agente quedó **delgado**, igual que
> `session-closer`: cero pasos y cero comandos del procedimiento en su cuerpo. Se le añadieron
> la definición de sesión (`D-08`), la tabla de tres actores con la auditora como fuente
> obligatoria, y la prohibición de declarar Gates (`RES-008`).

**Origen:** `T-020` · *severidad y estado, en el tablero* ↑

**Qué se debe.** `.claude/agents/session-starter.md` llegó escrito contra el proyecto de origen
y **no se tocó**: se adaptó primero el skill, por decisión del usuario.

**Es el mismo patrón que `DT-009`**, ya resuelto en el cierre: un agente que lleva el
procedimiento duplicado en el cuerpo **no delega, compite** — ante la discrepancia sigue su
propia copia, que es la vieja.

**Qué la salda.** `T-021`: dejarlo delgado —quién es, qué no puede hacer, e invoca el skill—
sin duplicar un solo paso, igual que se hizo con `session-closer`.

**Qué pasa si no se salda.** El arranque ejecutaría el procedimiento ajeno: leería `_context/`,
que no existe; ignoraría el tablero de la auditora; y reportaría sesiones por fecha en vez de
por `S-nnn`.

---

### `DT-009` · El agente `session-closer` contradice al skill

> **`Implementada` el 2026-08-26 (`T-019`).** El agente quedó **delgado**: dice quién es y qué
> no puede hacer, e invoca el skill. **No contiene ni un solo paso ni comando del
> procedimiento**, así que ya no puede competir con él. Se le añadieron la tabla de tres
> actores, la prohibición de `Verificada`, `debt_tec.md` como proponible y el aviso del
> repositorio público.

**Origen:** `D-07` · *severidad y estado, en el tablero* ↑

**Qué se debe.** `.claude/agents/session-closer.md` llegó escrito contra el proyecto de origen y
**no se tocó** en esta ronda, por decisión del usuario: primero el skill.

El agente dice *«invoca la skill `protocol-close`… síguelo tal como está escrito»*, pero además
**repite media parte del procedimiento en su propio cuerpo** — y esa copia es la vieja:

| El agente dice | El skill adaptado dice |
|---|---|
| comprobar que `app/static/*.js` sea el compilado de `frontend/*.ts` | ese control no existe; el Paso 2b regenera índices |
| «Paso 5b», «Paso 2b del protocolo» | la numeración cambió |
| cita `[D-016]`, `[D-019]`, `[L-006]` | el skill no cita ningún código; `L-006` aquí significa otra cosa |
| «no toques `_context/`» | esa carpeta no existe; son `_brief/` y `_methodology/` |
| cuatro archivos del porqué, seis en total | son **siete**, y `debt_tec.md` sí es proponible |
| dos actores | **tres**: falta la prohibición de marcar `Verificada` |

**Por qué importa más de lo que parece.** Un agente que lleva el procedimiento duplicado en el
cuerpo **no delega: compite**. Ante la discrepancia seguirá lo que tiene más cerca, que es su
propia copia desactualizada — y esa copia le manda ejecutar comprobaciones de un stack que este
proyecto no tiene.

**Qué la salda.** `T-019`: dejar el agente **delgado** —quién es, qué no puede hacer, e invoca
el skill— sin duplicar pasos. Lo que sea procedimiento vive en el skill y solo ahí.

---

### `DT-008` · El método pierde su nivel operativo

**Origen:** `D-04` · *severidad y estado, en el tablero* ↑

**Qué se debe.** `000_method.md` es **descriptivo**: define qué es cada fase, qué la
caracteriza y qué principios la rigen. `phases/` era **prescriptivo**: por cada una de las 8
fases declaraba qué autoriza, **qué prohíbe**, qué entradas exige, el procedimiento paso a
paso, los artefactos que produce, la **condición de salida** en forma de checklist, qué se
registra en la capa de persistencia y qué se entrega al Gate siguiente.

Eliminado `phases/`, el proyecto conserva el **qué** y pierde el **cómo**.

🚨 **Corregida por la auditoría `0004` (`S-004`). Esta deuda estaba mal medida y su premisa
principal era falsa.** Lo escrito arriba se conserva porque es el enunciado que la auditora
verificó; lo que sigue es lo comprobado, y **manda sobre el párrafo anterior**:

| De los 8 puntos enumerados | Estado real |
|---|---|
| qué autoriza · qué prohíbe · procedimiento · artefactos · registro en persistencia | **cubiertos** entre el canónico y `_guide/GUIDE.md` |
| **entradas exigidas** · **condición de salida** · **entrega al Gate** | **faltan** — «condición de salida» y «checklist» no aparecen ni una vez en el canónico, `GUIDE.md` ni `CLAUDE.md` |

⚠️ **La premisa sobre el Gate 1 era falsa.** Esta entrada decía que el Gate 1 se declararía
sin criterio operativo escrito. **No es cierto:** §29, §29.1, §30, §31, §32 y §19–§27 dan
para esa fase **más** nivel operativo del que `phases/` daba. El hueco no está en el Gate 1.

📌 **Y `GUIDE.md` no cubre lo que esta entrada suponía:** cubre el «cómo» de la
**construcción**, que `DT-008` daba por perdido. WSLT y GRTH tienen hoy más procedimiento
escrito que antes de `D-04`.

**Consecuencia sobre las tres opciones de abajo:** están dimensionadas para un hueco de ocho
puntos en seis etapas. El hueco medido es **de tres puntos y en un sitio**. Ninguna de las
tres se eligió sobre esta medición — se enunciaron sobre la anterior, que era peor de lo que
el problema es. `T-013` debe decidirse contra los tres puntos reales, no contra los ocho.

**Por qué se aceptó el hueco.** `D-04` es decisión del usuario y la ejecutora no la discute.
Se registra la consecuencia, no se revierte la decisión.

**Qué la salda.** Una de estas tres, a elegir por el usuario:

| | Opción | Coste |
|---|---|---|
| a | Reconstruir el nivel operativo dentro del propio `000_method.md` | Engorda el canónico; choca con `RES-007` si obliga a numerar |
| b | Recrear un directorio operativo con otro nombre y otra forma | Reintroduce lo que se acaba de eliminar |
| c | Operar sin procedimiento escrito, guiándose solo por el método | Cero coste ahora; las condiciones de salida de cada fase dejan de ser verificables |

**Qué pasa si no se salda.** Al abrir el Descubrimiento no habrá condición de salida
escrita: `§14` lista **qué produce** la fase —cinco salidas tras `TA-0007`— pero no **cuándo
se considera terminada**, ni quién lo declara. Eso es `TA-0015`, emitida por la auditoría
`0004` y **bloqueante**. ~~El Gate 1 se declararía sin criterio operativo escrito~~ —
comprobado falso, ver arriba.

**Nota.** Se vuelve bloqueante al abrir el Descubrimiento. ⚠️ **Pero ya no es el camino
crítico entero:** `TA-0016` bloquea el Gate 1 —escala numérica en `§24` sin ningún umbral—
**se decida lo que se decida en `T-013`**.

---

### `DT-007` · `CLAUDE.md` no existe

> **`Implementada` el 2026-08-26 (`T-007`).** `CLAUDE.md` existe en la raíz y recoge la
> asignación concreta: **el veredicto de un Gate lo emite la auditora, nunca la ejecutora**,
> junto con las reglas duras y el protocolo de persistencia. Con esto, `TA-0006` puede
> ejecutarse: al sacar la asignación del canónico ya hay dónde dejarla.

**Qué se debe.** El esquema de dos terminales —quién ejecuta, quién audita, quién declara los
Gates— **no está escrito en ningún archivo del repo**. Vive solo en la conversación.

**Por qué importa.** `TA-0006` exige mover ahí la asignación concreta al reformular §32 de
forma agnóstica. Sin `CLAUDE.md`, esa asignación se perdería al sacarla del canónico.

**Qué la salda.** `T-007` — hecha.

---

### `DT-011` · La cita de A.3 no está verificada del todo

**Qué se debe.** Verificando `A.3` del Anexo A —a raíz de que «`005` queda superado en este
punto» aparezca en tres sitios (§10, `A.1`, `A.3`)— aparecen dos defectos en su **cita**:

1. **El rango `010 §17–§31` sobrepasa por una sección.** `010 §31` es «Estado actual de la
   metodología», un recuento de cierre cuya primera mitad es **taxonomía**, no evaluación. El
   bloque de evaluación va de §17 a §30.
2. **«`005 §11` (dos párrafos)» es falso como medida.** Medido sobre
   `005_vertical.md:190–201`: **4 líneas de prosa y 7 viñetas**. Regla dura 7 — el número no
   se corrió.

**Lo sustantivo sí se verificó y se sostiene.** `010 §17–§30` cubre todo lo que dice
`005 §11`: sponsor que observa sin responder (§22), selección de usuarios representativos
(§23), evidencia observable sobre opinión (§19, §25), tarea concreta (§20), registro de
dificultades y observaciones (§21, §28), no sesgo (§30). Al dar `005 §11` por superado **no se
pierde contenido normativo**. `A.3` no es un segundo H-01.

**Por qué se aplazó.** Fuera del alcance de `TA-0001` (P-4). Son hallazgos nuevos sobre el
canónico, y el canónico es material que audita la otra terminal: corregirlos por cuenta propia
saltaría el circuito de `RES-008`.

**Qué la salda.** Que el usuario decida entre corregir la cita aquí, o trasladarla a la
auditora como hallazgo nuevo para que emita `TA`.

**Qué pasa si no se salda.** Poco, y ese es el riesgo: son defectos cosméticos sobre una
resolución correcta, así que nada se rompe. Pero es el mismo patrón de `L-008` —el anexo, que
nadie lee, dice cosas que nadie comprobó— y la próxima vez puede tocar una resolución que sí
importe.

---

### `DT-012` · `tools/mkindex.py` puede no escribir de forma atómica

**Qué se debe.** Pasar la escritura de `mkindex.py` a volcado atómico.

✅ **Comprobado, no es sospecha.** `tools/mkindex.py:95` escribe con
`f.write_text(txt, encoding="utf-8")`, que abre en modo `'w'` y **trunca al abrir**. Un fallo a
mitad de corrida trunca archivos de `_persistence/` — y como la herramienta recorre los siete,
no truncaría uno: truncaría el que estuviera en curso, con los ya procesados salvados y los
siguientes intactos.

**Por qué se aplazó.** Se detectó al final de la sesión, a raíz de `L-009`, y tocar la
herramienta que genera todos los índices no es un cambio para hacer con prisa ni sin pedirlo.

**Qué la salda.** Sustituir la línea 95 por volcado en `.tmp` seguido de `os.replace`.

**Qué pasa si no se salda.** Riesgo bajo de frecuencia y alto de impacto: la corrida es
rutinaria y se ejecuta al final de cada sesión, justo cuando el trabajo aún no está
commiteado y no hay red de `git`.

> 🔑 **Ya ocurrió, dos veces, en `S-005`** — no en `mkindex.py`, sino en un script equivalente
> escrito ad hoc para editar `tasks.md`. `_persistence/tasks.md` y `_persistence/lessons.md`
> quedaron truncados a 0 bytes al abrirse en modo escritura antes de que el contenido nuevo
> estuviera listo; se recuperaron con `git checkout --` porque el árbol estaba commiteado
> (`L-014`). Confirma el riesgo que esta entrada describe: **la mitigación no es solo para
> `mkindex.py`**, es para cualquier script que reescriba un archivo de `_persistence/`.

---

### `DT-013` · `progress.md` §6 («Mapa de archivos») no incluye `_temp/`, `_phases/` ni `_templates/`

**Qué se debe.** El árbol de ejemplo en `progress.md` §6 dice estar tomado «tras `D-04` y
`D-05`» y no lista `_temp/` (nuevo en `S-005`) ni `_phases/` y `_templates/` (aportados por el
usuario en `S-005`, sin decidir).

🚨 **Ampliado el 2026-08-27, tras el barrido que sugirió la auditoría `0005`: son cuatro, no
tres.** Contrastado el mapa contra `git ls-files`, **`_guide/` también falta**, y no tiene nada
que ver con `T-013`: existe desde `S-003` por `D-09` y `T-023`, está seguido por git y es una
de las tres capas que `GUIDE.md` §0 declara. Llevaba dos sesiones ausente del mapa sin que
nadie lo notara — **incluida la sesión que escribió esta misma deuda mirando ese mismo
árbol**.

🔑 Es el patrón de `L-013` otra vez: se miró el mapa para ver **qué sobraba por decidir**, no
para comprobar **qué faltaba**. Un inventario contra lo que uno tiene en la cabeza encuentra lo
que uno ya sospechaba.

**Por qué se aplazó.** Se detectó al cerrar `S-005`. `_phases/` y `_templates/` **no están
decididos** todavía (ver `T-013`, `D-12`), así que incluirlos en el mapa sería normalizar por
la puerta de atrás algo que el usuario no ha resuelto. `_temp/` sí existe y es estable
mientras dure `D-12`, y sí podría añadirse sin ese problema.

**Qué la salda.** Al resolverse `T-013`, actualizar el árbol de §6 completo. **`_guide/` no
espera a nadie: no depende de `T-013` y debe añadirse ya.** `_temp/` también puede añadirse de
forma aislada, porque es estable mientras dure `D-12`.

**Qué pasa si no se salda.** Bajo impacto: es un mapa de referencia, no un mecanismo del que
dependa nada. Pero un mapa que no refleja el árbol real deja de usarse para orientarse, que es
su único trabajo.
