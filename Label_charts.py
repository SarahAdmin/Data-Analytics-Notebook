ax = sns.barplot(data=df,x='example1',y='example2',hue='example3) or sns.barplot(data=mydf) 
for container in ax.containers: 
  ax.bar_label(container, fmt='£%.2f')
plt.show()
