# Import matplotlib library here
import matplotlib.pyplot as plt
# Let's rank some of our favorite snacks
snack_scores = [1, 2, 3]

slice_labels = ["smart sweets", "kit kat", "popcorn"]

colors = ["#99ccff", "#d3d3d3", "#000000"]

# Let's make a pie chart!
plt.pie(snack_scores, labels = slice_labels, colors = colors)

# Give your pie chart a title in the quotes
plt.title("RWR's favorite snacks", fontsize=22)

# Put the name of your file in the quotes and give it a .png extension
plt.savefig("snack_scores.png")

