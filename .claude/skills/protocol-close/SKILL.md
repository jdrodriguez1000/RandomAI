---
name: protocol-close
description: Protocolo de cierre de sesión del proyecto. Recoge la evidencia real del trabajo (git status, git diff, git log), actualiza de forma obligatoria _persistence/progress.md y _persistence/tasks.md, propone entradas de debt_tec.md, y solo revisa —sin escribirlos— decisions.md, assumptions.md, constraints.md y lessons.md, que son de la sesión principal; después deja la sesión cerrada con un commit y un push. Uso exclusivo del agente session-closer.
---

# Protocolo de cierre de sesión

Este protocolo lo ejecuta **únicamente** el agente `session-closer`. Su objetivo es dejar el
proyecto en un estado del que la próxima sesión pueda arrancar sola.

> 🔑 **La regla que gobierna todo el protocolo: se escribe desde la EVIDENCIA, no desde el
> relato.** No anotes «se hizo X» si X no aparece en el `git diff`.

La razón es concreta: tú no viste la conversación de hoy. Solo ves archivos. Si escribes desde
lo que te contaron, escribes rumores; si escribes desde el diff, escribes hechos.

## 🚨 Este proyecto tiene TRES actores, no dos

Antes de nada, porque condiciona el Paso 4:

| Actor | Escribe | No escribe |
|---|---|---|
| **Sesión principal** (ejecutora) | construye y registra el porqué en el momento | — |
| **Tú** (`session-closer`) | `progress.md`, `tasks.md`, propuestas a `debt_tec.md` | los cuatro del porqué |
| **Terminal auditora** | su propio repo, y **los estados `Verificada`** | no construye |

🚨 **Nunca marques una tarea `TA-nnnn` como `Verificada`.** Ese estado es el único de cierre y
**solo lo asigna la auditora**, tras comprobar la evidencia con sus propios ojos. Tú puedes
moverla a `Implementada`, que significa «lista para verificación», nunca «cerrada».

🚨 **Nunca escribas en `RandomAi_Auditor/`.** Ese repo no es nuestro. Se lee, se refleja en
`_persistence/tasks.md`, y el usuario traslada los cambios de estado.

## Paso 1 — Recoger la evidencia (antes de escribir nada)

En este orden, y sin saltarte ninguno:

```
git status
git diff
git diff --staged
git log --oneline -5
```

De ahí sale **qué pasó de verdad hoy**: qué archivos nacieron, cuáles cambiaron, y desde qué
punto se venía.

Si `git status` sale limpio y no hay nada sin commitear, **dilo y detente**: no hay sesión que
cerrar. No inventes avance para llenar el reporte.

⚠️ **Excepción única — el primer cierre del repositorio.** Si `git log` falla porque todavía no
existe ningún commit, no es un error: es el commit inicial. Sigue el protocolo normal; la
evidencia es entonces `git status`, que lista todo como sin seguimiento.

## Paso 2 — El traspaso, solo para el porqué

La sesión principal puede darte un traspaso corto: lo que se intentó, lo que se descartó, con
qué se trabó el usuario. Úsalo **solo para explicar el porqué** de lo que ya viste en el diff.

⚠️ **El traspaso nunca sustituye la evidencia.** Si el traspaso dice que se hizo algo y el diff
no lo muestra, manda el diff — y anótalo como discrepancia en el reporte.

Si no hay traspaso, el protocolo funciona igual, solo que con menos porqué.

## Paso 2b — Verificaciones previas al `git add`

Este paso es una **ranura**: contiene las comprobaciones que hay que hacer sobre el estado del
árbol **antes** de meterlo en un commit. Hoy hay una sola.

**Por qué va aquí y no más abajo, y son dos razones que importan las dos:**

- **Antes del `git add`**, porque el daño no es tener algo mal en el disco: es meterlo en el
  commit.
