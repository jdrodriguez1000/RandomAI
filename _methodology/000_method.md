# Método VERTICAL

> **Documento canónico.** Es la única versión vigente del método. Cuando este
> documento y una fuente de `sources/` digan cosas distintas, **manda este**.
>
> Las fuentes se conservan intactas en `sources/` como registro de cómo se diseñó
> el método. No se editan.

**Consolidado a partir de:** `sources/005_vertical.md` · `sources/010_prototyping.md` · `sources/015_evolution.md`

**Cada sección cita su origen** con la marca `↳`. Lo que lleva **➕** no está en las
fuentes: es una decisión tomada al consolidar, y está listada al final en el Anexo A.

---

# Parte I — Fundamentos

## 1. Propósito

El método VERTICAL transforma necesidades de negocio en software validado, mediante
prototipado, especificación incremental, Vertical Slices y trazabilidad completa.

Busca reducir el riesgo de construir software que no se use, que no resuelva el
problema, o que exija una inversión grande antes de descubrir que estaba mal.

No pretende eliminar la incertidumbre antes de empezar. Pretende **reducirla en el
momento en que es más barato hacerlo.**

↳ *005 §1 · 015 §1*

## 2. Principio rector

> **No se construye aquello que todavía no se entiende suficientemente bien.**

Esto **no** significa especificarlo todo antes de programar. Significa:

> Se define lo suficiente para empezar, se construye, se aprende, y se profundiza la
> definición a medida que el producto evoluciona.

↳ *005 §2*

## 3. Los cinco principios

1. Entender antes de construir.
2. Validar antes de invertir.
3. Construir incrementalmente.
4. Entregar valor mediante Vertical Slices.
5. Mantener trazabilidad desde la necesidad hasta la prueba.

↳ *005 §1*

## 4. La inversión crece por evidencia

Cada etapa responde **una pregunta distinta**, y cada una cuesta más que la anterior.
Solo se paga la siguiente cuando la anterior dio evidencia.

| Etapa | Pregunta que responde |
|---|---|
| **PROTOTIPO** | ¿La solución propuesta tiene sentido para el Actor Generador? |
| **MVP** | ¿El Actor Generador realmente adopta y usa la solución construida? |
| **EVOL** | ¿Cómo aumentamos el valor de algo que ya demostró adopción? |

> **No se realiza una inversión mayor hasta obtener evidencia suficiente que la
> justifique.**

Esto permite **detener una iniciativa temprano** cuando la evidencia dice que no vale
la pena continuar.

↳ *015 §2*

## 5. El ciclo completo

```text
NECESIDAD
    ↓
DESCUBRIMIENTO ............ actores, interesados, hipótesis
    ↓
PROTOTIPO INICIAL ......... camino feliz del Generador, descartable
    ↓
[ GATE 1 ] ................ ¿vale la pena construir?
    │
    ├── NO → replantear o detener
    │
    └── SÍ
         ↓
    PRODUCT BASELINE ...... PRD · BDD · SPEC · ARCHIT · ADR
         ↓
    WSLT .................. iteración 0: el esqueleto camina
         ↓
    GRTH-01 · GRTH-02 · … . Vertical Slices y tareas
         ↓
       MVP
         ↓
    [ GATE 2 ] ............ ¿vale la pena seguir invirtiendo?
         │
         ├── NO → aprender, replantear o detener
         │
         └── SÍ
              ↓
           EVOL-01 · EVOL-02 · …
              ↓
        (Release Objetivo, si el negocio lo necesita)
              ↓
           EVOL sigue
```

↳ *005 §3, §42 · 015 §34*

## 6. Filosofía de documentación

El método evita dos extremos:

| Extremo | Riesgo |
|---|---|
| **Sin documentación** — idea → código | decisiones implícitas, pérdida de conocimiento, sin trazabilidad, difícil de mantener |
| **Documentación exhaustiva antes de construir** | inversión prematura, documentos obsoletos, especificación basada en supuestos, poca capacidad de aprender |

La vía del método:

```text
Necesidad → Entender → Validar → Definir suficiente → Construir
         → Aprender → Definir más → Construir más
```

↳ *005 §40*

---

# Parte II — Actores e interesados

## 7. Qué es un actor

Un actor es una persona, rol, organización o sistema externo que interactúa con la
aplicación y tiene un propósito determinado dentro del proceso.

↳ *010 §4*

## 8. Tipo de actor y actor concreto

Son cosas distintas y no deben mezclarse.

