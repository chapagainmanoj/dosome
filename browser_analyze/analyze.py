import pandas as pd
import numpy as np
from urllib.parse import urlparse

import matplotlib.pyplot as plt
topN = 20

# Open our file
with open('/home/manoj/moz_hist.txt') as f:
    content = f.readlines()
# Strip whitespace then split on first occurrence of pipe character
raw_data = [line.split('|', 1) for line in [x.strip() for x in content]]
# We now have a 2D list.

data = pd.DataFrame(raw_data, columns=['datetime', 'url'])

parser = lambda u: urlparse(u).netloc
data.url = data.url.apply(parser)


# Aggregate domain entries
site_frequencies = data.url.value_counts().to_frame()
# Make the domain a column
site_frequencies.reset_index(level=0, inplace=True)
# Rename columns to appropriate names
site_frequencies.columns = ['domain', 'count']
# Display top 2
x = site_frequencies.head(topN)

print(x)

plt.figure(1, figsize=(10,10))
plt.title('Top $n Sites Visited'.replace('$n', str(topN)))
pie_data = site_frequencies['count'].head(topN).tolist()
pie_labels = None
# Uncomment to get specific domain names
pie_labels = site_frequencies['domain'].head(topN).tolist()
plt.pie(pie_data, autopct='%1.1f%%', labels=pie_labels)
plt.show()
