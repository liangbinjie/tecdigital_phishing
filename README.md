# Proyecto Educativo: Simulación de Sitio de Phishing sobre TecDigital

## Descripción

Este proyecto educativo tiene como propósito demostrar y explicar el funcionamiento de las páginas de phishing, específicamente aquellas que intentan aparentar ser plataformas legítimas para engañar a los usuarios y obtener información sensible.

Como ejemplo práctico y con fines exclusivamente académicos, se desarrolló una simulación inspirada visualmente en la plataforma TecDigital, con el objetivo de analizar las técnicas comúnmente utilizadas en ataques de ingeniería social y fortalecer la concientización en ciberseguridad.

> **Importante:**  
> Este proyecto fue desarrollado únicamente con fines educativos, de investigación y capacitación en seguridad informática. No debe utilizarse para actividades ilegales, recolección real de credenciales ni ataques contra terceros.

---

# Objetivos del Proyecto

- Comprender cómo funcionan los ataques de phishing.
- Analizar las técnicas de suplantación de identidad visual.
- Estudiar la interacción entre frontend, backend y almacenamiento de datos.
- Demostrar la importancia de verificar URLs y certificados.
- Promover buenas prácticas de ciberseguridad y concientización.

---

# Tecnologías Utilizadas

El proyecto fue desarrollado utilizando las siguientes tecnologías:

| Tecnología | Descripción |
|---|---|
| Python 3.14 | Lenguaje principal del backend |
| Flask | Framework web utilizado para la aplicación |
| PostgreSQL | Sistema gestor de base de datos |
| HTML/CSS | Interfaz visual de la página simulada |

---

# Arquitectura del Proyecto

El sistema se divide en varios componentes:

## Frontend

La interfaz web fue diseñada para asemejarse visualmente a una plataforma legítima, permitiendo demostrar cómo los atacantes intentan generar confianza mediante:

- Copias de diseño visual
- Logos e interfaces similares
- Formularios falsos de autenticación
- Uso de colores y estructuras familiares

## Backend

El backend fue desarrollado utilizando Flask, encargado de:

- Procesar solicitudes HTTP
- Manejar formularios
- Gestionar sesiones
- Comunicarse con la base de datos PostgreSQL

## Base de Datos

Se utilizó PostgreSQL para almacenar información de prueba generada durante la simulación.

Los datos almacenados fueron guardados utilizando mecanismos de encriptación con el fin de demostrar prácticas básicas de protección de información sensible dentro de aplicaciones web.

---

# Características Implementadas

- Simulación de página de inicio de sesión
- Captura controlada de credenciales de prueba
- Almacenamiento cifrado de datos
- Panel básico de administración
- Registro de eventos
- Arquitectura cliente-servidor

---

# Enfoque Educativo

Este proyecto busca enseñar conceptos relacionados con:

- Ingeniería social
- Phishing
- Suplantación de identidad
- Seguridad en aplicaciones web
- Protección de credenciales
- Concientización del usuario

Además, permite comprender por qué los usuarios deben:

- Revisar cuidadosamente las URLs
- Verificar certificados HTTPS
- Desconfiar de enlaces sospechosos
- Utilizar autenticación multifactor
- No reutilizar contraseñas

---

# Consideraciones Éticas

El proyecto fue realizado bajo un enfoque académico y controlado. No está destinado a:

- Robar información real
- Distribuir malware
- Realizar ataques reales
- Comprometer sistemas de terceros

Cualquier uso indebido del código o de las técnicas explicadas es responsabilidad exclusiva del usuario.

---

# Requisitos de Ejecución

## Dependencias principales

```bash
pip install requirements.txt
```

## Ejecución

```bash
python app.py
```

---

## Infraestructura y Hosting

El despliegue del proyecto fue realizado utilizando la plataforma Railway como servicio de hosting en la nube.

La utilización de Railway permitió:

- Despliegue rápido de la aplicación Flask
- Configuración sencilla de variables de entorno
- Integración con PostgreSQL
- Administración centralizada de servicios
- Acceso remoto para pruebas controladas

La infraestructura fue configurada únicamente con fines educativos y de demostración en entornos controlados.

---

# Servicio de Correos de Simulación

El proyecto también incluye un módulo de envío de correos electrónicos de simulación educativa utilizando los servicios SMTP de Gmail.

Este componente fue desarrollado con el objetivo de demostrar cómo funcionan las campañas de phishing por correo electrónico y cómo los atacantes intentan dirigir usuarios hacia páginas fraudulentas mediante técnicas de ingeniería social.
En este caso haciendonos pasar por la Datic.

## Funcionalidades

- Envío automatizado de correos electrónicos de prueba
- Integración con servidores SMTP de Gmail
- Plantillas HTML para simulación de correos
- Inclusión de enlaces hacia la página simulada
- Registro de eventos de envío

## Propósito Educativo

La implementación de este módulo permite analizar:

- Cómo operan las campañas de phishing por correo
- Técnicas de suplantación visual en emails
- Métodos utilizados para aumentar la credibilidad del mensaje
- Riesgos asociados a enlaces sospechosos
- Importancia de verificar remitentes y dominios

> **Nota:**  
> Este sistema fue diseñado exclusivamente para entornos controlados de aprendizaje y concientización en ciberseguridad. No debe utilizarse para enviar campañas reales ni para actividades fraudulentas.
