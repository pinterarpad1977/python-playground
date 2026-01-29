# **Python Playground — Dev Container + Docker + Jupyter + VS Code**

A clean, portable, fully containerized Python development environment designed for exploration, data analysis, and reproducible workflows.  
Built with:

- **Docker**
- **VS Code Dev Containers**
- **Python 3.11**
- **Jupyter Notebooks**
- **Mounted data and source folders**
- **Cross‑platform compatibility (Windows + macOS)**

This setup ensures that your entire environment — packages, tools, notebooks, and scripts — behaves identically across machines.

---

## **Project Structure**

```
python-playground/
│
├── .devcontainer/
│   └── devcontainer.json
│
├── data/              # Mounted folder for datasets (CSV, JSON, SQLite, etc.)
│
├── notebooks/         # Jupyter notebooks live here
│
├── src/               # Reusable Python modules and scripts
│
├── Dockerfile         # Defines the Python environment
│
└── README.md
```

---

## **Features**

### **✔ Fully containerized Python environment**
No local Python installation required.  
Everything runs inside a Docker container built from your `Dockerfile`.

### **✔ VS Code Dev Container integration**
VS Code opens *inside* the container, giving you:
- IntelliSense
- Python extension support
- Jupyter notebook support
- Integrated terminal running inside Docker

### **✔ Jupyter Notebook support**
Notebooks run directly inside the container using the same Python environment.

### **✔ Mounted `data/` folder**
Datasets placed in `data/` on your host machine appear instantly inside the container at `/app/data`.

### **✔ Clean project layout**
Separation of:
- notebooks  
- reusable Python modules  
- datasets  
- environment configuration  

---

## **Getting Started**

### **1. Install prerequisites**
- Docker Desktop  
- Visual Studio Code  
- Dev Containers extension  
- (Optional) Git

### **2. Open the project in VS Code**
```
File → Open Folder → python-playground
```

### **3. Reopen in Dev Container**
Press:
```
Ctrl+Shift+P → Dev Containers: Reopen in Container
```

VS Code will:
- build the Docker image  
- install Python + Jupyter inside the container  
- mount your project into `/app`  
- open a full development environment  

---

## **Using Jupyter Notebooks**

Create a new notebook:

```
notebooks/intro.ipynb
```

Run cells normally — VS Code will use the Python kernel from inside the container.

Example:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
```

---

## **Running Python Scripts**

Place scripts in:

```
src/
```

Example:

```python
# src/utils.py
def greet(name):
    return f"Hello, {name}!"
```

Run inside the container terminal:

```bash
python src/utils.py
```

Or import from notebooks:

```python
from src.utils import greet
greet("Arpad")
```

---

## **Working with Data**

Place datasets in:

```
data/
```

Access them inside notebooks or scripts:

```python
import pandas as pd

df = pd.read_csv("data/example.csv")
df.head()
```

---

## **Rebuilding the Environment**

If you modify the Dockerfile or devcontainer.json:

```
Ctrl+Shift+P → Dev Containers: Rebuild and Reopen in Container
```

---

## **Why This Setup Rocks**

- Zero configuration on new machines  
- Identical behavior on Windows and macOS  
- Perfect for data science, prototyping, and learning  
- Clean separation of code, notebooks, and data  
- Reproducible and version‑controlled  