- 🔑 **Antes de escribir `tasks.md` (Paso 4)**, porque estas comprobaciones **producen tareas**:
  una tarea que se marca hecha si sale verde, o una tarea nueva si sale mal. Corriéndolas
  después de escribir, su resultado llegaría tarde y no habría dónde anotarlo.
- **Después de la puerta del Paso 1**, porque las noches en que no hay nada que cerrar tampoco
  hay nada que comprobar.

### 2b.1 — Los índices de `_persistence/`, ¿están al día?

Cada archivo de `_persistence/` abre con un índice que lleva el **número de línea exacto** de
cada sección. Si alguien editó un archivo y no regeneró el índice, **los números apuntan a
donde ya no está lo que dicen**, y el índice miente sin que nada falle.

```bash
python tools/mkindex.py _persistence
```

El generador es idempotente y verifica su propio resultado: imprime `lineas OK` por archivo, o
`ERROR`.

**Hay tres resultados, no dos:**

| Qué sale | Qué significa | Qué haces |
|---|---|---|
| `lineas OK` en los 7 y sin cambios en el diff | los índices ya estaban al día | sigue al Paso 3 |
| `lineas OK` pero el diff muestra cambios | estaban desfasados y se acaban de arreglar | sigue, y dilo en el reporte |
| el comando falla, o algún `ERROR` | **no lo comprobaste** | commit igual, y a **Sin resolver** |

🚨 **La tercera fila es la importante.** Si falta `python`, falta el script o el generador da
error, no sabes si los índices están al día: sabes que **no miraste**. «No pude comprobarlo» no
es «está bien», y confundir las dos cosas es cómo se cuela todo lo que se cuela. Por eso son
tres filas y no dos.

⚠️ **Entre esta comprobación y el `git add` no se edita ningún archivo de `_persistence/`.** El
control solo vale si en medio nadie toca lo que se comprobó. Es una propiedad de la que este
protocolo depende, así que queda escrita.

⚠️ **Que falle no cancela el cierre.** Commiteas y subes igual, y va al reporte.

🚨 **La línea del reporte sale siempre**, esté al día o no. Sin ella, un cierre que comprobó y
uno que no se leen idénticos.

## Cómo se escriben estos archivos

Los siete archivos de `_persistence/` tienen la misma forma: **índice arriba, tablero después,
y el detalle debajo** en secciones con su código. Las convenciones de cada uno están escritas
dentro del propio archivo, en su sección `## Convenciones`.

Los códigos de este proyecto:

| Código | Archivo | Qué es |
|---|---|---|
| `S-nnn` | `progress.md` | sesión de trabajo |
| `T-nnn` | `tasks.md` | tarea propia |
| `TA-nnnn` | `tasks.md` | tarea emitida por la auditora |
| `D-nn` | `decisions.md` | decisión |
| `SUP-nnn` | `assumptions.md` | supuesto sin comprobar |
| `RES-nnn` | `constraints.md` | restricción |
| `L-nnn` | `lessons.md` | lección aprendida |
| `DT-nnn` | `debt_tec.md` | deuda técnica |

> 🚨 **El índice y las entradas se actualizan juntos, en la misma pasada.** Una entrada que no
> está en el índice es invisible: nadie la va a encontrar, porque nadie lee el archivo entero.
> Una línea de índice sin entrada apunta al vacío. Las dos formas de dejarlo a medias mienten
> igual.

Al añadir una entrada:

1. Dale el **siguiente id libre** (mira el último del tablero, no cuentes entradas).
2. Escribe la entrada en la sección de detalle.
3. Añade su fila al **tablero**.
4. Regenera el índice con `python tools/mkindex.py _persistence` — los números de línea no se
   escriben a mano.

Fechas absolutas (`2026-08-26`), nunca «ayer» ni «la semana pasada». En el tablero, títulos
cortos: tienen que caber en una fila y decidirse sin abrir la entrada.

## Paso 3 — `_persistence/progress.md` (obligatorio)

Actualízalo **siempre**, en dos sitios:

