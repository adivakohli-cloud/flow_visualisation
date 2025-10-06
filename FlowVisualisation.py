import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#predefined velocity fields
def vortex_flow(x, y):
    return -y, x

def uniform_flow(x, y):
    # return arrays that broadcast correctly whether x,y are scalars or ndarrays
    return np.ones_like(x) * 1.0, np.zeros_like(x)

def source_flow(x, y):
    r2 = x**2 + y**2 + 1e-6
    return x / r2, y / r2

def doublet_flow(x, y):
    r2 = x**2 + y**2 + 1e-6
    return (x**2 - y**2) / r2**2, (2 * x * y) / r2**2

flows = {
    "1": ("Vortex Flow", vortex_flow),
    "2": ("Uniform Flow", uniform_flow),
    "3": ("Source Flow", source_flow),
    "4": ("Doublet Flow", doublet_flow),
    "5": ("Custom Flow (user-defined)", None)
}

#default
velocity_field = vortex_flow
flow_name = "Vortex Flow"


#visualization routines
def plot_streamlines():
    x = np.linspace(-2, 2, 200)
    y = np.linspace(-2, 2, 200)
    X, Y = np.meshgrid(x, y)
    U, V = velocity_field(X, Y)

    plt.figure(figsize=(6,6))
    plt.streamplot(X, Y, U, V, density=1.2, arrowsize=1)
    plt.title(f"Streamlines - {flow_name}")
    plt.xlabel("x"); plt.ylabel("y")
    plt.axis("equal")
    plt.show()


def plot_pathlines():
    dt = 0.01
    steps = 800
    particles = np.array([[1.0, 0.0],
                          [0.5, 0.5],
                          [0.0, 1.0]])
    paths = [[pos.copy()] for pos in particles]

    for _ in range(steps):
        for j, (x, y) in enumerate(particles):
            u, v = velocity_field(x, y)
            # ensure scalars when lambdified returns arrays of shape ()
            particles[j] = [float(x + u * dt), float(y + v * dt)]
            paths[j].append(particles[j].copy())

    plt.figure(figsize=(6,6))
    for p in paths:
        p = np.array(p)
        plt.plot(p[:,0], p[:,1])
    plt.title(f"Pathlines - {flow_name}")
    plt.xlabel("x"); plt.ylabel("y")
    plt.axis("equal")
    plt.show()


def plot_streaklines():
    dt = 0.01
    steps = 500
    release_point = np.array([1.0, 0.0])
    streak_particles = []

    plt.figure(figsize=(6,6))
    for i in range(steps):
        if i % 10 == 0:
            streak_particles.append(release_point.copy())

        new_positions = []
        for (x, y) in streak_particles:
            u, v = velocity_field(x, y)
            new_positions.append([x + u*dt, y + v*dt])
        streak_particles = new_positions

        if i % 100 == 0 and streak_particles:
            pts = np.array(streak_particles)
            plt.scatter(pts[:,0], pts[:,1], label=f"t={i*dt:.2f}")

    plt.title(f"Streaklines - {flow_name}")
    plt.xlabel("x"); plt.ylabel("y")
    plt.axis("equal")
    plt.legend()
    plt.show()


def check_rotational():
    x, y = 1.0, 1.0
    dx = dy = 1e-5
    _, v1 = velocity_field(x+dx, y)
    _, v2 = velocity_field(x-dx, y)
    dv_dx = (v1 - v2) / (2*dx)

    u1, _ = velocity_field(x, y+dy)
    u2, _ = velocity_field(x, y-dy)
    du_dy = (u1 - u2) / (2*dy)

    vorticity = float(dv_dx - du_dy)
    print(f"\nApprox vorticity = {vorticity:.4e}")
    if abs(vorticity) < 1e-6:
        print(f"{flow_name} is irrotational.")
    else:
        print(f"{flow_name} is rotational.")


#custom flow input
def get_custom_flow():
    print("\nEnter formulas for u(x,y) and v(x,y)")
    print("Use python/numpy syntax. Examples: '-y', 'x/(x**2+y**2)', 'numpy.sin(x)*y'")
    ux_str = input("u(x,y) = ").strip()
    vy_str = input("v(x,y) = ").strip()

    x, y = sp.symbols('x y')
    try:
        ux_expr = sp.sympify(ux_str)
        vy_expr = sp.sympify(vy_str)
    except (sp.SympifyError, TypeError) as e:
        print("Could not parse expressions. Try simpler syntax. Error:", e)
        return None

    ux_func = sp.lambdify((x, y), ux_expr, "numpy")
    vy_func = sp.lambdify((x, y), vy_expr, "numpy")

    def custom_field(xv, yv):
        return ux_func(xv, yv), vy_func(xv, yv)

    return custom_field


#main
if __name__ == "__main__":
    print("Select a flow type:")
    for key, (name, _) in flows.items():
        print(f"{key}. {name}")

    choice = input("Enter choice (1-5): ").strip()
    if choice not in flows:
        print("Invalid choice, defaulting to Vortex Flow")
        choice = "1"

    flow_name, func = flows[choice]

    if choice == "5":
        custom = get_custom_flow()
        if custom is None:
            print("Falling back to Vortex Flow.")
            velocity_field = vortex_flow
            flow_name = "Vortex Flow"
        else:
            velocity_field = custom
            flow_name = "Custom Flow"
    else:
        velocity_field = func

    #running the visualizations
    plot_streamlines()
    plot_pathlines()
    plot_streaklines()
    check_rotational()
