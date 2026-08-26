---
name: protocol-start
description: Protocolo de inicio de sesión del proyecto RandomAI. Lee de forma obligatoria el estado de git, CLAUDE.md, _persistence/progress.md, _persistence/tasks.md y el tablero de la terminal auditora; a demanda decisions.md, assumptions.md, constraints.md, lessons.md y debt_tec.md. Con eso presenta en pantalla dónde está el proyecto, las últimas tareas realizadas y las siguientes. Uso exclusivo del agente session-starter.
---

# Protocolo de inicio de sesión

Este protocolo lo ejecuta **únicamente** el agente `session-starter`. Su objetivo es
reconstruir el estado del proyecto al comenzar una sesión y presentar un resumen accionable.

**Es de solo lectura.** No modifica ningún archivo.

## 🚨 Qué es una sesión en este proyecto

Una sesión **no es un día de trabajo**: es un bloque de tiempo. Puede haber una sesión por la
mañana, otra por la tarde y otra por la noche **del mismo día**.

> 🔑 **Consecuencia directa: las fechas no identifican sesiones. Los ids `S-nnn` sí.**

Nunca digas «la sesión de ayer» ni «la última sesión, del 26». Di **`S-007`**. Y para saber
cuál fue la última, mira el **id más alto**, nunca la fecha más reciente: varias filas pueden
compartir fecha siendo sesiones distintas, y ordenar por fecha las mezcla.

## Este proyecto tiene TRES actores

Condiciona el Paso 1c, que en otros proyectos no existe:

| Actor | Qué deja escrito |
|---|---|
| **Sesión principal** (ejecutora) | construye, y registra el porqué en el momento |
| **`session-closer`** | `progress.md`, `tasks.md`, propuestas de deuda, el commit |
| **Terminal auditora** | su propio repo `RandomAi_Auditor/`, y los estados `Verificada` |

La auditora trabaja **fuera de nuestras sesiones**. Puede haber verificado, rechazado o emitido
tareas entre anoche y ahora, y **nada en nuestro repo se entera solo**. Por eso hay que mirarla.

## Paso 1 — Evidencia obligatoria

Lee siempre, sin excepción, y **en este orden**.

### 1a. Primero el repositorio — es el hecho, no el relato

```
git log --oneline -5
git status -sb
```

🚨 **`-sb`, no `--short`.** Los dos listan los archivos sueltos, pero solo `-sb` imprime **la
línea de la rama**, que es donde se ve si la sesión anterior subió su trabajo:

```
## main...origin/main [ahead 1]      <-- hay un commit que no está en origin
```

Con `--short` esa línea no sale. Un commit sin subir es **invisible**: el repo se ve limpio, el
arranque no dice nada, y el trabajo de anoche existe solo en este disco.

⚠️ **Si `git log` falla porque no hay commits todavía**, no es un error: el repositorio está
recién creado. Dilo y sigue.

### 1b. Después, los tres archivos que siempre se leen

1. **`CLAUDE.md`** — qué es el proyecto y cómo se trabaja. Es corto a propósito y es el **ancla
   contra inventar**.
2. **`_persistence/progress.md`** — dónde estamos, qué se hizo, qué sigue.
3. **`_persistence/tasks.md`** — tareas con su estado.

De los dos de `_persistence/` lee **el índice y el tablero**, no el archivo entero. Ver *«Cómo
se leen estos archivos»* más abajo.

Si alguno no existe o está vacío, **dilo en el reporte** en lugar de inventar contenido.

### 1c. Y el tablero de la auditora

```
../RandomAi_Auditor/audits/tasks_audit.md
```

Lee su **Tablero** y compáralo con el de `_persistence/tasks.md`. Son dos copias de la misma
realidad y **pueden haberse separado desde la última sesión**.

🚨 **La auditora manda sobre los estados `TA-nnnn`.** Si su tablero dice `Verificada`,
`Rechazada` o `Descartada` y el nuestro dice otra cosa, **el suyo es el bueno** — nuestro
`tasks.md` es un espejo, y `Verificada` solo lo asigna ella.

⚠️ **No corrijas el desfase tú: repórtalo.** Este protocolo es de solo lectura, y actualizar
nuestro espejo es trabajo de la sesión. Y **nunca** escribas en `RandomAi_Auditor/`.

### Por qué el `git` va primero

> 🔑 **`progress.md` es lo que alguien escribió que pasó. `git log` es lo que pasó.**

Un archivo de estado puede quedar desactualizado —una sesión que se cayó, un cierre a medias— y
no tiene forma de avisarlo. El repositorio sí. Al leerlo primero, entras a los archivos ya
sabiendo si se les puede creer.

### Cinco desfases que hay que reportar