- **Tipo de actor** — la categoría funcional. Ejemplo: *Actor Generador*.
- **Actor concreto** — la persona, rol o sistema que desempeña esa función en una
  aplicación específica. Ejemplo: *Cliente*.

| Tipo de actor | Actor concreto (app de reciclaje) |
|---|---|
| Generador | Cliente |
| Coordinador | Analista de logística |
| Ejecutor | Conductor / recolector |
| Supervisor | Gerente de operaciones |
| Administrador de Plataforma | Administrador de TI |
| Integrador | Servicio de mapas |

Esta separación es lo que hace la taxonomía **reutilizable entre empresas**.

> La clasificación **no se construye a partir de los cargos** de la empresa, sino de
> **la función que el actor desempeña dentro de la aplicación.** «Gerente de
> Operaciones» no es una categoría: es un actor concreto que ejerce de Supervisor.

↳ *010 §13, §15 · 015 §6*

## 9. La taxonomía: seis actores

### 9.1. Actor Generador

Realiza la acción principal que **da origen** al proceso de la aplicación.

> **Si el Generador no existe o no usa la aplicación, no hay razón fundamental para
> que la aplicación exista.**

Por eso es el punto de partida de todo el método: el prototipo lo valida a él, y el
MVP se construye para él.

### 9.2. Actor Coordinador

Recibe las solicitudes generadas y **coordina** los recursos, personas y actividades
necesarias para que se ejecuten: organiza, asigna, prioriza, distribuye, reasigna.

### 9.3. Actor Ejecutor

**Ejecuta** física o directamente el trabajo originado en la aplicación.

> La diferencia con el Coordinador: **el Coordinador organiza el trabajo; el Ejecutor
> lo realiza.**

### 9.4. Actor Supervisor

Usa la información que genera la aplicación para **supervisar** resultados, evaluar
desempeño e informar decisiones. No es un nivel jerárquico: lo define la función, no
el cargo.

### 9.5. Actor Administrador de Plataforma

Administra el **funcionamiento de la plataforma**: usuarios, roles, permisos,
parámetros, catálogos, configuraciones, integraciones. No ejecuta el proceso de
negocio. Puede ser interno o un tercero.

### 9.6. Actor Integrador

Un **sistema, plataforma o servicio externo** que intercambia información o ejecuta
acciones mediante una integración. No es necesariamente una persona: ERP, sistema
contable, pasarela de pago, mapas, GPS, correo, WhatsApp, autenticación, APIs.

**Agrupación:**

| Grupo | Actores |
|---|---|
| De negocio | Generador · Coordinador · Ejecutor · Supervisor |
| De plataforma | Administrador de Plataforma |
| Externo | Integrador |

↳ *010 §5–§11, §16 · 005 §5 · 015 §4*

## 10. No existe «Actor Invitado»

«Invitado» no describe un comportamiento: describe una **condición de acceso**.

Un socio con acceso temporal a ciertos informes es **Supervisor + acceso temporal**.
Un auditor externo es **Supervisor + usuario externo**.

> Lo temporal, lo externo y lo restringido se tratan como **permisos y seguridad**,
> nunca como un tipo de actor.

⚠️ `sources/005_vertical.md` §5.6 todavía lo lista como séptimo actor. **Esa fuente
está superada en este punto**; manda esta sección.

↳ *010 §12* ➕ *(decisión de consolidación: 005 y 015 lo incluían; 010 lo refutaba)*

## 11. Los actores son potenciales, no obligatorios

Que un tipo exista en la taxonomía no significa que deba existir en el producto.

Una aplicación puede empezar **solo con Generador** e incorporar los demás cuando
exista una necesidad real y justificada.

| Tipo de aplicación | Actores |
|---|---|
| Sencilla | Generador + Administrador de Plataforma |
| Operativa | Generador + Coordinador + Ejecutor |
| Empresarial | los seis |

↳ *005 §6 · 010 §4*

## 12. Interesados

Además de los actores que **usan** la aplicación, se identifican los **interesados**
del proyecto. Un interesado puede: decidir, financiar, definir políticas, aportar
conocimiento, aprobar resultados, verse afectado, representar usuarios, o imponer
restricciones legales o técnicas.

Los interesados **no necesariamente usan** la aplicación. No confundirlos con actores.

↳ *005 §7*

---

# Parte III — Etapa 0 · Descubrimiento

## 13. Propósito

El proyecto empieza entendiendo, no definiendo pantallas.

Lo que hay que entender:

