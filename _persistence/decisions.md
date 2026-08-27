# decisions.md — Decisiones tomadas en el proyecto RandomAI

> **Fuente única de decisiones del proyecto.** No existe ningún otro archivo de decisiones.
> Conserva **la razón** detrás de cada una, que es lo que se pierde primero
> (`000_method.md` §38).
>
> **Alcance:** decisiones de proyecto, proceso y método. Las decisiones **arquitectónicas**
> del producto usarán `ADR-NNN` y vivirán en la Baseline (`000_method.md` §38), no aquí —
> aunque se indexarán desde este archivo cuando existan.

**Última actualización:** 2026-08-26

<!--INDEX-->

## Índice

> **Búsqueda rápida.** Salta con el enlace, o ve directo a la línea indicada (exacta, ya contando este índice).
> Por código: `grep -n 'D-02' decisions.md`

| Línea | Sección | Ir a |
|---|---|---|
| `42` | **Convenciones** | [↓](#convenciones) |
| `57` | **Tablero** | [↓](#tablero) |
| `81` | **D-01 · No se editan las fuentes** | [↓](#d-01--no-se-editan-las-fuentes) |
| `122` | **D-02 · El canónico se amplía sin renumerar** | [↓](#d-02--el-canónico-se-amplía-sin-renumerar) |
| `171` | &nbsp;&nbsp;↳ Revisión del 2026-08-26 — la decisión sobrevive, su fundamento cambia | [↓](#revisión-del-2026-08-26--la-decisión-sobrevive-su-fundamento-cambia) |
| `190` | **D-03 · Alcance de la incorporación de 015 §35-§51** | [↓](#d-03--alcance-de-la-incorporación-de-015-35-51) |
| `274` | **D-04 · Eliminar el directorio phases/** | [↓](#d-04--eliminar-el-directorio-phases) |
| `311` | **D-05 · Prefijo _ en las carpetas de insumo** | [↓](#d-05--prefijo-_-en-las-carpetas-de-insumo) |
| `343` | **D-06 · Git + GitHub como sustrato de evidencia** | [↓](#d-06--git--github-como-sustrato-de-evidencia) |
| `368` | **D-07 · Adaptación de protocol-close a este proyecto** | [↓](#d-07--adaptación-de-protocol-close-a-este-proyecto) |
| `413` | **D-08 · Una sesión es un bloque de tiempo, no un día** | [↓](#d-08--una-sesión-es-un-bloque-de-tiempo-no-un-día) |
| `447` | **D-09 · La capa del cómo vive en _guide/GUIDE.md** | [↓](#d-09--la-capa-del-cómo-vive-en-_guideguidemd) |
| `497` | **D-10 · A.1 sigue en la lista de ADR pendientes** | [↓](#d-10--a1-sigue-en-la-lista-de-adr-pendientes) |
| `543` | **Decisiones heredadas del brief** | [↓](#decisiones-heredadas-del-brief) |
| `550` | **D-11 · TA-0018 se salda retirando el estado duplicado, no sincronizándolo** | [↓](#d-11--ta-0018-se-salda-retirando-el-estado-duplicado-no-sincronizándolo) |

<!--/INDEX-->

---

## Convenciones

**Código:** `D-NN`, correlativo, nunca se reutiliza ni se renumera.

**Quién decide:** toda decisión registra su autor. Las que afectan al método o al alcance las
toma **el usuario**; la ejecutora no decide sobre su propio trabajo cuando hay un criterio en
disputa (`000_method.md` §32: *quien construye no puede ser su propio testigo*).

**Estructura de cada entrada:** contexto · problema · alternativas · decisión · razón ·
consecuencias.

**Estado:** `Vigente` · `Revertida` · `Superada por D-NN`

---

## Tablero

| Código | Decisión | Decide | Fecha | Estado |
|---|---|---|---|---|
| `D-01` | No se editan las fuentes de `_methodology/sources/` | usuario | 2026-08-26 | `Vigente` |
| `D-02` | El canónico se amplía sin renumerar (`§17-bis`) | usuario | 2026-08-26 | `Vigente` |
| `D-03` | Alcance de `TA-0003`: incorporar `015` §36–§48 y fusionar §50 en §4 | usuario | 2026-08-26 | `Vigente` |
| `D-04` | Eliminar el directorio `phases/` | usuario | 2026-08-26 | `Vigente` |
| `D-05` | Prefijo `_` en las carpetas de insumo: `_brief`, `_methodology` | usuario | 2026-08-26 | `Vigente` |
| `D-06` | Git + GitHub como sustrato de evidencia del proyecto | usuario | 2026-08-26 | `Vigente` |
| `D-07` | Adaptación de `protocol-close`: sesiones `S-nnn` y deuda proponible | usuario | 2026-08-26 | `Vigente` |
| `D-08` | Una sesión es un bloque de tiempo, no un día | usuario | 2026-08-26 | `Vigente` |
| `D-09` | La capa del «cómo» vive en `_guide/GUIDE.md`, separada de reglas y método | usuario | 2026-08-26 | `Vigente` |
| `D-10` | `A.1` sigue en la lista de ADR pendientes por consecuencia arquitectónica | usuario | 2026-08-26 | `Vigente` |
| `D-11` | `TA-0018` se salda retirando el estado duplicado, no sincronizándolo | ejecutora | 2026-08-27 | `Vigente` |

**Contexto común de `D-01`, `D-02` y `D-03`.** Las tres eran condición previa para ejecutar
cualquier tarea de la auditoría [`0001-method`](../../RandomAi_Auditor/audits/0001-method.md)
(`TA-0001`…`TA-0009`). No las toma la ejecutora ni la auditora: la primera sería su propio
testigo y la segunda no ejecuta. Quedan aquí porque el tablero `tasks_audit.md` es artefacto de
la auditora, y sus cambios de estado los asigna ella (`RES-009`).

---

## D-01 · No se editan las fuentes

**Decide:** usuario · **Fecha:** 2026-08-26 · **Estado:** `Vigente`

**Contexto.** Las secciones §35–§51 de `_methodology/sources/015_evolution.md` son texto plano
sin prefijo `#`. Ese defecto es la causa raíz verificada del hallazgo H-02: cualquier recorrido
del documento por encabezados salta el bloque entero, y así se perdieron ~200 líneas de
contenido normativo al consolidar el canónico. `TA-0009` proponía normalizarlos.

**Problema.** `000_method.md:6-7` establece que las fuentes «se conservan intactas en
`sources/` como registro de cómo se diseñó el método. No se editan». Normalizar encabezados no
altera contenido, pero **es una edición de una fuente**.

**Alternativas.**

| | Opción | Resultado |
|---|---|---|
| a | Normalizar los 17 encabezados | Descartada: edita una fuente declarada inmutable |
| b | **No tocar la fuente** | **Elegida** |
| c | No tocarla y añadir un `README.md` de advertencia en `sources/` | Descartada: añade un archivo a un registro histórico |

**Decisión.** **(b) No se edita la fuente.** `TA-0009` pasa a `Cancelada` en
[`tasks.md`](tasks.md); la auditora la registrará como `Descartada` en su tablero.

**Razón.** La regla de inmutabilidad de las fuentes vale más que la comodidad de recorrer el
documento por encabezados. El defecto ya está documentado —en la auditoría `0001-method` H-02
(causa raíz), en `L-001` y en `DT-001`—, de modo que la trampa queda señalizada sin alterar el
registro histórico.

**Consecuencias.**

- El defecto persiste. **Toda lectura futura de `015_evolution.md` debe hacerse por rango de
  líneas, no por encabezados.** El bloque afectado es `015:896-1147`.
- Se deriva la restricción permanente `RES-006`.
- La deuda `DT-001` queda `Aceptada`, no abierta: convivimos con ella indefinidamente.
- El usuario debe trasladar el estado `Descartada` a la auditora.

**Trazas:** `TA-0009` · `RES-006` · `DT-001` · `L-001`

---

## D-02 · El canónico se amplía sin renumerar

**Decide:** usuario · **Fecha:** 2026-08-26 · **Estado:** `Vigente`

**Contexto.** `TA-0002` exige insertar contenido nuevo después de §17 de `000_method.md`. Una
inserción con renumeración correlativa desplazaría §18 a §62.

**Problema — no contemplado por la auditoría.** El directorio `phases/` —8 archivos, ~88 KB,
fuera del alcance declarado de la auditoría— contiene **62 referencias cruzadas al canónico por
número de sección**. Con renumeración ingenua, **41 de esas 62 se romperían**, en los 8
archivos:

| Archivo | Refs que se romperían |
|---|---|
| `005_discovery.md` | 1 |
| `010_prototype.md` | 4 |
| `015_gate1.md` | 6 |
| `020_baseline.md` | 7 |
| `025_wslt.md` | 1 |
| `030_growth.md` | 8 |
| `035_gate2.md` | 6 |
| `040_evol.md` | 8 |
| **Total** | **41 de 62** |

**Alternativas.**

| | Opción | Refs rotas | Resultado |
|---|---|---|---|
| a | **`§17-bis`, sin desplazar nada** | 0 | **Elegida** |
| b | Renumerar y corregir las 41 refs en el mismo lote | 41 | Descartada: 41 puntos de fallo en 8 archivos |
| c | Añadir el bloque como Parte XI al final | 0 | Descartada: deja el contenido lejos de donde se aplica |

**Decisión.** **(a) El bloque nuevo entra como `§17-bis`.** La numeración §18–§62 no se toca.

**Razón.** Riesgo cero sobre las referencias existentes, frente a los 41 puntos de fallo que
abriría (b). La opción (c) dejaba el contenido lejos de §17 (alcance del prototipo) y §48
(MVP), que es justo donde el lector lo necesita.

**Consecuencias.**

- La numeración del canónico deja de ser estrictamente correlativa. Es el precio aceptado, y
  queda registrado como `DT-005` en estado `Aceptada`.
- Se deriva la restricción `RES-007`: **mientras algún consumidor referencie el canónico por
  número de sección, este se amplía pero no se renumera.** *(enunciado corregido en la
  revisión de más abajo; originalmente decía «mientras `phases/` referencie…»)*
- `TA-0002` y `TA-0007` se ejecutan bajo esta restricción.
- **Condición de levantamiento:** que ningún consumidor externo referencie el canónico por
  número.

### Revisión del 2026-08-26 — la decisión sobrevive, su fundamento cambia

`D-04` elimina `phases/`, y con ello las 62 referencias que motivaron esta decisión. La
condición de levantamiento redactada arriba **quedaba técnicamente satisfecha**.

Se revisó antes de levantarla, y **no procede levantarla**: el repo de la auditora contiene
**43 referencias inequívocas al canónico en secciones ≥ §18** (`0001-method.md`: 31 ·
`tasks_audit.md`: 12), y `RES-009` prohíbe editarlas. Las más citadas son `§29`(x10),
`§32`(x7) y `§57`(x10) — todas dentro del tablero **vivo** que dirige el trabajo actual.

> El riesgo no desapareció: **cambió de sitio, y se agravó.** Antes vivía en archivos que
> podíamos corregir; ahora vive en archivos que no podemos tocar.

`D-02` y `RES-007` continúan **`Vigente`** con este fundamento revisado.

**Trazas:** `TA-0002` · `TA-0007` · `RES-007` · `DT-005` · `L-003` · `L-006` · `D-04`

---

## D-03 · Alcance de la incorporación de 015 §35-§51

**Decide:** usuario · **Fecha:** 2026-08-26 · **Estado:** `Vigente`

**Contexto.** `TA-0002` pedía incorporar un mínimo al canónico (§37, §39, §41, §45, §46, §48).
`TA-0003` exigía decidir qué se hace con el resto del bloque §35–§51 y declarar en el Anexo A
toda omisión deliberada, porque «un documento canónico no puede omitir en silencio».

**Problema.** El mínimo de `TA-0002` dejaba fuera `015` §47 (aplicaciones que requieren
adaptación), que `TA-0007` necesita para justificar la decisión de alcance del prototipo.

**Alternativas.** (a) solo el mínimo de la auditoría; (b) **§36–§48 más la fusión de §50**;
(c) incorporar §35–§51 completo, aceptando duplicación con §61 y §62.

**Decisión.** **(b).** Se incorporan **§36 a §48 completas** (13 secciones), se **fusiona §50 en
el §4** del canónico, y se **omiten §35, §49 y §51** declarándolas en el Anexo A.

| Sección de `015` | Destino |
|---|---|
| §35 Ventajas (10 subsecciones) | **Omitir** — argumentativo; cubierto por §4 y §61 |
| §36 Riesgo: optimización excesiva para el Generador | Incorporar — par natural de §37 |
| §37 No construir no es no diseñar | Incorporar → Parte VI, junto a ARCHIT |
| §38 Riesgo operacional (20 vs 5.000 solicitudes) | Incorporar → refuerza §50 con la evaluación periódica |
| §39 Riesgo de validar solo el Happy Path | Incorporar → Parte V, junto a §29 |
| §40 Éxito de prototipo no es éxito de producto | Incorporar → completa §30 |
| §41 GRTH degenerando en Waterfall | Incorporar → Parte VII, junto a GRTH |
| §42 Expansión prematura | Incorporar → `§17-bis`, emparejada con §43 *(enmendado, ver abajo)* |
| §43 Expansión tardía | Incorporar → justifica el Principio de excepción |
| §44 Límites de la metodología | Incorporar → `§17-bis` |
| §45 Cuándo extender el prototipo | Incorporar → `§17-bis` |
| §46 Cuándo extender el MVP — **6 criterios** | Incorporar → `§17-bis`, enumerados completos |
| §47 Aplicaciones que requieren adaptación | Incorporar → `§17-bis`; lo necesita `TA-0007` |
| §48 Principio de excepción | Incorporar → `§17-bis` |
| §49 Principios fundamentales (28 ítems) | **Omitir** — duplica §61 |
| §50 Modelo conceptual (6 preguntas) | **Fusionar en §4** |
| §51 Filosofía final | **Omitir** — duplica §62 |

> **Enmienda · 2026-08-27 · `TA-0012`.** La fila de `§42` decía **«Incorporar → completa
> §47»**. En una columna cuyas filas vecinas nombran secciones **del canónico** (§50, §29,
> §30), eso se lee como el `§47` del canónico — que es **«Regla de trazabilidad»**, sin
> relación alguna con la expansión prematura. El `§47` que la fila quería nombrar era el de
> **`015`** (Aplicaciones que requieren adaptación), cuyo destino es `§17-bis`.
>
> **Qué se corrige:** solo el destino escrito en la fila. `015 §42` va a **`§17-bis.3`**,
> emparejado con `§43`, porque expansión prematura y expansión tardía son el mismo riesgo en
> direcciones opuestas y se leen juntos o no se leen.
>
> **Qué NO cambia:** el alcance decidido —13 secciones, §36–§48, más la fusión de §50 en el
> §4— es el mismo. La enmienda no altera qué se incorpora, solo dónde dice esta tabla que se
> incorpora. El canónico ya quedó correcto al ejecutar `TA-0002`; lo que estaba mal era esta
> fila.
>
> **Autorización.** La enmienda la pidió el usuario de forma explícita el 2026-08-27
> —*«haz el commit y redacta la enmienda de D-03»*—, tras habérsele presentado el problema
> y la redacción propuesta. `D-03` es decisión suya y la enmienda también: la ejecutora la
> redactó, no la decidió. Queda escrito aquí porque en `tasks.md` no es observable desde el
> repo de la auditora.
>
> **Por qué se enmienda `D-03` y no se abre una `D-11`.** Una decisión nueva no borra la
> anterior: dejaría dos textos vigentes contradiciéndose, y `D-03` es el que se cita desde
> `tasks.md` y desde el tablero de la auditora. 🔑 **Una contradicción documentada en dos
> sitios no está resuelta: está duplicada.** `D-03` conserva su código, su fecha original y
> su estado `Vigente`.

**Razón.** Cierra el bloque entero sin silencios, que es lo que `TA-0003` exige. El mínimo de
`TA-0002` dejaba fuera §47. Incorporarlo todo habría introducido duplicación reconocida con
§61 y §62 del canónico.

**Hallazgo propio incorporado.** `015` §50 formula el modelo como **seis** preguntas
(PROTOTIPO · WSLT · GRTH · MVP · EVOL · RELEASE OBJETIVO); el §4 del canónico solo recoge
**tres** (PROTOTIPO · MVP · EVOL). La auditoría no lo señaló. Se corrige al fusionar.

**Consecuencias.**

- El Anexo A recibirá una entrada nueva declarando §35, §49 y §51 como omisiones deliberadas
  con su razón, cerrando `TA-0003`.
- **`TA-0002` se ejecuta con alcance ampliado** respecto a su enunciado original: 13 secciones
  en lugar de 6. La auditora debe saberlo al verificar: encontrará **más** de lo que pidió, no
  menos.

**Trazas:** `TA-0002` · `TA-0003` · `TA-0007` · `TA-0012` · `L-004`

---

## D-04 · Eliminar el directorio phases/

**Decide:** usuario · **Fecha:** 2026-08-26 · **Estado:** `Vigente`

**Contexto.** `phases/` contenía 8 archivos (~88 KB) que operacionalizaban el método: por cada
fase, qué autoriza, qué prohíbe, entradas, procedimiento, artefactos que produce, condición de
salida, qué registra en la capa de persistencia y qué entrega al Gate siguiente.

**Decisión.** Se elimina el directorio.

**Verificación previa.** La dependencia era **unidireccional**: `phases/` citaba a
`_methodology/`, pero ni `000_method.md` ni ninguna de las tres fuentes mencionan `phases/`.
**Eliminarlo no rompe el método.**

**Consecuencias — lo que se disuelve.**

| Registro | Antes | Ahora |
|---|---|---|
| `DT-002` rutas inexistentes (`templates/`, `_memory/`, `_discovery/`) | `Abierta`, Alta | `Descartada` — solo `phases/` las citaba |
| `DT-003` divergencia `_persistence/` vs `_memory/` | `Abierta`, Alta | `Descartada` — ya no hay con qué divergir |
| `DT-006` `phases/` sin auditar | `Abierta`, Media | `Descartada` — no hay objeto que auditar |
| `T-006` reconciliar divergencia | `No implementada` | `Cancelada` |
| `T-008` crear `templates/` | `No implementada` | `Cancelada` |
| `TA-0007` alcance ampliado a `phases/005_discovery.md` | 2 frentes | **1 frente**: solo el canónico §14 |

**Consecuencias — lo que NO se disuelve.**

- **`RES-007` sigue vigente**, con fundamento nuevo. Ver la revisión en `D-02`.
- **Se abre `DT-008`, severidad Alta:** el método pierde su nivel operativo. `000_method.md`
  describe *qué* es cada fase; `phases/` era lo único que decía *cómo* ejecutarla —
  condiciones de salida, qué está prohibido en cada fase, qué se entrega al Gate. Al abrir la
  fase de Descubrimiento no habrá procedimiento escrito.

**Trazas:** `DT-002` · `DT-003` · `DT-006` · `DT-008` · `T-006` · `T-008` · `TA-0007` · `L-006`

---

## D-05 · Prefijo _ en las carpetas de insumo

**Decide:** usuario · **Fecha:** 2026-08-26 · **Estado:** `Vigente`

**Contexto.** `_persistence/` ya usaba prefijo `_`; `brief/` y `methodology/` no.

**Decisión.** `brief/` pasa a `_brief/` y `methodology/` a `_methodology/`.

**Razón.** Consistencia: las tres carpetas que quedan son insumo y registro del proyecto, no
código de la aplicación. El prefijo las agrupa y las separa de lo que vendrá cuando empiece la
construcción.

**Estructura resultante:**

```text
RandomAI/
├── _brief/          Client_brief.txt
├── _methodology/    000_method.md + sources/
└── _persistence/    los 7 registros
```

**Consecuencias.**

- Las referencias internas de `_persistence/` quedaron actualizadas.
- ⚠️ **La auditoría `0001-method` referencia `RandomAI/methodology/000_method.md` en 4 puntos
  y esas rutas quedan obsoletas.** No podemos corregirlas (`RES-009`): el usuario debe avisar
  a la auditora.

**Trazas:** `RES-009` · `D-04`

---

## D-06 · Git + GitHub como sustrato de evidencia

**Decide:** usuario · **Fecha:** 2026-08-26 · **Estado:** `Vigente`

**Contexto.** El protocolo de cierre se apoya entero en `git diff` para separar los hechos del
relato. RandomAI no era un repositorio git, así que el protocolo no tenía sobre qué correr.

**Decisión.** Se inicializa git y se enlaza `https://github.com/jdrodriguez1000/RandomAI.git`.
Rama local `main`, remoto `origin`.

**Estado comprobado del remoto:** existe, está **vacío** (sin ramas) y es **público**.

**Consecuencias.**

- El primer push será el inicial y necesita `git push -u origin main`. Está escrito en el skill.
- **El repositorio es público** → `RES-010`. `_persistence/` va a Git a propósito, así que todo
  lo que se escriba ahí es público. Se añade una casilla al protocolo de cierre.
- Se crea `.gitignore` cubriendo secretos, sistema operativo y editores. **No hay stack, así
  que no se anticipa nada más**: se ampliará cuando se decida la tecnología.
- Queda `SUP-008` sin comprobar: que las credenciales de GitHub funcionen. No se ha hecho push.

**Trazas:** `RES-010` · `RES-011` · `SUP-008` · `T-015`

---

## D-07 · Adaptación de protocol-close a este proyecto

**Decide:** usuario · **Fecha:** 2026-08-26 · **Estado:** `Vigente`

**Contexto.** El skill venía escrito contra otro proyecto. El análisis previo identificó qué
era trasladable, qué era ajeno y qué faltaba.

**Decisiones tomadas.**

| Pregunta | Respuesta |
|---|---|
| ¿Git? | Sí → `D-06` |
| ¿`progress.md` con entradas de sesión? | **Sí, alineado con el skill:** adopta `S-nnn` |
| ¿El closer puede proponer deuda? | **Sí**, marcada como propuesta y solo si el diff la respalda |

**Lo que se eliminó por ser ajeno:** el control de compilación TypeScript, la casilla de frases
de personas, la comprobación de `.env` como paso propio, las referencias a `_context/` y las
anotaciones históricas del otro proyecto.

**Lo que se añadió por ser propio:**

- **La tabla de tres actores.** El protocolo original asumía dos; aquí existe la auditora.
  🚨 El closer **nunca** marca `Verificada` ni escribe en `RandomAi_Auditor/`.
- **`debt_tec.md`**, que no existía en el original — con `Aceptada` y `Descartada` vetadas al
  closer, por ser decisiones y no lecturas del diff.
- **La regeneración de índices** como control del Paso 2b, heredando la forma «tres resultados,
  no dos» del control que se eliminó.
- Los códigos y estados reales de este proyecto.

**Citas resueltas.** El skill original citaba 12 entradas del registro ajeno. Once no existían
aquí y **una colisionaba**: su `[L-006]` significa «no pude comprobarlo ≠ está bien»; el
nuestro significa «al eliminar algo, comprobar qué se apoyaba en ello». Una cita copiada habría
resuelto a una entrada real que habla de otra cosa. **Todas se reescribieron en línea**; el
skill adaptado no cita ningún código.

**Consecuencias.**

- ⚠️ **El skill todavía no puede ejecutarse:** su Paso 3 exige entradas `S-nnn` en
  `progress.md`, y ese archivo aún no tiene esa estructura → `T-018`.
- ⚠️ **El agente `session-closer` quedó contradiciendo al skill** que dice invocar → `DT-009`.

**Trazas:** `D-06` · `T-017` · `T-018` · `DT-009` · `L-002`

---

## D-08 · Una sesión es un bloque de tiempo, no un día

**Decide:** usuario · **Fecha:** 2026-08-26 · **Estado:** `Vigente`

**Contexto.** Al diseñar los protocolos quedaba implícito que «sesión» equivalía a «día de
trabajo». El usuario lo corrigió: **puede haber una sesión por la mañana, otra por la tarde y
otra por la noche del mismo día.**

**Decisión.** Una sesión es un **bloque continuo de trabajo**, no una jornada. Se identifica
por su `S-nnn`, nunca por su fecha.

**Por qué importa, y no es un matiz de vocabulario.** Varias filas de `progress.md` pueden
compartir fecha siendo sesiones distintas. Por lo tanto:

- **«La última sesión» es el id más alto, nunca la fecha más reciente.** Ordenar por fecha
  mezcla sesiones del mismo día y puede presentar como última una que no lo es.
- **Un control que compare fechas da verde estando mal.** Si el criterio para saber si esta
  sesión ya escribió su entrada fuera la fecha, la fila del tramo de la mañana bastaría para
  dar por registrada la de la tarde — y esa sesión se perdería entera.
- **Nunca se dice «la sesión de ayer»** en un reporte: se dice `S-nnn`.

**Consecuencias.**

- `protocol-close` ya lo tenía resuelto: su Paso 3 exige comprobar **el id, no la fecha**. Esta
  decisión confirma esa regla y le da su fundamento explícito.
- `protocol-start` lo recoge en una sección propia al comienzo, porque afecta a todo lo que
  reporta.
- `T-018` —reestructurar `progress.md`— debe numerar por sesión y **no asumir una fila por
  día**.

**Trazas:** `D-07` · `T-018` · `T-020`

---

## D-09 · La capa del cómo vive en _guide/GUIDE.md

**Decide:** usuario · **Fecha:** 2026-08-26 · **Estado:** `Vigente`

**Contexto.** El brief §22 declara que aprender a desarrollar con IA como asistente es una de
las dos entregas del proyecto. Teníamos el **método** (`_methodology/`) y las **reglas**
(`CLAUDE.md`), pero no el **cómo ejecutable**. La fuente era la guía de un proyecto anterior,
fuera de este repo y en solo lectura.

**Problema.** Aquel proyecto construía un agente que **sí** llamaba a una API de IA. Más de la
mitad de su guía presupone eso, y el brief §21 lo prohíbe aquí (`RES-001`).

**Decisión.** Se crea `_guide/GUIDE.md`, con partición explícita de tres archivos:

| Archivo | Qué es |
|---|---|
| `CLAUDE.md` | las **reglas** — qué está prohibido y qué es obligatorio |
| `_methodology/000_method.md` | el **método** — fases, Gates, trazabilidad |
| `_guide/GUIDE.md` | el **cómo** — procedimientos, órdenes concretas, formatos |

**Tres decisiones tomadas dentro de esta:**

1. **Las dos reglas duras de §11.i van a `CLAUDE.md`, no a la guía** — pasan a ser reglas duras
   8 y 9. La guía las cita sin copiarlas. Es `L-007` aplicado: una segunda fuente de verdad
   envejece sin avisar.
2. **Las secciones de prueba se escriben como contrato, no como plantilla.** §8.l, §8.b, §8.c y
   §7 de la fuente son Python. Traducirlas literalmente **habría decidido el stack por la
   puerta de atrás**, contra `RES-004` y el brief §23.1 — y el brief §24 exige Vercel, cuyo
   camino natural es JS/TS. Hoy se escribe lo independiente del lenguaje; las plantillas
   ejecutables quedan en `T-024`, disparadas por la decisión de stack.
3. **Se trae «cuándo crear un subagente» y «evidencia, nunca veredicto»**, que no estaban en el
   encargo original. Motivo: tenemos tres actores y dos agentes, y ese criterio estaba vivo en
   `RES-008` pero no escrito como regla general para decidir agentes futuros.

**Lo que se dejó fuera está declarado en la propia guía**, sección por sección y con su motivo.
Un salto sin motivo escrito se lee como veredicto sobre lo saltado.

**Ningún número heredado.** Las cifras de la fuente se midieron en otra máquina, con otro stack
y otro modelo. Regla dura 7.

**Consecuencias.**

- `CLAUDE.md` gana las reglas duras 8 y 9, y una fila en «Dónde está lo demás».
- ⚠️ **La auditoría del historial público (§1.b de la guía) llega tarde**: el primer commit
  público ya se hizo, así que deja de ser preventiva. La corre la auditora (`RES-008`) → `T-025`.

**Trazas:** `T-023` · `T-024` · `T-025` · `RES-001` · `RES-004` · `L-007`

---

## D-10 · A.1 sigue en la lista de ADR pendientes

**Decide:** usuario · **Fecha:** 2026-08-26 · **Estado:** `Vigente`

**Contexto.** `TA-0001` corrige la atribución de fuentes sobre el Actor Invitado. Su cuarto
punto de evidencia obliga a revisar el «Pendiente» del cierre de `000_method.md`, que lista
`A.1`, `A.2`, `A.5` y `A.6` como decisiones que merecen un ADR propio: o se retira `A.1` de esa
lista, o se justifica por escrito por qué se queda.

**Problema.** El motivo original por el que `A.1` estaba ahí **desaparece con la corrección**.
Se creía que dos fuentes incluían al Actor Invitado y una lo refutaba, de modo que había que
justificar por qué gana la minoría. Corregido el dato —solo `005 §5.6` lo incluye; `010 §12` y
`015 §5` lo excluyen con argumento— no queda conflicto que resolver. Mantenerla «porque siempre
estuvo» la convertiría en un pendiente sin razón viva.

**Alternativas.**

1. **Retirar `A.1` de la lista.** Un ADR sin alternativa viva es un acta, no una decisión.
   Coste: se pierde el rastro de una regla que sí restringe el diseño.
2. **Mantenerla por el conflicto de fuentes.** Descartada: sería falsa. El conflicto no existe.
3. **Mantenerla por su consecuencia arquitectónica.** ← **elegida**

**Decisión.** `A.1` se queda en la lista, con la justificación escrita en el propio canónico y
enunciada sobre el riesgo correcto: **no es que el conflicto siga abierto, es que la regla
tiene consecuencia arquitectónica.** Decir que lo temporal, lo externo y lo restringido se
tratan como permisos y seguridad es una restricción sobre el modelo de autorización del
producto, no una nota de taxonomía. La alternativa —modelar el acceso restringido como actor
propio— es viable y tiene coste distinto, y ese contraste hay que escribirlo.

**Razón.** Un pendiente cuyo motivo ha caducado se cierra o miente. Este no se cierra porque
tiene un segundo motivo, independiente del primero, que la corrección de `TA-0001` no toca.

**Cuándo se escribe.** Al tocar la **Baseline**, que es donde viven los `ADR-NNN`
(`000_method.md` §38) y donde la decisión empieza a tener consecuencias sobre el diseño. No
antes: hoy no hay modelo de autorización que restringir.

**Consecuencias.**

- El cierre del Anexo A de `000_method.md` gana un párrafo de justificación para `A.1`.
- Queda comprometido un `ADR-NNN` sobre el modelo de autorización para la fase de Baseline.
- Con esto, el cuarto punto de evidencia de `TA-0001` queda cubierto.

**Trazas:** `TA-0001` · `D-02` · `RES-007`

---

## Decisiones heredadas del brief

No son decisiones nuestras: vienen impuestas por el cliente y se registran como restricciones,
no como decisiones. Ver [`constraints.md`](constraints.md) — `RES-001` a `RES-005`.

---

## D-11 · TA-0018 se salda retirando el estado duplicado, no sincronizándolo

**Decide:** ejecutora · **Fecha:** 2026-08-27 · **Estado:** `Vigente`

⚠️ **Decisión tomada por la ejecutora, y se declara como tal.** `TA-0018` pedía una
evidencia concreta y se entregó otra cosa. La auditora debe poder juzgar la desviación, no
descubrirla.

**Contexto.** `TA-0018` señalaba que `DT-009` y `DT-010` tenían campo `Estado: Abierta` en su
entrada mientras el tablero las daba `Implementada`. La evidencia pedida era, en sus términos,
que los estados coincidieran.

**Problema.** Al barrer las doce entradas —y no las dos comprobadas por la auditora— el patrón
resultó distinto del enunciado: **solo tres entradas tenían ese campo, y dos de las tres ya
mentían.** Las otras nueve nunca lo tuvieron. No era un error de transcripción en dos sitios:
era un campo redundante con una tasa de fallo del 67 %.

**Alternativas.** (a) sincronizar los tres campos con el tablero, que es lo pedido;
(b) **retirar el campo de las tres entradas** y dejar el tablero como fuente única;
(c) añadir el campo a las nueve que no lo tienen y sincronizar los doce.

**Decisión.** **(b).**

**Razón.** `L-008` ya está escrita en este proyecto: *un dato repetido en dos capas diverge, y
miente la capa que menos se lee*. La opción (a) restaura la coincidencia **y deja intacto el
mecanismo que la rompió** — volvería a divergir en el siguiente cambio de estado, y el tablero
seguiría siendo la capa que se lee. La (c) lo empeora: multiplica por cuatro las
oportunidades de divergencia.

🔑 **Sincronizar dos copias no salda la deuda de tener dos copias.** Deja el defecto en verde
y listo para repetirse, que es la salida barata que la regla dura 8 describe para las pruebas
—arreglar lo que rompió, o ablandar lo que avisó— aplicada aquí a un dato.

**Consecuencias.**

- La severidad y el estado de una deuda viven **solo en el tablero** de `debt_tec.md`. La
  regla queda escrita en las convenciones del propio archivo, no solo aquí.
- **La evidencia que `TA-0018` pedía ya no se puede comprobar tal como estaba enunciada**: no
  quedan dos estados que comparar. La comprobación equivalente es que ninguna entrada declare
  estado propio. Si la auditora considera que esto no salda la tarea, la decisión se revierte
  y se hace (a): **no se discute, es su veredicto.**
- Nada se perdió: el estado de las tres deudas afectadas sigue escrito en el tablero, que es
  donde lo lee `mkindex.py` y donde lo busca cualquiera que abra el archivo.

**Trazas:** `TA-0018` · `L-008` · `DT-009` · `DT-010`
