# 005_discovery — Diseño del flujo de Descubrimiento

> 🚧 **ARCHIVO DE TRABAJO. NO ES NORMATIVO.**
>
> Vive en `_temp/` a propósito. Recoge el diseño acordado en conversación durante `S-005`
> para que no se pierda, **pero nada de aquí obliga todavía**. Cuando el flujo esté
> entendido y acordado, sus piezas se repartirán entre `_methodology/000_method.md`,
> `_phases/`, `_templates/` y `_guide/GUIDE.md` — ver §11.
>
> **Origen:** `D-12`. **Razón trazable:** `TA-0015` (bloqueante) · `T-013` · `DT-008`.

**Escrito:** 2026-08-27 (`S-005`) · **Estado:** `Borrador en discusión`

---

## 0. Qué problema resuelve este documento

El Descubrimiento es la primera fase del método y hoy tiene dos huecos:

1. **No tiene condición de salida escrita.** `§13` dice qué hay que entender y `§14` lista
   cinco salidas. No hay nada que diga cuándo termina la fase, quién lo declara ni contra
   qué. Eso es `TA-0015`, y es bloqueante.
2. **No tiene procedimiento.** `D-04` eliminó `phases/`, que era lo único que decía *cómo*
   ejecutar cada fase. Eso es `DT-008`, y su decisión pendiente es `T-013`.

Este documento diseña el flujo completo para poder cerrar los dos.

**Y añade un tercer objetivo, pedido por el usuario en `S-005`:** que el flujo sea
**estandarizado y aplicable a cualquier proyecto de desarrollo de software**, no solo a
RandomAI, y que las salidas puedan **generarse con agentes de IA** dentro de un flujo con
observabilidad, evaluación, rúbricas y seguridad.

📌 **Esto no choca con la regla dura 1.** El producto final no llama a ninguna API de IA. Los
agentes de este flujo están del lado de **construir**, y el brief lo autoriza explícitamente:
*«este proyecto servirá como ejercicio para aprender a desarrollar software utilizando
inteligencia artificial como asistente»* (`_brief/Client_brief.txt:581`, §22).

---

## 1. Los cuatro quienes

| | Quién | Qué hace | Qué **no** hace |
|---|---|---|---|
| 👤 | **Cliente / usuario** | entrega el brief, responde preguntas, decide | — |
| 🤖 | **Agente extractor** | lee el brief, extrae lo que hay, enumera lo que falta | responder por el cliente · declarar nada terminado |
| ⚙️ | **Terminal ejecutora** | orquesta, consolida, redacta | declarar el cierre de la fase |
| 🔍 | **Terminal auditora** | verifica y **declara el cierre** | construir |

🔑 **El agente extractor es un subagente que solo conoce el brief.** No recibe la
conversación de la sesión ni el contexto del proyecto. Es deliberado: `GUIDE.md` §8 —*«¿este
agente necesita saber MENOS que yo, o MÁS? Menos, y su valor está en no saber»*—. Un
extractor que conoce nuestras conclusiones deja de ser un lector independiente del brief y
se convierte en un eco.

---

## 2. Entradas

| | Qué | Sin esto |
|---|---|---|
| **E1** | El **brief** del cliente | no hay de dónde extraer |
| **E2** | **Acceso a una persona** que pueda responder | la fase **no puede empezar** |

**E1 llega mal formulado por definición.** Desordenado, ambiguo, incompleto, y casi siempre
escrito en forma de solución en vez de necesidad. Eso no es un defecto del cliente:
**desvestirlo es el trabajo de la fase.** Si llegara ordenado, la fase sobraría.

🚨 **E2 no se sustituye con un agente mejor.** Un agente muy bueno es la suposición más
convincente de todas. Si no hay acceso a una persona, la fase no empieza — no se compensa
con inferencia.

### Comprobado en el brief de RandomAI

| Qué se buscó | Resultado |
|---|---|
| `actualmente · hoy en día · manualmente · a mano · papel · excel` | **1 coincidencia**, y es «la combinación actualmente mostrada» (`:158`) |

**723 líneas describiendo la solución. Cero describiendo el problema.** Es el caso típico, no
la excepción, y es exactamente lo que el bucle de extracción existe para detectar.

