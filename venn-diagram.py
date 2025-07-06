import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import matplotlib.patches as mpatches

# Set IEEE style parameters
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 10,
    'figure.titlesize': 12
})

# Create figure
fig, ax = plt.subplots(figsize=(7, 5))
ax.set_title("Research Gap Analysis in Emotion-Aware Systems", 
             fontweight='bold', pad=20)

# Create Venn diagram
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1),  # Equal sized circles
          set_labels=('Emotion\nClassification', 
                     'Privacy\nPreservation', 
                     'Blockchain\nVerification'),
          set_colors=('#5da5da', '#60bd68', '#f17cb0'),  # IEEE color palette
          alpha=0.7,
          ax=ax)

# Label the intersections
v.get_label_by_id('100').set_text('High Accuracy\nModels [5-9]')
v.get_label_by_id('010').set_text('Federated\nLearning [11-13]')
v.get_label_by_id('001').set_text('ERC-725\nSystems [14-16]')
v.get_label_by_id('110').set_text('+15% Error Rate\n[12,13]')
v.get_label_by_id('101').set_text('Cloud-Dependent\n[22]')
v.get_label_by_id('011').set_text('Non-Emotional\nUse Cases [20,21]')
v.get_label_by_id('111').set_text('Our Work')
v.get_label_by_id('111').set_fontweight('bold')

# Add annotation arrow
ax.annotate('Unaddressed Gap', xy=(0.5, 0.4), xytext=(0.3, 0.6),
            arrowprops=dict(arrowstyle='->', lw=1.5),
            fontsize=9, ha='center')

# Add legend with IEEE-style citations
legend_elements = [
    mpatches.Patch(facecolor='#5da5da', label='Transformer Models [5-9]'),
    mpatches.Patch(facecolor='#60bd68', label='Privacy Methods [11-13]'),
    mpatches.Patch(facecolor='#f17cb0', label='Blockchain Systems [14-16]')
]
ax.legend(handles=legend_elements, loc='lower center', 
          bbox_to_anchor=(0.5, -0.15), ncol=3)

plt.tight_layout()

# Save in IEEE recommended formats
plt.savefig('research_gap_venn.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('research_gap_venn.png', format='png', bbox_inches='tight', dpi=300)
plt.show()