# TecnoMarket - Sistema de Gestión de Tienda

## Descripción
TecnoMarket es una aplicación web basada en Flask para la gestión de una tienda online. Proporciona una interfaz de panel de control para realizar seguimiento de productos, clientes y pedidos, facilitando la monitorización del rendimiento de la tienda y el inventario.

## Características y Funcionalidades
- **Gestión de Productos**: Seguimiento de detalles de productos incluyendo nombre, precio, stock y categoría
- **Gestión de Clientes**: Monitorización de información de clientes, estado de actividad e historial de pedidos
- **Seguimiento de Pedidos**: Visualización de detalles de pedidos, totales de ventas y fechas de transacciones
- **Panel de Control**: Obtén métricas clave de un vistazo incluyendo:
  - Total de productos en stock
  - Número de clientes activos
  - Cliente principal por cantidad de pedidos
  - Ingresos totales por ventas

## Tecnologías Utilizadas
- **Backend**: Python, Flask
- **Frontend**: HTML, plantillas Jinja2
- **Almacenamiento de Datos**: Estructuras de datos en memoria (puede extenderse a bases de datos)

## Estructura del Proyecto
```
Tienda_Gestion/
├── app.py              # Archivo principal de la aplicación con rutas Flask y lógica de negocio
├── templates/          # Plantillas HTML para la interfaz web
│   └── dashboard.html  # Plantilla principal del panel de control
└── README.md           # Documentación del proyecto
```

## Cómo Ejecutar la Aplicación
1. Asegúrate de tener Python y Flask instalados:
   ```
   pip install flask
   ```

2. Clona el repositorio o descarga el código fuente

3. Navega al directorio del proyecto:
   ```
   cd Tienda_Gestion
   ```

4. Ejecuta la aplicación:
   ```
   python app.py
   ```

5. Abre tu navegador web y ve a:
   ```
   http://localhost:5000/dashboard
   ```

## Mejoras Futuras
- Integración con base de datos
- Autenticación de usuarios
- Funcionalidades de gestión de inventario
- Informes y análisis de ventas
