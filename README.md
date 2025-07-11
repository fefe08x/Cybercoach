Descripción de la funcionalidad del desarrollo WEB
Nuestra página web CYBER-COACH está centrada en ayudar a las personas a mejorar el rendimiento físico, desde ejercicios, rutinas y dietas. El objetivo es que de manera fácil y sencilla los usuarios puedan acceder a información detallada sobre lo recién mencionado y que puedan iniciar con este cambio en sus vidas.
Ofrecemos de manera gratuita una gran variedad de rutinas, cada una con un enfoque diferente para que se pueda elegir en base a las preferencias de uno. Explicadas de manera sencilla con una mezcla de texto y cuadros para que sea más cómodo a la vista. Cabe recalcar que cada rutina además de explicar su funcionamiento, beneficios y recomendaciones agregamos un ejemplo de la rutina completa muy recomendable para cualquier público.
También tenemos una sección de ejercicios. Simplemente está dividida por músculos y cada apartado tiene una gran cantidad de videos sobre los ejercicios posibles de dicho músculo. Creemos que de esta manera va a ser más simple de entender que poniendo la explicación de cómo se hace.
La última sección es una de dietas. Está dividida en diferentes tipos de dietas, ideal para poder elegir la que uno crea correspondiente, y si no lo tiene claro, aprender sobre cuál es la mejor opción. Explicadas en simples pasos y con ejemplos para evitar algún tipo de dudas.
Damos la opción de poder registrarse, esto se explicará más adelante porque está relacionado con el chatbot.
Por último al final de la página de Inicio está la posibilidad de dirigirse a el Instagram de CYBER-COACH, junto con el WhatsApp (a futuro el de un profesional) y el Mail.
Explicación de la integración del tema (chatbot con IA)
Antes de la explicación del chatbot es bueno recalcar que cambiamos mucho de ideas porque ninguna nos convencía, hasta pensamos en hacer una pwa. Luego de muchos ida y vuelta logramos decidirnos por el tema de la IA usando y creando un chatbot.
El chatbot está pensado no como la “estrella” de la página, está pensado como un gran complemento, que la haga más novedosa y moderna a la página. Por este motivo decidimos no dar el chatbot de manera fácil, que sea algo novedoso que solo los que se loguean en nuestra página puedan usarlo.
Utilizamos Voiceflow para crearlo ya que por lo que pudimos investigar es de las mejores desde su implementación y su forma de crear el chatbot, teniendo en cuenta el plan gratuito. Lamentablemente su posibilidad de uso no es muy grande, principalmente por el tema del gasto de tokens, calculamos que aproximadamente con el plan que tenemos del chatbot se puede utilizar unas 10 / 12 veces con respuestas amplias (mientras más amplia y detallada más tokens gasta), esto es una de las mejoras futuras (explicado más abajo). 
Se basa en explicar sobre rutinas y dietas de manera un poco más personalizada. Ese es el objetivo de nuestro chatbot, que el usuario pueda sacarse alguna duda específica o si algo no quedó muy claro. Da la posibilidad de que el usuario le pueda decir si tiene alguna dificultad de movilidad, algo que no pueda comer, entre otras. El bot toma las respuestas y responde de manera que uno siente que está hablando con una persona. Hay que recalcar que no reemplazamos para nada a ningún profesional del tema, simplemente es una ayuda para la gente que sienta que es lo que necesita para comenzar, que sirva de incentivo para una vida, quizás, más saludable. Cómo explicamos lo bueno hay que decir lo que puede generar problemas que es su posible limitación de respuestas, pedimos paciencia que a futuro se van a implementar mejoras.
Descripción de los desafíos encontrados y cómo los resolvimos
Durante el desarrollo del sistema web, enfrentamos varios desafíos importantes, principalmente en el backend.

Optimización del Código HTML:
Inicialmente, el uso de vídeos en la página de ejercicios generaba un código HTML extenso y complejo.
Esto afectaba la legibilidad para otros desarrolladores y dificultaba la escalabilidad del sistema.
La solución inicial fue migrar la información de los vídeos al backend usando diccionarios (clave-valor), mejorando la legibilidad pero manteniendo limitaciones de escalabilidad.
Implementación de Base de Datos:
Para mejorar la escalabilidad, implementamos una base de datos usando SQLAlchemy.
Esta librería nos permitió interactuar con la base de datos de manera más eficiente y tratar las entidades como objetos Python.
La combinación con el comportamiento del framework (Render template) mejoró significativamente la legibilidad, eficiencia y escalabilidad del proyecto.
Sistema de Autenticación y ChatBot:
Implementamos un sistema de login y recuperación de contraseña, lo que permitió crear un ChatBot exclusivo para usuarios registrados.
Inicialmente, el chat solo era visible en la página donde estaba implementado.
Resolvimos esto usando una página base (Base.HTML) que sirve como plantilla para todas las demás páginas, permitiendo así que el chat esté disponible en todas las secciones del sitio.
Conexión con Base de Datos:
El mayor desafío técnico fue la conexión con la base de datos.
Comenzamos con una implementación local y, al final del desarrollo, tuvimos que migrar a las credenciales proporcionadas por el host.
Esta migración requería una reconfiguración cuidadosa para mantener la funcionalidad del sistema.
Estas soluciones mejoran significativamente la estructura del proyecto, su mantenibilidad y su capacidad para escalar en el futuro.

Conclusiones y posibles mejoras futuras 
Durante el desarrollo de este trabajo práctico se desarrollaron habilidades no solamente de desarrollo web, si no conocimientos de ambos lados, tanto frontend, como backend, entre los que destacamos:

Conclusiones
Utilización fluida de la interfaz de línea de comandos (instalación de dependencias, etc).
Conexión con base de datos.
Manejo de peticiones GET, POST, etc. Muy importante para la autentificación.
Hosting (nunca habíamos subido una página a internet)
Utilización de Git y GitHub.
Testing (programas probadores para las funciones) y pruebas locales antes de modificar el repositorio.
Consideramos que cuando son los alumnos quienes eligen el tema de su proyecto a desarrollar, lo llevan a cabo incluso con mejor predisposición ya que se desarrollan habilidades para  plasmar nuestras ideas en un sistema funcional.

Posibles mejoras futuras
Chatbot: A medida que tengamos más tokens agregaremos mejores respuestas y variedad de las mismas. 
Sistema de pago para el uso del chatbot : Un chat gratuito para cada usuario registrado. Añadir un método de pago para los siguientes chats. Estas mejoras con el fin de que cada usuario “pague” sus propias tokens y de esta manera no se acaben. Esto evitaría quedarnos sin tokens ya que cada usuario “pagaría” los suyos.
Recuperación de contraseña por Mail.
Estilizar más la interfaz.
Contactar con algún profesional así agregar su número de contacto en la parte inferior de la página de Inicio.
Implementación de tienda de suplementos y accesorios.
Mayor seguridad general. Protección contra inyección SQL, entre otras.



