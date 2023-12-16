# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Define the path
path = '/Users/ataago/Documents/git/tableConvertorXYs/input/'
out_path = '/Users/ataago/Documents/git/tableConvertorXYs/output/'


def gen_wordcloud(freq, out_file_path):

    # Generate a word cloud for 'Sustainable Practice'
    wordcloud = WordCloud(
        width=1600, height=800, background_color='white'
    ).generate_from_frequencies(frequencies=freq)

    # Display the word cloud
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout()
    # plt.title('Word Cloud for Sustainable Practice', fontweight='bold', fontsize=20, color='darkred')

    # Save the word cloud as a .png file
    plt.savefig(out_file_path, bbox_inches='tight')


# Reload the data
data = pd.read_excel(path + "PracticesWithImpacts(edited2).xlsx", header=0)

gen_wordcloud(
    freq=data['Sustainable Practice'].value_counts(),
    out_file_path=out_path + 'wordcloud_sustainable_practice.png'
)

gen_wordcloud(
    freq=data['Performance Outcome'].value_counts(),
    out_file_path=out_path + 'wordcloud_performance_outcome.png'
)
