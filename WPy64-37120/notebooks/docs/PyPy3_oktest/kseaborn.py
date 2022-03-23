# Seaborn
# for more examples, see http://stanford.edu/~mwaskom/software/seaborn/examples/index.html
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
df = sns.load_dataset("iris")
sns.pairplot(df, hue="species", height=1.5)
plt.show()
