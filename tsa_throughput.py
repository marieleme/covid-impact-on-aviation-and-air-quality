from bs4 import BeautifulSoup
import requests
import pandas as pd
from matplotlib import pyplot as plt
import locale
from datetime import date

tsa_url = "https://www.tsa.gov/coronavirus/passenger-throughput"


def scrub_table_from_url(url):
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")

    table = soup.find("table")
    table_rows = table.tbody.find_all("tr")

    headings = []
    for td in table_rows[0].find_all("td"):
        # remove any newlines and extra spaces from left and right
        headings.append(td.text.replace('\n', '').replace('\t', '').strip())

    print(headings)

    # Iterate over
    data = []
    for row in table_rows[1:]:
        tds = [td.contents[0] for td in row.find_all("td")]
        if len(tds) == 0:
            continue

        data.append(tds)

    return headings, data


h, d = scrub_table_from_url(tsa_url)

df = pd.DataFrame(d, columns=h)
# df[h[0]] = df[h[0]].apply(lambda t: str(t))
df[h[1]] = df[h[1]].apply(lambda t: int(t.replace(',', '')))
df[h[2]] = df[h[2]].apply(lambda t: int(t.replace(',', '')))


print(df.dtypes)
print(df)
ax = plt.gca()

df.plot(kind='line', x=h[0], y=h[1], ax=ax)
df.plot(kind='line', x=h[0], y=h[2], color='red', ax=ax)

plt.savefig('tsa_plot.png')

df.to_csv(f'tsa_data/tsa_data_{date.today()}.csv')
