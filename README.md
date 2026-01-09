# 3D Renderer Using Pygame

A lightweight **software-based 3D rendering engine** built with **Python and Pygame**. This project demonstrates the fundamentals of a 3D graphics pipeline, including camera transformations, perspective projection, and rendering `.obj` models without relying on OpenGL or external 3D engines.

---

## 📌 Project Overview
This renderer implements a minimal 3D pipeline from scratch:

- Camera movement and view transformation
- Perspective projection using matrix math
- Loading and rendering Wavefront `.obj` files
- Real-time rendering loop using Pygame

The project is designed for **learning, experimentation, and portfolio demonstration** of low-level graphics concepts.

---

## 🧠 Core Concepts Implemented
- Homogeneous coordinates
- World → View → Projection → Screen space transformations
- Perspective divide
- Software raster-style rendering (wireframe / polygon-based)

---

## 📁 Project Structure
```text
project/
│
├── main.py	        # Main application loop
├── camera.py          # Camera position, rotation, and controls
├── projection.py      # Perspective projection matrices
├── object_3d.py       # 3D object representation and drawing logic
├── matrix_function.py	# Contains needed matrix functions for the camera logic
├── objects/		# Example objects to test out the renderer
│   ├── Sting-Sword-lowpoly.obj
│   └── t_34_obj.obj
```

---

## 🚀 How It Works

### 1. Renderer Initialization
- Initializes Pygame
- Creates the rendering window
- Sets resolution, FPS, and clock

### 2. Camera Setup
- Positions the camera in 3D space
- Handles keyboard-based movement and rotation

### 3. Projection System
- Builds a **perspective projection matrix**
- Converts 3D coordinates into 2D screen space

### 4. Object Loading
- Parses `.obj` files
- Extracts vertices and faces
- Converts them into renderable objects

### 5. Render Loop
- Clears the screen
- Applies transformations
- Draws the object
- Updates the display at a fixed FPS

---

## 🧩 Key Files Explained

### `main.py`
Acts as the **entry point** and controls the main loop.

Responsibilities:
- Window creation
- Scene setup
- Event handling
- Frame rendering

---

### `camera.py`
Defines the camera system:
- Position and orientation
- View matrix construction
- Keyboard-based controls

---

### `projection.py`
Handles perspective projection:
- Near and far clipping planes
- Field-of-view handling
- Projection-to-screen matrix mapping

---

### `object_3d.py`
Manages 3D objects:
- Stores vertices and faces
- Applies transformation matrices
- Draws edges or faces onto the screen

---

## 🎮 Controls
| Key | Action |
|---|---|
| W / S | Move forward / backward |
| A / D | Strafe left / right |
| Arrow Keys | Rotate camera |
| ESC / Close Window | Exit |

---

## 🛠️ Requirements
- Python 3.8+
- Pygame
- NumPy

Install dependencies:
```bash
pip install pygame numpy
```

---

## ▶️ Running the Project
```bash
python main.py
```

Ensure the `.obj` model path is correct:
```python
self.object = self.get_obj_file_object("objects/Sting-Sword-lowpoly.obj")
```

---

## 📈 What This Project Demonstrates
- Strong understanding of 3D math and linear algebra
- Graphics pipeline fundamentals
- Software rendering techniques
- Clean separation of concerns in system design

---

## 🧠 Learning Outcomes
- How perspective projection works internally
- How 3D engines transform and render geometry
- How real-time rendering loops are structured

---

## 🏷️ Portfolio Note
This project intentionally avoids GPU acceleration to emphasize **core graphics principles**. It is ideal for showcasing foundational knowledge in:

- Computer Graphics
- Game Engine Architecture
- Mathematical Modeling

---

**Author:** Spondan Bandyopadhyay

---
