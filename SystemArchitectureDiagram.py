import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import matplotlib.lines as mlines

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': 'Times New Roman',
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 12,
    'legend.fontsize': 9,
    'figure.titlesize': 14
})

fig, ax = plt.subplots(figsize=(7.5, 4.5))
ax.axis('off')

colors = {
    'input': '#4d4d4d',
    'processing': '#5da5da',
    'security': '#60bd68',
    'blockchain': '#f17cb0',
    'application': '#b2912f',
    'performance': '#b276b2'
}

# Component positions and sizes
components = {
    'Text Input': {'x': 0.1, 'y': 0.7, 'type': 'circle', 'color': colors['input']},
    'Edge Processing': {'x': 0.25, 'y': 0.7, 'width': 0.18, 'height': 0.25, 'color': colors['processing']},
    'Privacy Layer': {'x': 0.45, 'y': 0.7, 'width': 0.18, 'height': 0.2, 'color': colors['security']},
    'Blockchain': {'x': 0.65, 'y': 0.7, 'width': 0.18, 'height': 0.25, 'color': colors['blockchain']},
    'Applications': {'x': 0.85, 'y': 0.7, 'width': 0.18, 'height': 0.25, 'color': colors['application']}
}

details = {
    'Edge Processing': [
        "DistilRoBERTa Model",
        "Text Preprocessing",
        "Emotion Classification",
        "Confidence Scoring"
    ],
    'Privacy Layer': [
        "Data Anonymization",
        "SHA-3 Hashing"
    ],
    'Blockchain': [
        "ERC-725 Identity",
        "Smart Contracts",
        "Emotion Ledger"
    ],
    'Applications': [
        "Mental Health",
        "Customer Service",
        "Adaptive Learning"
    ]
}

# Draw components and details
for name, props in components.items():
    if props.get('type') == 'circle':
        circle = Circle((props['x'], props['y']), 0.045, fc=props['color'], ec='black', linewidth=1.2, zorder=2)
        ax.add_patch(circle)
        ax.text(props['x'], props['y'], name, ha='center', va='center', fontsize=10, fontweight='bold', color='white', zorder=3)
    else:
        rect = Rectangle((props['x']-props['width']/2, props['y']-props['height']/2),
                         props['width'], props['height'],
                         fc=props['color'], ec='black', linewidth=1.2, alpha=0.85, zorder=2)
        ax.add_patch(rect)
        # Title
        ax.text(props['x'], props['y']+props['height']/2-0.03, name, ha='center', va='top', fontsize=10, fontweight='bold', color='white', zorder=3)
        # Details, evenly spaced inside the box
        if name in details:
            n = len(details[name])
            for i, item in enumerate(details[name]):
                y_pos = props['y'] + props['height']/2 - 0.06 - (i+0.5)*props['height']/n
                ax.text(props['x'], y_pos, item, ha='center', va='center', fontsize=8, color='white', zorder=3)

# Draw arrows
arrow_style = dict(arrowstyle="->", color="black", linewidth=1.2, connectionstyle="arc3,rad=0", shrinkA=5, shrinkB=5)
positions = [components[c] for c in components]
arrow_pairs = [
    ('Text Input', 'Edge Processing'),
    ('Edge Processing', 'Privacy Layer'),
    ('Privacy Layer', 'Blockchain'),
    ('Blockchain', 'Applications')
]
for src, dst in arrow_pairs:
    x1 = components[src]['x']
    x2 = components[dst]['x']
    y = components[src]['y']
    ax.annotate("", xy=(x2-components[dst].get('width',0)/2-0.01, y), xytext=(x1+components[src].get('width',0)/2+0.01, y), arrowprops=arrow_style)

# Add performance metrics as a single box at the bottom center
perf_text = "94.2% Accuracy\n1,200 sent/sec\n21K+ Corpus\n7 Emotions"
ax.add_patch(Rectangle((0.38, 0.18), 0.24, 0.13, color=colors['performance'], ec='black', lw=1.2, zorder=2))
ax.text(0.5, 0.245, "Performance", ha='center', va='bottom', fontsize=10, fontweight='bold', color='white')
ax.text(0.5, 0.22, perf_text, ha='center', va='top', fontsize=9, color='white')

# Title
ax.set_title("System Architecture: Emotion-Aware AI with Blockchain Verification", y=1.02, fontweight='bold')

# Legend
legend_elements = [
    mlines.Line2D([], [], color=colors['processing'], marker='s', linestyle='None', markersize=8, label='NLP Processing'),
    mlines.Line2D([], [], color=colors['security'], marker='s', linestyle='None', markersize=8, label='Security Layer'),
    mlines.Line2D([], [], color=colors['blockchain'], marker='s', linestyle='None', markersize=8, label='Blockchain'),
    mlines.Line2D([], [], color=colors['application'], marker='s', linestyle='None', markersize=8, label='Applications')
]
ax.legend(handles=legend_elements, loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.15))

plt.tight_layout()
plt.savefig('IEEE_Architecture_Diagram.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('IEEE_Architecture_Diagram.png', format='png', bbox_inches='tight', dpi=300)
plt.show()