- Por qué existe la necesidad.
- Para qué se necesita la aplicación.
- Qué problema se quiere resolver, y **quién lo tiene**.
- Quién usará la solución.
- Qué resultado espera la empresa.
- Qué procesos existen hoy.
- Qué restricciones existen.
- Qué sistemas actuales participan.
- Qué interesados deben ser consultados.

↳ *005 §4*

## 14. Salidas del Descubrimiento

- Registro de necesidades (`N-xxx`)
- Actores identificados y clasificados
- Interesados identificados
- **Hipótesis** a validar con el prototipo

↳ *005 §39*

---

# Parte IV — Etapa 1 · Prototipo Inicial

## 15. Propósito

Validar la **hipótesis funcional fundamental** del producto antes de invertir en el MVP.

> El prototipo es **un artefacto de validación funcional, no una versión preliminar
> del producto.**

Este malentendido es el riesgo principal de la etapa: el sponsor puede creer que *«el
prototipo representa la aplicación que se va a construir»*. No lo es.

↳ *010 §1, §2*

## 16. Características

El prototipo es:

- rápido;
- económico;
- **descartable**;
- funcionalmente enfocado;
- suficientemente realista para permitir interacción;
- construido alrededor del **camino feliz**.

Puede ser HTML cliqueable, mockup, simulación o prototipo interactivo.

**No** requiere arquitectura definitiva, **no** contempla todos los actores, **no**
implementa todos los casos de uso, y **no** se evalúa con los criterios de un MVP.

**No es software productivo.**

↳ *005 §9 · 010 §2*

## 17. Alcance y duración

**Alcance:** el camino feliz del **Actor Generador**, porque es la condición de
existencia de la aplicación.

**Duración:** máximo aproximado de **3 a 4 semanas**. El límite existe para mantenerlo
como una inversión pequeña; no se perfecciona indefinidamente.

↳ *005 §8 · 015 §8, §9*

## 18. Qué busca validar

- El usuario entiende la solución.
- El flujo resulta natural.
- La solución resuelve la necesidad.
- El usuario está dispuesto a usarla.
- Las funcionalidades principales tienen sentido.
- El camino feliz es viable.
- No hay problemas funcionales importantes.

↳ *005 §10*

## 19. Principio de evaluación: comportamiento, no opinión

El objetivo **no** es saber si al usuario «le gusta».

> **El objetivo es determinar si el Actor evaluado puede comprender y ejecutar
> correctamente el camino feliz.**

El enfoque tradicional —mostrar el prototipo y pedir opinión— falla porque el usuario
puede sentirse comprometido con la empresa, querer agradar al sponsor, sentirse
evaluado, aceptar algo que no entendió, sugerir funciones innecesarias, o afirmar que
lo usaría sin haber demostrado que puede usarlo.

> **La evaluación pasa de «preguntar qué piensa el usuario» a «observar cómo se
> comporta frente a una tarea».**

↳ *010 §17, §18, §25*

## 20. Los diez principios de no sesgo

1. No explicar previamente cómo usar el prototipo.
2. Presentar **una tarea**, no una secuencia de clics.
3. Permitir que el usuario explore.
4. No corregir inmediatamente los errores.
5. No responder preguntas de forma que revelen la solución.
6. Evitar que el sponsor intervenga.
7. Registrar el comportamiento antes que las opiniones.
8. Preguntar **después** de la interacción.
9. Usar usuarios representativos.
10. Separar las observaciones del usuario de las decisiones del negocio.

↳ *010 §30*

## 21. La tarea

Se entrega **contexto y tarea**, nunca instrucciones.

| ❌ No se dice | ✅ Se dice |
|---|---|
| «Haz clic en *Solicitar recolección* y luego selecciona la fecha.» | «Imagina que tienes varias bolsas de material reciclable en tu oficina y quieres que la empresa las recoja. Usa esta aplicación para hacerlo.» |

Durante la tarea se observa: ¿entiende dónde empezar? ¿encuentra la opción correcta?
¿comprende los campos y las opciones? ¿sabe qué información introducir? ¿completa el
proceso? ¿comete errores? ¿se bloquea? ¿necesita ayuda?

↳ *010 §19, §20*

## 22. Roles de la sesión

| Rol | Hace | No hace |
|---|---|---|
| **Facilitador** | explica el ejercicio, entrega la tarea, pregunta neutral, observa, registra | enseñar la solución; intervenir más de lo mínimo |
| **Usuario** | realiza la tarea | — |
| **Observadores** (empresa) | observan, toman notas, registran comportamientos | **intervenir durante la interacción** |
| **Sponsor** | observa | responder las preguntas del usuario durante la prueba |

