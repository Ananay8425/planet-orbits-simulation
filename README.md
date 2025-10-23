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
🔹 Gravitational Force

Each planet’s motion is determined using Newton’s Law of Universal Gravitation:

𝐹
=
𝐺
𝑚
1
𝑚
2
𝑟
2
F=G
r
2
m
1
	​

m
2
	​

	​


where

G = 6.67430 × 10⁻¹¹ (gravitational constant)

m₁, m₂ = masses of two bodies

r = distance between them

🔹 Motion Update

Acceleration is derived from the net force:

𝑎
=
𝐹
𝑚
a=
m
F
	​


Then velocity and position are updated using:

𝑣
=
𝑣
+
𝑎
⋅
𝑑
𝑡
v=v+a⋅dt
𝑥
=
𝑥
+
𝑣
⋅
𝑑
𝑡
x=x+v⋅dt

Each frame represents 1 day (DT = 86400 seconds).

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
