# GUIDE.md — Cómo se ejecuta el trabajo con IA en RandomAI

> **Razón trazable:** brief §22 — *«este proyecto servirá como ejercicio para aprender a
> desarrollar software utilizando inteligencia artificial como asistente»*. Esa es una de las
> dos entregas del proyecto, y hasta hoy no tenía sitio propio.

**Última actualización:** 2026-08-26

<!--INDEX-->

## Índice

> **Búsqueda rápida.** Salta con el enlace, o ve directo a la línea indicada (exacta, ya contando este índice).
> Por código: `grep -n 'sabotea' GUIDE.md`

| Línea | Sección | Ir a |
|---|---|---|
| `48` | **0. Qué es esto, y qué no** | [↓](#0-qué-es-esto-y-qué-no) |
| `61` | &nbsp;&nbsp;↳ Origen y traducción | [↓](#origen-y-traducción) |
| `71` | &nbsp;&nbsp;↳ Lo que se dejó fuera, con su motivo | [↓](#lo-que-se-dejó-fuera-con-su-motivo) |
| `87` | **1. Qué nunca sube a Git** | [↓](#1-qué-nunca-sube-a-git) |
| `108` | &nbsp;&nbsp;↳ 1.b Auditar el historial | [↓](#1b-auditar-el-historial) |
| `149` | **2. Dos shells en la misma máquina, dos gramáticas** | [↓](#2-dos-shells-en-la-misma-máquina-dos-gramáticas) |
| `179` | **3. Las tres preguntas** | [↓](#3-las-tres-preguntas) |
| `208` | **4. Nada corre solo por defecto** | [↓](#4-nada-corre-solo-por-defecto) |
| `254` | **5. Cómo se prueba** | [↓](#5-cómo-se-prueba) |
| `263` | &nbsp;&nbsp;↳ 5.a El caso de prueba es un DATO, no código repetido | [↓](#5a-el-caso-de-prueba-es-un-dato-no-código-repetido) |
| `271` | &nbsp;&nbsp;↳ 5.b Las tres familias, y la que todo el mundo se salta | [↓](#5b-las-tres-familias-y-la-que-todo-el-mundo-se-salta) |
| `295` | &nbsp;&nbsp;↳ 5.c Las seis reglas | [↓](#5c-las-seis-reglas) |
| `311` | &nbsp;&nbsp;↳ 5.d Pruebas de coherencia — las que cazan olvidos | [↓](#5d-pruebas-de-coherencia--las-que-cazan-olvidos) |
| `327` | &nbsp;&nbsp;↳ 5.e Lo que cambia el mundo: efectos secundarios | [↓](#5e-lo-que-cambia-el-mundo-efectos-secundarios) |
| `341` | &nbsp;&nbsp;↳ 5.f 🚨 Comprueba que tus pruebas sirven: sabotea | [↓](#5f--comprueba-que-tus-pruebas-sirven-sabotea) |
| `370` | &nbsp;&nbsp;↳ 5.g El límite, que hay que saber decir | [↓](#5g-el-límite-que-hay-que-saber-decir) |
| `377` | **6. Preflight: falla temprano, de barato a caro** | [↓](#6-preflight-falla-temprano-de-barato-a-caro) |
| `410` | **7. 🚨 El ciclo cuando el que teclea es un agente** | [↓](#7--el-ciclo-cuando-el-que-teclea-es-un-agente) |
| `419` | &nbsp;&nbsp;↳ El reparto, en cuatro pasos | [↓](#el-reparto-en-cuatro-pasos) |
| `433` | &nbsp;&nbsp;↳ Las dos reglas duras | [↓](#las-dos-reglas-duras) |
| `442` | &nbsp;&nbsp;↳ Lo que se mira, y es barato y local | [↓](#lo-que-se-mira-y-es-barato-y-local) |
| `452` | &nbsp;&nbsp;↳ 🚨 Y una tentación que hay que nombrar para no caer en ella | [↓](#-y-una-tentación-que-hay-que-nombrar-para-no-caer-en-ella) |
| `464` | **8. Cuándo crear un subagente** | [↓](#8-cuándo-crear-un-subagente) |
| `490` | &nbsp;&nbsp;↳ 8.b Evidencia, nunca veredicto | [↓](#8b-evidencia-nunca-veredicto) |
| `518` | **9. Cómo se entrega un hallazgo** | [↓](#9-cómo-se-entrega-un-hallazgo) |

<!--/INDEX-->

---

## 0. Qué es esto, y qué no

Tres archivos y tres trabajos distintos. Si dos dicen cosas distintas, manda el de la izquierda:

| Archivo | Qué es | Ejemplo |
|---|---|---|
| **`CLAUDE.md`** | las **reglas** — qué está prohibido y qué es obligatorio | *«ante un test rojo se arregla el código»* |
| **`_methodology/000_method.md`** | el **método** — fases, Gates, trazabilidad | *«el prototipo valida el camino feliz del Generador»* |
| **`_guide/GUIDE.md`** *(este)* | el **cómo** — procedimientos, órdenes concretas, formatos | *«el diff de los tests se mira aparte del diff del código»* |

🚨 **Este archivo no repite reglas.** Si una regla vive en `CLAUDE.md`, aquí se cita y no se
copia — una segunda fuente de verdad envejece sin avisar (`L-007`).

### Origen y traducción

Se extrajo de `GUIDE.md` de un proyecto anterior, que construía un agente que **sí** llamaba a
una API de IA. Aquí el producto **no llama a ninguna** (brief §21, `RES-001`), así que más de
la mitad de aquella guía no aplica y **no se trajo**. Cada sección cita su origen con `↳`.

⚠️ **Ningún número de aquel proyecto se copió.** Sus cifras se midieron en otra máquina, con
otro stack y otro modelo. Regla dura 7: *ningún número sin una corrida detrás*. Donde hace
falta un umbral, se mide aquí o se registra como `SUP-nnn` con cómo comprobarlo.

### Lo que se dejó fuera, con su motivo

Un salto sin motivo escrito se lee como veredicto sobre lo saltado.

| Qué | Por qué no está |
|---|---|
| Bucle agéntico, frenos del harness, streaming, elección de modelo, precios, ventanas de contexto, `count_tokens`, `thinking` | El producto no llama a ninguna API de IA (`RES-001`) |
| Evaluación con jueces, rúbricas, intervalos de confianza sobre corridas del modelo | Miden la conducta de un modelo. Aquí no hay modelo que medir |
| Depuración de prompts · Skills · TypeScript | Vetado explícitamente por el usuario, y presupone stack |
| El «ciclo B» de conducta y sus líneas base | Mismo motivo: mide un modelo. Del ciclo de trabajo solo se trae lo que sostiene §7 |
| Memoria persistente del producto | Es memoria del *producto* sobre sus usuarios. Nuestra `_persistence/` es memoria del *proceso*. Confundirlas sería un error |
| El mapa de archivos de aquel repo | Se trae la **regla** —Git no olvida—, no su tabla |
| Guardrail e inyección de prompt | Son ataques contra un agente. No aplica |

---

## 1. Qué nunca sube a Git

↳ *GUIDE §2*

⚠️ **Git no olvida.** Borrar un archivo después **no lo borra del historial**. Por eso lo que
nunca debe subir se decide **antes** del primer commit, no después.

Hoy, en este proyecto:

| Qué | ¿Sube? |
|---|---|
| `_brief/`, `_methodology/`, `_persistence/`, `_guide/`, `CLAUDE.md`, `tools/` | **Sí.** Son la historia del proyecto |
| `.env` y variantes | ❌ **Nunca.** Ya está en `.gitignore` |
| Credenciales, tokens, rutas personales | ❌ **Nunca**, y `.gitignore` **no las cubre** si están pegadas dentro de un `.md` |

🚨 **El repositorio es público** (`RES-010`), y `_persistence/` va a Git a propósito. El camino
por el que algo se escapa **no es el archivo grande que alguien vigila: es el ejemplo pequeño
dentro de una lección que nadie revisó.**

📌 Cuando se decida el stack, esta tabla se amplía **el mismo día**, no la semana siguiente.

### 1.b Auditar el historial

↳ *GUIDE §2.b*

Responde una sola pregunta: **¿entró alguna vez algo que no debía?**

🚨 **Lo corre la terminal auditora, no la ejecutora** (`RES-008`): quien construye no puede ser
su propio testigo. Y **llega tarde**: el primer commit público ya se hizo. El marco «se decide
antes del primer commit» ya no nos protege, así que la auditoría deja de ser preventiva y pasa
a ser una comprobación de daños.

Las tres preguntas, en PowerShell:

```powershell
# 1. ¿Existió alguna vez un archivo prohibido? (mira NOMBRES, no contenido)
git log --all --name-only --pretty=format: | Sort-Object -Unique |
  Select-String -Pattern '^\.env$|\.pem$|\.key$'

# 2. ¿Entró alguna vez una credencial? (mira CONTENIDO de todos los commits)
git log -p --all | Select-String -CaseSensitive -Pattern `
  'sk-ant-[A-Za-z0-9_-]{20,}', 'ghp_[A-Za-z0-9]{36}', `
  '-----BEGIN [A-Z ]*PRIVATE KEY-----'

# 3. ¿Entró un correo personal? (el patrón, no una dirección escrita aquí)
git log -p --all | Select-String -Pattern '[A-Za-z0-9._%+-]+@(gmail|hotmail|outlook)\.com'
```

**Lo esperado es CERO en las tres.** Si alguna devuelve algo, el arreglo **no** es borrar el
archivo: es rotar la credencial. Es más barato y más seguro que reescribir historia publicada.

> 🚨 **Un patrón flojo miente, y mentir mucho es peor que no mirar.** Un detector que grita
> veinte veces y las veinte son falsas **es un detector que dejarás de mirar**. El día que haya
> algo de verdad, tus ojos ya aprendieron a saltárselo. Ancla los patrones al **formato** de lo
> que buscas —longitud, prefijo, `-CaseSensitive`— nunca a una palabra suelta.

📌 **Y un patrón solo es creíble después de verlo en rojo.** Antes de fiarte de estas tres,
dales líneas envenenadas a propósito y comprueba que las cazan. Un detector que solo se ha
visto en verde no se distingue de uno vacío.

---

## 2. Dos shells en la misma máquina, dos gramáticas

↳ *GUIDE §3.a*

Trabajamos en **Windows**, donde conviven **PowerShell** y **Bash** (Git Bash). Se parecen lo
suficiente para confundirse y **no comparten sintaxis**. Escribir la de uno en el otro no
siempre da error: a veces «funciona» y ensucia algo.

| Para esto | PowerShell | Bash |
|---|---|---|
| Texto de varias líneas | `@'` … `'@` | `<<'EOF'` … `EOF` |
| Variable de entorno | `$env:NOMBRE` | `$NOMBRE` |
| Tirar la salida a la basura | `2>$null` | `2>/dev/null` |
| Escapar un carácter | `` ` `` (tilde invertida) | `\` |

> 🔑 **El modo de fallo que importa no es el error: es el resultado ligeramente equivocado.** Un
> error se arregla en el momento. Un mensaje de commit malformado ya subido, no — arreglarlo
> pediría `--amend` y `push --force`, que reescriben historia publicada y están **prohibidos**
> (`RES-011`). Se queda el ruido para siempre.

📌 **La regla:** antes de pegar texto de varias líneas en un comando, mira **qué shell** lo va a
leer. Si dudas, usa `<<'EOF'` de Bash.

⚠️ **Y una comprobada en este proyecto, el 2026-08-26:** la ruta `/tmp/x.py` escrita desde Bash
y leída después por Python **no es la misma ruta**. Python en Windows la resolvió como
`\tmp\x.py` y no encontró el archivo. Si un script se escribe desde una herramienta y se ejecuta
desde otra, **usa rutas absolutas**.

---

## 3. Las tres preguntas

↳ *GUIDE §6.b*

No se construyen el día 1: se les da **dueño y sitio** antes de la primera línea del producto.

- [ ] **Evaluación** — ¿dónde viven las pruebas? Se crea el archivo aunque tenga un solo caso.
      **Y ese caso tiene que salir en ROJO una vez**, antes de arreglarlo. → §5
- [ ] **Observabilidad** — ¿dónde queda registro de lo que hizo el scraper? Fecha, qué se
      pidió, cuántos sorteos llegaron, cuántos eran nuevos, y qué falló. **Ábrelo una vez** y
      responde una pregunta con él: un registro que nadie leyó es disco ocupado.
- [ ] **Datos y fuente externa** — aquí «seguridad» no son permisos de herramientas: es **de
      dónde vienen los datos y qué se hace con ellos**. Se escribe: qué se descarga, cada
      cuánto, qué se guarda, y qué pasa cuando la fuente miente o no está.

> ⚠️ **Ninguna de las tres se marca prometiendo tenerla en cuenta.** Se marca con un artefacto
> que existe: un archivo, una corrida en rojo, un registro abierto.

**El orden es por dependencia, no por importancia:** observabilidad antes que datos. Sin
registro no puedes demostrar qué devolvió la fuente el día que devolvió algo raro.

📌 **Traducción de la tercera, para que no quede abstracta.** Las preguntas concretas de este
proyecto: ¿qué pasa si la página de Baloto cambia su HTML? ¿si publica un sorteo a medias? ¿si
devuelve 200 con una página de mantenimiento? ¿cuántas veces al día es razonable pedirle algo?
El brief las deja abiertas en §23.11 y §23.12; esta casilla obliga a que tengan dueño antes de
escribir el scraper.

---

## 4. Nada corre solo por defecto

↳ *GUIDE §6.e*

En el proyecto de origen esta regla era sobre dinero: un script que llamaba a una API de pago no
podía cobrar por el simple hecho de ejecutarlo. **Aquí no hay dinero, y la regla sobrevive
igual** — solo cambia qué es lo caro.

> **La pregunta es: ¿qué pasa si corro esto sin mirar?**

Correr un módulo en pelado es lo que se hace para ver si sigue compilando y si sus pruebas
siguen verdes. **Si ese mismo comando dispara la carga inicial del histórico, la comprobación
más inocente del día se convierte en cientos de peticiones a un sitio de terceros** — y no
avisa: se ve igual que una suite.

**Los dos casos peligrosos de este proyecto:**

| Qué | Qué pasa si se corre sin mirar |
|---|---|
| **El scraper** | Peticiones a la fuente oficial. Nadie nos autorizó a martillearla, y un patrón de tráfico raro puede acabar en bloqueo |
| **La carga inicial del histórico** | Además, **escribe en la base de datos**. Corrida dos veces puede duplicar sorteos o pisar lo que ya estaba |

**La forma, cuando exista el código:**

```
<ejecutar el módulo>              -> SIEMPRE inofensivo. Pruebas, informes, comprobaciones.
<ejecutar el módulo> --descargar  -> lo que sale a la red, y solo con la bandera puesta.
```

En pelado, el módulo imprime su informe, corre sus pruebas y **dice con todas las letras** qué
bandera hace falta.

> 🚨 **Y la lección que costó dos veces en el proyecto de origen: la prosa no es un freno.**
>
> Allí escribieron una tabla avisando de qué archivos cobraban. Primero falló por estar
> incompleta —quien buscó el suyo y no lo encontró concluyó que era de los seguros; **una
> advertencia con lista incompleta no avisa a medias: tranquiliza**—. La completaron, y **volvió
> a fallar igual**: nadie consulta una tabla antes de un comando que lleva cien veces saliendo
> bien.
>
> **El arreglo no fue una tabla mejor: fue un freno en el código.** Un módulo capaz de salir a
> la red debe tener el freno puesto o una razón escrita de por qué no lo necesita. La prosa es
> el mapa; **el que para la mano es el código.**

---

## 5. Cómo se prueba

↳ *GUIDE §8.l · §8.b · §8.c*

🚨 **Esta sección está a medias a propósito.** Lo que sigue es el **contrato**: qué debe cumplir
una prueba, independientemente del lenguaje. Las **plantillas ejecutables** no se escriben
todavía porque **no hay stack decidido** (brief §23.1, `RES-004`), y escribirlas en un lenguaje
concreto sería decidirlo por la puerta de atrás. Se escriben el día que se decida → `T-024`.

### 5.a El caso de prueba es un DATO, no código repetido

Una tabla de casos —etiqueta, entradas, resultado esperado— recorrida por un bucle que compara e
imprime `ok`/`FALLA`. **Añadir el caso 27 debe ser una línea.**

Con aserciones sueltas son dos líneas por caso, y **el primer fallo mata el programa**: te
enteras de un problema por corrida en vez de los siete que hay.

### 5.b Las tres familias, y la que todo el mundo se salta

| Familia | Qué es | En este proyecto |
|---|---|---|
| camino feliz | la entrada normal | una combinación válida cualquiera |
| **bordes** | el cero, el vacío, lo negativo, lo enorme, el límite exacto | ⬇ los de abajo |
| lo malo | lo que **debe** ser rechazado | tres consecutivos; una balota repetida; superbalota 17 |

**Los bordes de RandomAI, que son los que nadie prueba hasta que aparecen:**

- **Generador:** balota `1` y balota `43`; superbalota `1` y `16`. Exactamente **dos**
  consecutivos (válido) frente a exactamente **tres** (inválido) — los dos lados del límite.
- **Prioridad** (brief §26): el último sorteo excluye 5 balotas y 1 superbalota. ¿Queda siempre
  espacio para generar? Es aritmética, y está sin hacer → `SUP-007`.
- **Estadística:** un número que **nunca ha salido**. No tiene última aparición ni intervalo
  medio, así que cualquier resta o división sobre él es un borde real, no teórico.
- **Comparación:** cero aciertos; los cinco aciertos; acertar la superbalota y ninguna balota.
- **Actualización incremental:** la fuente no trae nada nuevo; trae un solo sorteo; trae un
  hueco en medio.

> El camino feliz se prueba solo mientras escribes, y lo malo se prueba porque acabas de
> escribir la validación. **Los bordes no se le ocurren a nadie hasta que un usuario los
> encuentra.**

### 5.c Las seis reglas

1. **Imprimir no es probar.** Si tú miras la salida y decides, el juez eres tú y no hay prueba.
   La prueba dice `ok`/`FALLA` sola.
2. **Un caso, una variable.** Un caso con dos defectos pasa a verde cuando arreglas uno, con el
   otro todavía roto.
3. **Captura los reventones como un resultado más.** Sin eso, la suite muere en el caso que
   revienta y no ves los siguientes. Que algo reviente **es un comportamiento**, y va en la
   misma tabla.
4. **No compares el texto del error, solo que haya error.** Si comparas la redacción, mejorar el
   mensaje rompe la prueba.
5. **Cada caso independiente.** Si el orden importa, son N casos encadenados, no N pruebas.
6. **Un caso de prueba es la forma más duradera de escribir una decisión.** El comentario se
   ignora; el caso rojo pregunta *«¿seguro?»*. Si se acepta que la superbalota puede repetir un
   número de las balotas, se escribe el caso que lo dice.

### 5.d Pruebas de coherencia — las que cazan olvidos

↳ *GUIDE §8.c*

No prueban comportamiento: prueban que **no se te olvidó nada al añadir una pieza**. Cuestan
cero y avisan en un segundo.

En este proyecto, cuando exista el código:

- ¿Toda regla de validación declarada tiene una comprobación que la aplique?
- ¿Todo campo que el brief exige del histórico (§3) se está guardando?
- ¿Los dos universos siguen separados —balotas 1–43 y superbalota 1–16— en **todos** los
  cálculos, no solo en el que se acaba de escribir?

Su momento llega cuando añades la sexta regla y se te olvida enchufarla.

### 5.e Lo que cambia el mundo: efectos secundarios

El scraper y la carga inicial **escriben**. Ahí, lo que la función devuelve **es un recibo, no
la verdad**.

- **Estado conocido antes de CADA caso**, no una vez al principio. El dato que dejó la corrida
  de ayer hace pasar «el registro existe» aunque la función ya no escriba.
- **Comprueba dos cosas:** que exista **y** que el contenido coincida. Podría crearlo vacío o
  escribirlo dos veces.
- **En los casos que esperan rechazo, comprueba que el almacén quedó intacto.** Una función
  puede escribir y *después* devolver error.
- **Nunca contra la base de datos de verdad.** Una suite con efecto secundario destructivo **no
  se ve roja: se ve verde**, mientras borra lo que no debía.

### 5.f 🚨 Comprueba que tus pruebas sirven: sabotea

**Ninguna prueba vale hasta verla roja.**

Rompe a propósito la línea que hace el trabajo y **exige ver el rojo**. Si sigue en verde, la
prueba no estaba mirando lo que creías. Restaura y confirma el verde.

> Una prueba en rojo dice dónde está el problema. Una prueba en verde **no** dice que no haya
> problema: dice que **tu comparación no lo ve**.

**Qué sabotear aquí, en orden de lo que más enseña:**

| Rompe esto | Y mira si la prueba ve que… |
|---|---|
| **quién** entra en la combinación, no cuántos | no basta contar que hay 5 números |
| el **freno** de consecutivos (`> 2` → `>= 2`, o al revés) | lo prohibido sigue prohibido |
| un **borde** exacto (`<= 43` → `< 43`) | probaste los **dos** lados, no uno |
| el **orden** de las balotas al comparar aciertos | *«¿está?»* no es *«en qué posición?»* |
| el **desvío** del almacén de pruebas | tu trampa contra la base de datos real salta |

**Y tres cosas que solo se aprenden saboteando:**

1. ⭐ **Un defecto puede reportar ÉXITO.** El conteo sigue dando 5 y el mensaje sigue diciendo
   lo mismo, con el número equivocado dentro. Solo lo ven los casos que preguntan **quién**.
2. ⚠️ **Prefiere el caso genérico al concreto.** El concreto revienta y dice *«se rompió»*; el
   que recorre la tabla entera dice **qué** arreglar.
3. ⚠️ **Si al romper algo la prueba se cuelga o revienta en vez de ponerse roja, no lo
   ignores.** Un rojo que dice *«me colgué»* no dice *«la tabla está mal»*.

### 5.g El límite, que hay que saber decir

Una suite no dice *«mi código está bien»*. Dice *«estas 26 cosas se comportan como dije»*. Todo
lo demás sigue sin explorar — y **anotar dónde acaba la prueba es parte de tenerla**.

---

## 6. Preflight: falla temprano, de barato a caro

↳ *GUIDE §7*

Un script de verificación que se corre **antes** de lo caro. El orden es de más barato a más
caro, para que lo que falla más falle primero:

```
1. ¿Está el entorno de ejecución en la versión que hace falta?
2. ¿Están las dependencias?
3. ¿Existe la configuración, y no es la plantilla de ejemplo sin rellenar?
4. ¿La configuración FUNCIONA?   -> una petición real, mínima, a la fuente
```

> **El paso 4 es el que casi todos se saltan, y es el único que prueba la verdad.** Que exista
> una URL configurada no dice que responda; que responda no dice que devuelva lo que esperas.

🚨 **Y cada fallo imprime DOS cosas: qué pasó y qué hacer.**

```
[FALTA] <qué pasó>
        -> <qué hacer para arreglarlo>
```

Un preflight que solo dice qué falta obliga a buscar la solución; uno que dice las dos cosas se
resuelve sin salir de la terminal. Es la diferencia entre un diagnóstico y una tarea.

📌 **Adaptado a este proyecto**, el paso 4 es una petición mínima a la fuente de Baloto — la más
pequeña posible, no la carga inicial. Y va con la bandera de §4: **el preflight no descarga el
histórico.**

---

## 7. 🚨 El ciclo cuando el que teclea es un agente

↳ *GUIDE §11.i* — **la sección más importante de esta guía.**

Todo lo demás está escrito suponiendo que el ciclo lo corre una persona. Aquí no: el código lo
escribe una sesión de Claude, y **esa misma sesión escribe y corre las pruebas**.

> **El ciclo no cambia. Cambia quién puede ser testigo de qué.**

### El reparto, en cuatro pasos

| Paso | Quién | Qué se exige VER |
|---|---|---|
| **1. El criterio** | **el usuario**, en prosa, **antes** | la frase escrita, con sus casos de borde (§5.b) |
| **2. Rojo → verde** | la sesión que construye | **el rojo**, con su salida cruda. Sin rojo previo no hubo prueba |
| **3. Refactor** | la sesión que construye | el diff toca código y **no** toca pruebas |
| **4. Verificar** | **la terminal auditora**, desde fuera | lo medido contra lo dicho, **no el reporte** |

⚠️ **El paso 1 no es opcional y es el que sostiene los otros tres.** Si el criterio lo inventa
la misma sesión que escribe el código, el paso 2 se vuelve teatro —una prueba que él definió,
que él hace fallar, que él hace pasar— y el paso 4 audita **contra un criterio que escribió el
auditado**.

### Las dos reglas duras

Viven en `CLAUDE.md` como **reglas duras 8 y 9**, no aquí. Se citan para que el ciclo se
entienda entero:

1. **Ante una prueba roja se arregla el código.** Modificar o borrar una prueba exige
   autorización explícita del usuario, con la razón escrita.
2. **Pide el refactor de forma explícita, cada ciclo.**

### Lo que se mira, y es barato y local

- 🔍 **El diff de las pruebas, APARTE del diff del código.** Una prueba ablandada no se anuncia:
  solo se ve ahí. Sin esa separación, la regla 8 es una nota — nadie llega a saber si se tocó.
- 🔍 **Que el rojo EXISTIERA.** Una prueba que nunca falló no probó nada, y **mirando el verde
  no se distingue de una vacía**.

📌 **El saboteo (§5.f) es obligatorio, pero no cubre esto.** Demuestra que la prueba vigila esa
línea; **nunca que la línea sea la correcta**. Eso solo lo dice el criterio del paso 1.

### 🚨 Y una tentación que hay que nombrar para no caer en ella

**Repartir el ciclo entre varios agentes:** uno para el rojo, otro para el verde, otro para el
refactor. **No.**

El del verde lee la prueba del rojo, así que **no hay testigo independiente**; y su única
métrica de éxito pasa a ser *«que pase»*, que es la orden mal formulada convertida en puesto de
trabajo. **El ciclo lo corre un solo agente, seguido:** la continuidad es lo que el ciclo
fabrica.

---

## 8. Cuándo crear un subagente

↳ *GUIDE §11.i.2 · §11.i.3*

Vale para cualquier trabajo, no solo para pruebas. **Un agente puede hacer dos cosas seguidas;
lo que no puede es ser testigo de sí mismo.** Ese es el único corte que compra algo.

> ⭐ **LA PREGUNTA QUE DECIDE:**
> **¿Este agente necesita saber MENOS que yo, o MÁS?**
>
> **Menos, y su valor está en no saber** → es un agente.
> **Más, o todo lo mío** → es un traspaso, y los traspasos pierden. Hazlo tú.

| Razón para crearlo | Qué compra | Señal de que NO es el caso |
|---|---|---|
| **Independencia de criterio** | un testigo que no vio construir | tienes que pasarle tu contexto → es un eco |
| **Aislamiento de ruido** | que un log enorme no entre en tu contexto | te importa el detalle, no la conclusión |
| **Paralelismo real** | tiempo | la segunda tarea espera el resultado de la primera |

❌ **El corte equivocado, y es el que se le ocurre a todo el mundo: por fases del trabajo**
(analizar → escribir → probar → revisar). Copia el organigrama de una empresa, donde los roles
existen porque una persona no puede estar en dos sitios. **Un agente no tiene ese problema.**

📌 **`session-starter` pasa la pregunta:** necesita saber **menos** — arranca en frío y ese es
su valor. `session-closer` también: no vio la conversación, y por eso escribe desde la evidencia.

### 8.b Evidencia, nunca veredicto

Si algún día se crea un agente que revise dentro de la sesión que construye, **antes** de pasar
el trabajo a la auditora:

| Recibe | **No** recibe |
|---|---|
| el criterio escrito por el usuario | el relato de cómo se llegó al código |
| el diff y los artefactos | qué se intentó y se descartó |
| poder correr comandos | **permiso de escribir** |

> 🚨 **Las dos reglas que impiden que se vuelva una coartada:**
>
> 1. **Entrega evidencia, no veredicto.** No dice *«todo bien»*: dice *«corrí esto, salió
>    esto»*, con la salida cruda pegada. **Un veredicto desplaza la auditoría; una evidencia la
>    alimenta.**
> 2. **Lista cerrada, no «busca problemas».** Lo que no está en la lista **no se declara limpio:
>    se declara NO MIRADO.**

⚠️ **No sustituye a la terminal auditora.** No puede juzgar si el criterio estaba bien ni si
algo se recortó en silencio: eso exige estar **fuera del marco**, no en otro proceso dentro de
él. Lo que hace es quitarle el trabajo mecánico.

📌 **Y por qué la regla 1 no es cosmética:** *el resumen sale peor que el documento*. Un
verificador que resume convierte la evidencia en opinión, que es lo único que no queríamos.

---

## 9. Cómo se entrega un hallazgo

↳ *GUIDE §6.d*

Sirve hacia el usuario y hacia la terminal auditora. **La marca va en la primera línea, nunca
en el remate.**

**Un hallazgo suelto:**

```markdown
## 🔴 Importancia ALTA · no bloqueante

<qué pasa, en una o dos frases>

<la evidencia: archivo:línea, o el comando que lo enseña>

<el arreglo>

**No es bloqueante** porque <qué NO impide hoy>.
```

**Varios de golpe** — tabla, y se lee sin abrir ninguno:

```markdown
| qué | importancia | urgencia | qué significa |
|---|---|---|---|
| <cosa> | **alta** | **bloqueante** | <qué se rompe si sigues> |
| <cosa> | media | no | <por qué puede esperar> |
```

**Qué obliga cada marca:**

| Marca | Qué se escribe |
|---|---|
| 🔴 **alta** | el párrafo completo con evidencia |
| 🟡 **media** | dos o tres líneas |
| ⚪ **baja** | **una línea, o no se entrega** |
| **bloqueante** | **obligatorio**: qué bloquea y qué se rompe si sigues |
| no bloqueante | nada extra |

⚠️ **Los dos errores que esta plantilla existe para evitar:**

1. **Escribir «bloqueante» sin la frase de qué se rompe.** Si no sale la frase, no era
   bloqueante: era una tarea que apetecía hacer primero.
2. **Argumentar bien algo de importancia baja.** Un párrafo sólido sobre una nimiedad cuesta lo
   mismo de leer que uno sobre lo que paraba el trabajo, y **se lleva la atención por delante**.

📌 **La casilla `alta / no bloqueante` se revisa al cerrar sesión**, porque es la que nadie
hace: no grita y no tiene fecha.

📌 Encaja con los ejes que ya usa la auditora en `tasks_audit.md` —importancia y urgencia por
separado—, así que un hallazgo escrito así se convierte en tarea sin traducción.