📌 **A favor de este brief:** su §23 «Decisiones pendientes» (`:619-631`) enumera **13 huecos
que el cliente reconoce**. Es una lista de `SUP-xxx` regalada, y una prueba de fuego: si el
Descubrimiento termina sin que esos 13 aparezcan como supuestos o restricciones, el proceso
no funcionó.

---

## 3. Salidas

| Artefacto | Qué contiene | De dónde sale |
|---|---|---|
| `005_needs.md` | necesidades `N-xxx`, **sin nombrar pantallas** | bucle A · vuelta 1 |
| `010_actors.md` | actores por función, **solo los que existen** | bucle A · vuelta 2 |
| `015_stakeholders.md` | quién decide, financia, aprueba o se ve afectado | bucle A · vuelta 3 |
| `025_constraints.md` | `RES-xxx` firmes · `SUP-xxx` por verificar | bucle A · vuelta 4 |
| `020_hypothesis.md` | la hipótesis **con su condición de falsación**, sellada | bloque B · B2 |
| Decisión de alcance | qué actores entran al prototipo, **con su justificación** | bloque B · B3 |

**Y un resultado alternativo perfectamente válido:** `NO CONTINÚA`, si no hay Generador real.
No es un fracaso — es el resultado más barato que el método puede dar.

### ⚠️ Incoherencia detectada, pendiente de resolver

Las cinco plantillas de `_templates/_discovery/` y las cinco salidas del canónico `§14` son
cinco y cinco, **pero no las mismas cinco**:

| | ¿Salida en `§14`? | ¿Tiene plantilla? |
|---|---|---|
| necesidades · actores · interesados · hipótesis | sí | sí |
| **restricciones y supuestos** | **no** | sí (`025_constraints.md`) |
| **decisión de alcance del prototipo** | **sí** | **no** |

**Causa:** las plantillas son anteriores a `TA-0007`, que añadió la quinta salida en `S-004`.

**Explicación posible para restricciones:** `RES-xxx` y `SUP-xxx` van a
`_persistence/constraints.md` y `assumptions.md`, así que quizá no sean salida *de fase* sino
escritura *en persistencia* — pero entonces sobra la plantilla. **Sin resolver.**

---

## 4. Bloque A · El bucle de extracción

Se repite **cuatro veces**, una por cada artefacto que se puede **sacar** del brief y de la
cabeza del cliente.

| # | Paso | Quién | Produce |
|---|---|---|---|
| **A1** | Lee el brief y extrae lo que **sí** responde | 🤖 | borrador, cada entrada con `origen: brief:<línea>` |
| **A2** | Enumera lo que el brief **no** responde | 🤖 | cuestionario, cada pregunta con el hueco que llena |
| **A3** | Responde | 👤 | respuestas — o **«no sé»**, que es respuesta válida |
| **A4** | Consolida en el artefacto | ⚙️ | respuesta → `origen: usuario:<fecha>` · «no sé» → `SUP-xxx` |

↺ **A3 puede abrir preguntas nuevas y devolver a A2.** Una respuesta suele destapar una
pregunta que no estaba en el cuestionario. **Lo único que impide que el bucle gire para
siempre es la condición de salida** — sin ella, la fase termina cuando alguien se cansa.

### Por qué A1 y A2 son el mismo agente

Son las dos mitades de una sola lectura: lo que el brief responde y lo que no son
complementos del mismo análisis. Partirlo en dos agentes obligaría a leer el brief dos veces
con dos criterios y arriesgaría que no cuadren. Además `GUIDE.md` §8 (`:483-485`) prohíbe
explícitamente cortar agentes **por fases del trabajo**.

### A2 es el producto más valioso del bucle

> Un agente leyendo un brief desordenado es **excelente enumerando lo que falta** — mucho
> mejor que una persona, que rellena los huecos sin darse cuenta de que los rellenó.

Redactar necesidades bonitas lo hace cualquiera. Decir *«el brief no dice cómo se hace esto
hoy»* es el trabajo que de verdad se quiere automatizar.

### El cuestionario de A2: tres reglas