Si el usuario pregunta *«¿aquí debo poner la dirección?»*, el sponsor **no** responde
«sí». El facilitador mantiene la neutralidad y deja que el usuario decida.

↳ *010 §22*

## 23. Selección de usuarios

No se eligen los usuarios fáciles de conseguir o afines a la empresa. **Antes** de la
prueba se define qué características debe tener un usuario real del Actor evaluado:
experiencia baja/media/alta, tipo de cliente, frecuencia de uso, contexto operativo,
tipo de necesidad.

El objetivo es que los participantes **representen razonablemente al Actor real**.

↳ *010 §23*

## 24. Los cuatro estados de resultado

Llegar al final no basta: hay que registrar **cómo** se llegó.

| Estado | Significado | Valor |
|---|---|---:|
| **Éxito autónomo** | completa sin ayuda | 3 |
| **Éxito con dudas** | completa sin ayuda, pero con dudas importantes → debe analizarse | 2 |
| **Éxito con ayuda** | el facilitador intervino → **no es un éxito completo** | 1 |
| **Fracaso** | no completa → el flujo necesita revisión | 0 |

La escala es un apoyo. Lo importante es **identificar patrones y entender causas**.

↳ *010 §21*

## 25. Preguntas posteriores

Después de la tarea, y solo después, preguntas neutrales:

- **Comprensión** — «¿Qué creías que iba a pasar cuando hiciste clic aquí?»
- **Dificultad** — «¿Hubo algún momento en que no supieras qué hacer?»
- **Expectativa** — «¿Esperabas encontrar alguna otra opción?»
- **Necesidad** — «¿Qué información necesitarías realmente para completar esto?»
- **Proceso actual** — «¿Cómo haces esto hoy?»

La última es especialmente importante: permite comparar la solución propuesta con el
comportamiento real.

↳ *010 §24*

## 26. Las cuatro dimensiones de validación

| | Pregunta |
|---|---|
| **A · Ejecución** | ¿Puede el usuario completar la tarea? |
| **B · Comprensión** | ¿Comprende lo que hace y el significado de las opciones? |
| **C · Necesidad** | ¿El flujo representa una forma válida de resolver su necesidad real? |
| **D · Negocio** | ¿El flujo representa correctamente el proceso que la empresa quiere implementar? |

**C y D se mantienen diferenciadas.** El usuario valida *«esto representa cómo yo
haría esta tarea»*; la empresa valida *«este flujo es compatible con nuestro
proceso»*. Puede ocurrir que el usuario lo use bien y el sponsor descubra que choca
con una regla interna — o al revés. **Ambas deben ser satisfactorias.**

↳ *010 §26, §27*

## 27. Una observación no es un requisito

Los usuarios dirán cosas como *«sería bueno que también pudiera hacer X»*. Eso **no**
significa que el prototipo fracasó por no tener X.

Las observaciones se clasifican después como: problema funcional · problema de
comprensión · problema de usabilidad · necesidad no contemplada · sugerencia · nueva
funcionalidad potencial · caso excepcional · requisito de negocio · idea para una
fase posterior.

> **Una observación del usuario no se convierte automáticamente en un requisito del
> MVP.**

↳ *010 §28*

---

# Parte V — Gate 1 · ¿Vale la pena construir?

## 28. La pregunta

> **¿Vale la pena construir el MVP?**

Es la **primera barrera de inversión** del método.

↳ *015 §27*

## 29. Criterios de aprobación

El prototipo se considera exitoso cuando hay evidencia suficiente de que:

1. El problema identificado es relevante.
2. La solución propuesta es comprensible.
3. El Actor Generador puede ejecutar el flujo principal **de forma autónoma**.
4. La solución satisface razonablemente la necesidad.
5. No existen problemas funcionales fundamentales que impidan continuar.
6. Existe confianza suficiente para realizar la inversión del MVP.
7. **La empresa considera válido el proceso de negocio representado.** *(dimensión D)*

**Definición de éxito:**

> Usuarios representativos del Actor evaluado **completan de forma autónoma** el
> camino feliz definido, **comprenden** lo que hacen, y **confirman** que el flujo es
> una forma válida de resolver la necesidad — **y la empresa valida el proceso de
> negocio representado.**

↳ *005 §12 · 010 §29*

