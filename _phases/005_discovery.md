# Fase 005 · DESCUBRIMIENTO

> **Etapa 0 del ciclo.** Entender la necesidad antes de que exista nada que construir.
>
> **La lee:** la terminal **ejecutora**.
> **Definiciones:** `methodology/000_method.md` §7–§14. Este archivo **no define
> conceptos** — dice qué se hace con ellos.

---

## 1. Qué autoriza esta fase

- Entrevistar al sponsor, a los interesados y a usuarios potenciales.
- Observar cómo se hace hoy el trabajo, sin la aplicación.
- Leer sistemas, formatos, hojas de cálculo y procesos existentes.
- Registrar necesidades e identificarlas (`N-001`, `N-002`, …).
- Clasificar actores según la taxonomía de seis (§9 del método).
- Identificar interesados.
- Registrar restricciones — legales, técnicas, presupuestales, de plazo.
- Formular **la hipótesis** que el prototipo validará.

## 2. Qué prohíbe esta fase

Esto es lo importante de la fase, y es donde el trabajo se descarrila solo.

| ❌ Prohibido | Por qué |
|---|---|
| **Diseñar pantallas** | todavía no se sabe qué problema resuelven |
| **Elegir tecnología** | no hay nada que sostener aún; eso es `020_baseline` |
| **Escribir código** — de producto o de prototipo | el prototipo es la fase siguiente |
| **Escribir PRD, SPEC o ARCHIT** | son artefactos de `020_baseline`, después del Gate 1 |
| **Prometer alcance o fechas** | no hay evidencia todavía para prometer nada |
| **Asumir que existen los seis actores** | los actores son **potenciales**, no obligatorios (§11) |
| **Convertir una petición en requisito** | una petición no es una necesidad (§4 de esta fase) |

> **Si en Descubrimiento aparece un archivo `.html` o `.py`, la fase se rompió.**

## 3. Entradas — qué debe existir antes de empezar

Solo dos cosas, y la primera suele venir mal formulada:

1. **Una necesidad expresada por alguien.** Casi siempre llega disfrazada de solución
   («necesito una app», «necesito un dashboard»). Está bien: desvestirla es el trabajo.
2. **Acceso** al sponsor y a personas que puedan hablar del proceso real.

Si falta el acceso, la fase **no puede empezar**. No se sustituye con suposiciones.

## 4. Procedimiento

### Paso 1 — Separar la necesidad de la solución

Lo primero que dice el cliente es casi siempre una solución, no una necesidad.

| Lo que dijo | La necesidad detrás | La pregunta que la destapa |
|---|---|---|
| «Necesito una app para pedir recogidas» | los clientes no tienen forma de pedir una recogida sin llamar por teléfono | *¿qué pasa hoy cuando alguien quiere una recogida?* |
| «Necesito un dashboard» | nadie sabe cuántas recogidas se cumplieron | *¿qué decisión tomarías con ese dato?* |

**La pregunta que más sirve, y se repite en toda la fase:**

> **¿Cómo haces esto hoy?**

Una necesidad se registra como `N-xxx` **solo cuando se puede enunciar sin nombrar
una pantalla**.

### Paso 2 — Responder las nueve preguntas

No se avanza hasta tener respuesta —o un «no se sabe» explícito— a las nueve:

1. ¿Por qué existe la necesidad?
2. ¿Para qué se necesita la aplicación?
3. ¿Qué problema se quiere resolver?
4. ¿Quién tiene el problema?
5. ¿Quién usará la solución?
6. ¿Qué resultado espera obtener la empresa?
7. ¿Qué procesos existen actualmente?
8. ¿Qué restricciones existen?
9. ¿Qué sistemas actuales participan?

📌 Un **«no se sabe»** escrito vale más que una respuesta inventada: se convierte en
un supuesto (`SUP-xxx`) y alguien tendrá que ir a verificarlo.

### Paso 3 — Identificar y clasificar los actores

Para cada actor real de la aplicación se anota **el tipo** y **el actor concreto**:

```text
Tipo: Generador          Concreto: Cliente que solicita la recogida
Tipo: Coordinador        Concreto: Analista de logística
Tipo: Integrador         Concreto: Servicio de mapas
```

**Reglas al clasificar:**

- Se clasifica por **función dentro de la aplicación**, nunca por el cargo en la
  empresa (§8 del método).
- **No existe Actor Invitado.** El acceso temporal o externo es un permiso, no un tipo
  (§10 del método).
- **Solo se registran los actores que existen en este producto.** Un actor sin actor
  concreto detrás no se anota.

### Paso 4 — Encontrar al Generador, y comprobarlo

Es el paso que decide si hay proyecto.

> **Si el Generador no existe o no usará la aplicación, no hay razón fundamental para
> que la aplicación exista.**

