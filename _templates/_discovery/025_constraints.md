# Restricciones y supuestos — <NOMBRE DEL PROYECTO>

| | |
|---|---|
| **Artefacto** | `_discovery/025_constraints.md` |
| **Fase que lo produce** | `005_discovery` |
| **Estado** | `BORRADOR` |
| **Abierto** | `<AAAA-MM-DD>` |
| **Cerrado** | `<AAAA-MM-DD, o — mientras siga en BORRADOR>` |
| **Escrito por** | terminal **ejecutora** |

> ⚠️ **Las fechas las lee la auditora y las cruza contra el historial de Git.**
> Una fecha declarada que no cuadra con la del commit manda el Gate a `NO AUDITABLE`.

---

## 1. Dos cosas distintas, y se comportan distinto

| | Qué es | Qué se hace con ello |
|---|---|---|
| **Restricción** (`RES-xxx`) | un límite **conocido y firme** — presupuesto, plazo, ley, sistema obligatorio | se **respeta**; condiciona el diseño |
| **Supuesto** (`SUP-xxx`) | algo que **se cree pero no se ha verificado** | se **verifica**, o se marca como riesgo abierto |

> **Un supuesto que nadie escribió se comporta como un hecho.** Escribirlo es lo único
> que lo mantiene sujeto a revisión.

🚨 **La pregunta que los separa:** *¿alguien puede enseñarme dónde está escrito, o quién
lo decidió?* Sí → `RES`. No → `SUP`, por muy obvio que parezca.

📌 Este archivo es el **desagüe de la fase**: aquí llegan los «no se sabe» de las nueve
preguntas (`005_needs.md` §1), los interesados con `TODAVÍA NO` (`015_stakeholders.md`
§3) y todo lo que en `010_actors.md` se afirmó sin verificar.

---

## 2. Restricciones — `RES-xxx`

| # | Restricción | Tipo | Quién la impone | Qué condiciona | Verificada el |
|---|---|---|---|---|---|
| `RES-001` | `<el límite, en una frase>` | `<legal · técnica · presupuestal · plazo · sistema obligatorio · operativa>` | `<I-00x de 015_stakeholders.md · ley · contrato>` | `<qué decisión de diseño queda condicionada>` | `<AAAA-MM-DD>` |
| `RES-002` | `<…>` | `<…>` | `<…>` | `<…>` | `<…>` |

### Ficha — solo para las que cambian lo que se puede construir

### RES-001 · `<título corto>`

| Campo | Contenido |
|---|---|
| **Enunciado** | `<…>` |
| **Dónde está escrita** | `<documento, política, contrato, correo — con fecha>` |
| **Quién la confirmó** | `<persona, no «se sabe que»>` |
| **Qué pasa si se ignora** | `<la consecuencia concreta: multa, rechazo, no se despliega>` |
| **¿Tiene vencimiento?** | `<no · vence el AAAA-MM-DD y entonces deja de aplicar>` |
| **Afecta a** | `<N-xxx · el prototipo · el MVP · el despliegue>` |

⚠️ Una restricción **sin fuente que se pueda enseñar** no es una restricción: es un
supuesto con voz firme. Bájala a §3.

---

## 3. Supuestos — `SUP-xxx`

| # | Supuesto | De dónde salió | Qué se rompe si es falso | Cómo se verifica | Dueño | Verificar antes de | Estado |
|---|---|---|---|---|---|---|---|
| `SUP-001` | `<lo que se cree y no se ha comprobado>` | `<pregunta 4 sin respuesta · dicho por I-002 · asumido al clasificar actores>` | `<la consecuencia concreta>` | `<la acción que lo resuelve: preguntar a X, mirar Y>` | `<quién>` | `<AAAA-MM-DD o «la sesión 1 del prototipo»>` | `POR VERIFICAR` |
| `SUP-002` | `<…>` | `<…>` | `<…>` | `<…>` | `<…>` | `<…>` | `POR VERIFICAR` |

**Los cuatro estados posibles:**

| Estado | Significado |
|---|---|
| `POR VERIFICAR` | todavía no se sabe · lleva dueño y fecha |
| `VERIFICADO` | resultó cierto → normalmente pasa a §2 como `RES-xxx`, o deja de importar |
| `FALSO` | resultó no ser cierto → ver §4, algo tiene que cambiar |
| `RIESGO ABIERTO` | **no se puede verificar antes de necesitarlo** · se acepta a sabiendas |

🚨 **`RIESGO ABIERTO` es una decisión, no un cajón de sastre.** Va con quién lo aceptó y
por qué no se pudo verificar. Un supuesto que lleva meses en `POR VERIFICAR` sin fecha
**ya es un riesgo abierto**, solo que sin nadie que lo haya decidido.

📌 Las tres columnas que hacen el trabajo son **«qué se rompe si es falso»**, **dueño** y
**verificar antes de**. Sin ellas la tabla es una lista de intuiciones.

---

## 4. Supuestos que se resolvieron

El rastro. No se borra ninguna fila: un supuesto que resultó falso explica decisiones
que después nadie entiende.

| # | Resultó | Verificado el | Qué cambió por eso |
|---|---|---|---|
| `SUP-001` | `<VERIFICADO · FALSO>` | `<AAAA-MM-DD>` | `<pasó a RES-004 · se reescribió N-002 · nada>` |

---

## 5. Lo que se decidió NO averiguar todavía