## 30. Qué significa aprobar, y qué no

Aprobar el Gate 1 **no** significa que el producto esté definido.

Significa exactamente esto:

> **Hay evidencia suficiente para justificar la construcción del MVP.**

Y **no** autoriza EVOL. Solo autoriza el MVP.

↳ *005 §12 · 015 §15, §24*

## 31. Resultados posibles

| Resultado | Consecuencia |
|---|---|
| **Aprobado** | → Product Baseline → WSLT |
| **No aprobado** | → aprender, replantear la hipótesis, o detener |

Detener aquí es un **resultado válido y barato**. Es el propósito de la etapa.

↳ *005 §3 · 015 §14, §15*

## 32. ➕ Quién declara el Gate

El veredicto del Gate **no lo emite quien construyó el prototipo.**

Quien construye no puede ser su propio testigo: un sistema que se revisa a sí mismo
comprueba que es coherente, no que sea cierto. El Gate lo declara la **terminal
auditora** contra los criterios de §29 y la evidencia registrada de las sesiones.

➕ *(adición de consolidación — conecta el método con el esquema de dos terminales;
las fuentes no asignan dueño al veredicto)*

---

# Parte VI — Product Baseline

## 33. Qué es

Una vez aprobado el Gate 1 se construye la **Baseline del Producto**: no una
documentación exhaustiva, sino **la información necesaria para empezar a construir de
manera controlada.**

Se compone de: **PRD · BDD · SPEC · ARCHIT · ADR**.

↳ *005 §13*

## 34. PRD — Product Requirements Document

La perspectiva del **producto**: propósito, problema, objetivos, alcance inicial,
propuesta de valor, actores, necesidades, restricciones, criterios generales de éxito.

Evoluciona durante la construcción.

↳ *005 §14*

## 35. BDD — Behavior Driven Development

El **comportamiento esperado**: Features, Scenarios, reglas de negocio.

```gherkin
Feature: Solicitar recogida

  Scenario: Solicitud de recogida exitosa
    Given el Generador se encuentra autenticado
    When solicita una recogida válida
    Then la aplicación registra la solicitud
```

Evoluciona incrementalmente.

↳ *005 §15*

## 36. SPEC — Project Specification

Lo necesario para **construir**: funcionalidades, reglas, datos, interfaces,
validaciones, requisitos funcionales y no funcionales, restricciones, integraciones.

No se especifican funcionalidades que todavía no se van a construir.

↳ *005 §16*

## 37. ARCHIT — Architecture

En dos niveles:

- **Arquitectura Base** — principios, componentes principales, límites, tecnologías,
  integraciones conocidas, seguridad, despliegue, atributos de calidad relevantes.
- **Arquitectura Incremental** — se amplía a medida que las Vertical Slices
  introducen nuevas necesidades.

> **La arquitectura también aprende.**

↳ *005 §17*

## 38. ADR — Architecture Decision Records

Cada decisión arquitectónica importante se registra con: **contexto, problema,
alternativas, decisión, consecuencias.**

Conserva **la razón** detrás de la decisión, que es lo que se pierde primero.

↳ *005 §18*

## 39. Documentación incremental

PRD, BDD, SPEC y ARCHIT **no son documentos que deban terminarse antes de programar.
Son artefactos vivos.**

> **Definir suficientemente el futuro inmediato y no especular sobre el futuro
> lejano.**

```text
Baseline → WSLT → GRTH → nueva información
        → actualización de PRD/BDD/SPEC/ARCHIT → nueva Vertical Slice
```

↳ *005 §19*

---

# Parte VII — Construcción

## 40. WSLT — Walking Skeleton (Iteración 0)

Comprueba que **existe un camino técnico de extremo a extremo**, con los elementos
principales conectados:

```text
Usuario → Frontend → Backend → Base de datos → Respuesta
```

No busca entregar el MVP. Busca demostrar que:

> **La arquitectura propuesta puede sostener el desarrollo del producto.**

↳ *005 §20 · 015 §16*

## 41. GRTH — Growth

Después del WSLT empieza el crecimiento progresivo hacia el MVP, en una o varias
iteraciones:

```text
WSLT → GRTH-01 → GRTH-02 → GRTH-03 → MVP
```

Cada GRTH incorpora nuevas capacidades hasta alcanzar el alcance definido para el MVP.

↳ *005 §21 · 015 §18, §19*

## 42. Vertical Slices

> Una **unidad incremental de construcción** que entrega una capacidad funcional
> completa o significativamente utilizable, **atravesando de extremo a extremo** las
> capas necesarias del sistema.

