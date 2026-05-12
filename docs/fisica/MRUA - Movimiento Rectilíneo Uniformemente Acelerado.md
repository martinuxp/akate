A diferencia del MRU, aquí la velocidad **no es constante**, sino que cambia. Imagina que estás en un semáforo y la luz cambia a verde: el auto no aparece mágicamente a 50 km/h, sino que va **aumentando su rapidez** poco a poco. Eso es la aceleración, una de las variables del MRUA.

> [!DEFINICIÓN]
> El MRUA es el movimiento en línea recta donde la velocidad cambia de manera uniforme (siempre aumenta o disminuye la misma cantidad cada segundo).
> 

Como el profe no enseño más, nos enfocaremos solo en calcular la **Aceleración**.

## 📝 Términos fáciles

- **Velocidad Inicial ($v_i$):** La velocidad con la que empieza el objeto. (Si dice "parte del reposo", es **0**).

- **Velocidad Final ($v_f$):** La velocidad que alcanza después de un tiempo.

- **Tiempo ($t$):** Cuánto demoró ese cambio de velocidad.

- **Aceleración ($a$):** Qué tan rápido cambió la velocidad.


---

## 📐 La Fórmula (la única por ahora)

Para calcular la aceleración, restamos la velocidad final por la inicial y las dividimos por el tiempo:

$$a = \frac{v_f - v_i}{t}$$

> [!Dato Akate]
>
> > 
> > 1. Si el resultado es **positivo**, el objeto está acelerando (va más rápido).
> > 2. Si el resultado es **negativo**, el objeto está frenando.
> >

---
## 🏃 Ejemplo 1 - El auto que acelera

**Problema:** Un auto que viaja a **10 m/s** aumenta su velocidad hasta llegar a **30 m/s** en apenas **4 segundos**. ¿Cuál fue su aceleración?

### 1. Recoge los datos

- $v_i = 10 \text{ m/s}$

- $v_f = 30 \text{ m/s}$

- $t = 4 \text{ s}$

### 2. Resuelve

$$a = \frac{30 - 10}{4}$$

$$a = \frac{20}{4}$$

**Resultado:** $a = 5 \text{ m/s}^2$

---

## 🧐 ¿Por qué el resultado es $m/s^2$?

Es la forma de decir que la velocidad cambia "tantos metros por segundo, **cada segundo**".

Por eso el segundo aparece dos veces ($s \cdot s$), lo que se escribe como $s^2$.

> [!Recuerda!]
> ¡Y recuerda añadirlo siempre y que no se te olvide!

---

## 🛑 Ejemplo 2 - Cuando el objeto frena

**Problema:** Un ciclista que va a **8 m/s** frena en seco hasta detenerse en **2 segundos**. ¿Cuál es su aceleración?

### 1. Datos

- $v_i = 8 \text{ m/s}$

- $v_f = 0 \text{ m/s}$ (porque se detuvo).

- $t = 2 \text{ s}$


### 2. Resolución

$$a = \frac{0 - 8}{2}$$

$$a = \frac{-8}{2}$$

**Resultado:** $a = -4 \text{ m/s}^2$

> [!Recuerda!]
> _El signo menos significa que está perdiendo velocidad._

---

## 🔄 Ejemplo 3 - Conversión necesaria

**Problema:** Un tren parte del reposo y alcanza **72 km/h** en **10 segundos**. Calcula su aceleración en $m/s^2$.

### ⚠️ ¡Cuidado!

Primero debemos pasar los **72 km/h** a **m/s** usando nuestro "Número Mágico" que vimos en la seccion de MRU.

> [!Resumen de Conversiones.]
> - **1 hora** = $3600 \text{ segundos}$
> 
> - **1 minuto** = $60 \text{ segundos}$
> 
> - **km/h $\rightarrow$ m/s**: Divide por $3,6$
> 
> - **m/s $\rightarrow$ km/h**: Multiplica por $3,6$

Para pasar de **km/h** a **m/s** dividiremos el **72** por **3,6.**
 - $72 \div 3,6 = 20 \text{ m/s}$


### Ahora resolvemos:

- $v_i = 0$
    
- $v_f = 20 \text{ m/s}$
    
- $t = 10 \text{ s}$
    

$$a = \frac{20 - 0}{10} = 2 \text{ m/s}^2$$

---

## 🖥️ Akate _"MRUA - Aceleración"_ Prompt

Copia este prompt especializado:

Plaintext

```
Actúa como un Asistente de Estudio de "Akate". Mi objetivo hoy es aprender exclusivamente a calcular la ACELERACIÓN en el MRUA.

### 📋 Reglas:
1. **Fórmula Única:** Céntrate solo en a = (vf - vi) / t. No uses fórmulas de distancia por ahora.
2. **Conceptos:** Ayúdame a identificar cuándo vi es 0 (reposo) y cuándo vf es 0 (detenerse).
3. **Práctica:** Dame ejercicios para calcular aceleración, incluyendo algunos donde deba convertir km/h a m/s antes de empezar.
4. **Corrección:** Si olvido poner el "al cuadrado" en la unidad (m/s2), recuérdamelo, es muy importante para la prueba.

¡Empecemos! Pregúntame si prefieres un tono formal o informal.
```