| Lo que ves | Qué significa | Dilo así |
|---|---|---|
| el último commit **no** aparece reflejado en `progress.md` | la sesión anterior no cerró bien | *«⚠️ `progress.md` va por detrás del último commit»* |
| `git status` tiene cambios sin commitear | quedó trabajo suelto | *«⚠️ hay N archivos sin commitear»* |
| la primera línea de `git status -sb` dice `ahead` | la sesión anterior **no subió** | *«🚨 N commits sin subir a `origin` — el trabajo existe solo en este disco»* |
| hay commits que tocan `_persistence/` **posteriores** al último que tocó `progress.md` | el archivo de estado se selló antes que la última entrada | *«⚠️ `progress.md` se selló en `<hash>` y hay N commits posteriores de `_persistence/`»* |
| el tablero de la auditora y nuestro `tasks.md` discrepan | la auditora avanzó fuera de nuestras sesiones | *«⚠️ `TA-nnnn` figura `<X>` en la auditora y `<Y>` en nuestro espejo»* |

La cuarta se comprueba con **dos** órdenes, no con una:

```
git log --oneline -3
git log --oneline -2 -- _persistence/progress.md
```

Si el hash de arriba **no** es el mismo que el de abajo, mira qué tocaron los commits de en
medio. Si tocaron `_persistence/` y `progress.md` no está entre ellos, **el estado quedó
congelado antes que la última entrada**.

> 🔑 **Y el error va en la dirección cara.** Un estado que dice *«ya está hecho»* cuando falta
> se descubre solo: alguien va a hacerlo y no lo encuentra. Uno que dice **«falta»** sobre algo
> terminado **no se descubre — se paga repitiéndolo**, y se paga con la sesión que este
> protocolo existe para ahorrar.

🚨 **La tercera es la única que se pierde para siempre.** Las dos primeras son desorden: el
trabajo está guardado, solo mal contado. En la tercera **no está guardado en ningún otro
sitio** — un disco que falle esa noche se lleva la sesión entera.

Es también la única que **no puede haberse anotado en `tasks.md`**: cuando el cierre supo que
el push había fallado, su commit ya estaba hecho. Por eso el arranque tiene que mirarlo con sus
propios ojos en vez de fiarse de los archivos. El razonamiento completo está en
`protocol-close`, Paso 4.

Si la ves, **dilo arriba del todo y propón subirlo como primera acción.**

Si detectas cualquier desfase, **el reporte lo dice arriba del todo**, antes del estado.

### 🚨 La regla que manda sobre todas

**Todo lo que digas sobre QUÉ ES el proyecto tiene que salir de un archivo que abriste en esta
corrida.** Si no lo abriste, no lo digas.

Vale para el alcance, la tecnología, el método y qué significa cada fase. **No completes con lo
que suele llevar un proyecto de este tipo.** Aquí hay 13 decisiones técnicas explícitamente
abiertas: cualquier cosa que suene razonable sobre el stack **está inventada**.

Si algo no está escrito en ningún sitio, di **«no está registrado»**. Es una respuesta válida y
útil. Rellenarlo no lo es.

## Paso 2 — Lectura a demanda

Estos archivos **no** se leen por defecto. Léelos solo cuando algo del Paso 1 lo justifique, y
teniendo clara **qué pregunta concreta** quieres responder con cada uno:

| Archivo | Léelo cuando… |
|---|---|
| `_persistence/decisions.md` | progress/tasks mencionen una decisión, un cambio de rumbo, o una tarea dependa de una previa |
| `_persistence/constraints.md` | las siguientes tareas toquen áreas con límites conocidos |
| `_persistence/assumptions.md` | haya tareas apoyadas en supuestos sin confirmar, o supuestos que puedan haber caducado |
| `_persistence/lessons.md` | se vaya a repetir un tipo de trabajo que ya falló antes |
| `_persistence/debt_tec.md` | haya deuda que bloquee lo siguiente, o propuestas del cierre sin confirmar |
| `_brief/Client_brief.txt` | haya dudas sobre qué pidió el cliente. **Es largo: ve a la sección concreta** |
| `_methodology/000_method.md` | haya dudas sobre la fase, los Gates o los artefactos |

⚠️ **`_methodology/sources/015_evolution.md` se lee por rango de líneas, no por encabezados.**
Sus secciones §35–§51 (líneas 896–1147) no llevan `#` y un recorrido por encabezados las salta.

## Cómo se leen estos archivos

Los siete archivos de `_persistence/` tienen la misma forma: **índice arriba, tablero después,
detalle debajo**.

> 🔑 **El tablero es la respuesta por defecto; el detalle es la excepción.**

1. **Lee el índice**, que trae el **número de línea exacto** de cada sección.
2. **Decide desde el tablero.** La mayoría de las veces el título y el estado bastan.
3. **Baja al detalle solo si el tablero no responde**, saltando a la línea que dice el índice —
   no leyendo el archivo de arriba abajo.