↳ *005 §22 · 015 §17*

## 43. Feature y Vertical Slice no son sinónimos

Una Vertical Slice puede contener una Feature, varias Features relacionadas, o parte
de una Feature grande. Y una Feature puede requerir varias Vertical Slices.

```text
Feature "Programar recogida recurrente"
   ├── VS-01 Crear recurrencia
   ├── VS-02 Modificar recurrencia
   ├── VS-03 Cancelar recurrencia
   └── VS-04 Gestionar excepciones

VS-01 "Solicitar recogida"
   ├── Feature: Seleccionar material
   ├── Feature: Indicar ubicación
   └── Feature: Seleccionar fecha
```

↳ *005 §23*

## 44. Tareas

Cada Vertical Slice se descompone en tareas **pequeñas, específicas, verificables,
claramente delimitadas y trazables a su Vertical Slice.**

```text
VS-01 Crear solicitud
  T-001 Crear entidad Solicitud
  T-002 Crear tabla Solicitudes
  T-003 Crear API de creación
  T-004 Crear formulario de material
  T-005 Crear formulario de ubicación
  T-006 Implementar validación
  T-007 Implementar confirmación
  T-008 Crear pruebas
```

> La tarea debe ser **lo bastante pequeña para que su estado pueda determinarse
> claramente.**

↳ *005 §24*

## 45. Trazabilidad

Es un principio fundamental. Toda unidad de construcción debe poder relacionarse con
una razón funcional o de negocio.

```text
NECESIDAD → FEATURE → SCENARIO → VERTICAL SLICE → TASK → IMPLEMENTACIÓN → PRUEBA
```

Y funciona **en las dos direcciones**:

| Dirección | Pregunta que responde |
|---|---|
| **Hacia adelante** — necesidad → prueba | ¿Cómo se implementó esta necesidad? |
| **Hacia atrás** — prueba → necesidad | ¿Por qué estamos construyendo esto? |

↳ *005 §25, §26*

## 46. Identificadores

| Prefijo | Elemento |
|---|---|
| `N-001` | Necesidad |
| `F-001` | Feature |
| `S-001` | Scenario |
| `VS-001` | Vertical Slice |
| `T-001` | Task |
| `TC-001` | Test Case |
| `ADR-001` | Decisión arquitectónica |

```text
N-001 → F-001 → S-001 → VS-001 → T-001 → TC-001
```

↳ *005 §27*

## 47. Regla de trazabilidad

> **Nada se construye sin una razón trazable.**

Si aparece una tarea que no puede relacionarse con una Vertical Slice, Scenario,
Feature o necesidad, **debe cuestionarse su inclusión.**

Esto controla: scope creep · funcionalidades innecesarias · tareas huérfanas ·
trabajo no justificado · desviaciones del MVP.

↳ *005 §28*

---

# Parte VIII — MVP y Gate 2

## 48. Qué es el MVP

Una versión **real y utilizable** que resuelve el problema principal, con el software,
la persistencia, las reglas de negocio y la seguridad que correspondan.

**Duración:** no tiene una fija — 8, 12, 16 semanas o lo que sea razonable. Lo
importante no son las semanas:

> **El MVP debe permanecer enfocado en entregar el mínimo valor real al Actor
> Generador.**

↳ *010 §3 · 015 §20, §21*

## 49. Operación híbrida

El MVP puede funcionar **solo con el Actor Generador**. Los demás actores pueden
seguir usando temporalmente los procesos existentes:

```text
Generador → APLICACIÓN MVP → información → Excel / Sheets / software existente → Coordinador
```

> **No es obligatorio digitalizar todo el ecosistema para lanzar el MVP.**

Esto concentra la inversión inicial en validar la adopción del Generador.

↳ *005 §34 · 015 §22*

## 50. Condición de viabilidad de la operación híbrida

Aunque los demás actores no estén en el MVP, hay que evaluar si los procesos
existentes **pueden absorber** el trabajo que genera la nueva aplicación.

No basta decir *«el Coordinador seguirá usando Excel»*. Hay que preguntar:

> **¿El proceso manual sigue siendo operacionalmente viable con el volumen que
> genera el MVP?**

Si la respuesta es no, puede ser necesario **incorporar anticipadamente** al
Coordinador u otro actor.

↳ *015 §23*

## 51. Gate 2 — ¿Vale la pena seguir invirtiendo?