**1 · Se deriva del brief, nunca es genérico.** Un formulario fijo pregunta cosas que el
brief ya contesta, y eso tiene un coste que no se ve: **le enseña al cliente que el
cuestionario no se leyó**, y el cliente que cree que no lo lees empieza a responder por
encima — justo en las preguntas que sí importaban. Cada pregunta debe poder decir qué hueco
llena; una pregunta cuya respuesta está en el brief es un defecto del cuestionario, y se
detecta abriendo el brief.

**2 · Es una agenda de conversación, no un formulario para rellenar solo.**

> **Un cuestionario devuelve respuestas a las preguntas que hiciste. Una conversación
> devuelve lo que no sabías preguntar.**

Y en Descubrimiento, por definición, no sabes lo que no sabes. Segundo problema: las
respuestas escritas vuelven a llegar **en forma de solución** — preguntas «¿cómo eliges los
números hoy?» y responden «necesito que la app los genere». En conversación repreguntas; en
un formulario esa casilla ya figura contestada.

**3 · Se pregunta por el pasado concreto, no por los deseos.**

| ❌ Produce ficción | ✅ Produce dato |
|---|---|
| «¿te gustaría ver estadística de los números?» | «¿cuándo jugaste por última vez? ¿cómo elegiste esos cinco números?» |
| «¿usarías una app para registrar tus jugadas?» | «¿sabes cuántos aciertos tuviste el mes pasado? ¿dónde lo miraste?» |
| «¿qué te gustaría que hiciera la aplicación?» | «¿qué hiciste la última vez que quisiste saber si habías acertado?» |

La columna izquierda pide **predecir el propio comportamiento futuro**, que las personas
hacen mal y con optimismo. La derecha pide **recordar lo que se hizo**, que lo hacen
razonablemente bien. Y la izquierda casi siempre devuelve «sí»: un «sí» a una pregunta así no
es evidencia, es cortesía.

### Las nueve preguntas de `§13` no son un paso aparte

Son la **lista de cobertura** que garantiza que el cuestionario de A2 no se dejó nada:

1. ¿Por qué existe la necesidad?
2. ¿Para qué se necesita la aplicación?
3. ¿Qué problema se quiere resolver?
4. ¿Quién tiene el problema?
5. ¿Quién usará la solución?
6. ¿Qué resultado espera obtener la empresa?
7. ¿Qué procesos existen actualmente?
8. ¿Qué restricciones existen?
9. ¿Qué sistemas actuales participan?

**Si una de las nueve no está respondida ni declarada «no se sabe», el bucle no ha
terminado.** Un «no se sabe» escrito vale más que una respuesta inventada: se convierte en
`SUP-xxx` y alguien tendrá que ir a verificarlo.

### Las cuatro vueltas

| Vuelta | Artefacto | Nota |
|---|---|---|
| 1 | `005_needs.md` | una necesidad se registra **solo cuando se puede enunciar sin nombrar una pantalla** |
| 2 | `010_actors.md` | por **función dentro de la aplicación**, nunca por el cargo. **No existe Actor Invitado** (§10) |
| 3 | `015_stakeholders.md` | pueden decidir o bloquear **sin usar la aplicación** |
| 4 | `025_constraints.md` | `RES-xxx` se respeta · `SUP-xxx` se verifica |

---

## 5. Bloque B · Lo que no se extrae

Estos tres no están en ninguna parte. **No se sacan: se deciden.**

| # | Paso | Quién | Produce |
|---|---|---|---|
| **B1** | **Comprobar el Generador** | 👤 decide · ⚙️ documenta | sigue… o **`NO CONTINÚA`** |
| **B2** | **Formular la hipótesis** con su condición de falsación | 👤 con ⚙️ | `020_hypothesis.md`, **sellada** |
| **B3** | **Decidir el alcance del prototipo** y justificarlo | 👤 | decisión + porqué escrito |

### B1 · El paso que decide si hay proyecto

> **Si el Generador no existe o no usará la aplicación, no hay razón fundamental para que la
> aplicación exista.**

La comprobación es concreta: **nombre y apellido, o un perfil real alcanzable.** «Los
clientes» no es un Generador identificado. «Las empresas que hoy llaman por teléfono para
pedir recogida, unas 40 al mes» sí lo es.

🚨 Si no se puede identificar un Generador real y alcanzable, **la fase termina aquí con un
`NO CONTINÚA`**, con su razón escrita.

