import numpy as np
import matplotlib.pyplot as plt

# --- Key points (correct values) ---
S = np.array([1.0, 0.0])
R = np.array([-2.0, 1.0])
R2 = np.array([1.0, -2.0])
R1 = np.array([4.0, 4.0])
Q2 = np.array([1.0, 1.0])
Q1 = np.array([0.4, -0.8])

# --- Parabola points ---
y_vals = np.linspace(-4.5,4.5, 600)
x_par = y_vals**2 / 4.0  # y^2 = 4x

# --- Tangent lines ---
def tangent_line(t, x_min=-3, x_max=4.5, n=300):
    xs = np.linspace(x_min, x_max, n)
    ys = t*xs + 1/t
    return xs, ys

xt1, yt1 = tangent_line(-1)   # tangent at R2
xt2, yt2 = tangent_line(0.5)  # tangent at R1

# --- Extended SR lines ---
x_sr2 = np.full(100, 1.0)
y_sr2 = np.linspace(-2.5, 2.5, 100)

m_sr1 = 4/3
x_sr1 = np.linspace(-1.0, 4.5, 100)
y_sr1 = m_sr1*(x_sr1 - S[0]) + S[1]

# --- Perpendiculars RQ ---
x_rq2 = [R[0], Q2[0]]
y_rq2 = [R[1], Q2[1]]
x_rq1 = [R[0], Q1[0]]
y_rq1 = [R[1], Q1[1]]

# --- Plotting ---
plt.figure(figsize=(9,7))

# Parabola
plt.plot(x_par, y_vals, color='blue', linewidth=2)

# Tangents
plt.plot(xt1, yt1, 'r--', linewidth=1.6)
plt.plot(xt2, yt2, 'g--', linewidth=1.6)

# Extended SR lines
plt.plot(x_sr1, y_sr1, 'k-.', linewidth=1.5)
plt.plot(x_sr2, y_sr2, 'k-.', linewidth=1.5)

# Perpendiculars
plt.plot(x_rq1, y_rq1, 'm:', linewidth=1.5)
plt.plot(x_rq2, y_rq2, 'c:', linewidth=1.5)

# Points with coordinates labels
points = {
    'S': (S, '(1, 0)'),
    'R': (R, '(-2, 1)'),
    'R₂': (R2, '(1, -2)'),
    'R₁': (R1, '(4, 4)'),
    'Q₂': (Q2, '(1, 1)'),
    'Q₁': (Q1, '(0.4, -0.8)')
    
}

for name, (p, val) in points.items():
    plt.scatter(p[0], p[1], s=80, color='orange', edgecolor='black', zorder=6)
    dx, dy = 0.1, 0.1
    if name == 'R₂': dx, dy = 0.25, -0.05
    if name == 'R₁': dx, dy = 0.05, -0.2
    if name == 'S': dx, dy = 0.1,-0.2
    if name == 'Q₁': dx, dy = 0.3, 0.0
    if name == 'Q₂': dx, dy = 0.14, 0.0
    if name == 'R': dx, dy = -1.2, 0.1
    plt.text(p[0]+dx, p[1]+dy, f"{name}{val}", fontsize=10, weight='bold')

# Line labels
def label_line(x, y, label, offset=(0.1,0.1), color='k', fs=10):
    xm = (x[0]+x[-1])/2
    ym = (y[0]+y[-1])/2
    plt.text(xm+offset[0], ym+offset[1], label, fontsize=fs, color=color, weight='semibold')



# Axes and aesthetics
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.axis('equal')
plt.grid(True, linestyle='--', alpha=0.4)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Clean Diagram: Parabola y²=4x with Tangents, SR lines, and Perpendiculars')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.tight_layout()
plt.savefig("../figs/fig18.png")
plt.show()

