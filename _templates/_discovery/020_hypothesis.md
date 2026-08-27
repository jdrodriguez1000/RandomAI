# Hipótesis — <NOMBRE DEL PROYECTO>

| | |
|---|---|
| **Artefacto** | `_discovery/020_hypothesis.md` |
| **Fase que lo produce** | `005_discovery` |
| **Estado** | `SELLADA` |
| **Sellada el** | `<AAAA-MM-DD>` |
| **Escrito por** | terminal **ejecutora** |

> 🚨 **ESTE ARCHIVO NO LLEVA `BORRADOR`. NACE SELLADO, Y ES EL ÚNICO DE LOS CINCO.**
>
> El Gate 1 comprueba dos cosas en el historial de Git, y las dos son sobre este archivo:
>
> 1. Que existía **antes** de la sesión 1 del prototipo.
> 2. Que **no cambió durante la fase** → `git log --oneline -- _discovery/020_hypothesis.md`
>    debe devolver **un solo commit**.
>
> **Por eso este archivo se escribe entero antes del primer `git add`.** Se piensa, se
> discute y se corrige **sin commitear**. El commit es el sello.
>
> ⚠️ **Un segundo commit aquí manda el Gate 1 a `NO AUDITABLE`** — y no por sospecha:
> una hipótesis que cambia mientras se corre el prototipo describe lo que salió, no lo
> que se apostaba. No hay forma de saber cuál era la apuesta original, y el Gate no
> tiene contra qué comparar.

---

## 1. La hipótesis

> **<Una sola frase. Observable en una sesión con un usuario.>**

Ejemplo de la forma que debe tener:

> *«El cliente que hoy llama por teléfono puede solicitar una recogida por sí solo, sin
> ayuda, en menos de 3 minutos.»*

---

## 2. La condición de falsación

**Una hipótesis vale si se puede escribir qué observación la tumbaría.** Si no se
puede, es un deseo, y el Gate 1 no tendrá contra qué medir.

> **Esta hipótesis queda TUMBADA si:** `<la observación concreta que la rompe>`

| Campo | Contenido |
|---|---|
| **Qué se observa** | `<el comportamiento, no la opinión>` |
| **Con cuántos participantes** | `<número fijado ahora, antes de la primera sesión>` |
| **Umbral** | `<cuántos de esos N tienen que lograrlo para que la hipótesis siga en pie>` |
| **Estado que cuenta como logro** | `<Éxito autónomo · Éxito autónomo o con dudas>` |
| **Ventana** | `<en cuántas sesiones y en qué plazo>` |

🚨 **La métrica, la ventana y el umbral se declaran AQUÍ, antes del primer dato.**
Medir hasta que el número guste no es medir: es elegir el resultado.

📌 **«Éxito con ayuda» no es éxito autónomo.** Si la hipótesis dice «sin ayuda», tres
de cinco con ayuda la tumban, por bien que se vea el prototipo.

---

## 3. De dónde sale

| Campo | Contenido |
|---|---|
| **Necesidad que valida** | `<N-001 de 005_needs.md>` |
| **Actor Generador** | `<el actor concreto de 010_actors.md §2>` |
| **Dimensión principal** | `<A · Ejecución · B · Comprensión · C · Necesidad · D · Negocio>` |
| **Cómo se hace hoy** | `<el proceso real sin la aplicación — es la vara de comparación>` |

📌 Si la hipótesis no se puede amarrar a una `N-xxx` y a un Generador con nombre, no
está lista para sellarse.

---

## 4. El perfil del usuario representativo

Quién cuenta como Generador válido en una sesión de evaluación.

> 🚨 **Se define AQUÍ, en Descubrimiento.** Si se define después de las sesiones, se
> define **a la medida de quien vino** — y entonces cualquier resultado encaja.

| Campo | Contenido |
|---|---|
| **Perfil que califica** | `<…>` |
| **Qué lo descalifica** | `<conoce el proyecto · trabaja en el equipo · ya usó el prototipo>` |
| **Cuántos participantes** | `<número, fijado ahora>` |
| **De dónde saldrán** | `<canal real de reclutamiento>` |

📌 Este perfil se copia tal cual a `_prototype/010_participants.md` al abrir la fase
siguiente. **Aquí es donde se decide; allá es donde se registra quién vino de verdad.**

---

## 5. Lo que esta hipótesis NO afirma

Se escribe para que el Gate 1 no se convierta en un examen de cosas que nunca se
apostaron.

- No afirma que el producto sea rentable.
- No afirma que el prototipo esté bien hecho — es descartable, su calidad no es criterio.
- No afirma que al sponsor le vaya a gustar — el gusto no es evidencia.
- `<…lo demás que quede fuera a propósito>`

---

## 6. Comprobación antes del ÚNICO commit

Todo esto se revisa **antes** de `git add`, porque después ya no se puede tocar.

