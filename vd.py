import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_hickory_venn_diagram():

    fig, ax = plt.subplots(figsize=(10, 10))

    fig.patch.set_facecolor('#E6E6E6')
    ax.set_facecolor('#E6E6E6')

    circle_settings = [
        {'center': (0.35, 0.6), 'radius': 0.35},  # Top Left
        {'center': (0.65, 0.6), 'radius': 0.35},  # Top Right
        {'center': (0.5, 0.35), 'radius': 0.35}   # Bottom
    ]

    for circle in circle_settings:
        c = patches.Circle(
            circle['center'],
            circle['radius'],
            linewidth=6,
            edgecolor='black',
            facecolor='none'
        )
        ax.add_patch(c)

    text_elements = [
        # Top Left (Straight lines) - Changed to E, F, H, Z
        (0.23, 0.70, 'E', 'black', 35),
        (0.19, 0.60, 'F', 'black', 35),
        (0.26, 0.51, 'H', 'blue', 35),
        (0.28, 0.76, 'Z', 'black', 35),

        # Top Right (Curved lines) - Changed to D, Q, G
        (0.76, 0.74, 'D', 'black', 35),
        (0.85, 0.65, 'Q', 'black', 35),
        (0.75, 0.65, 'G', 'black', 35),
        (0.79, 0.78, '8', 'black', 35), # Added a number with curves

        # Bottom (Greek Lowercase/General) - Changed to alpha, lambda, beta
        (0.50, 0.09, 'λ', 'black', 40),
        (0.43, 0.14, 'β', 'black', 40),
        (0.56, 0.16, 'θ', 'black', 40),
        (0.49, 0.23, 'δ', 'green', 40),

        # Top Intersection (Mixed Straight/Curved) - Changed to P, 5
        (0.50, 0.75, '%', 'black', 35),
        (0.45, 0.80, 'P', 'black', 35),
        (0.49, 0.65, '5', 'red', 35),
        (0.53, 0.58, 'D', 'black', 35),

        # Left Intersection (Greek Straight-ish) - Changed to Delta, Sigma
        (0.25, 0.44, 'Δ', 'black', 40),
        (0.35, 0.32, 'Σ', 'black', 40),
        (0.29, 0.35, 'Ξ', 'black', 40),

        # Right Intersection (Greek Curved) - Changed to rho, alpha
        (0.60, 0.45, 'ρ', 'black', 40),
        (0.65, 0.31, 'α', 'black', 40),
        (0.75, 0.39, 'Ω', 'black', 40),

        # Center (Target)
        (0.40, 0.45, '?', 'black', 45)
    ]

    for x, y, char, color, size in text_elements:
        ax.text(
            x, y, char,
            color=color,
            fontsize=size,
            ha='center',
            va='center',
            fontfamily='serif',
            fontweight='bold'
        )

    # 4. Final Formatting
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # 5. Save/Show
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    create_hickory_venn_diagram()
