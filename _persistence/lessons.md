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
| `42` | **Convenciones** | [↓](#convenciones) |
| `50` | **Tablero** | [↓](#tablero) |
| `71` | **Detalle** | [↓](#detalle) |
| `73` | &nbsp;&nbsp;↳ L-001 · Leer 015_evolution.md por líneas, no por encabezados | [↓](#l-001--leer-015_evolutionmd-por-líneas-no-por-encabezados) |
| `89` | &nbsp;&nbsp;↳ L-002 · No repetir el canónico sin contrastarlo | [↓](#l-002--no-repetir-el-canónico-sin-contrastarlo) |
| `106` | &nbsp;&nbsp;↳ L-003 · Medir el impacto antes de renumerar | [↓](#l-003--medir-el-impacto-antes-de-renumerar) |
| `127` | &nbsp;&nbsp;↳ L-004 · El alcance declarado de una auditoría es su límite | [↓](#l-004--el-alcance-declarado-de-una-auditoría-es-su-límite) |
| `146` | &nbsp;&nbsp;↳ L-005 · Un fallo de formato puede perder contenido normativo | [↓](#l-005--un-fallo-de-formato-puede-perder-contenido-normativo) |
| `169` | &nbsp;&nbsp;↳ L-007 · Quien delega un procedimiento no puede llevar una copia encima | [↓](#l-007--quien-delega-un-procedimiento-no-puede-llevar-una-copia-encima) |
| `202` | &nbsp;&nbsp;↳ L-006 · Al eliminar algo, comprobar qué se apoyaba en ello | [↓](#l-006--al-eliminar-algo-comprobar-qué-se-apoyaba-en-ello) |
| `234` | &nbsp;&nbsp;↳ L-008 · Un dato repetido en dos capas diverge, y miente la que menos se lee | [↓](#l-008--un-dato-repetido-en-dos-capas-diverge-y-miente-la-que-menos-se-lee) |
| `277` | &nbsp;&nbsp;↳ L-009 · Escribir en el sitio destruye el original antes de saber si va a funcionar | [↓](#l-009--escribir-en-el-sitio-destruye-el-original-antes-de-saber-si-va-a-funcionar) |
| `311` | **L-010 · Una frase de cierre bien escrita es la forma más fácil de colar una regla inventada** | [↓](#l-010--una-frase-de-cierre-bien-escrita-es-la-forma-más-fácil-de-colar-una-regla-inventada) |
| `356` | **L-011 · Ampliar una cita introduce defectos sin tocar el texto, y el diff no los enseña** | [↓](#l-011--ampliar-una-cita-introduce-defectos-sin-tocar-el-texto-y-el-diff-no-los-enseña) |
| `423` | **L-012 · Medí el hueco inventariando lo que se fue, no comprobando lo que falta** | [↓](#l-012--medí-el-hueco-inventariando-lo-que-se-fue-no-comprobando-lo-que-falta) |
| `474` | **L-013 · Caracterizar un archivo por su índice no es haberlo leído** | [↓](#l-013--caracterizar-un-archivo-por-su-índice-no-es-haberlo-leído) |
| `519` | **L-014 · Abrir un archivo en escritura antes de tener el contenido listo lo destruye** | [↓](#l-014--abrir-un-archivo-en-escritura-antes-de-tener-el-contenido-listo-lo-destruye) |

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
| `L-011` | Ampliar una cita introduce defectos sin tocar el texto, y el diff no los enseña | Método | 2026-08-27 |
| `L-012` | Medí el hueco inventariando lo que se fue, no comprobando lo que falta | Método | 2026-08-27 |
| `L-013` | Caracterizar un archivo por su índice no es haberlo leído | Proceso | 2026-08-27 |
| `L-014` | Abrir un archivo en escritura antes de tener el contenido listo lo destruye | Técnica | 2026-08-27 |

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

---

## L-011 · Ampliar una cita introduce defectos sin tocar el texto, y el diff no los enseña

**Categoría:** Método · **Fecha:** 2026-08-27 · Origen: auditoría `0003` (`TA-0014`)

**Qué pasó.** Al fusionar `015 §50` en el `§4` del canónico, la marca pasó de `↳ *015 §2*`
a `↳ *015 §2, §50*`. La auditora contrastó las filas MVP y EVOL de la tabla contra `015
§50`, no las encontró, y abrió `TA-0014`.

Comprobado: **esas filas vienen de `015 §2`** (`015_evolution.md:45-53`), que sigue citado
en la misma marca. La marca es un **conjunto**, no una atribución fila a fila, y cada
afirmación de `§4` está cubierta por uno de los dos. El hallazgo concreto no se sostiene y
se devolvió con evidencia.

**Pero la clase de defecto que persigue es real, y ese es el valor de la lección.**

> 🔑 **`L-010` y esta son la misma comprobación en dos direcciones.** En `L-010` se añadió
> texto bajo una marca existente. Aquí se amplía una marca sobre texto existente. En ambos
> casos el resultado es idéntico: una afirmación queda atribuida a una fuente que no la
> dice.

**Por qué esta dirección es la peligrosa.** La primera deja rastro: hay líneas nuevas en el
`git diff`, y una revisión del contenido las encuentra. **La segunda no cambia ni una
palabra del texto afectado.** El diff muestra una sola línea tocada —la de la marca— y el
texto que esa línea pasó a cubrir aparece como contexto sin modificar. Quien revise el
cambio lee «se añadió una fuente» y da por hecho que añadir fuentes solo puede mejorar la
atribución.

📌 **Y hay un sesgo que lo remata:** al ampliar una marca uno comprueba —si comprueba— que
**la fuente nueva aporta algo al bloque**. Esa comprobación siempre sale bien: por eso se
añadió. La que hay que hacer es la contraria y es más cara: **¿el conjunto citado cubre
cada afirmación que queda debajo?**

**Qué haremos distinto.** Toda ampliación de una marca `↳` obliga a recorrer el bloque
entero contra el **conjunto** de fuentes citadas, no contra la añadida. Se hace **cada
vez**, aunque la ampliación parezca inofensiva.

**Aplicado a las seis marcas que amplió `TA-0002`.** Bloque por bloque, contra la fuente
abierta:

| Marca | Afirmación no trivial del bloque | Cubierta por |
|---|---|---|
| `§4` | filas MVP y EVOL de la tabla | `015 §2:45-53`, casi literal |
| `§29` | las ocho situaciones que el prototipo no valida | `015 §39:980-990` |
| `§30` | «un prototipo exitoso no demuestra adopción» | `015 §40`; el resto ← `015 §15` |
| `§37` | «no construir innecesariamente, pero tampoco imposibilitar» | `015 §37`, literal; lista de actores ← `015 §36` |
| `§41` | «cada iteración debería entregar capacidad demostrable» | `015 §41` |
| `§50` | 20 vs 5.000 y la evaluación periódica | `015 §38` |

Las seis limpias. Lo que en cada bloque no procede de fuente lleva su `➕` con remisión al
Anexo, por `TA-0010`.

⚠️ **Esta tabla se escribió en una segunda pasada.** La primera versión de esta lección
afirmaba el barrido sin dejar la evidencia, y la auditoría `0004` lo señaló: había
comprobado `§4` y dado por buenas las otras cinco. **Afirmar una comprobación no es
hacerla** — y es precisamente el reproche que esta lección le hace al que amplía una marca
sin recorrer el bloque. Que saliera limpia no la hace prescindible: el coste de saltársela
es un defecto invisible al diff.

⚠️ **Corolario sobre el trabajo ajeno.** El hallazgo era incorrecto en su caso concreto y
correcto en su método. Verificarlo antes de aceptarlo (`P-1`) evitó tocar un `§4` que
estaba bien; descartarlo entero por eso habría perdido la lección. **Un hallazgo puede
fallar en el ejemplo y acertar en la regla.**

**Trazas:** `TA-0002` · `TA-0010` · `TA-0014` · `L-010` · `P-1`

---

## L-012 · Medí el hueco inventariando lo que se fue, no comprobando lo que falta

**Categoría:** Método · **Fecha:** 2026-08-27 · Origen: auditoría `0004`

**Qué pasó.** Al eliminarse `phases/` (`D-04`) escribí `DT-008`, severidad Alta, declarándola
**bloqueante para abrir el Descubrimiento**. La auditoría la contrastó punto por punto:

- de los **ocho** elementos que enumeré, **cinco ya estaban cubiertos** entre el canónico y
  `_guide/GUIDE.md`. Faltan tres: entradas exigidas, condición de salida, entrega al Gate.
- **la premisa principal era falsa.** Escribí que el Gate 1 se declararía sin criterio
  operativo. El Gate 1 tiene `§29`, `§29.1`, `§30`, `§31`, `§32` y `§19`–`§27`: **más** nivel
  operativo del que `phases/` le daba.
- `GUIDE.md` cubre el «cómo» de la construcción, que `DT-008` daba por perdido. WSLT y GRTH
  tienen hoy **más** procedimiento escrito que antes de `D-04`.

**Cómo se produjo el error, que es lo que hay que recordar.** Escribí `DT-008` abriendo
`phases/` y **listando lo que contenía**. Cada punto de esa lista era cierto: eso estaba ahí
y dejó de estar. Lo que nunca hice fue la otra mitad —**ir al resto del proyecto y comprobar
punto por punto si algo más lo cubría**—. El resultado tiene toda la apariencia de una
medición: ocho elementos concretos, verificables, ninguno inventado.

> 🔑 **Un inventario de lo que se fue no es una medida de lo que falta.** Se parecen tanto
> que el primero se pasa por el segundo sin que nadie lo note — empezando por quien lo
> escribe.

**Por qué importa más de lo que parece.** `DT-008` no era una nota: era el **camino crítico
declarado** del proyecto. Bloqueaba la apertura del Descubrimiento, y sostuvo `T-013` —una
decisión del usuario con tres opciones— **dimensionada sobre ocho puntos y seis etapas cuando
el hueco real son tres puntos en un sitio.** Las tres opciones se enunciaron contra un
problema más grande que el problema. Durante dos sesiones el proyecto planificó contra una
medición que nadie había comprobado.

⚠️ **Y no había forma de detectarlo desde dentro.** `DT-008` la escribió quien sufría el
hueco, y quien lo sufre lo estima por lo que echa de menos, no por lo que queda. Es
literalmente `§32` —*quien construye no puede ser su propio testigo*— aplicado a un
diagnóstico en vez de a un Gate. **Una deuda declarada bloqueante por la propia ejecutora es
una candidata a auditoría, no un hecho.**

**Qué haremos distinto.** Toda deuda que se declare **bloqueante** exige, antes de anotarse:
recorrer sus puntos **contra el resto del proyecto**, uno por uno, y escribir qué los cubre o
que nada los cubre. Si no se ha hecho, la deuda se anota igual pero **con la severidad sin
asignar** y diciendo que la medición está pendiente. Una severidad Alta sin comprobación
detrás no es una advertencia: es una desviación de la planificación.

📌 **Corolario para `T-013`.** No se decide sobre las tres opciones tal como están escritas:
están dimensionadas contra el hueco equivocado. Se redimensionan primero.

**Trazas:** `DT-008` · `D-04` · `T-013` · `TA-0015` · `L-006`

---

## L-013 · Caracterizar un archivo por su índice no es haberlo leído

**Categoría:** Proceso · **Fecha:** 2026-08-27 · Origen: `S-005`, señalado por el usuario

**Qué pasó.** El usuario pidió diseñar observabilidad, evaluación y rúbricas para el agente
que extrae información del brief. Recorrí `_guide/GUIDE.md` **por encabezados** —un `grep` de
`^## `— y a partir de esa lista le dije que el repo no cubría nada de eso. Diseñé la capa
entera desde cero. Cuando el usuario preguntó si había leído el archivo, lo leí completo:

| Lo que afirmé | Lo que dice `GUIDE.md` |
|---|---|
| «observabilidad: nada» | **§3** (`:185-192`) ya la pide, junto a evaluación y seguridad de datos |
| «rúbricas: nada» | **§0** (`:78`) las **excluyó a propósito**, con su motivo escrito |
| «seguridad: parcial» | **§0** (`:83`) excluyó inyección de prompt, también con motivo |
| «hace falta una capa nueva» | **§0** (`:50-56`) fija el reparto: esto es `GUIDE.md`, no un archivo aparte |

**Cómo se produjo el error.** Un índice bien hecho **da la sensación de haber leído**: enumera
todas las secciones, así que parece cubrir el contenido. Pero un índice dice **de qué habla**
un archivo, no **qué dice**. Y lo que más importaba aquí —las exclusiones con su motivo— es
justo lo que ningún índice recoge: una tabla dentro de una sección, sin encabezado propio.

> 🔑 **«No está» es una afirmación sobre el archivo entero, y no se sostiene con un
> recorrido por encabezados.** Afirmar una ausencia exige haber mirado donde podría estar.

**Por qué importa más que un detalle.** El error no fue de matiz: **la recomendación
estructural era equivocada.** Propuse construir una capa nueva cuando el reparto ya estaba
decidido en `D-09`, y le dije al usuario que no existía material que sí existía y estaba
auditado. Si no llega a preguntar, el plan de trabajo habría arrancado torcido.

📌 **Y lo que se recuperó al leerlo:** las exclusiones de `GUIDE.md` §0 llevan su motivo
escrito, y **dos de esos motivos han caducado** al introducir agentes en la construcción. Eso
solo se ve leyendo la tabla. El propio archivo lo había previsto (`:73`): *«un salto sin
motivo escrito se lee como veredicto sobre lo saltado»*.

**Qué haremos distinto.** Antes de afirmar que algo **no está** en un archivo del repo, se lee
entero. Un recorrido por encabezados sirve para **encontrar** algo, nunca para **descartarlo**.

⚠️ **Emparenta con `L-001`**, que dice lo mismo sobre `015_evolution.md`: sus §35–§51 no
llevan `#` y cualquier recorrido por encabezados las salta. Allí costó ~200 líneas normativas;
aquí, una recomendación estructural errónea. **Es la misma familia de fallo, y ya van dos.**

**Trazas:** `L-001` · `D-09` · `P-1` · `GUIDE.md` §0

---

## L-014 · Abrir un archivo en escritura antes de tener el contenido listo lo destruye

**Categoría:** Técnica · **Fecha:** 2026-08-27 · Origen: `S-005`, incidente real (dos veces)

**Qué pasó.** Un script de Python que editaba `_persistence/tasks.md` hacía, en este orden:

```python
io.open(p, "w", encoding="utf-8").write(s)   # <- destructivo
```

El contenido `s` llevaba pares de sustitución mal formados, así que `.write()` lanzó
`UnicodeEncodeError`. Pero **la apertura en modo `w` ya había truncado el archivo a 0 bytes.**
`tasks.md` quedó vacío: 354 líneas perdidas.

**El fallo no estaba en el contenido: estaba en el orden.** Abrir en `w` trunca **antes** de
escribir nada, así que cualquier error posterior deja el archivo destruido en vez de intacto.

⚠️ **Y volvió a pasar en la misma sesión, con la corrección puesta.** Escribí un ayudante
`guardar()` que decía codificar primero… pero seguía siendo una sola expresión:

```python
open(p, "wb").write(s.encode("utf-8"))   # open() se evalúa ANTES que encode()
```

Python evalúa `open(p, "wb")` —que trunca— y **después** el argumento. `lessons.md` quedó a
cero. **Escribir la intención correcta no basta: hay que separarla en dos sentencias.**

```python
data = s.encode("utf-8")      # si algo falla, falla AQUÍ
with open(p, "wb") as f:      # el archivo no se toca hasta que el contenido es válido
    f.write(data)
```

🔑 **Y la lección que vale más que la técnica: lo que salvó los dos archivos fue que
estaban commiteados.** `git checkout -- <archivo>` los devolvió íntegros en un segundo. Un
script que reescribe un archivo del repo **se corre sobre árbol limpio, o no se corre** — si
hay cambios sin commitear, el respaldo no existe.

⚠️ **Consecuencia sobre cómo se comprueba.** Un archivo truncado **no da error después**:
`grep` devuelve cero coincidencias y parece que la búsqueda falló, no que el archivo esté
vacío. Tras cualquier escritura por script, comprobar el **tamaño**, no solo la ausencia de
excepción.

**Trazas:** `P-5` · `D-06`
