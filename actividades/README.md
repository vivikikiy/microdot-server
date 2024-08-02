# actividades

Acá se suben, en el directorio de cada actividad, los archivos que se trabajaron para cumplir con la consigna. La estructura de archivos dentro del ESP32 normalmente debe respetar lo siguiente:

```bash
.
├── boot.py
├── index.html
├── main.py
├── scripts
│   ├── base.js
│   └── index.js
└── styles
    ├── base.css
    └── styles.css
```

Cada actividad tiene un template de algunos de esos archivos para comenzar a usar. El archivo `index.html` contiene un template que se debe respetar, solo usando el área definida dentro de la etiqueta **main** para trabajar. En cada actividad, se debe cambiar los valores de **title** y **h1** por el número de actividad y se debe completar con el apellido y nombre del alumno en el **footer**.

Además, se proporcionan un `base.js` y un `base.css` genéricos para que el template funcione. Cualquier desarrollo propio de CSS o JS debe hacerse en archivos separados llamados **styles.css** y **index.js** respectivamente.