**a) La sección `## 1. Dónde estamos`**, arriba. Es lo único que se lee al abrir sesión, así
que se sobrescribe entera: fase, estado, bloqueo activo y situación en una frase.

**b) Una entrada nueva `S-nnn`** en la sección de sesiones, más su fila en el tablero, con:

1. **¿En qué fase del método va el proyecto?** (ver `_methodology/000_method.md`)
2. **¿Qué quedó hecho hoy?** — solo lo que está en el diff.
3. **¿Cuál es el siguiente paso concreto?** No «seguir con la auditoría», sino la primera
   acción de mañana.

### 🚨 La pregunta NO es «¿está el archivo al día?»

Es: **«¿tiene ESTA sesión su propia fila, con un id nuevo?»**

```
grep -n '^| `S-' _persistence/progress.md | head -1
```

🚨 **El criterio es el ID, no la fecha.** Esa fila tiene que llevar el id de ESTA sesión: uno
**más alto** que el `S-nnn` que había al arrancar. Si arriba sigue el mismo id con el que
empezaste, **falta la entrada** — y hay que escribirla, diga lo que diga la sección
`Dónde estamos`.

⚠️ **Por qué el criterio no puede ser la fecha.** Puede haber **varios cierres el mismo día**.
Comparar fechas no distingue dos tramos de la misma jornada: la última fila ya llevaría la
fecha de hoy siendo de otra sesión, y el control daría verde con la sesión entera sin registrar.

🔑 **Dos señales van a engañarte, y las dos se repiten:**

- **`Dónde estamos` puede estar ya escrita**, porque la sesión principal la actualiza durante
  el día. **Un archivo medio actualizado es peor que uno sin tocar: el trozo bueno avala al
  malo.**
- **Un árbol limpio no prueba que la entrada esté escrita.** Significa «no queda trabajo», pero
  también puede significar «el trabajo se commiteó antes de que llegara el cierre».

## Paso 4 — `_persistence/tasks.md` (obligatorio)

Aquí el tablero **es** el archivo: el estado de cada tarea vive en su fila.

**Los estados de este proyecto:**

`No implementada` · `En curso` · `Implementada` · `Cancelada` · `Suspendida`

- Mueve a `Implementada` solo lo que la evidencia respalde.
- Deja en `En curso` lo que quedó a mitad, y di **en qué punto** quedó — eso sí baja al detalle,
  porque no cabe en una fila.
- `Cancelada` y `Suspendida` **requieren razón registrada**. Si no tienes la razón, no cambies
  el estado: pregúntalo en el reporte.
- Añade las tareas nuevas que aparecieron hoy, con su id.

🚨 **`Verificada` no lo escribes tú, nunca.** Ver la tabla de los tres actores, arriba.

Una tarea que se entiende en una línea **se queda en el tablero** y no baja al detalle. No
infles el archivo.

Si una tarea estaba marcada como hecha y el diff la contradice, **desmárcala** y dilo en el
reporte.

**Aquí entra también lo que produjo el Paso 2b**, que ya corriste: si los índices salieron al
día, no hay nada que anotar; si fallaron o no se pudieron comprobar, la tarea nueva se añade
con su id. Ese es el motivo de que aquel control vaya arriba y no abajo.

### 🚨 Lo único que NO puede entrar aquí: el resultado del push

**El push no se anota en `tasks.md`, y no es un olvido: es imposible.** Para saber si el push
funcionó, el commit ya tiene que existir — y `tasks.md` va dentro de ese commit. Cualquier cosa
que quisieras escribir aquí sobre el push se escribiría antes de que el push ocurriera.

🔑 **Un segundo commit tampoco lo arregla:** tendría exactamente el mismo problema con su propio
push, y así hasta el infinito. No hay orden de pasos que lo resuelva.

**Su sitio es el reporte de hoy**, en «Sin resolver» (Paso 6b y Paso 7). Y el arranque de mañana
debe leer `git status -sb` —no `--short`— porque `--short` no imprime la línea de la rama y un
commit sin subir le resulta **invisible**.

## Paso 5 — `_persistence/debt_tec.md`: aquí sí propones

La deuda técnica es el único registro del porqué que **sí deja rastro en la evidencia**: algo a
medias, un `TODO`, una comprobación que quedó sin hacer, un archivo que quedó inconsistente.

Por eso, a diferencia de los cuatro de abajo, **puedes proponer entradas** — con dos condiciones:

1. **Solo lo que el diff respalde.** Nada de deuda intuida.
2. **Marcada como propuesta en el reporte**, para que el usuario la confirme o la tumbe.

Los estados: `Abierta` · `En curso` · `Implementada` · `Aceptada` · `Descartada`.

⚠️ **`Aceptada` y `Descartada` no las escribes tú:** significan «decidimos convivir con esto» y
«esto dejó de ser deuda», y las dos son decisiones del usuario, no lecturas del diff.

## Paso 6 — Los otros cuatro: **revísalos, no los escribas**

`decisions.md`, `assumptions.md`, `constraints.md` y `lessons.md` **no son tuyos**. Los escribe
la sesión principal, en el momento en que las cosas pasan, porque una decisión no aparece en el
`git diff`: nace en la conversación.

Tú no estuviste ahí. Escribirlos sería inventar.

**Lo que sí haces: comprobar que no se quedaron cortos.**

1. Léelos.
2. Compáralos con lo que muestra el diff.
3. Si el diff enseña algo que **claramente fue una decisión** y no está anotado —se eligió una
   alternativa, se cambió una estructura, se descartó un camino— **no lo escribas tú**:
   señálalo en el reporte, para que el usuario lo dicte.

🚨 **Los cuatro se reportan siempre, aunque no falte nada.** El Paso 8 tiene una sección propia
para ellos: cada uno sale con «al día» o con lo que falta por anotar. Sin esa línea, un cierre
que revisó y uno que no revisó se ven igual.

### 🚨 Una casilla más, obligatoria: qué entra al repositorio público

**El repositorio de este proyecto es público, y `_persistence/` va a Git a propósito** — es la
historia del proyecto. Así que pregunta, en voz alta, sobre el diff de hoy:

> **¿Entró algo que no debería ser público?** Credenciales, tokens, rutas personales, datos de
> terceros, contenido de fuentes externas copiado sin necesidad.

Si entró, **sale** — y se sustituye por un equivalente inventado, dicho como inventado.

⚠️ **Honestidad sobre su fuerza, y va escrito porque importa: esto pregunta, no detecta.** No es
un test y no muerde. `.gitignore` cubre `.env`, pero **no cubre una credencial pegada dentro de
una lección**. Ese es el camino por el que algo se escapa sin que ninguna herramienta lo note.
**Marcarla sin haber mirado el diff es marcarla con una intención.**

📌 Se reporta siempre, igual que los cuatro.

**La única excepción, y es mecánica:** si un supuesto de `assumptions.md` quedó comprobado por
la evidencia del diff, puedes moverlo a `decisions.md` o `lessons.md` y borrarlo de
`assumptions.md`. Eso no es interpretar, es aplicar la regla del ascenso — y **dilo en el
reporte**. Al moverlo, toca **los dos tableros**: la fila sale del de origen y entra en el de
destino, con id nuevo, y se regenera el índice.

## Paso 7 — El commit y el push

**Primero la verificación, después el commit.** Nunca al revés.

```
git status
```

🚨 Comprueba que **no aparezca ningún archivo de secretos** (`.env` y variantes). Si aparece,
**detente**, no añadas nada y repórtalo: falta una línea en `.gitignore`. Git no olvida — si una
credencial entra al historial, borrar el archivo después no la borra.

Si está limpio:

```
git add -A
git commit -m "..."
```

El mensaje dice **qué avanzó y por qué**, no qué archivos cambiaron: eso ya lo sabe Git.
Primera línea corta, y debajo lo que valga la pena. Termina siempre con:

```
Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

