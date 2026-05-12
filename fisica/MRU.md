Imagina que vas caminando en línea recta a una velocidad fija (por ejemplo, 10 km/h constantes). Eso es el **MRU**. También puedes imaginar un auto en autopista sin acelerar ni frenar: recorre la misma distancia cada segundo.

> [!DEFINICIÓN]
> El **Movimiento Rectilíneo Uniforme (MRU)** es el movimiento de un objeto en línea recta con velocidad constante, lo que significa que recorre distancias iguales en tiempos iguales.

El MRU es fundamental para entender la física clásica y las leyes de Newton, ya que nos permite analizar objetos antes de estudiar movimientos más complejos con aceleración.

## 📝 Términos faciles

- **Distancia ($d$):** Qué tan lejos llegaste.

- **Velocidad ($v$):** Qué tan rápido vas (en MRU, siempre es igual).

- **Tiempo ($t$):** Cuánto demoraste en ir de un punto a otro.

---

## 📐 El Triángulo Mágico

Una forma práctica de recordar las fórmulas es usando este triángulo:
![Triángulo Mágico](../assets/img/Pasted%20image%2020260510030317.png){ width="280" }

> **TIP:** Para usarlo, simplemente tapa con tu dedo la variable que quieres encontrar.
> 
> - Si las variables quedan **una al lado de la otra**, se multiplican.
>    
> - Si una está **arriba de la otra**, se dividen.
>    

### Las Fórmulas

- **Si buscas Distancia ($d$):** Tapas la $d$ y quedan $v$ y $t$ juntas. $$d = v \cdot t$$

- **Si buscas Velocidad ($v$):** Tapas la $v$ y queda $d$ sobre $t$. $$v = \frac{d}{t}$$
- **Si buscas Tiempo ($t$):** Tapas la $t$ y queda $d$ sobre $v$.$$t = \frac{d}{v}$$

---

## 🏃 Ejemplo 1 - El maratonista

**Problema:** Si un maratonista corre a una velocidad constante de **5 m/s** por un lapso de **30 s**, ¿qué distancia recorrió?

### 1. Recoge los datos

- **Velocidad ($v$):** $5 \text{ m/s}$

- **Tiempo ($t$):** $30 \text{ s}$

### 2. Resuelve

De acuerdo al triángulo, la fórmula es $d = v \cdot t$. Reemplazamos:

$$d = 5 \text{ m/s} \cdot 30 \text{ s}$$

$$d = 150 \text{ m}$$

---

## 🧐 ¿Por qué m/s × s = metros?

Imagínalo como una simplificación de fracciones en matemática.

1. **La estructura:** Tienes una fracción multiplicada por los segundos:
    
    $$\frac{\text{metros}}{\text{segundos}} \times \text{segundos}$$
    
2. **La cancelación:** Cuando una unidad está arriba (numerador) y la misma está afuera multiplicando, se "cancelan" entre sí.
    
    $$\frac{\text{metros}}{\cancel{\text{segundos}}} \times \cancel{\text{segundos}} = \text{metros}$$
    

> **Explicación rápida:** Si tienes 3 manzanas por caja y compras 2 cajas, las "cajas" se cancelan y te quedan solo "manzanas". Aquí es igual: la rapidez nos dice cuántos metros recorres en cada segundo, y al multiplicarlo por el tiempo total, obtenemos la distancia total.

---

## 🕒 Ejemplo 2: Calculando el Tiempo

**Problema:** Un ciclista viaja por una ruta recta a una velocidad constante de **12 m/s**. Si debe recorrer una distancia de **600 metros**, ¿cuánto tiempo tardará en llegar?

### 1. Datos

- **Velocidad ($v$):** $12 \text{ m/s}$

- **Distancia ($d$):** $600 \text{ m}$


### 2. Resolución

Usando el triángulo, tapamos la $t$ y obtenemos la fórmula: $t = \frac{d}{v}$

$$t = \frac{600 \text{ m}}{12 \text{ m/s}}$$

$$t = 50 \text{ s}$$

**Resultado:** El ciclista tardará **50 segundos**.

---

## 🏎️ Ejemplo 3: Calculando la Velocidad

**Problema:** Un vehículo de prueba recorre una pista recta de **2000 metros** en un tiempo de **40 segundos**. ¿Cuál es la velocidad constante del vehículo?

### 1. Datos

- **Distancia ($d$):** $2000 \text{ m}$

- **Tiempo ($t$):** $40 \text{ s}$


### 2. Resolución

Tapamos la $v$ en nuestro triángulo y nos queda: $v = \frac{d}{t}$

