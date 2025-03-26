# ej_00

## Consigna

Como primera actividad preliminar, vamos a intentar conectar el ESP32 del kit a la red WiFi y mostrar la dirección de IP en la pantalla OLED que viene en la placa de desarrollo.

### Conexión a internet

Tomando como base la función `connect_to()` siguiente:

```python
def connect_to(ssid : str, passwd : str) -> None:
    """Conecta el microcontrolador a la red indicada.

    Parameters
    ----------
    ssid : str
        Nombre de la red a conectarse
    passwd : str
        Contraseña de la red
    """
    
    import network
    from time import sleep
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, passwd)
        while not sta_if.isconnected():
            print(".",end="")
            sleep(.05)
    
    print()
    print("Network config:", sta_if.ifconfig())
    print()
```

Resolver lo siguiente:

1. Probar la conexión del ESP32 a la red de Cooperadora Alumnos pasando los argumentos siguientes dentro del archivo `boot.py`:

```python
connect_to("Cooperadora Alumnos", "")
```

2. Una vez que hayan probado y asegurado que la conexión se resuelve, identificar en qué consisten los cuatro grupos de números que muestra la consola.
3. Convertir la función `connect_to()` en una que retorne la dirección de IP que asigna el router. Para eso:
  
  * Eliminar todas las instancias de `print()` que use la función para evitar que use la consola.
  * Hacer un `return` del elemento apropiado que devuelve `sta_if.ifconfig()` que coincida con la dirección de IP que necesitamos.

3. Una vez implementada la función, testear que funciona llamando en el `boot.py` a la función como `print(connect_to("Cooperadora Alumnos", ""))`. El resultado debería ser la dirección de IP de nuestro microcontrolador.

### Uso de pantalla OLED

1. Grabar la biblioteca `ssd1306.py` del siguiente [repositorio](https://github.com/stlehmann/micropython-ssd1306) en el sistema de archivos del ESP32.
2. Identificar los pines de I2C (SDA y SCL) que están mapeados del ESP32 a la pantalla.
3. Hacer la inicialización correspondiente de la pantalla según la documentación y ejemplos del repositorio de orígen.
4. Testear un mensaje sencillo como "Hola mundo!".
5. Una vez que se haya garantizado que la pantalla funciona, mostrar la dirección de IP asignada por el router en la pantalla OLED.

### Recursos adicionales

* Biblioteca de [network](https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html) de Micropython
* Repositorio de la pantalla OLED que usa el [SSD1306](https://github.com/stlehmann/micropython-ssd1306)
