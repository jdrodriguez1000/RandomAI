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
| `35` | **Convenciones** | [↓](#convenciones) |
| `43` | **Tablero** | [↓](#tablero) |
| `57` | **Detalle** | [↓](#detalle) |
| `59` | &nbsp;&nbsp;↳ L-001 · Leer 015_evolution.md por líneas, no por encabezados | [↓](#l-001--leer-015_evolutionmd-por-líneas-no-por-encabezados) |
| `75` | &nbsp;&nbsp;↳ L-002 · No repetir el canónico sin contrastarlo | [↓](#l-002--no-repetir-el-canónico-sin-contrastarlo) |
| `92` | &nbsp;&nbsp;↳ L-003 · Medir el impacto antes de renumerar | [↓](#l-003--medir-el-impacto-antes-de-renumerar) |
| `113` | &nbsp;&nbsp;↳ L-004 · El alcance declarado de una auditoría es su límite | [↓](#l-004--el-alcance-declarado-de-una-auditoría-es-su-límite) |
| `132` | &nbsp;&nbsp;↳ L-005 · Un fallo de formato puede perder contenido normativo | [↓](#l-005--un-fallo-de-formato-puede-perder-contenido-normativo) |
| `148` | &nbsp;&nbsp;↳ L-007 · Quien delega un procedimiento no puede llevar una copia encima | [↓](#l-007--quien-delega-un-procedimiento-no-puede-llevar-una-copia-encima) |
| `181` | &nbsp;&nbsp;↳ L-006 · Al eliminar algo, comprobar qué se apoyaba en ello | [↓](#l-006--al-eliminar-algo-comprobar-qué-se-apoyaba-en-ello) |

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