⛔ **Comandos prohibidos, sin excepción:** `git commit --amend`, `git reset`, `git checkout --`,
`git restore`, `git rebase`, `git clean`, `git push --force` y cualquier otra cosa con
`--force`. Tu trabajo es **añadir** historia, nunca reescribir ni borrar la que hay.

### El cierre no acaba en el commit

```
git push
```

⚠️ **Si es el primer push del repositorio**, la rama todavía no existe en el remoto:

```
git push -u origin main
```

🔑 **Un `git push` a secas solo añade, y por eso sí es tuyo** — encaja con la regla de arriba,
no la rompe. Lo que reescribe historia es `--force`, y ese sigue prohibido.

Después, siempre:

```
git status -sb
```

🚨 **Si la primera línea todavía dice `ahead`, el push no ocurrió** —remoto sin configurar,
credenciales, red— y el trabajo existe solo en este disco. **No lo tapes:** va en el reporte, en
«Sin resolver», con lo que salió mal. Un disco roto esa noche se lleva la sesión entera.

⚠️ **Y ahí se queda: en el reporte.** No vuelvas atrás a anotarlo en `tasks.md` —ya está
commiteado— ni abras un commit nuevo para arreglarlo. El porqué está en el Paso 4.

> 🔑 La regla no es «si no hay hash, no hubo cierre»: eso se cumple entero y el trabajo se queda
> sin subir igual, porque **un commit es local**. La regla es **«si el hash no está en
> `origin`, no hubo cierre»**, y se comprueba con `git status -sb`, no con el hash.

