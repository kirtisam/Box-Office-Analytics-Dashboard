# Box-Office-Analytics-Dashboard
Box Office Analytics Dashboard (Power BI)
Analyze. Compare. Predict.
Understand what makes a movie a box office hit vs. a flop using interactive visuals, real-world KPIs, and DAX-powered insights.
Analyzing Box Office Movie Performance Using Web Scraping and Power BI

**Objective**
The goal of this project is to identify why some movies succeed and others fail at the box office by analyzing key metrics such as gross revenue, % change, theater count, and total gross.
We collected real-time movie data using web scraping from The-Numbers.com and visualized insights using Power BI.
Tools & Technologies Used
 Python (Web Scraping)
Google Co lab (Cloud-based coding platform)
Power BI (Data Modeling & Visualization)
Microsoft Word (Documentation)

**Data Collection Method – Web Scraping**
We used Python and Beautiful Soup to scrape the weekend box office report from [The-Numbers.com].
Step:
1. Open the Google col ab
2. Run the following Code

Import requests
from bs4 import BeautifulSoup
import pandas as pd
# URL for the box office data
url = "https://www.the-numbers.com/box-office-chart/weekend/2024/07/05"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# Extract table
tables = soup.find_all("table")
target_table = tables[1]
# Read rows
rows = target_table.find_all("tr")
data = []
for row in rows[1:]:
cols = [col.text.strip() for col in row.find_all("td")]
 if cols:
data.append(cols)
# Define headers
headers = ["Rank", "Previous Rank", "Movie Title", "Distributor", "Gross", "% LW", "Theaters", "Change", "Per Theater", "Total Gross", "Week"]
# Create DataFrame
df = pd.DataFrame(data, columns=headers)
df.to_csv("box_office_data.csv", index=False)
df.head()


**Data Cleaning in Power BI (Power Query Editor)**
**Cleaning Steps:**
Removed special characters from columns like Gross, % LW, and Total Gross (e.g., $, %, ,)
Converted columns to appropriate types:
1)Gross, Total Gross: Decimal Number
2)% LW: Decimal (after dividing by 100)
3)Rank, Theaters: Whole Number
Removed rows with null values or text errors in numeric fields
Used Transform > Trim & Clean to sanitize text columns
Promoted first row as headers and removed unnecessary header rows if repeated
Fixing Errors:
Used "Remove Errors" option on custom column if error rows occurred
Filtered out nulls in Gross using "Keep Rows Where Not Null"
Deleted "Errors in box_office_data" query, which was automatically created for debugging


**Hit/Flop/Super Hit Classification**
Movies were classified into Flop, Hit, or Super Hit based on thresholds set on the Total Gross value.
This classification helps segment movies by commercial success and analyze profitability trends by category.
 Profitability Analysis by Hit Category
A visual summary shows cumulative revenue earned by movies in each Hit/Flop Category.This helps identify how much revenue comes from each segment and provides clarity on overall profitability driven by "Super Hit" titles.
  Weekly Ranking Trend
Tracked each movie’s position (Rank) over multiple weeks.
Highlighted movies that sustained a Top 1 ranking over consecutive weeks, indicating consistent public interest and stronger lifetime value.
Distributor Profitability Analysis
Linked each movie to its distributor to measure revenue contribution and hit count per distributor.Identified which distributors consistently released profitable films, enabling insights into studio performance and release strategy effectiveness.

<img width="474" alt="image" src="https://github.com/user-attachments/assets/f3047493-08e8-4c67-a820-5510aeb63bcf" />
<img width="468" alt="image" src="https://github.com/user-attachments/assets/4afe4400-b67f-4ff8-876b-7861fb7c525c" />
<img width="489" alt="image" src="https://github.com/user-attachments/assets/8f221f84-4289-4b47-bc8e-ee59c20588a6" />
<img width="455" alt="image" src="https://github.com/user-attachments/assets/df83ccc4-73cb-4352-a13f-1100e3a893cc" />

