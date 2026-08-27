# Actores — <NOMBRE DEL PROYECTO>

| | |
|---|---|
| **Artefacto** | `_discovery/010_actors.md` |
| **Fase que lo produce** | `005_discovery` |
| **Estado** | `BORRADOR` |
| **Abierto** | `<AAAA-MM-DD>` |
| **Cerrado** | `<AAAA-MM-DD, o — mientras siga en BORRADOR>` |
| **Escrito por** | terminal **ejecutora** |

> ⚠️ **Las fechas las lee la auditora y las cruza contra el historial de Git.**
> Una fecha declarada que no cuadra con la del commit manda el Gate a `NO AUDITABLE`.

---

## 1. Los actores de este producto

Un actor se clasifica por **la función que cumple dentro de la aplicación**, nunca por
su cargo en la empresa. «Gerente de Operaciones» no es un tipo: es un actor concreto
que ejerce de **Supervisor**.

🚨 **Solo se listan los tipos que existen en este producto.** Un tipo sin actor
concreto detrás **no se anota aquí** — se declara ausente en §3.

| Tipo de actor | Actor concreto | Grupo | Qué hace dentro de la aplicación | Necesidad que atiende |
|---|---|---|---|---|
| `<Generador>` | `<…>` | de negocio | `<…>` | `<N-001>` |
| `<Coordinador>` | `<…>` | de negocio | `<…>` | `<N-002>` |
| `<Integrador>` | `<…>` | externo | `<…>` | `<N-00x>` |

📌 Si un actor concreto no se puede amarrar a ninguna `N-xxx` de `005_needs.md`,
pregúntate por qué está en la lista.

---

## 2. El Actor Generador — la ficha que decide si hay proyecto

> **Si el Generador no existe o no usará la aplicación, no hay razón fundamental para
> que la aplicación exista.**

Por eso lleva ficha propia: el prototipo lo valida **a él**, y el MVP se construye
**para él**.

| Campo | Contenido |
|---|---|
| **Actor concreto** | `<…>` |
| **Acción que da origen al proceso** | `<la acción principal, la que arranca todo>` |
| **Identificación** | `<nombre y apellido, o un perfil real y alcanzable CON NÚMERO>` |
| **¿Es alcanzable hoy?** | `<sí / no — y cómo se llega a ellos>` |
| **Quién confirma que existen** | `<persona o documento que lo sostiene, no una suposición>` |
| **Cómo hace hoy esa acción** | `<el proceso sin la aplicación>` |
| **Verificado el** | `<AAAA-MM-DD>` |

**La comprobación es concreta, y tiene dos columnas:**

| ❌ No es un Generador identificado | ✅ Sí lo es |
|---|---|
| «los clientes» | «las empresas que hoy llaman por teléfono para pedir recogida, unas 40 al mes» |
| «los usuarios del área» | «las 6 analistas del turno de la mañana en la sede norte» |

### Veredicto de la fase

- [ ] **Hay Generador real y alcanzable** → la fase continúa.
- [ ] **NO hay Generador real y alcanzable** → la fase termina aquí con `NO CONTINÚA`.

Si el veredicto es `NO CONTINÚA`, se escribe por qué y se cierra el proyecto:

> **Motivo del `NO CONTINÚA`:** `<…>`

🚨 **`NO CONTINÚA` no es un fracaso: es el resultado más barato que puede dar el
método.** Cuesta una fase de entrevistas en vez de un MVP entero.

---

## 3. Tipos de actor que NO existen en este producto

Los actores son **potenciales, no obligatorios**. Que un tipo exista en la taxonomía no
significa que deba existir aquí.

Esta tabla se llena **igual de en serio que la §1**: declarar una ausencia es una
decisión con fecha; dejar el hueco en blanco es un olvido que nadie puede distinguir de
una decisión.

| Tipo ausente | Por qué no existe en este producto | ¿Podría aparecer después? |
|---|---|---|
| `<Ejecutor>` | `<nadie ejecuta trabajo físico originado en la app>` | `<no>` |
| `<Supervisor>` | `<hoy nadie mide resultados; podría entrar en EVOL>` | `<sí — EVOL>` |

---

## 4. Permisos y condiciones de acceso

⚠️ **No existe «Actor Invitado».** «Invitado» describe una **condición de acceso**, no
un comportamiento. Lo temporal, lo externo y lo restringido son **permisos y
seguridad**, nunca un tipo de actor.

| Actor concreto | Su tipo | Condición de acceso |
|---|---|---|
| `<Auditor externo>` | `<Supervisor>` | `<externo · solo lectura · solo informes>` |
| `<Socio comercial>` | `<Supervisor>` | `<temporal · vence el AAAA-MM-DD>` |