La **segunda barrera de inversión**. La pregunta cambia respecto al Gate 1:

| | Pregunta |
|---|---|
| **Gate 1 · Prototipo** | ¿El usuario **podría** usar esta solución? |
| **Gate 2 · MVP** | ¿El usuario **realmente adopta y usa** esta solución? |

El MVP se evalúa **en condiciones reales de uso**.

**Criterios de aprobación** — evidencia suficiente de que:

1. El Actor Generador puede usar la aplicación.
2. Logra realizar la actividad principal.
3. Obtiene el valor esperado.
4. Existe **adopción real**.
5. Existe **utilización real o recurrente**.
6. Vale la pena seguir invirtiendo.

La métrica exacta depende del producto: usuarios activos, frecuencia, transacciones,
porcentaje de adopción, recurrencia, retención, reducción de trabajo, satisfacción,
cumplimiento de objetivos. **Se define antes de medir, no después.** ➕

↳ *015 §24, §25, §27*

## 52. Resultados posibles

| Resultado | Consecuencia |
|---|---|
| **MVP exitoso** | adopción y valor → **EVOL** |
| **MVP no exitoso** | → aprender, replantear, modificar o detener |

> **Es preferible descubrir tras invertir en un MVP que la solución no será usada,
> que descubrirlo después de haber construido todo el producto.**

↳ *015 §26 · 005 §36*

---

# Parte IX — EVOL · Evolución

## 53. Propósito

Las iteraciones EVOL aumentan progresivamente el valor de una solución **que ya
demostró adopción**.

```text
MVP → EVOL-01 → EVOL-02 → EVOL-03 → EVOL-N
```

No hay un número predeterminado.

↳ *005 §33 · 015 §28, §29*

## 54. Qué incorpora

Nuevas funcionalidades del Generador · funcionalidades de los demás actores ·
Integradores · mejoras · automatizaciones · nuevas capacidades de negocio.

Las nuevas capacidades vienen principalmente de **los usuarios** y **del negocio**.

↳ *005 §33 · 015 §29*

## 55. Incorporación progresiva de otros actores

EVOL es donde entran Coordinador, Ejecutor, Supervisor, Administrador e Integradores
— cuando hay necesidad real y justificada, no por completitud.

↳ *005 §34 · 015 §31*

## 56. El doble beneficio de evolucionar a la vista

1. **Los usuarios ven crecer la aplicación.**
2. **Ven reflejadas sus necesidades** — perciben que las nuevas capacidades responden
   a lo que ellos plantearon.

Esto favorece adopción, confianza, participación, retroalimentación y apropiación del
producto.

↳ *005 §37*

## 57. Prototipo de Evolución

Durante GRTH o EVOL aparecen nuevas necesidades. **No todas requieren prototipado.**

| | Prototipo Inicial | Prototipo de Evolución |
|---|---|---|
| **Cuándo** | al comienzo del proyecto | durante la evolución |
| **Pregunta** | ¿la solución tiene sentido para el Generador? | ¿esta nueva capacidad resuelve bien la necesidad, y cuál es la mejor forma de implementarla? |
| **Autoriza** | construir el MVP | construir la funcionalidad |

**No es una etapa nueva del ciclo.** No reemplaza ni modifica WSLT, GRTH, MVP ni
EVOL: es una herramienta que se usa dentro de ellos cuando hace falta.

↳ *005 §29 · 015 Anexo §3, §4*

## 58. Cuándo usarlo y cuándo no

**El criterio que decide:**

> **Nivel de incertidumbre × impacto de equivocarse.**

| Se usa cuando | No hace falta para |
|---|---|
| aparece una funcionalidad con comportamiento desconocido | cambios simples |
| hay varias alternativas funcionales | cambios visuales menores |
| cambia significativamente el comportamiento del usuario | modificaciones evidentes |
| hay alto riesgo de rechazo | funcionalidades ya validadas |
| la funcionalidad es crítica | cambios de bajo riesgo |
| se incorpora un nuevo actor | correcciones claramente definidas |
| hay interacción entre varios actores | |
| hay incertidumbre importante sobre el flujo | |

> **El método no busca convertir el prototipado en burocracia.**

↳ *005 §30, §31*

## 59. Principio de proporcionalidad

> **El esfuerzo de prototipado debe ser proporcional a la incertidumbre y al costo de
> equivocarse.**

Un Prototipo de Evolución puede ser un boceto, un wireframe, HTML, una simulación o un
mockup. **No tiene que tener la profundidad del Prototipo Inicial.**