## Paso 8 — Reporte en pantalla

En español, sin relleno:

```
## Cierre de sesión — <fecha>

### Lo que dice la evidencia
- <N> archivos tocados: <los principales>
- <qué quedó hecho, según el diff>

### _persistence/ actualizado
- progress.md — <S-nnn nueva> · <en una línea, qué cambió en «Dónde estamos»>
- tasks.md — <N implementadas, N pendientes, N nuevas>
- debt_tec.md — <sin novedad | PROPUESTA: DT-nnn ... (pendiente de confirmar)>

### Los cuatro del porqué — revisados, no escritos
- decisions.md — <al día | falta anotar: ...>
- assumptions.md — <al día | falta anotar: ... | ascendido SUP-nnn → D-nn>
- constraints.md — <al día | falta anotar: ...>
- lessons.md — <al día | falta anotar: ...>
- 🚨 Repositorio público — <nada sensible, diff mirado | 🚨 SACAR: ...>

### Commit
Índices de `_persistence/` — <al día | regenerados | 🚨 SIN COMPROBAR — <qué falló>>
<hash corto> — <primera línea del mensaje>
<"subido a origin, `git status -sb` sin ahead" | 🚨 "SIN SUBIR — <qué falló>">

### Para mañana
<el siguiente paso concreto, tal como quedó en progress.md>

### Sin resolver        <-- omitir si no hay nada
- <discrepancias entre el traspaso y el diff>
- <lo que quedó a medias y en qué punto>
- <lo que hay que preguntarle al usuario>
```

## Reglas del protocolo

- **No inventes** avances, fechas, decisiones ni tareas.
- **No escribas código** ni arregles nada, aunque veas algo roto. Anótalo en `tasks.md` y sigue.
  Cerrar la sesión no es el momento de abrirla otra vez.
- **No toques `_brief/` ni `_methodology/`.** Describen el encargo y el método, no la sesión. Y
  las fuentes de `_methodology/sources/` **no se editan nunca**, ni para arreglar formato.
- **No dupliques.** Cada archivo tiene un trabajo: si algo ya está escrito en `_methodology/`,
  no lo repitas en `_persistence/`.
- **Escribe corto.** Un `progress.md` que nadie lee no orienta a nadie.
