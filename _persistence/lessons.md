# lessons.md — Lecciones aprendidas del proyecto RandomAI

> Lo que aprendimos **haciendo**, y que no estaba escrito en ningún documento. Será «la fuente
> más rica del proyecto» cuando haya producto vivo.
>
> Una lección no es una anécdota. Debe responder: **qué pasó**, **qué aprendimos** y
> **qué haremos distinto**. Sin la tercera parte, no es una lección.

**Última actualización:** 2026-08-26

<!--INDEX-->

## Índice

> **Búsqueda rápida.** Salta con el enlace, o ve directo a la línea indicada (exacta, ya contando este índice).
> Por código: `grep -n 'L-002' lessons.md`

| Línea | Sección | Ir a |
|---|---|---|
| `38` | **Convenciones** | [↓](#convenciones) |
| `46` | **Tablero** | [↓](#tablero) |
| `63` | **Detalle** | [↓](#detalle) |
| `65` | &nbsp;&nbsp;↳ L-001 · Leer 015_evolution.md por líneas, no por encabezados | [↓](#l-001--leer-015_evolutionmd-por-líneas-no-por-encabezados) |
| `81` | &nbsp;&nbsp;↳ L-002 · No repetir el canónico sin contrastarlo | [↓](#l-002--no-repetir-el-canónico-sin-contrastarlo) |
| `98` | &nbsp;&nbsp;↳ L-003 · Medir el impacto antes de renumerar | [↓](#l-003--medir-el-impacto-antes-de-renumerar) |
| `119` | &nbsp;&nbsp;↳ L-004 · El alcance declarado de una auditoría es su límite | [↓](#l-004--el-alcance-declarado-de-una-auditoría-es-su-límite) |
| `138` | &nbsp;&nbsp;↳ L-005 · Un fallo de formato puede perder contenido normativo | [↓](#l-005--un-fallo-de-formato-puede-perder-contenido-normativo) |
| `161` | &nbsp;&nbsp;↳ L-007 · Quien delega un procedimiento no puede llevar una copia encima | [↓](#l-007--quien-delega-un-procedimiento-no-puede-llevar-una-copia-encima) |
| `194` | &nbsp;&nbsp;↳ L-006 · Al eliminar algo, comprobar qué se apoyaba en ello | [↓](#l-006--al-eliminar-algo-comprobar-qué-se-apoyaba-en-ello) |
| `226` | &nbsp;&nbsp;↳ L-008 · Un dato repetido en dos capas diverge, y miente la que menos se lee | [↓](#l-008--un-dato-repetido-en-dos-capas-diverge-y-miente-la-que-menos-se-lee) |
| `269` | &nbsp;&nbsp;↳ L-009 · Escribir en el sitio destruye el original antes de saber si va a funcionar | [↓](#l-009--escribir-en-el-sitio-destruye-el-original-antes-de-saber-si-va-a-funcionar) |
| `303` | **L-010 · Una frase de cierre bien escrita es la forma más fácil de colar una regla inventada** | [↓](#l-010--una-frase-de-cierre-bien-escrita-es-la-forma-más-fácil-de-colar-una-regla-inventada) |

<!--/INDEX-->

---

## Convenciones

**Código:** `L-NNN`, correlativo, nunca se reutiliza.

**Categoría:** `Método` · `Proceso` · `Técnica` · `Producto` · `Negocio`

---

## Tablero

| Código | Lección | Categoría | Fecha |
|---|---|---|---|
| `L-001` | `015_evolution.md` debe leerse por rango de líneas, no por encabezados | Proceso | 2026-08-26 |
| `L-002` | No repetir afirmaciones del canónico sin contrastarlas con las fuentes | Método | 2026-08-26 |
| `L-003` | Contar **todas** las referencias entrantes antes de tocar una numeración | Proceso | 2026-08-26 |
| `L-004` | Una auditoría acota su alcance; lo que queda fuera sigue sin revisar | Proceso | 2026-08-26 |
| `L-005` | Un defecto de formato puede causar una pérdida de contenido normativo | Técnica | 2026-08-26 |
| `L-006` | Al eliminar algo, comprobar qué se apoyaba en ello, no solo qué contenía | Proceso | 2026-08-26 |
| `L-007` | Quien delega un procedimiento no puede llevar una copia encima | Proceso | 2026-08-26 |
| `L-008` | Un dato repetido en dos capas diverge, y miente la capa que menos se lee | Método | 2026-08-26 |
| `L-009` | Escribir en el sitio destruye el original antes de saber si va a funcionar | Técnica | 2026-08-26 |
| `L-010` | Una frase de cierre bien escrita es la forma más fácil de colar una regla inventada | Método | 2026-08-27 |

---

## Detalle

### `L-001` · Leer `015_evolution.md` por líneas, no por encabezados

**Qué pasó.** Las secciones §35–§51 de `015_evolution.md` (líneas 896–1147) están escritas como
texto plano, sin prefijo `#`. Cualquier recorrido del documento por encabezados las salta por
completo. Así se perdieron ~200 líneas de contenido normativo al consolidar el canónico
(hallazgo H-02).

**Qué aprendimos.** Un índice de encabezados **no es** un índice del documento. Solo es un
índice de lo que está bien formateado.

**Qué haremos distinto.** Antes de dar por leída una fuente, contrastar el número de líneas del
archivo contra el rango efectivamente leído. En esta fuente concreta, siempre por rango de
líneas. Ver `RES-006` y `DT-001` — el defecto **no se corrigió**, sigue ahí.

---

### `L-002` · No repetir el canónico sin contrastarlo

**Qué pasó.** Al resumir el método, la ejecutora repitió la afirmación del canónico de que
«005 y 015 incluían el Actor Invitado y 010 lo refutaba». Es falsa: `015:76` declara seis tipos
y `015:154` dice literalmente que el Actor Invitado no forma parte de la taxonomía. La
auditoría lo detectó (H-01); la ejecutora no.

**Qué aprendimos.** Un documento que se declara canónico invita a confiar en él, y esa
confianza es justamente lo que impide auditarlo. Leer el canónico **y** las fuentes no es
redundancia: es la única forma de detectar que el canónico se equivocó al citarlas.

**Qué haremos distinto.** Cuando un documento cite a otro que también tenemos delante,
comprobar la cita. Y en general: **verificar los hallazgos ajenos antes de aceptarlos, y los
propios antes de afirmarlos.** Es el mismo principio de `RES-008` aplicado a la lectura.

---

### `L-003` · Medir el impacto antes de renumerar

**Qué pasó.** La auditoría recomendó insertar una sección nueva después de §17 sin advertir que
`phases/` contenía 62 referencias cruzadas por número de sección. Una renumeración correlativa
habría roto **41 de ellas** en los 8 archivos de fase.

**Qué aprendimos.** En documentación con referencias cruzadas por número, la numeración **es
una interfaz pública**. Cambiarla es un cambio incompatible, no una mejora cosmética.

**Qué haremos distinto.** Antes de cualquier renumeración, contar las referencias entrantes —
**y no solo las que podemos corregir.** Se convirtió en la decisión `D-02` y en la restricción
`RES-007`.

**Ampliación del 2026-08-26.** Al eliminar `phases/` (`D-04`) las 62 referencias desaparecieron
y la restricción parecía poder levantarse. No: quedaban **43 referencias en el repo de la
auditora**, que `RES-009` nos impide editar. La lección se refina: **el inventario de
referencias entrantes debe cubrir también los repos que no controlamos**, que son justamente
los peligrosos.

---

### `L-004` · El alcance declarado de una auditoría es su límite

**Qué pasó.** La auditoría `0001-method` declaró como objeto `000_method.md` y lo auditó bien.
Pero `phases/` —8 archivos, ~88 KB que operacionalizaban el método— quedó sin revisar. Dos
consecuencias reales aparecieron ahí: el riesgo de las 62 referencias (`L-003`) y un segundo
frente para `TA-0007` en `phases/005_discovery.md`.

**Qué aprendimos.** Una auditoría correcta puede dejar riesgos abiertos sin equivocarse en
nada, simplemente porque estaban fuera de su alcance. **«Auditado» no significa «todo
auditado».**

**Qué haremos distinto.** Al recibir una auditoría, leer primero su §1 Alcance y preguntar
explícitamente qué quedó fuera.

**Nota del 2026-08-26.** `phases/` fue eliminado (`D-04`), así que la ampliación concreta ya no
procede. La lección sobrevive a su ejemplo: **«auditado» nunca significa «todo auditado».**

---

### `L-005` · Un fallo de formato puede perder contenido normativo

**Qué pasó.** Diecisiete encabezados sin `#` provocaron la omisión silenciosa de seis reglas
normativas del método, incluida una —los seis criterios de `015` §46— cuya ausencia **invirtió
una regla**: el canónico enunciaba «solo Generador» como absoluto cuando la fuente lo define
como regla con excepciones tasadas.

**Qué aprendimos.** El formato no es presentación. En documentos que se procesan por
estructura, **el formato es semántica**, y un fallo de formato puede cambiar lo que el
documento significa.

**Qué haremos distinto.** Tratar la consistencia estructural de los documentos del proyecto
como un requisito, no como estética. Aplicable a los artefactos que vengan: PRD, BDD, SPEC.

**Segunda aparición, 2026-08-26.** `tools/mkindex.py` indexó un `##` que estaba **dentro de un
bloque de código** —la plantilla de hallazgo de la guía— y lo ofreció como si fuera una
sección. El índice era técnicamente correcto y **mandaba al lector a un ejemplo creyendo que
iba a un apartado**. 🔑 La vuelta de tuerca: aquí el que confundió formato con semántica no fue
un humano, **fue nuestra propia herramienta**. Corregido: `headings()` salta los bloques
cercados. Una herramienta que genera índices también puede mentir, y hay que mirarla igual.

---

### `L-007` · Quien delega un procedimiento no puede llevar una copia encima

**Qué pasó.** Los dos agentes heredados —`session-closer` y `session-starter`— decían
«invoca la skill y síguela tal como está escrita», y **acto seguido repetían media parte del
procedimiento en su propio cuerpo**: comprobaciones concretas, orden de los pasos, comandos.

Cuando adaptamos los skills a este proyecto, esas copias quedaron desfasadas de golpe. El
agente de cierre seguía mandando comprobar una compilación de TypeScript que aquí no existe.

**Qué aprendimos.** Un agente que lleva el procedimiento duplicado **no delega: compite**. Y
ante la discrepancia gana la copia, porque la tiene más cerca — y la copia es siempre la más
vieja, porque el procedimiento se mantiene en el otro sitio.

> 🔑 **La duplicación no es redundancia útil: es una segunda fuente de verdad que envejece
> sin avisar.** Nadie la actualiza, porque quien edita el skill cree que ha terminado.

**Qué haremos distinto.** Reparto estricto y escrito dentro de cada archivo:

| Archivo | Contiene |
|---|---|
| **agente** | quién eres · qué **no** puedes hacer · a qué skill delegas |
| **skill** | qué hacer · en qué orden · con qué comandos · qué reportar |

Ni un paso ni un comando del procedimiento en el cuerpo de un agente. Si hace falta un
criterio, se busca en el skill.

📌 **Y un corolario que sí muerde.** `session-starter` no tiene `Write` ni `Edit` entre sus
`tools`. Su «solo lectura» **no depende de que se porte bien: la herramienta no está.** De
todas las reglas de este montaje, esa es de las poquísimas que no se pueden incumplir por
descuido. Cuando exista la opción de convertir una regla en una imposibilidad, se convierte.

---

### `L-006` · Al eliminar algo, comprobar qué se apoyaba en ello

**Qué pasó.** Al eliminar `phases/` la comprobación evidente era la de siempre: ¿alguien
depende de este directorio? La respuesta fue tranquilizadora — el método no lo menciona, la
dependencia era unidireccional, borrarlo no rompía nada.

Pero había una segunda pregunta, menos evidente y más importante: **¿qué decisiones nuestras
se justificaban en su existencia?** `D-02` y `RES-007` se apoyaban **enteramente** en las 62
referencias de `phases/`, hasta el punto de que su condición de levantamiento estaba redactada
como «si `phases/` deja de referenciar por número». Al borrarlo, esa condición quedaba
satisfecha por accidente, y la restricción se habría levantado sola.

Habría sido un error: quedaban 43 referencias equivalentes en el repo de la auditora, **que no
podemos editar**.

**Qué aprendimos.** Borrar algo no solo elimina lo que contiene: **puede satisfacer, sin que
nadie lo advierta, la condición de salida de una decisión tomada por otro motivo.** Una
justificación redactada sobre un ejemplo concreto caduca cuando el ejemplo desaparece, aunque
el riesgo siga intacto.

**Qué haremos distinto.** Antes de eliminar un directorio o artefacto, dos preguntas, no una:

1. ¿Qué depende de esto? *(la habitual)*
2. **¿Qué decisiones, restricciones o deudas se justifican en su existencia?** Revisar
   `decisions.md`, `constraints.md` y `debt_tec.md` buscando su nombre.

Y al redactar una condición de levantamiento, **enunciarla sobre el riesgo, no sobre el
ejemplo que lo ilustra**. `RES-007` decía «si `phases/`…»; ahora dice «que ningún consumidor
externo referencie el canónico por número».

---

### `L-008` · Un dato repetido en dos capas diverge, y miente la que menos se lee

**Qué pasó.** El hallazgo H-01 de la auditoría [`0001-method`](../../RandomAi_Auditor/audits/0001-method.md)
no fue un despiste aislado. `000_method.md` tiene, **por diseño**, dos capas que hablan de lo
mismo: el cuerpo enuncia la norma (§10, «No existe Actor Invitado») y el Anexo A registra cómo
se llegó a ella (`A.1`, con la lista de fuentes en conflicto). Ambas listaban las fuentes, y
ambas divergieron de la realidad **en el mismo sentido** —decían que `015` incluía al Actor
Invitado, cuando `015 §5` lo excluye explícitamente. Nadie lo notó hasta la auditoría.

**Qué aprendimos.** El modo de fallo no es «alguien se equivocó»: es **estructural**. Cuando un
dato vive en dos capas, la copia que se corrompe sin ruido es la de abajo —la que se consulta
menos— y por eso tarda más en detectarse. El cuerpo se lee cada vez que alguien aplica el
método; el anexo se lee cuando alguien pregunta «¿por qué esto es así?», que es casi nunca.

> 🔑 **La copia que miente es la que menos se lee, y es justo la que justifica la norma.** Una
> norma con su justificación falseada sigue pareciendo correcta: se aplica igual, y el error
> solo aparece cuando alguien va a revisarla.

⚠️ **La salida fácil está mal.** Deduplicar —que §10 remita al Anexo A en vez de repetir la
lista— arregla el síntoma **rompiendo la razón de ser de la estructura**: el Anexo A existe
para poder leer «qué cambió respecto a las fuentes» sin recorrer el cuerpo entero, y si el
cuerpo pasa a depender del anexo, se lee peor. La duplicación aquí es deliberada, no accidental.

**Qué haremos distinto.** La defensa no es deduplicar: es **que la divergencia se detecte**.

1. **Toda afirmación sobre lo que dice una fuente se verifica contra la fuente** — en el cuerpo
   y en el anexo, y **el anexo primero**, que es el que menos ojos recibe. Es `L-002` aplicado
   a la capa de abajo.
2. **Al corregir una capa, se corrige la otra en la misma tarea.** `TA-0001` lo hizo bien: pidió
   evidencia separada para §10 y para `A.1`, no una sola.
3. **Una afirmación repetida en tres sitios es señal, no ruido.** «La fuente `005` queda
   superada en este punto» aparece en §10, `A.1` y `A.3`. Que las escribieran manos distintas es
   exactamente la condición que produjo H-01: al detectarla se verifican **todas**, no solo la
   que disparó la revisión.

📌 **Y el mecanismo funcionó.** La divergencia se detectó —en la auditoría, que es donde debía
detectarse. La lección no es que fallara la defensa: es que este documento tiene una forma de
fallo conocida, y a partir de ahora está nombrada.

**Trazas:** `TA-0001` · `D-10` · `L-002` · `L-007`

---

### `L-009` · Escribir en el sitio destruye el original antes de saber si va a funcionar

**Qué pasó.** Al añadir `L-008` a este mismo archivo, abrí `lessons.md` en modo escritura y
fallé a mitad: el texto llevaba emojis mal escapados y Python lanzó `UnicodeEncodeError` **al
volcar**, no al preparar. Para entonces el archivo ya estaba truncado a cero bytes y el
contenido nuevo no llegó a escribirse. Se perdieron las 216 líneas de golpe.

Se recuperó íntegro con `git checkout -- _persistence/lessons.md`. Coste real: cero.

**Qué aprendimos.** `open(p, 'w')` **trunca al abrir**, no al escribir con éxito. Entre esa
truncación y el volcado hay una ventana en la que el archivo está vacío, y cualquier excepción
—codificación, permisos, disco— deja ahí el destrozo. El error de codificación fue la causa
inmediata; **la causa real fue el método de escritura**, que convierte cualquier fallo en
pérdida de datos.

> 🔑 **Una escritura que puede fallar a mitad no es una escritura: es un borrado con una
> segunda parte opcional.**

Y lo que lo salvó no fue mi cuidado, fue `D-06`: el archivo estaba en git. Un archivo aún no
commiteado no habría tenido esa red — que es justamente el estado de todo lo que se escribe
durante una sesión, antes del cierre.

**Qué haremos distinto.** Toda escritura sobre un archivo existente se hace **atómica**:
volcar a `<archivo>.tmp` y luego `os.replace(tmp, p)`. `os.replace` es atómico en Windows y
POSIX: o queda el archivo viejo entero, o el nuevo entero. Nunca el vacío.

📌 **Corolario, y es el que muerde.** Esto vale para `tools/mkindex.py`, que reescribe los
siete archivos de `_persistence/` en cada corrida. **Comprobado: no escribe de forma atómica**
— `tools/mkindex.py:95` usa `write_text`, que trunca al abrir. Registrado como `DT-012`.

**Trazas:** `L-008` · `D-06` · `DT-012`

---

## L-010 · Una frase de cierre bien escrita es la forma más fácil de colar una regla inventada

**Categoría:** Método · **Fecha:** 2026-08-27 · Origen: auditoría `0002-metodo-ampliado`
(`TA-0010`)

**Qué pasó.** Al incorporar `015` §36–§48 al canónico (`TA-0002`), cerré seis de los ocho
bloques con una frase rotunda de cosecha propia — *«…no es una condición de viabilidad: es
una foto»*, *«…es una fase de un waterfall con otro nombre»*—. Cada bloque llevaba su marca
`↳` apuntando a `015`. Ninguna de esas frases está en `015`.

La auditoría lo detectó y lo formuló mejor de lo que yo lo habría hecho: **no estaban mal
escritas, estaban mal marcadas.**

**Por qué importa, y no es cosmético.** Dos de las seis no eran adorno: **endurecían la
fuente.** `015 §41` dice que cada iteración *debería* entregar una capacidad demostrable;
mi cierre lo convertía en definición absoluta. `015 §39` dice que el límite del prototipo
*debe quedar explícito*; yo escribí que *forma parte del criterio de aprobación*, que es
otra cosa y más exigente. Un lector futuro habría aplicado una regla más dura creyendo que
venía de la fuente, y la marca `↳` le habría dado la razón.

> 🔑 **La marca `↳` es una afirmación sobre el origen, y una afirmación no comprobada es
> justo lo que `P-1` prohíbe. La escribí yo, sobre mi propio texto, sin comprobarla.**

**Por qué se me pasó.** El impulso no fue inventar: fue **cerrar bien el párrafo**. Una
sección que termina en una lista se siente incompleta, y la frase que la remata se siente
como redacción, no como contenido. Ahí está la trampa: **el modo «estoy escribiendo mejor»
y el modo «estoy añadiendo normativa» se sienten igual desde dentro.** Por eso no salta
ninguna alarma — y por eso hay que comprobarlo desde fuera, mirando la marca, no la prosa.

**Qué haremos distinto.** Al incorporar contenido de una fuente, el último paso no es
releer para que suene bien: es **recorrer el bloque frase por frase preguntando "¿esto está
en la fuente?"**. Lo que no esté, o se marca `➕` con entrada en el Anexo A, o se retira. La
comprobación se hace **sobre el bloque entero**, no sobre la lista principal: el defecto
vive en los bordes, no en el centro.

📌 **Corolario para la auditoría.** Verificar «que la lista esté completa» no basta.
`TA-0002` pasó sus seis criterios de cierre —los seis criterios de `015` §46 estaban
completos, en orden y sin pérdida— y aun así el bloque contenía regla inventada. **La
fidelidad del contenido incorporado y la fidelidad de sus bordes son dos comprobaciones
distintas.**

**Trazas:** `TA-0002` · `TA-0010` · `L-005` · `P-1`