### B2 · La hipótesis es la excepción del flujo

Las otras cuatro salidas se **extraen** — el material está en el brief o en la cabeza del
cliente y el trabajo es sacarlo. La hipótesis se **formula**: no está en ninguna parte, se
construye a partir de las otras cuatro, y es un acto de criterio, no de extracción. **Por eso
ningún agente la produce.**

**Una hipótesis vale si se puede escribir qué observación la tumbaría.** Si no se puede, es
un deseo.

| ❌ No sirve | ✅ Sirve |
|---|---|
| «la app va a mejorar el proceso de recogidas» | «el cliente que hoy llama por teléfono puede solicitar una recogida por sí solo, sin ayuda, en menos de 3 minutos» |
| «a los usuarios les va a gustar» | «el cliente entiende qué materiales puede entregar sin preguntarle a nadie» |

La segunda columna se observa en una sesión con un usuario. La primera no — y entonces el
Gate 1 no tiene contra qué comparar.

🚨 **Nace sellada, y es la única de las cinco.** Se piensa, se discute y se corrige **sin
commitear**; el commit es el sello. El Gate 1 comprueba en el historial que existía **antes**
de la primera sesión del prototipo y que **no cambió durante la fase**
(`git log --oneline -- _discovery/020_hypothesis.md` debe devolver **un solo commit**).
Escribir la hipótesis después es **describir lo que salió**.

### B3 · La decisión de alcance

Canónico `§14.1`. La decisión por defecto es **el Actor Generador solo** (`§17`), pero
`§17-bis.1` obliga a ampliar cuando el valor de la hipótesis dependa necesariamente de otro
actor, y `§17-bis.4` enumera los tipos de aplicación donde eso es previsible.

🚨 **No basta con registrar la decisión: hay que registrar por qué**, contrastado
explícitamente contra `§17-bis.1` y `§17-bis.4`. **Justificar la decisión por defecto también
es obligatorio**: decidir «solo el Generador» sin haber mirado `§17-bis` no es aplicar la
regla general, es no haber decidido.

---

## 6. Bloque C · El cierre

| # | Paso | Quién |
|---|---|---|
| **C1** | Declarar si la condición de salida se cumple | 🔍 **auditora** |

**Ni el agente ni la ejecutora cierran la fase.**

> El que genera no puede ser testigo de que lo generado esté completo. Con una persona el
> riesgo es que se le pase algo. **Con un generador el riesgo es el opuesto y peor: produce
> exactamente lo que la plantilla pide, siempre, tenga o no material detrás.** La plantilla se
> convierte en el molde de la respuesta.

🔴 **La condición de salida todavía no está escrita: es `TA-0015`, bloqueante.** Y su
segunda evidencia es precisamente **quién la declara** — el final del Descubrimiento **no es
un Gate**, así que `§32` no le asigna dueño automáticamente. Pendiente de decisión del
usuario; el argumento de arriba es la recomendación de la ejecutora, no un veredicto.

---

## 7. El flujo entero

```text
ENTRADAS ── E1 brief  +  E2 acceso a una persona
                    │
    ┌───────────────▼──────────────────────────────────┐
    │  BLOQUE A · bucle × 4                            │
    │  🤖 A1 extrae ─► 🤖 A2 pregunta ─► 👤 A3 responde  │
    │       ▲                                  │       │
    │       └────────── ⚙️ A4 consolida ◄──────┘       │
    │  → needs · actors · stakeholders · constraints   │
    └───────────────┬──────────────────────────────────┘
                    │
    ┌───────────────▼──────────────────────────────────┐
    │  BLOQUE B · criterio                             │
    │  B1 👤 ¿hay Generador? ──── no ──► NO CONTINÚA    │
    │  B2 👤 hipótesis + falsación (sellada, 1 commit)  │
    │  B3 👤 alcance del prototipo + justificación      │
    └───────────────┬──────────────────────────────────┘
                    │
    ┌───────────────▼──────────────────────────────────┐
    │  BLOQUE C · 🔍 la auditora declara el cierre      │
    └───────────────┬──────────────────────────────────┘
                    ▼
              GATE 1 · ¿vale la pena construir?
```

> **En una frase:** el agente extrae y pregunta · el humano responde y decide · la ejecutora
> consolida · la auditora cierra.