$$v = \frac{2000 \text{ m}}{40 \text{ s}}$$

$$v = 50 \text{ m/s}$$

**Resultado:** El vehículo se desplaza a **50 m/s**.

---

## 🔄 Ejemplo 4: Conversión de Unidades (km/h a m/s)

**Problema:** Un bus viaja por la carretera a **90 km/h**. ¿Cuál es su velocidad expresada en **m/s**?

### 💡 Hack del "Número Mágico"

Para pasar de **km/h a m/s** de forma rápida, solo tienes que **dividir por 3,6**. (Si quieres pasar de m/s a km/h, multiplicas por 3,6).

### Resolución

- **Velocidad en km/h:** $90$

- **Cálculo:** $90 \div 3,6$ $$v = 25 \text{ m/s}$$

**Resultado:** Viajar a 90 km/h es lo mismo que recorrer **25 metros cada segundo**.


---

## ⏱️ Ejemplo 5: Conversión de Tiempo (Minutos/Horas a Segundos)

**Problema:** Un avión vuela a una velocidad constante de **250 m/s** durante **2 minutos**. ¿Qué distancia recorrió en ese tiempo?

### ⚠️ ¡Cuidado aquí!

No puedes multiplicar $250 \text{ m/s}$ por $2 \text{ minutos}$ directamente, porque las unidades de tiempo no coinciden (segundos vs minutos). Debes convertir todo a **segundos**.

### 1. Convertir el tiempo

- $1 \text{ minuto} = 60 \text{ segundos}$

- $2 \text{ minutos} = 2 \cdot 60 = 120 \text{ segundos}$


### 2. Resolución

Ahora que tenemos el tiempo en segundos ($t = 120 \text{ s}$), usamos la fórmula de distancia: $d = v \cdot t$

$$d = 250 \text{ m/s} \cdot 120 \text{ s}$$

$$d = 30.000 \text{ m}$$

**(Opcional):** Si lo quieres en kilómetros, divides por 1000 $\rightarrow 30 \text{ km}$.

---

## 📝 Resumen de Conversiones:

- **1 hora** = $3600 \text{ segundos}$

- **1 minuto** = $60 \text{ segundos}$

- **km/h $\rightarrow$ m/s**: Divide por $3,6$

- **m/s $\rightarrow$ km/h**: Multiplica por $3,6$

## 🖥️ *"MRU"* Prompt
Copia y envia en el mensaje inicial el siguiente prompt en tu AI de preferencia para un estudio personalizado sobre el MRU:
```
Actúa como un Asistente de Estudio. Tu objetivo es ayudarme a comprender el Movimiento Rectilíneo Uniforme (MRU).

### 📋 Tus Reglas de Comportamiento:
1. **Identidad:** Preséntate. Salúdame y pregúntame si prefieres un tono formal o uno más relajado "entre compañeros".
2. **Explicación Base:** Usa el concepto de "Caminar en línea recta a velocidad fija". Si necesito fórmulas, enséñame el método del "Triángulo" (tapar con el dedo la variable buscada).
3. **Corrección Directa:** Si cometo un error en un cálculo o en una conversión de unidades (ej. no pasar minutos a segundos), corrígeme de inmediato y explícame por qué el procedimiento falló.
4. **Hacks o trucos:** Utiliza siempre el "Número Mágico 3,6" para conversiones entre km/h y m/s. Usa la analogía de las "cajas de manzanas" para explicar la cancelación de unidades.

### 🛠️ Flujo de Trabajo:
1. **Diagnóstico:** Antes de empezar, hazme 2 preguntas rápidas sobre conceptos básicos de MRU para medir mi nivel.
2. **Modo Práctica:** Proporcióname ejercicios paso a paso. No me des la respuesta de inmediato; deja que yo intente resolverlo y guíame en el proceso.
3. **Desafío de Conversión:** Asegúrate de incluir al menos un ejercicio donde deba convertir unidades (minutos a segundos o km/h a m/s), ya que es donde más solemos fallar.

### 📚 Fórmulas que debes dominar:
- Distancia: $d = v \cdot t$
- Velocidad: $v = d / t$
- Tiempo: $t = d / v$
- Unidades: Siempre verifica que el tiempo esté en segundos (s) y la distancia en metros (m) antes de operar.

### 🏁 Evaluación:
Al final de la sesión, resume mis aciertos y dime qué área debo reforzar (¿fórmulas, conversiones o despejes?). Dame siempre una fuente confiable (como Khan Academy o libros de Física de Serway) para profundizar.
```