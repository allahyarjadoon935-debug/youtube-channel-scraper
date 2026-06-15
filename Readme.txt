# 📺 YouTube Channel Scraper

A powerful Python-based YouTube Channel Scraper built with Streamlit, Selenium, Pandas, and Undetected ChromeDriver.

This application allows users to scrape publicly available video information from YouTube channels and export the collected data to Excel for analysis, reporting, content research, and competitor monitoring.

---

# 🚀 Features

* Scrape videos from any public YouTube channel
* Support for channel URLs and channel usernames
* Automatic scrolling to load all available videos
* Extract video titles
* Extract video URLs
* Extract upload dates
* Extract view counts
* Extract video durations
* Export results to Excel (.xlsx)
* Interactive Streamlit dashboard
* Automatic Chrome version detection
* Uses Undetected ChromeDriver for improved browser automation reliability

---

# 📊 Data Extracted

The scraper collects the following information:

| Field         | Description                  |
| ------------- | ---------------------------- |
| Title         | Video title                  |
| Duration      | Video duration               |
| Views         | Total view count             |
| Uploaded-Time | Upload date/time information |
| URL           | Direct video link            |

Example Output:

| Title           | Duration | Views  | Uploaded-Time | URL                     |
| --------------- | -------- | ------ | ------------- | ----------------------- |
| Python Tutorial | 12:34    | 250000 | 2 months ago  | https://youtube.com/... |

---

# 🛠️ Technologies Used

* Python
* Streamlit
* Selenium
* Pandas
* OpenPyXL
* Undetected ChromeDriver

---

# 📂 Project Structure

```text
youtube-channel-scraper/
│
├── app.py
├── youtube_scraper.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── driver/
    └── User Data1/
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/youtube-channel-scraper.git

cd youtube-channel-scraper
```

---

## 2. Create Virtual Environment (Recommended)

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac:

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

```txt
streamlit
pandas
selenium
undetected-chromedriver
openpyxl
```

---

# ▶️ Run Application

Start the Streamlit application:

```bash
streamlit run app.py
```

After execution, Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open it in your browser.

---

# 📖 How To Use

### Step 1

Launch the application.

### Step 2

Enter either:

* YouTube Channel URL

Example:

```text
https://www.youtube.com/@MrBeast
```

or

* Channel Username

Example:

```text
MrBeast
```

### Step 3

Click:

```text
Start Scraping
```

### Step 4

The scraper will:

* Open Chrome browser
* Navigate to the channel
* Scroll through all videos
* Extract video information
* Create an Excel file

### Step 5

Download the generated Excel file directly from the Streamlit interface.

---

# 📈 Use Cases

This project can be used for:

### Content Research

Analyze channel content and publishing trends.

### Competitor Analysis

Monitor competitors' video performance and publishing activity.

### YouTube Analytics

Collect structured video datasets for reporting and analysis.

### Data Science Projects

Build datasets for machine learning and statistical analysis.

### Market Research

Study content strategies within specific niches.

---

# 🔍 How It Works

1. User enters a channel URL or username.
2. Selenium launches Chrome using Undetected ChromeDriver.
3. Browser navigates to the channel Videos page.
4. The application scrolls until all videos are loaded.
5. Video containers are collected.
6. Metadata is extracted:

   * Title
   * Duration
   * Views
   * Upload Time
   * URL
7. Data is stored in a Pandas DataFrame.
8. Results are exported to Excel.
9. User downloads the file from Streamlit.

---

# 💾 Output Format

Excel File Example:

```text
youtube_data.xlsx
```

Columns:

```text
Title
Duration
Views
Uploaded-Time
URL
```

---

# ⚠️ Notes

* Internet connection is required.
* Google Chrome must be installed.
* Large channels may take longer to scrape.
* Scraping speed depends on internet performance and YouTube loading times.
* Publicly available data only is collected.

---

# 🐞 Troubleshooting

## Chrome Version Issues

Update Google Chrome to the latest version.

## Driver Errors

Reinstall dependencies:

```bash
pip install --upgrade selenium
pip install --upgrade undetected-chromedriver
```

## Streamlit Not Found

Install Streamlit:

```bash
pip install streamlit
```

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to your branch
5. Open a Pull Request

---

# ⭐ Support

If you find this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share it with other developers

---

# 📜 Disclaimer

This project is intended for educational and research purposes only.

Users are responsible for ensuring compliance with YouTube's Terms of Service and applicable laws when collecting or using data.
