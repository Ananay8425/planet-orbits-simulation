# Planet Orbits Simulation 

A fun project with visually engaging **planetary motion simulation** built using **Python and Pygame**, based on Newtonian gravity.  
It models the orbits of planets around the Sun using real-world astronomical data and physical equations.

---

## Features

- **Realistic gravitational motion** using Newton’s law of universal gravitation  
- **Toggle between outer and inner solar system views** (`Z` key to zoom)  
- **Trail tracking** for each planet to visualize orbital paths  
- **Time-step based simulation** (1 day per frame)  
- **Scalable simulation** with two distinct zoom levels:
  - Outer Solar System (`SCALE`)
  - Inner Solar System (`ZOOM_SCALE`)
- Smooth 60 FPS rendering with Pygame

---

## Controls

| Key | Action |
|-----|---------|
| `Z` | Toggle between zoomed-in and zoomed-out view |
| `ESC` / Close Window | Exit simulation |

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/planet-simulation.git
cd planet-simulation
```

### 2. Install Dependencies
```bash
pip install pygame
```

### 3. Run the Simulation
```bash
python main.py
```

---

# How It Works

### 🔹 Gravitational Force

<img src="https://latex.codecogs.com/svg.latex?\color{white}F=G\frac{m_1m_2}{r^2}" alt="F = G m1 m2 / r^2" />

where  
- \(G = 6.67430 \times 10^{-11}\) (gravitational constant)  
- \(m_1, m_2\) = masses of two bodies  
- \(r\) = distance between them

### 🔹 Motion Update

<img src="https://latex.codecogs.com/svg.latex?\color{white}a=\frac{F}{m}" alt="a = F/m" />

Then velocity and position are updated using:

<img src="https://latex.codecogs.com/svg.latex?\color{white}v=v+a\cdot dt" alt="v = v + a dt" />

<img src="https://latex.codecogs.com/svg.latex?\color{white}x=x+v\cdot dt" alt="x = x + v dt" />

Each frame represents **1 day** (`DT = 86400` seconds).


Then velocity and position are updated using:

v = v + a dt
x = x + v dt

Each frame represents **1 day** (`DT = 86400` seconds).

---

# Zoom System

Outer Solar System View:
Uses SCALE = 6e-11 (meters → pixels). Shows all planets up to Pluto.

Inner Solar System View:
Uses ZOOM_SCALE = 1e-9 for a closer look at Mercury–Earth region.

Press Z anytime to toggle views.

Trails are cleared upon zoom toggle for clarity.

---

# File Structure
```bash
planet-simulation/
│
├── main.py            # Core simulation file
├── README.md          # Project documentation
└── requirements.txt   # Dependencies (optional)
```