📌 Si esta tabla está vacía, bórrala. Solo se llena si hay accesos que no son el caso
normal del actor.

---

## 5. Comprobación antes de cerrar este archivo

- [ ] Hay un **Actor Generador identificado y alcanzable**, con actor concreto.
- [ ] Su identificación **no es un plural genérico**: tiene nombre, o perfil con número.
- [ ] Cada actor de §1 tiene **tipo** y **actor concreto**, separados.
- [ ] Ningún tipo se clasificó por el cargo en la empresa.
- [ ] **Solo están los actores que existen**; los ausentes se declaran en §3 con su motivo.
- [ ] No aparece ningún «Actor Invitado» — lo temporal y lo externo están en §4.
- [ ] Cada actor concreto se puede amarrar a una `N-xxx` de `005_needs.md`.
- [ ] **No queda ni un solo `<` en el archivo.**
- [ ] La sección «Guía de llenado» **está borrada**.
- [ ] La cabecera dice `CERRADO` y tiene fecha de cierre.

```bash
grep -n "<" _discovery/010_actors.md                 # debe no devolver nada
grep -n "Guía de llenado" _discovery/010_actors.md   # debe no devolver nada
grep -ni "invitado" _discovery/010_actors.md         # SOLO la advertencia de §4, ni una línea más
```

📌 El tercero **no** devuelve vacío a propósito: la advertencia de §4 nombra la palabra.
Lo que se comprueba es que **no aparezca en ninguna otra línea** — si sale en una fila
de §1, alguien lo metió como tipo de actor.

---
---

## Guía de llenado — ⚠️ BORRAR esta sección al cerrar el artefacto

> Existe para escribir el archivo. **No sobrevive al cierre de la fase.**

### Los seis tipos, en una línea cada uno

| # | Tipo | Qué hace | Grupo |
|---|---|---|---|
| 1 | **Generador** | realiza la acción que **da origen** al proceso | de negocio |
| 2 | **Coordinador** | **organiza** el trabajo: asigna, prioriza, distribuye, reasigna | de negocio |
| 3 | **Ejecutor** | **realiza** el trabajo física o directamente | de negocio |
| 4 | **Supervisor** | usa la información para **supervisar** resultados y decidir | de negocio |
| 5 | **Administrador de Plataforma** | usuarios, roles, permisos, parámetros, catálogos, integraciones | de plataforma |
| 6 | **Integrador** | **sistema externo** que intercambia información: ERP, pagos, mapas, correo, APIs | externo |

**La confusión más frecuente:** Coordinador vs Ejecutor.
> **El Coordinador organiza el trabajo; el Ejecutor lo realiza.**

**El Integrador no es una persona.** Un servicio de mapas es un actor.

### Cuántos actores debería haber

| Tipo de aplicación | Actores esperables |
|---|---|
| Sencilla | Generador + Administrador de Plataforma |
| Operativa | Generador + Coordinador + Ejecutor |
| Empresarial | los seis |

Una aplicación puede empezar **solo con Generador**. Que existan los seis en la
taxonomía no obliga a inventarlos aquí.

### Ejemplo — app de recogida de reciclaje

| Tipo | Actor concreto |
|---|---|
| Generador | Cliente que solicita la recogida |
| Coordinador | Analista de logística |
| Ejecutor | Conductor / recolector |
| Supervisor | Gerente de operaciones |
| Administrador de Plataforma | Administrador de TI |
| Integrador | Servicio de mapas |

### Errores que esta plantilla existe para evitar

| Error | Cómo se ve | Qué hacer |
|---|---|---|
| Clasificar por cargo | aparece «Gerente» como tipo | el cargo va en *actor concreto*; el tipo es la función |
| Inventar los seis | hay Supervisor y nadie mide nada | sacarlo de §1 y declararlo ausente en §3 |
| Generador en plural genérico | «los clientes» | nombre y apellido, o perfil **con número** |
| «Actor Invitado» | aparece un séptimo tipo | es Supervisor + un permiso → §4 |
| Confundir actor con interesado | el gerente que financia pero no usa la app | ese va en `015_stakeholders.md` |
| Declarar Generador sin verificar | nadie ha hablado con ninguno | es un `SUP-xxx`, no un hecho — a `025_constraints.md` |

### Lo que esta fase tiene PROHIBIDO, y aquí se cuela solo

Nada de pantallas por actor, ni de permisos técnicos, ni de roles del sistema. Aquí se
dice **quién** y **qué función**, no **qué ve** ni **con qué se autentica**.

📌 Definiciones: `methodology/000_method.md` §7–§12.
📌 Procedimiento: `phases/005_discovery.md` §4, pasos 3 y 4.
