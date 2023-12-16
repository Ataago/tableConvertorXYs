# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Define the path
path = 'G:/My Drive/PhD - VTU/202306 Conference & Journals special issues/'

# Reload the data
data = pd.read_excel(path + "PracticesWithImpacts(edited2).xlsx", header=0)

# Generate a word cloud for 'Sustainable Practice'
wordcloud_practice = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(data['Sustainable Practice'].value_counts())

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_practice, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Sustainable Practice', fontweight='bold', fontsize=20, color='darkred')
# Save the word cloud as a .png file
plt.savefig(path + '/Python Code/wordcloud_sustainable_practice.png')
plt.show()

# Generate a word cloud for 'Performance Outcome'
wordcloud_outcome = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(data['Performance Outcome'].value_counts())

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_outcome, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Performance Outcome', fontweight='bold', fontsize=20, color='darkred')
# Save the word cloud as a .png file
plt.savefig(path + '/Python Code/wordcloud_performance_outcome.png')
plt.show()
