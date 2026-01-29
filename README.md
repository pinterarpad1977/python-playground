# **Python Playground**

A clean, portable Python development environment powered by **Docker**, **VS Code Dev Containers**, and **Jupyter Notebooks**.  
Designed for reproducible workflows across Windows and macOS.

---

## **Features**

- Containerized Python 3.11 environment  
- Jupyter Notebook support inside VS Code  
- Mounted `data/` folder for datasets  
- `src/` folder for reusable Python modules  
- Identical setup on any machine (Windows, macOS, Linux)  
- No local Python installation required  

---

## **Project Structure**

```
python-playground/
├── .devcontainer/   # Dev Container configuration
├── data/            # Datasets (CSV, JSON, SQLite, etc.)
├── notebooks/       # Jupyter notebooks
├── src/             # Python modules and scripts
├── Dockerfile       # Environment definition
└── README.md
```

---

## **Getting Started**

### 1. Install prerequisites
- Docker Desktop  
- Visual Studio Code  
- Dev Containers extension  

### 2. Open the project in VS Code
```
Ctrl+Shift+P → Dev Containers: Reopen in Container
```

VS Code will build and open the full environment automatically.

---

## **Using Notebooks**

Create notebooks inside:

```
notebooks/
```

Example:

```python
import numpy as np
import matplotlib.pyplot as plt

plt.plot(np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)))
```

---

## **Using Python Modules**

Place scripts in:

```
src/
```

Import them in notebooks:

```python
from src.utils import greet
```

---

## **License**

MIT License — see `LICENSE` for details.