---

## 8. Trazabilidad al origen — la pieza que sostiene todo

### El problema

Los puntos 4 y 5 del encargo del usuario —el brief llega incompleto, y las salidas las
generan agentes— parecen dos temas. **Son una sola trampa:**

> Un hueco en el brief tiene dos salidas —ir a buscar el dato, o escribir algo plausible— y
> **en el artefacto terminado las dos se ven idénticas.**

Es la estructura de la regla dura 8: *«un rojo tiene dos salidas, y la segunda se siente como
haber arreglado algo»*. Aquí la segunda se siente como haber hecho el Descubrimiento. Y lo
agrava que un generador **siempre produce texto fluido**: la condición «hay al menos una
necesidad enunciada sin nombrar una pantalla» la satisface perfectamente una necesidad
inventada. La casilla se marca, la fase cierra, y el Gate 1 evalúa sobre ficción bien
redactada.

### La respuesta

**Cada entrada de cada artefacto lleva de dónde salió**, con tres valores y solo tres:

| Origen | Qué significa | ¿Cierra la fase? |
|---|---|---|
| `brief:<línea>` | está en el documento del cliente, citable | ✅ |
| `usuario:<fecha>` | lo respondió una persona | ✅ |
| `inferido` | lo dedujo el agente | ❌ **se degrada a `SUP-xxx`** |

Y la condición de salida gana una casilla que **una máquina puede declarar**:

> ☐ Ninguna entrada de los artefactos tiene origen `inferido`.

Se abre el archivo, se mira un campo, es cierto o es falso. **No hay juicio** — que es
exactamente lo que `TA-0015` exige con «comprobable sin interpretar».

📌 **Lo inferido no se prohíbe: se degrada.** El agente leyendo el brief *sí* debe proponer.
Lo que no puede es que su propuesta valga como hallazgo. Encaja con maquinaria que el
proyecto ya tiene: *un supuesto se anota con cómo se comprobaría*.

---

## 9. Observabilidad, evaluación y rúbrica del agente extractor

### 9.a Lo que se comprueba solo, sin criterio

| Comprobación | Cómo |
|---|---|
| Cada entrada tiene campo `origen` | falta el campo → falla |
| Ninguna cierra con `origen: inferido` | grep |
| Cada `brief:<línea>` existe y está en rango | el brief tiene 723 líneas; `brief:801` es un invento |
| El cuestionario no pregunta lo ya respondido | la palabra clave aparece en el brief → sospechoso |

Baratas, y atrapan el fraude burdo. Ninguna es la importante.

### 9.b La comprobación que sí importa: **cobertura**

> El fallo que un texto fluido esconde mejor no es la mentira. Es **la omisión.**

Un `005_needs.md` con seis necesidades bien trazadas se lee como trabajo completo aunque el
agente se haya saltado 200 líneas del brief. La comprobación va **al revés**: no se mira el
artefacto, se mira el brief.

```text
para cada sección del brief:
    ¿alguna N-xxx la cita?             → cubierta
    ¿está declarada como irrelevante?  → cubierta, con razón escrita
    ninguna de las dos                 → HUECO
```

Son dos conjuntos y una diferencia. **Ninguna cantidad de fluidez engaña a esto**, porque no
se lee la salida.

⚠️ **Con la advertencia que ya nos costó una tarea.** `TA-0020` salió porque un barrido buscó
*un formato* y no *el concepto*. Un chequeo de «no nombra pantallas» por lista de palabras
(`pantalla`, `botón`, `dashboard`) tiene ese mismo sesgo. Y `GUIDE.md` §1.b (`:138-141`) ya lo
dice: *«un patrón flojo miente, y mentir mucho es peor que no mirar»*. Sirve, pero **no puede
ser lo único**, y hay que escribir con qué se buscó.

### 9.c La rúbrica, y el error que no hay que cometer

| Dimensión | La pregunta |
|---|---|
| **Fidelidad** | ¿la línea citada sostiene lo que la entrada afirma? |
| **Desvestido** | ¿el enunciado dice el problema, o repite la solución del brief? |
| **Cobertura** | ¿cuántos huecos dejó? *(mecánico, §9.b)* |
| **Huecos bien vistos** | ¿el cuestionario pregunta lo que falta de verdad? |
| **Calidad de pregunta** | ¿pregunta por el pasado concreto o por deseos? |

