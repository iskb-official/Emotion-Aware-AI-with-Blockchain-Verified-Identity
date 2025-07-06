import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def draw_box(ax, text, xy, box_size=(4.2, 0.8)):
    x, y = xy
    width, height = box_size
    box = FancyBboxPatch((x - width / 2, y - height / 2), width, height,
                         boxstyle="round,pad=0.02", edgecolor="black", facecolor="white")
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=10, color='black')

def draw_arrow(ax, start, end):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))

fig, ax = plt.subplots(figsize=(7, 9))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# Y positions for boxes
y_positions = [11, 9.5, 8, 6.5, 5, 3.5, 2]

# Define steps (single-line text)
steps = [
    "Text Input",
    "Edge NLP (DistilRoBERTa)",
    "Emotion Classification (Real-time, Quantized)",
    "Data Minimization & SHA-3 Hashing",
    "Blockchain Anchoring (ERC-725, Smart Contract)",
    "Verification & Consistency Check",
    "Application Use (Mental Health, AI Bots)"
]

# Draw boxes and arrows
for i, text in enumerate(steps):
    draw_box(ax, text, (5, y_positions[i]))
    if i < len(steps) - 1:
        draw_arrow(ax, (5, y_positions[i] - 0.5), (5, y_positions[i + 1] + 0.5))

plt.tight_layout()
plt.savefig("methodology_flowchart.png", dpi=300, bbox_inches='tight')
plt.show()