- [ ] La hipótesis es **una sola frase** y se puede observar en una sesión.
- [ ] **No nombra ninguna pantalla, botón ni menú.**
- [ ] Está escrita la **condición de falsación**, y es una observación, no un adjetivo.
- [ ] Hay **número de participantes** y **umbral**, fijados antes del primer dato.
- [ ] Dice qué estado cuenta como logro, y si «con ayuda» cuenta o no.
- [ ] Está amarrada a una `N-xxx` y a un Generador con actor concreto.
- [ ] El **perfil del usuario representativo** está escrito, con lo que descalifica.
- [ ] **No queda ni un solo `<` en el archivo.**
- [ ] La sección «Guía de llenado» **está borrada**.
- [ ] La cabecera dice `SELLADA` y tiene fecha.

```bash
grep -n "<" _discovery/020_hypothesis.md                 # debe no devolver nada
grep -n "Guía de llenado" _discovery/020_hypothesis.md   # debe no devolver nada
git log --oneline -- _discovery/020_hypothesis.md        # debe devolver UNA sola línea
```

📌 El tercero es el que mira la auditora. Córrelo tú antes que ella.

---
---

## Guía de llenado — ⚠️ BORRAR esta sección antes del commit

> Existe para escribir el archivo. **No sobrevive al sello.**

### La prueba que separa una hipótesis de un deseo

> **¿Qué tendría que ver para saber que estoy equivocado?**

Si no hay respuesta, no es hipótesis.

| ❌ No sirve | ✅ Sirve |
|---|---|
| «La app va a mejorar el proceso de recogidas» | «El cliente que hoy llama por teléfono puede solicitar una recogida por sí solo, sin ayuda, en menos de 3 minutos» |
| «A los usuarios les va a gustar» | «El cliente entiende qué materiales puede entregar sin preguntarle a nadie» |
| «El flujo será intuitivo» | «4 de 5 clientes completan la solicitud en Éxito autónomo» |

La columna derecha se **observa**. La izquierda solo se opina — y el gusto no es
evidencia.

### Los cuatro estados de resultado

| Estado | Significado | Valor |
|---|---|---:|
| **Éxito autónomo** | completa sin ayuda | 3 |
| **Éxito con dudas** | completa sin ayuda, pero con dudas importantes | 2 |
| **Éxito con ayuda** | el facilitador intervino → **no es éxito completo** | 1 |
| **Fracaso** | no completa | 0 |

Al fijar el umbral hay que decir **cuáles de estos cuatro cuentan**. Es la decisión que
más gates decide, y la que más se deja para después.

### Las cuatro dimensiones de validación

| | Pregunta |
|---|---|
| **A · Ejecución** | ¿Puede el usuario completar la tarea? |
| **B · Comprensión** | ¿Comprende lo que hace y qué significan las opciones? |
| **C · Necesidad** | ¿El flujo es una forma válida de resolver su necesidad real? |
| **D · Negocio** | ¿El flujo representa el proceso que la empresa quiere implementar? |

**C y D no se funden.** El usuario puede usarlo bien y el sponsor descubrir que choca
con una regla interna. Si la hipótesis solo cubre A, decláralo en §5.

### Errores que esta plantilla existe para evitar

| Error | Cómo se ve | Qué hacer |
|---|---|---|
| Hipótesis escrita después | el commit es posterior a la sesión 1 | ya no hay arreglo: `NO AUDITABLE`. Solo se evita antes |
| Hipótesis retocada a mitad | dos commits sobre este archivo | no tocarlo. Lo que se aprenda va a `_prototype/020_observations.md` |
| Umbral sin número | «que la mayoría lo logre» | «4 de 5», decidido hoy |
| Umbral decidido al final | el número aparece en el informe del Gate | declararlo aquí es lo único que lo hace medida |
| Hipótesis con pantalla dentro | «el usuario encuentra el botón de agendar» | eso mide si sabe leer un botón, no si resuelve su necesidad |
| Varias hipótesis en una | «entiende, completa y además vuelve» | una sola. Las demás son de EVOL o del Gate 2 |
| Falsación imposible de romper | «el usuario podrá solicitar la recogida» | ¿con ayuda cuenta? ¿en cuánto tiempo? sin eso, nada la tumba |

### Si la hipótesis cambia de verdad

Puede pasar: en Descubrimiento se entendió mal el negocio y el prototipo lo destapa.
**No se edita este archivo.** Se registra en `_prototype/020_observations.md`, el Gate 1
juzga la hipótesis **que se selló**, y la nueva se escribe en el ciclo siguiente.

> Una hipótesis tumbada es un resultado, no un error. Una hipótesis corregida a mitad
> de camino no es ninguna de las dos cosas: es un archivo sin valor probatorio.

📌 Definiciones: `methodology/000_method.md` §18, §24, §26, §29.
📌 Procedimiento: `phases/005_discovery.md` §4 paso 7, y §8.
📌 Lo que el Gate 1 hace con esto: `phases/015_gate1.md` §3, comprobaciones 0 y 4.