🚨 **El error: puntuar de 1 a 5 sin decir qué aprueba.** Es literalmente `TA-0016` —el
canónico le puso al Gate 1 una escala en `§24` y **ningún umbral**—. Una escala sin umbral no
evalúa: produce un número que después se interpreta a conveniencia, sabiendo ya qué resultado
conviene.

**Cada dimensión se define contable o binaria**, y el umbral se fija **antes de la primera
corrida**. `GUIDE.md` §7 paso 1 (`:423`) ya lo exige para el ciclo de construcción: el
criterio lo escribe **el usuario, en prosa, antes**; si lo inventa quien construye, *«el paso
2 se vuelve teatro»*.

### 9.d Quién aplica la rúbrica

No el extractor. No otra instancia del mismo agente sobre el mismo brief:

> **Un juez LLM leyendo el mismo brief comparte el punto ciego del extractor.** Si una sección
> está redactada de forma rara y el extractor la pasó por alto, el juez probablemente también
> — porque juzga **lo que está**, no **lo que falta**.

Un juez es razonable para **fidelidad** y **desvestido**: compara dos cosas presentes. Es malo
para **cobertura**, que es la que importa. De ahí que la cobertura sea mecánica y no opinable.
El veredicto final es de la auditora.

📌 **El contrato del extractor ya está escrito** en `GUIDE.md` §8.b (`:503-507`): *«entrega
evidencia, no veredicto»* y *«lista cerrada: lo que no está en la lista no se declara limpio,
se declara NO MIRADO»*.

### 9.e Observabilidad: se guarda la corrida, no el artefacto

El `005_needs.md` no dice cómo se produjo. Sin eso, al cambiar el prompt no se puede saber si
mejoró:

| Se registra | Por qué |
|---|---|
| **hash del brief** | si el brief cambió, comparar corridas no significa nada |
| **versión del prompt / del agente** | es la variable que se está moviendo |
| **modelo y fecha** | el mismo prompt en otro modelo es otro experimento |
| **salida íntegra** | para volver a puntuarla con la rúbrica de mañana |
| **resultado de las comprobaciones** | qué pasó y qué falló, no solo el veredicto |

🔑 **Ventaja que casi ningún proyecto tiene:** todo esto ya es markdown en un repo con git. No
hace falta una plataforma de trazas — hace falta que **cada corrida sea un commit con sus
entradas fijadas**. El historial ya es el registro, y la auditora ya sabe leerlo.

### 9.f Validar los chequeos: saboteo

`GUIDE.md` §5.f (`:343`): **«ninguna prueba vale hasta verla roja»**. El chequeo de cobertura
de §9.b hay que **verlo fallar** sobre un brief con una sección omitida a propósito. Un
chequeo que solo se ha visto en verde no se distingue de uno vacío.

### 9.g El límite honesto: `n = 1`

Para saber si un cambio de prompt mejora algo hace falta un **caso de referencia** verificado.
Este brief puede ser el primero. **Pero con un solo brief no hay evaluación, hay un caso de
prueba** — un prompt ajustado contra un único ejemplo se ajusta *a ese ejemplo*. Y como lo
pedido es un proceso «aplicable a cualquier proyecto», esa es justo la parte que no
generaliza. → `SUP-009`.

---

## 10. Estado de las decisiones

### Decidido en conversación (`S-005`), pendiente de formalizar

| | Qué |
|---|---|
| ✅ | El bucle A se repite 4 veces; la hipótesis es la excepción y no la produce ningún agente |
| ✅ | El agente extractor entrega **borrador + lista de huecos**, nunca un veredicto |
| ✅ | Trazabilidad al origen con tres valores; `inferido` degrada a `SUP-xxx` |
| ✅ | La cobertura se comprueba contra el **brief**, no contra el artefacto, y es mecánica |
| ✅ | El umbral de la rúbrica se fija **antes** de la primera corrida |
| ✅ | La condición de salida se escribe **una sola vez**, en el canónico; el archivo de fase la **referencia** (`L-007`, `L-008`) |

### 🔴 Pendiente de decisión del usuario