Se escribe a propósito. Lo contrario —no averiguarlo y no decirlo— se ve igual desde
fuera, y dentro de dos meses parece un olvido.

| Qué no se averiguó | Por qué se pospuso | Cuándo toca |
|---|---|---|
| `<el volumen real de solicitudes por mes>` | `<no cambia nada antes del Gate 1>` | `<020_baseline>` |

---

## 6. Comprobación antes de cerrar este archivo

- [ ] Cada `RES-xxx` dice **dónde está escrita** y **quién la confirmó**.
- [ ] Ninguna `RES-xxx` se sostiene solo en «todo el mundo sabe que».
- [ ] Cada `SUP-xxx` tiene **dueño** y **fecha límite de verificación**.
- [ ] Cada `SUP-xxx` dice **qué se rompe si es falso**, con consecuencia concreta.
- [ ] Los `SUP-xxx` de otros artefactos llegaron aquí — ninguno quedó suelto en su archivo.
- [ ] Los `RIESGO ABIERTO` dicen **quién los aceptó**.
- [ ] Los resueltos están en §4, **no borrados**.
- [ ] `RES-xxx` y `SUP-xxx` están copiados a `_memory/constraints.md` y
      `_memory/assumptions.md` — este archivo es de la fase; `_memory/` los lleva a las
      siguientes.
- [ ] **No queda ni un solo `<` en el archivo.**
- [ ] La sección «Guía de llenado» **está borrada**.
- [ ] La cabecera dice `CERRADO` y tiene fecha de cierre.

```bash
grep -n "<" _discovery/025_constraints.md                   # debe no devolver nada
grep -n "Guía de llenado" _discovery/025_constraints.md     # debe no devolver nada
grep -c "POR VERIFICAR" _discovery/025_constraints.md       # cada uno necesita dueño Y fecha
grep -rn "SUP-" _discovery/ | grep -v 025_constraints       # cada SUP citado fuera debe existir aquí
```

📌 El cuarto es el que se olvida: una plantilla manda un `SUP-003` a este archivo y aquí
nunca llega. Queda un identificador que no apunta a nada.

---
---

## Guía de llenado — ⚠️ BORRAR esta sección al cerrar el artefacto

> Existe para escribir el archivo. **No sobrevive al cierre de la fase.**

### Ejemplo — app de recogida de reciclaje

**Restricciones:**

| # | Restricción | Tipo | Quién la impone |
|---|---|---|---|
| `RES-001` | Los datos de clientes no salen del país | legal | Jurídica (`I-002`) |
| `RES-002` | El presupuesto del MVP es de 3 meses de trabajo | presupuestal | Dirección (`I-001`) |
| `RES-003` | Las solicitudes deben quedar en el ERP existente | sistema obligatorio | TI |

**Supuestos:**

| # | Supuesto | Qué se rompe si es falso | Cómo se verifica |
|---|---|---|---|
| `SUP-001` | Los clientes tienen un celular con datos | la hipótesis entera: no podrían solicitar solos | preguntarlo en las 5 sesiones del prototipo |
| `SUP-002` | El ERP tiene una API | habría que digitar a mano; cambia el proceso | pedir la documentación a TI |

### La pregunta que convierte un adjetivo en supuesto

> **¿Cómo lo sé?**

Si la respuesta es *«me lo dijeron»*, *«se asume»* o *«es obvio»* → `SUP-xxx`.
Si es *«está en este documento, firmado por esta persona»* → `RES-xxx`.

### Errores que esta plantilla existe para evitar

| Error | Cómo se ve | Qué hacer |
|---|---|---|
| Supuesto ascendido a restricción | «el ERP tiene API» en la tabla de `RES` | nadie enseñó la documentación → es `SUP` |
| Supuesto sin dueño | fila completa menos la columna «dueño» | sin dueño no se verifica nunca; ponerle nombre o marcarlo `RIESGO ABIERTO` |
| Supuesto sin consecuencia | «los usuarios saben usar un celular» | si no se puede escribir qué se rompe, quizá no importa: bórralo |
| `POR VERIFICAR` eterno | seis meses, misma fila | ya es riesgo abierto; que alguien lo acepte por escrito |
| Restricción inventada por precaución | «debe funcionar sin internet», y nadie lo pidió | eso es diseño disfrazado de límite. Fuera |
| Borrar los resueltos | §4 vacía y §3 más corta que ayer | el rastro explica decisiones que después nadie entiende |
| Restricción con fecha de caducidad tratada como eterna | una política que vence en marzo | anotar el vencimiento: deja de aplicar y nadie lo revisa |

### Por qué esto no es papeleo

Las restricciones y los supuestos son lo único de Descubrimiento que **sigue actuando
en todas las fases siguientes**. Una necesidad se convierte en feature y se olvida; un
supuesto falso reaparece en Baseline, en el WSLT y en el Gate 2, cada vez más caro.

Por eso los dos se copian a `_memory/` al cerrar la fase: este archivo es el registro
de lo que se supo **ese día**; `_memory/` es lo que viaja.

### Lo que esta fase tiene PROHIBIDO, y aquí se cuela solo

**Elegir tecnología.** Una restricción técnica dice *«tiene que hablar con este ERP»*,
no *«usaremos PostgreSQL»*. La primera es un límite del mundo; la segunda es una
decisión de `020_baseline`, y aquí no toca.

📌 Definiciones: `methodology/000_method.md` §13.
📌 Procedimiento: `phases/005_discovery.md` §4 paso 6, y §7.
