# assumptions.md — Supuestos del proyecto RandomAI

> Todo lo que estamos dando por cierto **sin haberlo verificado**. Cada supuesto debe
> validarse en algún momento, y hasta entonces es un riesgo abierto.
>
> Un supuesto que se confirma se marca `Confirmado` y deja de ser riesgo.
> Un supuesto que se refuta se marca `Refutado` y **obliga a revisar lo que dependía de él**.

**Última actualización:** 2026-08-26

<!--INDEX-->

## Índice

> **Búsqueda rápida.** Salta con el enlace, o ve directo a la línea indicada (exacta, ya contando este índice).
> Por código: `grep -n 'SUP-001' assumptions.md`

| Línea | Sección | Ir a |
|---|---|---|
| `37` | **Convenciones** | [↓](#convenciones) |
| `50` | **Tablero** | [↓](#tablero) |
| `66` | **Detalle** | [↓](#detalle) |
| `68` | &nbsp;&nbsp;↳ SUP-001 · La fuente oficial expone el histórico completo | [↓](#sup-001--la-fuente-oficial-expone-el-histórico-completo) |
| `85` | &nbsp;&nbsp;↳ SUP-002 · El histórico incluye premio/acumulado | [↓](#sup-002--el-histórico-incluye-premioacumulado) |
| `99` | &nbsp;&nbsp;↳ SUP-003 · La fuente distingue Baloto de Revancha | [↓](#sup-003--la-fuente-distingue-baloto-de-revancha) |
| `110` | &nbsp;&nbsp;↳ SUP-004 · Vercel sostiene persistencia y actualización programada | [↓](#sup-004--vercel-sostiene-persistencia-y-actualización-programada) |
| `123` | &nbsp;&nbsp;↳ SUP-005 · El Actor Generador es el jugador | [↓](#sup-005--el-actor-generador-es-el-jugador) |
| `140` | &nbsp;&nbsp;↳ SUP-006 · Hay volumen histórico suficiente | [↓](#sup-006--hay-volumen-histórico-suficiente) |
| `152` | &nbsp;&nbsp;↳ SUP-008 · Las credenciales de GitHub funcionan | [↓](#sup-008--las-credenciales-de-github-funcionan) |
| `167` | &nbsp;&nbsp;↳ SUP-007 · La prioridad no bloquea la generación | [↓](#sup-007--la-prioridad-no-bloquea-la-generación) |
| `181` | &nbsp;&nbsp;↳ SUP-009 · El flujo de Descubrimiento generaliza a cualquier proyecto | [↓](#sup-009--el-flujo-de-descubrimiento-generaliza-a-cualquier-proyecto) |

<!--/INDEX-->

---

## Convenciones

**Código:** `SUP-NNN`, correlativo, nunca se reutiliza. Nomenclatura heredada de `phases/`,
eliminada por `D-04`; la convención se conserva.

**Estado:** `Por validar` · `Confirmado` · `Refutado` · `Obsoleto`

**Cada supuesto declara:** qué se asume · por qué importa · **cómo se validará** · cuándo.

> Un supuesto sin método de validación declarado no es un supuesto: es un deseo.

---

## Tablero

| Código | Supuesto | Impacto si es falso | Estado |
|---|---|---|---|
| `SUP-001` | La página oficial de Baloto expone el histórico completo de forma accesible | Alto | `Por validar` |
| `SUP-002` | El histórico publicado incluye premio/acumulado por sorteo y por juego | Alto | `Por validar` |
| `SUP-003` | El histórico distingue claramente resultados de Baloto y de Revancha | Alto | `Por validar` |
| `SUP-004` | Vercel puede sostener persistencia + actualización programada dentro del plan disponible | Alto | `Por validar` |
| `SUP-005` | El Actor Generador es el propio jugador/usuario final | Medio | `Por validar` |
| `SUP-006` | Existe volumen histórico suficiente para que el cálculo estadístico sea significativo | Medio | `Por validar` |
| `SUP-007` | La restricción de prioridad (§26 del brief) nunca deja el generador sin combinación válida | Medio | `Por validar` |
| `SUP-008` | Las credenciales de GitHub están configuradas y el push funcionará | Medio | `Por validar` |
| `SUP-009` | El flujo de Descubrimiento diseñado en `S-005` sirve para cualquier proyecto, no solo RandomAI | Medio | `Por validar` |

---

## Detalle

### `SUP-001` · La fuente oficial expone el histórico completo

**Qué se asume.** Que la página oficial de Baloto permite leer el histórico de resultados y no
solo el último sorteo.

**Por qué importa.** Los §3 y §7 del brief dependen enteramente de esto: sin histórico no hay
carga inicial, ni estadística, ni indicador. **Es el supuesto que sostiene el producto.**

**Cómo se validará.** Inspección directa de la fuente durante el Descubrimiento, antes de
prototipar. No por documentación de terceros: mirando la página.

**Si es falso.** Hay que replantear la fuente de datos. El brief §23.3 deja el método de
obtención como decisión pendiente, así que hay margen — pero el producto no sobrevive sin
alguna fuente de histórico.

---

### `SUP-002` · El histórico incluye premio/acumulado

**Qué se asume.** Que el valor del premio/acumulado está disponible **por sorteo histórico**, no
solo el acumulado vigente hoy.

**Por qué importa.** El brief lo exige en §3 (histórico mínimo), §14, §15 y §27.

**Cómo se validará.** Junto con `SUP-001`, en la misma inspección.

**Si es falso.** El histórico se carga sin premio y el dato queda solo para sorteos futuros;
hay que avisar al cliente porque reduce lo pedido en §27.

---

### `SUP-003` · La fuente distingue Baloto de Revancha

**Qué se asume.** Que ambos juegos son separables sin ambigüedad en el origen.

**Por qué importa.** Todo el §13–§15 del brief compara por separado. Y §7 exige no mezclar
universos.

**Cómo se validará.** Inspección de la fuente.

---

### `SUP-004` · Vercel sostiene persistencia y actualización programada

**Qué se asume.** Que el §24 del brief es realizable sin infraestructura adicional.

**Por qué importa.** Es restricción del cliente (`RES-002`), no elección nuestra.

**Cómo se validará.** En la fase de Baseline (ARCHIT), y se demostrará en el **WSLT** — que es
exactamente para lo que existe el Walking Skeleton (`000_method.md` §40).

**Si es falso.** Se registra como `ADR` y se consulta al cliente: la restricción es suya.

---

### `SUP-005` · El Actor Generador es el jugador

**Qué se asume.** Que quien genera el proceso —generar combinación y registrar juego— es el
usuario final que juega.

**Por qué importa.** `000_method.md` §9.1: si el Generador no existe o no usa la aplicación, no
hay razón para que la aplicación exista. **Es la primera pregunta del Descubrimiento.**

**Cómo se validará.** Fase `005_discovery`. Es literalmente su condición de salida.

**Nota.** El brief §22 declara que el proyecto es también un ejercicio de aprendizaje. Eso
abre la posibilidad de que el interesado principal y el Actor Generador sean la misma persona,
lo que **debilita la validación del prototipo** (`000_method.md` §23: usuarios representativos).
A resolver en Descubrimiento.

---

### `SUP-006` · Hay volumen histórico suficiente

**Qué se asume.** Que el histórico disponible da base estadística para «intervalo promedio entre
apariciones» (brief §8) con sentido.

**Por qué importa.** Con pocos sorteos, el indicador 🟢/⚪ sería ruido presentado como señal —
justo lo que el brief §9 y §19 prohíben comunicar.

**Cómo se validará.** Al completar la carga inicial: contar sorteos y apariciones por número.

---

### `SUP-008` · Las credenciales de GitHub funcionan

**Qué se asume.** Que `git push` a `origin` va a autenticar sin intervención.

**Por qué importa.** El protocolo de cierre define que **un commit es local**: si el hash no
llega a `origin`, no hubo cierre. Todo el mecanismo de respaldo depende de esto.

**Cómo se validará.** En el primer `git push -u origin main`. No se ha hecho todavía: el remoto
está vacío y **el push es una publicación**, así que se hará cuando el usuario lo autorice.

**Si es falso.** El cierre lo detecta solo: `git status -sb` seguirá diciendo `ahead` y el
protocolo obliga a reportarlo en «Sin resolver» en lugar de taparlo.

---

### `SUP-007` · La prioridad no bloquea la generación

**Qué se asume.** Que excluir los números del último sorteo (brief §26) más la regla de máximo
dos consecutivos (§25) siempre deja combinaciones válidas disponibles.

**Por qué importa.** Un generador que no puede generar es un fallo funcional en el botón
principal del producto.

**Cómo se validará.** Cálculo combinatorio en diseño técnico + prueba determinística. Con 43−5
= 38 balotas disponibles y 16−1 = 15 superbalotas, el espacio parece amplio, pero **es
aritmética, no opinión: hay que hacerla**.

---

### `SUP-009` · El flujo de Descubrimiento generaliza a cualquier proyecto

**Qué se asume.** Que el flujo diseñado en `_temp/005_discovery.md` —bucle de extracción ×4,
bloque de criterio, trazabilidad al origen y rúbrica del extractor— sirve para **cualquier
proyecto de desarrollo de software**, y no solo para el brief de RandomAI sobre el que se
pensó.

**Por qué importa.** Es el **primer objetivo** que el usuario declaró en `S-005`: un proceso de
Descubrimiento estandarizado. Si el supuesto es falso, lo que tendremos es un procedimiento a
medida de este brief **con apariencia de estándar** — y eso no se descubre al escribirlo, sino
en el segundo proyecto, con el método ya normalizado y citado.

**Cómo se validará.** Corriendo el bucle de extracción completo sobre el brief de **otro**
proyecto, de otro dominio, y midiendo cuántas piezas hay que cambiar. Mientras solo se haya
corrido sobre este brief, `n = 1`: eso es un caso de prueba, no una evaluación. Un prompt o un
procedimiento ajustado contra un único ejemplo se ajusta **a ese ejemplo**.

**Si es falso.** Las piezas atadas a este dominio se identifican y **bajan a la capa de
artefactos**, que es específica del proyecto, dejando fase y plantillas genéricas. No se
descarta el flujo: se reparte mejor.

**Mitigación mientras tanto.** Escribir fase y plantillas sin ejemplos del dominio, sin
supuestos sobre el tipo de aplicación, y con las decisiones concretas de RandomAI fuera de
esas dos capas.

---
