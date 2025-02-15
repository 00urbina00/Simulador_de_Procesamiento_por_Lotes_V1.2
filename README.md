# Simulador de Procesamiento por Lotes

## Descripción

Este proyecto es un simulador de procesamiento por lotes con una interfaz gráfica que permite la creación, ejecución y manipulación de procesos en un sistema de simulación. Los procesos pueden ser generados de manera automática o manual y se ejecutan en lotes, lo que simula cómo un sistema operativo gestiona la ejecución de múltiples procesos de manera secuencial.

El simulador permite la interacción en tiempo real a través de teclas para pausar, continuar, interrumpir o terminar procesos. Además, está diseñado para manejar entradas/salidas y errores de manera eficiente. 

**Versión Actual: 1.0.2**  
Esta es la segunda versión del programa, pero la primera publicada en GitHub.

## Características

- **Generación Automática de Procesos:** Ahora puedes generar procesos automáticamente o cambiarlos a modo manual para crear procesos uno a uno.
- **Interacción con Teclado:** Utiliza teclas específicas para controlar los procesos:
  - `I` – Interrumpir proceso (simula Entrada/Salida)
  - `E` – Terminar proceso por error
  - `P` – Pausar proceso
  - `C` – Continuar ejecución del proceso
- **Lotes de Procesos:** Los procesos se agrupan en lotes de un máximo de 5, lo que ayuda a simular cómo un sistema operativo organiza los procesos.
- **Interfaz Gráfica:** La interfaz permite una visualización clara de los procesos en ejecución, junto con sus estados y métricas.
- **Botón para Limpiar Consolas:** Permite limpiar las consolas de salida, también eliminando el historial de procesos terminados.
- **Manejo de Hilos:** Se implementaron hilos de ejecución para simular el procesamiento paralelo y evitar que el programa entre en un bucle infinito o termine sin finalizar los procesos.
- **Actualización en Tiempo Real:** Un `QTimer` actualiza constantemente la interfaz utilizando variables de texto para la comunicación entre hilos y mostrar los datos de manera sincronizada.

## Instrucciones de Uso

1. **Descargar el archivo ejecutable (.exe)** desde la sección de "Releases" de este repositorio.
2. **Ejecutar el archivo descargado**. No es necesario instalar nada adicional.
3. **Generar procesos:**
   - En el modo **automático**, el simulador generará procesos de manera predeterminada.
   - En el modo **manual**, puedes crear procesos uno por uno ingresando los datos de cada uno.
4. **Interacción:**
   - Usa las teclas `I`, `E`, `P`, `C` para interactuar con los procesos:
     - `I`: Interrumpe el proceso actual (simula una Entrada/Salida).
     - `E`: Termina el proceso actual debido a un error.
     - `P`: Pausa el proceso actual.
     - `C`: Continúa la ejecución del proceso pausado.
5. **Limpiar Consolas:** Haz clic en el botón de "Limpiar Consola" para borrar el historial de procesos terminados y restablecer la salida.
6. **Visualización:** La interfaz te permitirá ver el estado de los procesos, los lotes y el historial de acciones realizadas.

## Requisitos

- **SO:** Windows, Linux o macOS (dependiendo del archivo `.exe` proporcionado).
- **Dependencias:** El proyecto ya está compilado en un archivo `.exe`, por lo que no requiere dependencias externas ni compilación.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto o agregar nuevas características, abre un **issue** o envía un **pull request**.

## Licencia

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