La comprobación es concreta: **poner nombre y apellido, o al menos un perfil real
alcanzable.** «Los clientes» no es un Generador identificado. «Las empresas que hoy
llaman por teléfono para pedir recogida, unas 40 al mes» sí lo es.

🚨 **Si no se puede identificar un Generador real y alcanzable, la fase termina aquí
con un `NO CONTINÚA`.** No es un fracaso: es el resultado más barato que puede dar el
método.

### Paso 5 — Identificar interesados

Distintos de los actores: pueden decidir, financiar, aprobar, aportar restricciones o
verse afectados, **sin usar la aplicación**. Se anota qué aporta cada uno y qué puede
bloquear.

### Paso 6 — Registrar restricciones y supuestos

Se separan, porque se comportan distinto:

| | Qué es | Qué se hace con ello |
|---|---|---|
| **Restricción** (`RES-xxx`) | un límite **conocido y firme** — presupuesto, plazo, ley, sistema obligatorio | se respeta; condiciona el diseño |
| **Supuesto** (`SUP-xxx`) | algo que **se cree pero no se ha verificado** | se verifica, o se marca como riesgo abierto |

> Un supuesto que nadie escribió se comporta como un hecho. Escribirlo es lo único que
> lo mantiene sujeto a revisión.

### Paso 7 — Formular la hipótesis

Es la salida principal de la fase, y la que el prototipo pondrá a prueba.

**Una hipótesis vale si se puede escribir qué observación la tumbaría.** Si no se
puede, es un deseo.

| ❌ No sirve | ✅ Sirve |
|---|---|
| «La app va a mejorar el proceso de recogidas» | «El cliente que hoy llama por teléfono puede solicitar una recogida por sí solo, sin ayuda, en menos de 3 minutos» |
| «A los usuarios les va a gustar» | «El cliente entiende qué materiales puede entregar sin preguntarle a nadie» |

La segunda columna se puede **observar en una sesión con un usuario**. La primera, no
— y por eso el Gate 1 no tendría contra qué comparar.

📌 La hipótesis se escribe **antes** de construir el prototipo, no después. Escribirla
después es describir lo que salió.

---

## 5. Artefactos que produce

Viven en el repositorio del proyecto, en `_discovery/`:

```
_discovery\
├── 005_needs.md          ← N-001, N-002, … cada una sin nombrar pantallas
├── 010_actors.md         ← tipo + actor concreto, solo los que existen
├── 015_stakeholders.md   ← qué aporta y qué puede bloquear cada uno
├── 020_hypothesis.md     ← la hipótesis, con su condición de falsación
└── 025_constraints.md    ← RES-xxx (firmes) y SUP-xxx (por verificar)
```

⚠️ Las plantillas de estos cinco archivos aún no están escritas → `templates/`.

## 6. Condición de salida

La fase termina cuando **las cinco son ciertas**:

- [ ] Hay al menos una necesidad `N-xxx` enunciada **sin nombrar una pantalla**.
- [ ] Hay un **Actor Generador identificado y alcanzable**, con actor concreto.
- [ ] Los actores están clasificados por función, y **solo los que existen**.
- [ ] Los interesados están identificados.
- [ ] Hay **una hipótesis con su condición de falsación escrita**.

Si alguna falla, la fase sigue abierta. **No se pasa a `010_prototype` con una
hipótesis que no se puede tumbar**: el prototipo saldría sin nada que validar y el
Gate 1 no tendría criterio.

**Resultado alternativo válido:** `NO CONTINÚA`, si no hay Generador real. Se registra
por qué y se cierra.

## 7. Qué registra la ejecutora en `_memory/`

| Archivo | Qué escribe aquí |
|---|---|
| `progress.md` | la línea de fase: `FASE: DISCOVERY` → al cerrar, `FASE: PROTOTYPE` |
| `assumptions.md` | **todos los `SUP-xxx`** — esta fase es la que más produce |
| `constraints.md` | los `RES-xxx` encontrados |
| `lessons.md` | lo que se aprendió del negocio y no estaba en ningún documento |
| `tech-debt.md` | nada todavía: aún no hay código que pueda tener deuda |

---

## 8. Lo que esta fase le entrega al Gate 1

El Gate 1 lo cierra **la terminal auditora**, no la ejecutora (§32 del método). Para
poder hacerlo necesita que de aquí salgan dos cosas, y son las que más se olvidan:

1. **La hipótesis con su condición de falsación** — sin ella no hay contra qué medir
   el prototipo.
2. **El perfil del usuario representativo** — quién cuenta como Generador válido en
   una sesión de evaluación. Si se define después de las sesiones, se define a la
   medida de quien vino.

📌 Las dos se escriben **en esta fase**, y no se tocan durante `010_prototype`.