Un archivo de `_persistence/` puede crecer mucho. Leerlo entero para sacar una línea del
reporte gasta contexto que hará falta después, cuando toque trabajar.

### 🚨 El campo de estado manda sobre la prosa

En los tableros, cada fila termina en su **estado**. **Para decir qué falta, lee el CAMPO — no
resumas el párrafo del detalle.**

> 🔑 **El párrafo cuenta la historia de la entrada; el campo dice cómo acabó.** Cuando alguien
> corrige una entrada suele reescribir el párrafo y **olvidarse del campo**, o al revés. Si los
> dos se contradicen, **no elijas: repórtalo como desfase** y sigue el campo mientras tanto.

Extraer los campos cuesta una orden y no gasta contexto:

```
grep -n '^| `T' _persistence/tasks.md | grep -E '`No implementada`|`En curso`'
```

### 🚨 Lo cerrado no se reporta como abierto

Aquí nada se tacha: **el estado va en su columna**, y hay que leerlo.

| Archivo | No reportes como abierto |
|---|---|
| `tasks.md` | `Implementada` · `Cancelada` · `Suspendida` |
| `debt_tec.md` | `Implementada` · `Aceptada` · `Descartada` |
| `decisions.md` | `Revertida` · `Superada por D-nn` |
| `assumptions.md` | `Confirmado` · `Refutado` · `Obsoleto` |

Una entrada cerrada **conserva su texto a propósito**, para que se entienda qué se creía y por
qué dejó de valer. **Ese texto está ahí para explicar, no para reportarlo como vigente.** Si
hace falta mencionarla, se dice *«`DT-003`, descartada»* — nunca lo que decía cuando estaba
abierta.

```
grep -n '`Cancelada`\|`Descartada`\|`Aceptada`\|`Superada por`\|`Refutado`' _persistence/*.md
```

### 🚨 Y el caso más traicionero: la entrada revisada

Una entrada puede seguir **`Vigente`** y aun así tener su fundamento cambiado más abajo, en una
sección de **revisión** dentro de la propia entrada.

> 🔑 **Quien lee solo el principio se lleva el motivo viejo, y el estado le confirma que está
> vigente.** No hay ninguna marca en el tablero que avise.

Antes de citar el *porqué* de una decisión, **comprueba si su entrada tiene una revisión
posterior**, y cita esa. Si el tablero te da un número o una condición, **contrástalo con la
entrada completa antes de reportarlo** — es lo único que separa un dato de un recuerdo.

## Paso 3 — Reporte en pantalla

En español, sin relleno:

```
## ⚠️ Desfase detectado        <-- omitir si no hay ninguno
- <qué no cuadra entre el repositorio, los archivos y el tablero de la auditora>

## Dónde estamos
<fase del método, estado y bloqueo activo, según progress.md>
<última sesión: S-nnn>

## Últimas tareas realizadas
- <código> <tarea>
- ...

## Siguientes tareas
🔻 <bloqueo o condición vigente, si lo hay>   <-- obligatorio si existe, y va PRIMERO
1. <código> <tarea> — <por qué es la siguiente>
2. ...

## Contexto relevante        <-- omitir si no leíste archivos del Paso 2
- **Decisiones:** ...
- **Restricciones:** ...
- **Supuestos:** ...
- **Lecciones:** ...
- **Deuda:** ...
```

Reglas del reporte:

- 🔻 **Un bloqueo vigente es OBLIGATORIO si existe, y va el primero de «Siguientes tareas».**
  Búscalo en `progress.md` y en `debt_tec.md`.
- ⚠️ **Un bloqueo se cita por su ACCIÓN, no por la fecha en que se espera.** Escribirlo como
  *«lo primero de la próxima fase»* lo deja gastado en cuanto esa fase empieza.
- 🚨 **Un bloqueo no se cuelga de una tarea que no lo tiene.** Si no sabes de cuál es, **dilo
  suelto: el bloqueo importa más que su dueño.**
- 🚨 **No inventes relaciones entre tareas.** Cada una se describe con lo que dice **su** fila.
  Si dos se parecen, no se mezclan: se citan las dos por su código.
- **Distingue las dos familias de tareas.** `TA-nnnn` las emite la auditora y solo ella las
  cierra; `T-nnn` son nuestras. No las presentes como una sola lista sin decir cuál es cuál.
- Máximo 5 elementos por lista; si hay más, quédate con los más recientes o prioritarios y
  dilo.
- Cita el archivo de origen cuando un dato pueda ser ambiguo.
- **Contexto relevante** solo con lo que cambie la decisión de qué hacer ahora, no como resumen
  de los archivos.
- Termina señalando bloqueos o información faltante, si los hay.
- **No modifiques ningún archivo.** Este protocolo es de solo lectura.
