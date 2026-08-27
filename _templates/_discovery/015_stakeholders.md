# Interesados — <NOMBRE DEL PROYECTO>

| | |
|---|---|
| **Artefacto** | `_discovery/015_stakeholders.md` |
| **Fase que lo produce** | `005_discovery` |
| **Estado** | `BORRADOR` |
| **Abierto** | `<AAAA-MM-DD>` |
| **Cerrado** | `<AAAA-MM-DD, o — mientras siga en BORRADOR>` |
| **Escrito por** | terminal **ejecutora** |

> ⚠️ **Las fechas las lee la auditora y las cruza contra el historial de Git.**
> Una fecha declarada que no cuadra con la del commit manda el Gate a `NO AUDITABLE`.

---

## 1. Quién es un interesado, y quién no

Un **interesado** puede decidir, financiar, definir políticas, aportar conocimiento,
aprobar resultados, verse afectado, representar usuarios o imponer restricciones
legales o técnicas.

> **Los interesados no necesariamente usan la aplicación.** Esa es toda la diferencia
> con un actor: el actor **usa**, el interesado **influye**.

📌 Una misma persona puede ser las dos cosas. Cuando lo sea, aparece en los dos
archivos, y aquí se dice.

---

## 2. Los interesados de este proyecto

| # | Persona o rol | Organización | Rol frente al proyecto | Qué aporta | Qué puede bloquear | ¿Es también actor? |
|---|---|---|---|---|---|---|
| `I-001` | `<…>` | `<…>` | `<financia / decide / aprueba / define políticas / aporta conocimiento / se ve afectado / representa usuarios / impone restricciones>` | `<…>` | `<…>` | `<no · sí → Supervisor>` |
| `I-002` | `<…>` | `<…>` | `<…>` | `<…>` | `<…>` | `<no>` |

**Las dos columnas que hacen el trabajo son «qué aporta» y «qué puede bloquear».**
Un interesado que no aporta nada y no puede bloquear nada no es un interesado: es un
espectador, y no va en esta tabla.

---

## 3. Ficha de cada interesado

Solo llevan ficha los que pueden **bloquear** algo. Los demás se quedan en la tabla.

### I-001 · `<nombre o rol>`

| Campo | Contenido |
|---|---|
| **Rol frente al proyecto** | `<…>` |
| **Qué aporta** | `<conocimiento, presupuesto, aprobación, acceso, una política>` |
| **Qué puede bloquear, y en qué momento** | `<qué decisión concreta se detiene si dice que no, y cuándo llega ese momento>` |
| **Qué necesita para no bloquear** | `<lo que hay que enseñarle, medirle o pedirle>` |
| **Restricciones que impone** | `<RES-xxx de 025_constraints.md · —>` |
| **Cómo se llega a él** | `<canal real: quién lo presenta, con qué frecuencia se le puede consultar>` |
| **Consultado el** | `<AAAA-MM-DD · TODAVÍA NO>` |

<!-- Copia el bloque para I-002, I-003, … -->

🚨 **Un interesado que puede bloquear y con el que nadie ha hablado todavía no es un
riesgo abstracto: es una fecha que aún no ha llegado.** Si «Consultado el» dice
`TODAVÍA NO`, eso es un `SUP-xxx` en `025_constraints.md`, no una casilla vacía.

---

## 4. Quién tiene que aprobar qué

El mapa de las aprobaciones que hacen falta antes de que el proyecto pueda avanzar.
Se llena con lo que se sepa hoy; lo que no se sepa se escribe como «no se sabe».

| Decisión | Quién la aprueba | Cuándo se necesita |
|---|---|---|
| `<presupuesto del MVP>` | `<I-001>` | `<después del Gate 1>` |
| `<acceso a los datos de clientes>` | `<I-003>` | `<antes de la primera sesión de prototipo>` |
| `<…>` | `<no se sabe → SUP-xxx>` | `<…>` |

📌 Esta tabla **no promete fechas ni alcance** — eso lo prohíbe la fase. Dice quién
decide, no cuándo estará hecho.

---

## 5. La frontera: quién quedó dónde

El rastro de las personas que se consideraron y dónde aterrizaron. Existe porque la
pregunta *«¿este es actor o interesado?»* se vuelve a hacer sola dentro de tres meses.

