---
myst:
  html_meta:
    "description lang=en": |
      Top-level documentation for pydata-sphinx theme, with links to the rest
      of the site..
html_theme.sidebar_secondary.remove: true
---

# Calculator

```{mermaid}
flowchart TB
    add:::id1 ==> minus:::id1
    classDef id1 fill:#f9f,stroke:#333,stroke-width:4px
```


```{seealso}
This is seealso
```

## Documents

The content of the `Calculator` API.

```{toctree}
:maxdepth: 1

markdown/index
```

## API

The content of the `Calculator` API.

```{toctree}
:maxdepth: 2

api/index
```