↳ *005 §32*

## 60. No existe una etapa FINAL

El producto no se trata como algo que llega a una única versión definitiva. EVOL
continúa mientras exista **valor, necesidad, oportunidad e inversión justificada.**

Si el negocio necesita señalar una versión como objetivo, se usa **Release Objetivo**
(o Release / Milestone / Version), definido por proyecto, contrato, estrategia,
negocio, cliente u objetivo de producto.

Pero un Release Objetivo **no cierra el producto**: después pueden seguir EVOL-04,
EVOL-05, EVOL-06…

↳ *005 §38 · 015 §32, §33*

---

# Parte X — Resumen

## 61. Los diez principios del método

| # | Principio |
|---|---|
| 1 | **Validar antes de invertir** — el prototipo reduce el riesgo antes del MVP |
| 2 | **Construir lo mínimo necesario** — el MVP se concentra en el Generador |
| 3 | **No construir todo para todos** — los demás actores entran cuando se justifican |
| 4 | **Especificar incrementalmente** — PRD, BDD, SPEC y ARCHIT son artefactos vivos |
| 5 | **La arquitectura también aprende** — WSLT y las Vertical Slices la validan |
| 6 | **Prototipar cuando haya incertidumbre** — no toda funcionalidad lo necesita |
| 7 | **Construir mediante Vertical Slices** — cada incremento entrega capacidad trazable |
| 8 | **Dividir en tareas pequeñas** — específicas, verificables, trazables |
| 9 | **Mantener trazabilidad** — nada se construye sin razón trazable |
| 10 | **Evaluar el MVP** — el prototipo autoriza construir; la adopción autoriza evolucionar |

↳ *005 §41*

## 62. Definición

> El método VERTICAL es un enfoque **incremental y trazable** para desarrollar
> software. Empieza comprendiendo una necesidad, valida la hipótesis con un Prototipo
> Inicial, establece una Baseline suficiente para construir, desarrolla el producto
> mediante WSLT, GRTH y Vertical Slices, descompone cada incremento en tareas
> pequeñas, mantiene trazabilidad desde la necesidad hasta las pruebas, y usa
> Prototipos de Evolución cuando la incertidumbre lo justifica.
>
> Su objetivo no es construir software. Es **construir progresivamente el software
> correcto, reduciendo el costo de equivocarse y manteniendo evidencia de por qué
> cada parte del producto existe.**

↳ *005 §43*

---

# Anexo A — Decisiones tomadas al consolidar

Lo que este documento cambió respecto a las tres fuentes. Todo lo marcado **➕** en el
cuerpo aparece aquí.

| # | Decisión | Fuentes en conflicto | Resolución |
|---|---|---|---|
| **A.1** | **No existe Actor Invitado.** La taxonomía tiene **seis** actores | `005 §5.6` y `015 §5` lo incluyen; `010 §12` lo refuta con argumento | Gana `010`: «invitado» es una **condición de acceso**, no un comportamiento. Se trata como permiso |
| **A.2** | **Los Gates son piezas de primera clase**, con sección propia y criterios listados | `015 §27` los nombra explícitos; `005` los deja implícitos en el diagrama | Se adoptan de `015` y se les da estructura propia (§28–§32, §51–§52) |
| **A.3** | **La evaluación de prototipos se toma en su versión profunda** | `010 §17–§31` (detallada) vs `005 §11` (dos párrafos) | Gana `010`. `005` queda superado en este punto |
| **A.4** | **La taxonomía de actores se declara una sola vez** | aparece en las tres fuentes, con redacciones distintas | Se unifica en §9, tomando `010` como base por ser la más razonada |
| **A.5** | ➕ **El veredicto de un Gate no lo emite quien construyó** | ninguna fuente asigna dueño al veredicto | Adición. Conecta el método con el esquema de dos terminales (§32) |
| **A.6** | ➕ **La métrica de adopción del Gate 2 se define antes de medir** | `015 §25` lista métricas posibles sin decir cuándo se eligen | Adición. Elegir la métrica después de ver el resultado no es medir |
| **A.7** | **Se elimina la voz de deliberación** | las tres fuentes usan «se consideró…», «hasta este punto», «inicialmente se denominó…» | El método se enuncia en presente y sin condicionales. La deliberación queda en `sources/` |

⚠️ **Pendiente:** A.1, A.2, A.5 y A.6 merecen un ADR propio con contexto, alternativas
y consecuencias. Aún no se han escrito.