| Persona o rol | Actor | Interesado | Por qué |
|---|---|---|---|
| `<Gerente de operaciones>` | `<sí — Supervisor>` | `<sí — aprueba el presupuesto>` | `<usa los informes Y financia>` |
| `<Director financiero>` | `<no>` | `<sí — I-001>` | `<financia, no usa la aplicación>` |
| `<Jefe de bodega>` | `<no>` | `<no>` | `<se enteró del proyecto; ni aporta ni bloquea>` |

---

## 6. Comprobación antes de cerrar este archivo

- [ ] **Los interesados están identificados** — es una de las cinco condiciones de
      salida de la fase.
- [ ] Cada uno dice **qué aporta** y **qué puede bloquear**; ninguna de las dos vacía.
- [ ] Los que pueden bloquear tienen **ficha**, con el momento en que bloquean.
- [ ] Ningún interesado está aquí solo porque «hay que tenerlo contento».
- [ ] Nadie aparece como interesado **solo** por usar la aplicación → ese es un actor.
- [ ] Los que son las dos cosas están en §5 y en `010_actors.md`.
- [ ] Los `TODAVÍA NO` consultados tienen su `SUP-xxx` en `025_constraints.md`.
- [ ] **No queda ni un solo `<` en el archivo.**
- [ ] La sección «Guía de llenado» **está borrada**.
- [ ] La cabecera dice `CERRADO` y tiene fecha de cierre.

```bash
grep -n "<" _discovery/015_stakeholders.md                 # debe no devolver nada
grep -n "Guía de llenado" _discovery/015_stakeholders.md   # debe no devolver nada
grep -n "TODAVÍA NO" _discovery/015_stakeholders.md        # cada línea necesita su SUP-xxx
```

---
---

## Guía de llenado — ⚠️ BORRAR esta sección al cerrar el artefacto

> Existe para escribir el archivo. **No sobrevive al cierre de la fase.**

### Las ocho formas de ser interesado

Decidir · financiar · definir políticas · aportar conocimiento · aprobar resultados ·
verse afectado · representar usuarios · imponer restricciones legales o técnicas.

Si alguien no encaja en ninguna, probablemente no es un interesado.

### Actor o interesado — la pregunta que lo resuelve

> **¿Abriría la aplicación para hacer su trabajo?**
> **Sí → actor** (va en `010_actors.md`). **No, pero puede parar el proyecto → interesado.**

Y sí, puede ser los dos. El gerente que revisa los informes **y** firma el presupuesto
es Supervisor en `010_actors.md` e `I-00x` aquí. No se elige uno: se escriben los dos.

### Ejemplo — app de recogida de reciclaje

| # | Persona o rol | Rol frente al proyecto | Qué aporta | Qué puede bloquear |
|---|---|---|---|---|
| `I-001` | Director de operaciones | financia y aprueba | el presupuesto del MVP | la inversión, después del Gate 1 |
| `I-002` | Jurídica | impone restricciones | la política de datos personales | el acceso a datos de clientes |
| `I-003` | Jefe de flota | se ve afectado | conoce las rutas reales | nada formalmente, pero su gente ejecuta |

### Errores que esta plantilla existe para evitar

| Error | Cómo se ve | Qué hacer |
|---|---|---|
| Lista de organigrama | doce nombres, ninguno con «qué bloquea» | quitar a los que ni aportan ni bloquean |
| Interesado que es actor | el analista que usa la app está aquí y no en actores | va en `010_actors.md`; aquí solo si además influye |
| «Qué puede bloquear: nada» | la columna rellena por cortesía | si no bloquea nada, no lleva ficha; si tampoco aporta, sale de la tabla |
| Bloqueo sin momento | «podría oponerse» | *qué decisión* se detiene y *cuándo* llega esa decisión |
| Jurídica descubierta tarde | aparece después del Gate 1 | quien impone restricciones legales se busca **en esta fase** |
| Confundir sponsor con Generador | «el que paga es el usuario» | el sponsor financia; el Generador **usa**. Casi nunca son el mismo |

### Lo que esta fase tiene PROHIBIDO, y aquí se cuela solo

**Prometer alcance o fechas.** Una reunión con el que financia empuja sola hacia
«entonces en octubre estaría». No hay evidencia todavía para prometer nada: lo que sale
de aquí es quién decide, no cuándo se entrega.

📌 Definiciones: `methodology/000_method.md` §12.
📌 Procedimiento: `phases/005_discovery.md` §4, paso 5.
