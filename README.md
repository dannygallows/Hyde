# Hyde

**→ [dannygallows.github.io/Hyde](https://dannygallows.github.io/Hyde)**

A zero-dependency static site generator written in Python from scratch.
Transforms a directory of Markdown files into a structured HTML website via a custom template engine.

---

## How it works

Recursively walks `content/`, parses Markdown, injects into `template.html`, writes to `docs/`.

---

## Usage

```bash
# Build
bash build.sh

# Build and serve at localhost:8888
bash main.sh

# Test
bash test.sh
```

---

## Structure

```
Hyde/
├── src/            # Python source
├── content/        # Markdown input
├── static/         # CSS and assets
├── docs/           # HTML output → GitHub Pages
├── template.html   # Page layout
└── test.sh         # unittest runner
```

---

## Stack

Python · unittest · HTML/CSS · GitHub Pages
