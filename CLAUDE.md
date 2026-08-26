# RandomAI — Baloto / Revancha

Aplicación de histórico, generación de combinaciones y estadística descriptiva sobre los
sorteos de Baloto y Revancha de Colombia.

**Qué hace exactamente y hasta dónde llega → `_brief/Client_brief.txt`.**

⚠️ **Nada de tecnología está decidido todavía** — stack, base de datos, método de obtención de
datos y diseño son decisiones abiertas (brief §23). No las supongas: cuando toque, se deciden
y se registran.

## Cómo se trabaja aquí: dos terminales

| | Hace | No hace |
|---|---|---|
| **Ejecutora** (esta) | construye, corrige, registra | declarar el veredicto de un Gate; escribir en el repo de la auditora |
| **Auditora** | audita, verifica, recomienda, emite tareas `TA-nnnn` | construir la aplicación |

🚨 **El veredicto de un Gate lo emite la auditora, nunca esta terminal.** Quien construye no
puede ser su propio testigo: un sistema que se revisa a sí mismo comprueba que es coherente,
no que sea cierto. Igual con las tareas de auditoría: **que la ejecutora informe «hecho» no las
cierra.** El único estado de cierre es `Verificada`, y solo lo asigna la auditora.

📌 El principio general está en `_methodology/000_method.md`; **la asignación concreta a estas
dos terminales vive aquí y solo aquí.**

## Reglas duras — no se rediscuten

Si crees que alguna está mal, **dilo, no la cambies solo.**

1. 🚨 **El producto final no llama a ninguna API de IA.** Ni OpenAI, ni Anthropic, ni Gemini.
   La generación, la estadística y la comparación son código convencional. La IA construye
   esto; **no forma parte de esto**.
2. 🚨 **El indicador estadístico no se presenta jamás como predicción**, garantía,
   recomendación de apuesta ni probabilidad superior. Es descriptivo. Los sorteos son
   independientes y el histórico no anticipa nada.
3. **Las fuentes de `_methodology/sources/` no se editan.** Son el registro de cómo se diseñó
   el método. Ni siquiera para arreglar formato.
4. **El canónico se amplía, nunca se renumera** (`§17-bis`, no desplazar §18+). Hay
   referencias por número en repos que no podemos tocar.
5. **No se escribe en `RandomAi_Auditor/`.** Se lee, se refleja en `_persistence/tasks.md`, y
   el usuario traslada los cambios de estado.
6. **Alcance estricto.** Nada fuera del flujo definido sin definirlo antes. Lo pide el cliente
   y lo exige el método.
7. **Ningún número sin una corrida detrás.** Conteos, tamaños y porcentajes se miden, no se
   recuerdan. Si es estimación, se dice.
8. 🚨 **Ante una prueba roja se arregla el CÓDIGO.** Modificar o borrar una prueba exige
   autorización explícita **del usuario**, con la razón escrita. No de la sesión que construye,
   no de la auditora. 🔑 El porqué: un rojo tiene dos salidas —arreglar lo que rompió, o
   ablandar lo que avisó— y la segunda es más rápida, deja todo en verde y **se siente como
   haber arreglado algo**. Sin esta regla, la salida barata siempre gana.
9. **Pide el refactor de forma explícita, cada ciclo.** Dirigido al usuario: es él quien tiene
   que pedirlo. 🔑 El porqué: me detengo en verde porque *«las pruebas pasan»* es la última
   condición comprobable que me dieron. No es pereza: se acabó el criterio. ⚠️ No choca con
   `P-4` —cambios quirúrgicos—: `P-4` prohíbe refactorizar **por mi cuenta**; esta obliga a
   **preguntar** si toca, y la respuesta puede ser que no.

> 🔍 **Cómo se comprueban estas dos, porque solas no son comprobables.** El diff de las pruebas
> se mira **aparte** del diff del código: una prueba ablandada no se anuncia, solo se ve ahí. Y
> hay que comprobar **que el rojo existiera**: una prueba que nunca falló no probó nada, y
> mirando el verde no se distingue de una vacía. Procedimiento en `_guide/GUIDE.md` §7.

## Cómo se construye

**P-1. Verifica antes de afirmar.** Vale para los hallazgos ajenos y para los propios. Un
documento que se declara canónico invita a confiar en él, y esa confianza es justo lo que
impide auditarlo: **si cita a otro que tienes delante, comprueba la cita.**

**P-2. No decidas en silencio.** Ante una ambigüedad que cambie el resultado, **detente y
pregunta** — en prosa, y **una pregunta a la vez**. Las decisiones sobre método, alcance o
proceso son del usuario, no de esta terminal. Lo que se decida se registra **en el momento**.

**P-3. Nada se construye sin una razón trazable.** Toda tarea debe poder relacionarse hacia
atrás con una necesidad. Una tarea huérfana se cuestiona, no se hace.

**P-4. Cambios quirúrgicos.** Toca solo lo que la tarea necesita. No reorganices lo que
funciona ni borres lo preexistente sin permiso.

**P-5. Terminado = comprobado.** Evidencia observable: contenido de archivo, salida de
comando, resultado de prueba. **«Ya está hecho» no es evidencia.**

