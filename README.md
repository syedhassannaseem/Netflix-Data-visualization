# 🎬 Netflix Data Visualization  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![VS Code](https://img.shields.io/badge/VS-Code-007ACC) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-lightgrey) ![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-green)


## 📌 Project Overview  
This project explores and visualizes the **Netflix Movies & TV Shows dataset** using **Python, Pandas, and Matplotlib** in **VS Code**.  
It includes multiple visualizations to understand Netflix’s content library, such as the distribution of Movies vs TV Shows, content ratings, release year trends, movie duration patterns, and top contributing countries.  

---

## 📂 Dataset  
- **Source:** [Netflix Movies and TV Shows Dataset  
- **File:** `netflix_titles.csv`  
- **Columns include:**  
  - `show_id` → Unique ID for each show  
  - `type` → Movie or TV Show  
  - `title` → Name of the content  
  - `director` → Director(s)  
  - `cast` → Actors  
  - `country` → Country of origin  
  - `date_added` → Date added to Netflix  
  - `release_year` → Release year  
  - `rating` → Content rating (e.g., PG, TV-MA)  
  - `duration` → Duration (minutes or seasons)  
  - `listed_in` → Genre(s)  
  - `description` → Short summary  

---

## 🛠️ Tools & Technologies  
- **Python 3**  
- **Pandas** → Data cleaning & manipulation  
- **Matplotlib** → Data visualization  
- **VS Code** → Development environment  

---

## 📊 Visualizations in the Project  
1. **Content Type Distribution**  
   - Bar chart showing the number of Movies vs TV Shows on Netflix.  
   - 📎 Output file: `bar.png`  

2. **Ratings Breakdown**  
   - Pie chart showing the percentage distribution of ratings.  
   - 📎 Output file: `pie.png`  

3. **Release Year Trends**  
   - Line plot showing how many Movies were released each year.  
   - 📎 Output file: `plot.png`  

4. **Movie Duration Analysis**  
   - Histogram of movie durations (minutes).  
   - 📎 Output file: `hist.png`  

5. **Top Countries by Content**  
   - Horizontal bar chart of the top 10 countries with the highest number of shows.  
   - 📎 Output file: `barh.png`  

6. **Movies vs TV Shows Over the Years**  
   - Subplots comparing yearly releases of Movies and TV Shows.  
   - 📎 Output file: `subplots.png`  

---

## 🚀 How to Run the Project  
1. Clone this repository:  
   ```bash
   git clone https://github.com/syedhassannaseem/netflix-data-visualization.git
   cd netflix-data-visualization
