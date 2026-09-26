# Mantenimiento del perfil

El perfil se publica desde el README de `main`. No requiere framework, instalación de paquetes ni compilación.

## Estructura y publicación

- `README.md`: presentación pública en español e inglés.
- `assets/banner/`: SVG del banner, con soporte para tema oscuro y movimiento reducido.
- `assets/projects/`: capturas de los proyectos; se muestran a 480 píxeles de ancho.
- `assets/cv/`: PDF descargable. Conservar su nombre o actualizar ambos enlaces del README.
- `.github/workflows/snake.yml`: genera las animaciones en `dist/` y las publica en la raíz de la rama `output`.
- `.github/workflows/validate.yml`: ejecuta las comprobaciones en pushes a `main`, pull requests y manualmente.
- `scripts/validate_profile.py`: validación sin dependencias adicionales, con Python 3.9 o posterior.

La rama `output` contiene exclusivamente archivos generados. No confundirla con una carpeta `output/` dentro de `main`: esa copia antigua se eliminó porque el perfil no la utilizaba. No editar manualmente la rama generada.

## Actualizar contenido

1. Editar la presentación y experiencia en español y en inglés en el mismo cambio. Mantener empresa, fechas y responsabilidades consistentes.
2. Para cada proyecto, actualizar descripción, tecnologías, enlaces y captura con texto alternativo descriptivo. Mantener una experiencia breve y dejar el detalle profesional en el CV o LinkedIn.
3. Para editar el banner, conservar su `viewBox`, textos accesibles y regla `prefers-reduced-motion`.
4. Actualizar la fecha del pie únicamente cuando cambie el contenido del perfil.
5. Ejecutar `python3 scripts/validate_profile.py` y `git diff --check` desde la raíz.
6. Revisar el README renderizado en GitHub, en pantalla estrecha y con temas claro y oscuro. Comprobar manualmente demos y descarga del CV.

El validador comprueba higiene básica de Markdown, bloques de código, etiquetas HTML estructurales, texto alternativo de imágenes HTML, destinos locales y XML de los SVG. Está adaptado al formato de enlaces inline del repositorio: no sustituye un parser completo de Markdown, no valida anclas ni comprueba disponibilidad de servicios externos.

## Estadísticas y contribuciones

Las dos tarjetas del README se solicitan a la API de [GitHub Profile Summary Cards](https://github.com/vn7n24fzkq/github-profile-summary-cards). No son imágenes guardadas en el repositorio y no dependen del workflow de la serpiente.

El 14 de septiembre de 2026 ambas URLs respondieron HTTP 200 con SVG y `Cache-Control: public, max-age=14400` (cuatro horas). Pueden mostrar datos en caché; esto no garantiza una actualización puntual cada cuatro horas. La tarjeta de lenguajes cuenta repositorios por lenguaje, no dominio profesional ni tiempo de programación. El enlace bajo las tarjetas permite consultar directamente la actividad en GitHub.

Si dejan de responder, comprobar las URLs del README y el estado del proveedor. No añadir parámetros aleatorios para forzar recargas. La serpiente se genera diariamente y también al actualizar `main` o ejecutar manualmente su workflow; revisar su historial en Actions si deja de actualizarse.

## Actions

Las Actions se fijan a SHA completos, con la etiqueta de referencia en un comentario. Para actualizarlas, revisar el cambio del proveedor, resolver el commit de la versión elegida y actualizar SHA y comentario juntos. El workflow de validación tiene permisos de lectura; el de publicación necesita `contents: write` para la rama `output`.

No reintroducir una regla de concurrencia en la serpiente sin investigar: el historial del repositorio registra que se retiró tras ejecuciones atascadas en cola.

## CV verificable

El contenido del CV se mantiene en `scripts/build_cv.py`. Requiere Python y ReportLab. Ejecutar `python scripts/build_cv.py` regenera el PDF del perfil; también acepta una ruta de salida como argumento. La copia del portfolio debe sincronizarse y revisarse visualmente después de cada cambio.

Las tres contribuciones de Peek fueron confirmadas por Francisco: integración individual MQTT entre Express/MongoDB y NestJS; corrección de iconos de autobuses en mapas Next.js; portal administrativo para operaciones NFC. No se atribuyen métricas no proporcionadas ni se identifican clientes.
