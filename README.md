Proyecto: Simulación de sistema de ascensores


Descripción

Este proyecto simula el funcionamiento de múltiples ascensores con un sistema en el que, una vez dentro del ascensor, los pasajeros seleccionan su destino mediante un panel de botones.

Componentes Principales

Clase Elevador: 

Cada ascensor tiene un nombre único, una posición actual (piso), y una dirección en la que se está moviendo (hacia arriba, hacia abajo o en reposo). 

Función assign_elevator: se encarga de asignar el ascensor más cercano a un piso solicitado por un usuario. 

Uso

Para utilizar el sistema, los usuarios deben ingresar números de piso y presionar enter desde la consola para solicitar un ascensor.

El sistema utiliza hilos (threads) para permitir que múltiples ascensores se muevan simultáneamente y atiendan múltiples solicitudes de usuarios de forma concurrente.

Restricciones generales:

Un ascensor no puede parar en una planta a recoger pasajeros si ya hay otro ascensor parado en esa planta.

Las llamadas realizadas dentro de un ascensor siempre se sirven secuencialmente en la dirección del mismo, es decir, éste no podrá saltarse ninguna planta de destino de un pasajero. 

Un ascensor no cambia de dirección mientras lleve pasajeros a bordo, es decir, hasta que no haya servido a todos los pasajeros.

Los ascensores no aceptan llamadas desde el ascensor en la dirección contraria a la de viaje, es decir, los pasajeros no deberían poder acceder a un ascensor que viaje en dirección contraria a su planta destino. 

Los ascensores no aceptan llamadas desde el ascensor en la dirección contraria a la de viaje, es decir, los pasajeros no deberían poder acceder a un ascensor que viaje en dirección contraria a su planta destino. 

Teniendo la posibilidad de subir o bajar, el ascensor siempre preferirá subir[1].

Siguientes pasos:

Agregar limite de pasajeros/limite de peso.

Agregar interfaz grafica, imprimir sonido de elevador cuando se llega al piso deseado.

Control de puertas (abir/cerrar).


[1]	P. F. C. Achedad, «Algoritmos para la asignación de llamadas en sistemas de tráfico vertical selectivo en bajada», 2003.
