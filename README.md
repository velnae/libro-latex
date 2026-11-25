# Programar para resolver

Fundamentos del pensamiento computacional y desarrollo de soluciones. El libro reúne cuatro capítulos sobre análisis de problemas, diseño de algoritmos, programación en Python y pruebas de software. El caso de presupuesto para materiales conecta las cuatro etapas.

## Compilar el PDF

Instala TeX Live o MiKTeX con XeLaTeX, `latexmk`, Biber, `biblatex-apa` y `csquotes`. Ejecuta el siguiente comando desde la carpeta que contiene `main.tex`.

```bash
latexmk -xelatex main.tex
```

La compilación genera `main.pdf` con índices, enlaces internos y referencias en APA 7. En Overleaf, importa el ZIP del repositorio y selecciona `main.tex` como archivo principal y XeLaTeX como compilador.

## Archivos del libro

| Archivo o carpeta | Contenido |
| --- | --- |
| `main.tex` | Orden del libro |
| `config/` | Metadatos y estilo |
| `preliminares/` | Portada e introducción |
| `capitulos/` | Desarrollo de los cuatro capítulos |
| `tablas/` y `figuras/` | Tablas e ilustraciones |
| `finales/` | Conclusiones, glosario y referencias |
| `referencias.bib` | Fuentes citadas |
| `recursos/` | Ejemplos, pseudocódigo y pruebas de Python |

Consulta la [guía de ejecución](recursos/README.md) para reproducir los ejemplos y las pruebas del proyecto integrador.