**P-6. Antes de eliminar algo, dos preguntas, no una.** ¿Qué depende de esto? — y sobre todo
**¿qué decisiones o restricciones se justifican en su existencia?** Borrar algo puede
satisfacer sin querer la condición de salida de una decisión tomada por otro motivo.

**P-7. Idioma: español**, también en comentarios y documentos. Los identificadores de código,
cuando exista, en inglés.

## Dónde está lo demás

Este archivo no lleva el detalle. Ábrelo cuando toque:

| carpeta | ábrela cuando… |
|---|---|
| `_brief/` | dudes qué pidió el cliente o si algo entra en el alcance |
| `_methodology/` | dudes cómo se trabaja: fases, Gates, trazabilidad, artefactos |
| `_guide/` | vayas a probar, escribir un script que salga a la red, o entregar un hallazgo |
| `_persistence/` | inicies o cierres sesión, o necesites saber por qué algo es como es |

⚠️ **Si no lo abres, no lo sabes.** No supongas el alcance ni el método: están escritos.
Inventarlos suena convincente y cuesta un rediseño.

⚠️ **`_methodology/sources/015_evolution.md` se lee por rango de líneas, no por encabezados.**
Sus secciones §35–§51 (líneas 896–1147) no llevan `#` y cualquier recorrido por encabezados las
salta. Ya costó ~200 líneas normativas una vez.

## Inicio de sesión

Al comenzar cada sesión de trabajo, antes de responder cualquier otra cosa, delega en el agente
`session-starter` y muestra su reporte al usuario. Solo después de eso atiende la petición del
usuario.

Aplica también cuando el usuario pida retomar el trabajo a mitad de conversación («¿en qué
íbamos?», «estado del proyecto»).

El procedimiento vive en la skill `protocol-start`; **no lo repliques aquí ni lo ejecutes por
tu cuenta.**

🚨 **Una sesión no es un día de trabajo: es un bloque de tiempo.** Puede haber una por la
mañana, otra por la tarde y otra por la noche del mismo día. Por eso las sesiones se
identifican por su `S-nnn` y **nunca por su fecha**: la última es la del id más alto, no la de
la fecha más reciente. Ver `D-08`.

## Cierre de sesión

Al terminar cada sesión de trabajo, delega en el agente `session-closer` y muestra su reporte
al usuario. Él recoge la evidencia con `git`, actualiza `progress.md` y `tasks.md`, propone
entradas de `debt_tec.md`, y hace el commit del día con su push.

Aplica también cuando el usuario lo pida a mitad de conversación («cerremos», «guarda el
avance», «terminamos por hoy»).

El procedimiento vive en la skill `protocol-close`; **no lo repliques aquí ni lo ejecutes por
tu cuenta.**

⚠️ **Lo que el closer NO puede hacer, y por eso es cosa tuya:** los cuatro archivos del porqué
—`decisions.md`, `assumptions.md`, `constraints.md`, `lessons.md`— **no son suyos**. Él arranca
en frío y solo ve archivos; un porqué nace en la conversación y no aparece en ningún `git
diff`. Si llegas al cierre sin haberlos escrito, esa información **ya se perdió**.

## Persistencia

`_persistence/` es la memoria de **cómo se construyó** esto, entre sesiones. Siete archivos,
cada uno con su índice arriba y sus entradas con código.

**Quién escribe cada uno depende de dónde nace la información:**

| archivo | qué guarda | cuándo se escribe |
|---|---|---|
| `progress.md` | dónde estamos y qué sigue | al cerrar sesión |
| `tasks.md` | tareas `TA-nnnn` y `T-nnn`, con estado | al cerrar sesión |
| `decisions.md` | decisiones `D-nn`, con su porqué | **en el momento** |
| `assumptions.md` | supuestos `SUP-nnn` sin comprobar | **en el momento** |
| `constraints.md` | restricciones `RES-nnn` | **en el momento** |
| `lessons.md` | lecciones `L-nnn` | **en el momento** |
| `debt_tec.md` | deuda `DT-nnn`, con estado | **en el momento** — el closer puede *proponer* |

**Por qué se parten así.** Lo que *hiciste* queda en los archivos y se puede reconstruir al
cerrar. Lo que *decidiste* no queda en ningún lado: nace en la conversación y ahí se muere.

> 🔑 **Una decisión anotada tres horas después es una decisión a medio recordar.** El porqué
> es lo primero que se evapora.

**Reglas de escritura:**

- 🚨 **Entrada e índice se actualizan juntos.** Una entrada que no está en el índice no
  existe: nadie lee el archivo entero para encontrarla. El índice lleva **números de línea** y
  **no se escriben a mano**: tras editar, `python tools/mkindex.py _persistence`.
- Un supuesto se anota **con cómo se comprobaría**. Sin eso no es un supuesto, es un deseo.
- **Los supuestos se mueren ascendiendo:** al comprobarse, salen de `assumptions.md` y entran
  en `decisions.md` o en `lessons.md`. Se borran del primero — en dos sitios, una copia acaba
  mintiendo.
- Una decisión registra **contexto, alternativas, decisión, razón y consecuencias**. Y su
  condición de levantamiento, si la tiene, **enunciada sobre el riesgo, no sobre el ejemplo
  que lo ilustra**.
- `decisions.md` es **fuente única**. No se crean archivos de decisiones aparte.
