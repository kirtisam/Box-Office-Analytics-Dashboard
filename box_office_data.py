import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the target URL
url = "https://www.the-numbers.com/box-office-chart/weekend/2024/07/05"

# Add headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    # Send HTTP GET request
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table")

    if len(tables) < 2:
        raise ValueError("Expected table not found on the page.")

    target_table = tables[1]  # Still works if structure is same
    rows = target_table.find_all("tr")

    # Extract table data
    data = []
    for row in rows[1:]:
        cols = [col.text.strip() for col in row.find_all("td")]
        if cols:
            data.append(cols)

    # Define headers manually (could also extract from <th>)
    headers = [
        "Rank", "Previous Rank", "Movie Title", "Distributor",
        "Gross", "% LW", "Theaters", "Change", "Per Theater",
        "Total Gross", "Week"
    ]

    # Create DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Save to CSV
    df.to_csv("box_office_data.csv", index=False)
    print("✅ Data saved to box_office_data.csv")

except Exception as e:
    print(f"❌ Error occurred: {e}")
print(df.head())