| | Qué | Bloquea |
|---|---|---|
| **1** | **Quién declara el cierre del Descubrimiento** (C1). Recomendación: la auditora, por §6 | `TA-0015` |
| **2** | **Enmendar `D-04`** para readmitir `_phases/` y `_templates/` | `T-013`, y con ello el paso siguiente |
| **3** | Resolver la incoherencia de §3: restricciones sin salida, alcance sin plantilla | escribir plantillas |

⚠️ **Sobre la 2, y es `P-6`:** `D-04` está `Vigente` y al borrar `phases/` disolvió `DT-002`,
`DT-003` y `DT-006` con el argumento de que *«solo `phases/` las citaba»*. Los archivos que
hoy están en `_phases/` citan `_memory/` (`:187`) y `tech-debt.md` (`:195`): **`DT-003` renace
literalmente** si entran así. Volver es enmendar `D-04`, y eso es decisión del usuario.

---

## 11. Dónde vive cada pieza cuando esto se formalice

`GUIDE.md` §0 (`:50-56`) fija el reparto, y hay que respetarlo:

| Capa | Archivo | Qué se lleva de aquí |
|---|---|---|
| **Reglas** | `CLAUDE.md` | la asignación de **quién declara** el cierre (como ya hace con los Gates) |
| **Método** | `_methodology/000_method.md` | la **condición de salida** (`TA-0015`) — y **solo aquí** |
| **Fase** | `_phases/005_discovery.md` | entradas, bloques A/B, procedimiento, prohibiciones. **Referencia** la condición, no la repite |
| **Plantillas** | `_templates/_discovery/*.md` | el campo `origen` en las cinco, más la que falta para B3 |
| **Cómo con IA** | `_guide/GUIDE.md` | §9 entero: rúbrica, cobertura, observabilidad de corridas, seguridad de entrada |

🔑 **§9 no es una capa nueva: son secciones de `GUIDE.md`.** Y hay tres filas de su tabla «Lo
que se dejó fuera» (§0) cuyo motivo **ha caducado** al introducir agentes en la construcción:

| Fila | Motivo escrito | Estado |
|---|---|---|
| `:78` evaluación con jueces, rúbricas | *«aquí no hay modelo que medir»* | ❌ **caducado** |
| `:83` guardrail e inyección de prompt | *«son ataques contra un agente. No aplica»* | ❌ **caducado** — el brief lo escribe alguien de fuera y el agente lo lee |
| `:77` bucle agéntico, frenos del harness, elección de modelo | *«el producto no llama a ninguna API de IA»* | 🟡 **parcial** — cierto del producto, no de los agentes que construyen |

📌 **El material se puede recuperar porque el motivo estaba escrito.** Si esas filas dijeran
solo «no aplica», hoy no sabríamos si revisarlas. `GUIDE.md:73` lo anticipó: *«un salto sin
motivo escrito se lee como veredicto sobre lo saltado»*.

---

## 12. Orden de trabajo propuesto

```text
0 · decisiones 1 y 2 del §10                     ← usuario
1 · TA-0015 — condición de salida en el canónico,
    con trazabilidad al origen y dueño declarado  ← desbloquea el Descubrimiento
2 · GUIDE.md — levantar las tres filas de §11 y
    escribir §9 aplicado al extractor             ← barato: el archivo ya es genérico
3 · _phases/005_discovery.md — actualizar rutas,
    5ª salida, referenciar la condición,
    ejemplos genéricos
4 · _templates/ — campo origen + plantilla de B3
5 · TA-0016 — umbral del Gate 1                   ← bloqueante aparte
6 · correr el flujo sobre este brief              ← primer caso de referencia
```

---

## 13. Salvedad sobre «aplicable a cualquier proyecto»

Lo pedido es que el flujo sirva para cualquier proyecto de desarrollo de software. **Eso solo
se sabe probándolo contra más de uno.**

Lo que sí se puede garantizar es que no quede atado a RandomAI: sin ejemplos del dominio, sin
supuestos sobre el tipo de aplicación, y con las decisiones concretas en la capa de
artefactos, no en la de fase o plantilla. Que *de verdad* sea universal es una afirmación que
solo el segundo proyecto puede sostener. → `SUP-009`.
