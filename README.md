# Programar para resolver

Fundamentos del pensamiento computacional y desarrollo de soluciones. Edición LaTeX del manuscrito académico de 2026.

## Qué se hizo en esta edición

1. **Recuperar el manuscrito.** Se tomó como punto de partida [`Programar_para_resolver_Libro_completo.docx`](https://docs.google.com/document/d/1ZiKtKFfWoX3sgFNd7ujvz9gT9cROt0BW/edit), actualizado el 25 de noviembre de 2026. Su SHA-256 es `e85eb8d1cfd8dfdaddb5f4b32ab6bab75a19cfff3a5bf8b6730427e060ca2362`.
2. **Separar estructura y contenido.** Se trasladaron las dos partes, los cuatro capítulos y sus 35 secciones numeradas. Los objetivos, el público, el alcance y las herramientas se reúnen en la guía de lectura. La presentación, la introducción y los anexos tienen archivos propios.
3. **Homogeneizar la edición.** Las 57 tablas tienen un estilo común de títulos, encabezados, notas y columnas. Los ocho diagramas se trazaron como figuras vectoriales editables en TikZ. El índice general, los índices de tablas y figuras, y las referencias cruzadas se generan al compilar.
4. **Unificar el caso de presupuesto.** El punto de partida es S/ 100,00 con materiales por S/ 46,50 y un saldo de S/ 53,50. El diseño, los programas y la matriz de pruebas comparten las reglas, incluido el resultado de `evaluar_compra(presupuesto, materiales)`.
5. **Fundamentar los capítulos.** `referencias.bib` reúne las fuentes que se citan en el libro. BibLaTeX y Biber generan las citas y referencias en APA 7.
6. **Completar las actividades.** El anexo C incluye respuestas, procedimientos, resultados esperados y criterios para evaluar los desafíos. El anexo A contiene las once pruebas del programa integrador.

## Compilar el libro

**En local**

1. Clona este repositorio o descarga y descomprime su ZIP. Instala una distribución TeX Live o MiKTeX que incluya XeLaTeX, `latexmk`, Biber, `biblatex`, `biblatex-apa` y `csquotes`.
2. Abre una terminal en la carpeta que contiene `main.tex`.
3. Ejecuta el siguiente comando.

   ```bash
   latexmk -xelatex main.tex
   ```

4. Abre `main.pdf`. `latexmk` ejecuta Biber y repite las pasadas necesarias para resolver los índices, las citas y los enlaces internos.

**En Overleaf**

1. Crea un proyecto importando el ZIP.
2. Selecciona `main.tex` como documento principal y XeLaTeX como compilador.
3. Compila el proyecto. Overleaf ejecuta Biber para generar la bibliografía del documento.

La compilación usa las fuentes Latin Modern, la localización española de Babel y los paquetes distribuidos por TeX Live para tablas, TikZ, listados y navegación. Los listados se incorporan desde archivos locales y se compilan sin `shell-escape`.

## Dónde editar

| Cambio | Archivo o carpeta |
| --- | --- |
| Partes y orden de lectura | `main.tex` |
| Título, subtítulo, autoría, institución y año | `config/metadatos.tex` |
| Márgenes, encabezados, tablas y colores | `config/estilo.tex` |
| Presentación, introducción y guía de lectura | `preliminares/` |
| Contenido de los capítulos | `capitulos/01-…tex` a `capitulos/04-…tex` |
| Tablas | `tablas/`, un archivo por tabla |
| Diagramas | `figuras/`, un archivo TikZ por figura |
| Bibliografía | `referencias.bib` |
| Conclusiones, glosario, anexos y recursos | `finales/` |
| Solucionario | `finales/anexo-c-solucionario.tex` |
| Python y pseudocódigo | `recursos/` |

1. Edita el capítulo y, si corresponde, su tabla, diagrama o archivo de código.
2. Conserva las etiquetas `\label{...}` que ya se citan desde otros archivos. Al añadir una tabla, toma como modelo una de `tablas/` y crea una etiqueta única. La numeración se asigna al compilar.
3. Vuelve a compilar y verifica las páginas y enlaces afectados. Si modificaste el proyecto de Python, ejecuta sus pruebas desde `recursos/proyecto/`.

### Versionado con Git

Para continuar el trabajo con el historial publicado, clona el repositorio y compila el libro.

```bash
git clone https://github.com/velnae/libro-latex.git
cd libro-latex
latexmk -xelatex main.tex
```

Consulta [la guía de recursos](recursos/README.md) para ejecutar el código y reproducir las pruebas.
