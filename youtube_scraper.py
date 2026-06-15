import os
import plistlib
from pathlib import Path
import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import base64
import time
import pandas as pd
from datetime import datetime

def get_installed_chrome_version():
    """Automatically detect the exact Chrome version installed on your PC"""
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")
        version, _ = winreg.QueryValueEx(key, "version")
        major_version = int(version.split('.')[0])
        print(f"✅ Detected Chrome version: {major_version} on your PC")
        return major_version
    except Exception as e:
        print(e)
        print("⚠️ Could not detect Chrome version automatically. Will let undetected_chromedriver try.")
        return get_installed_chrome_version_mac()

def get_installed_chrome_version_mac():
    """Detect Chrome version on macOS using Info.plist"""
    try:
        plist_path = "/Applications/Google Chrome.app/Contents/Info.plist"
        
        with open(plist_path, "rb") as f:
            plist = plistlib.load(f)
        
        version = plist.get("CFBundleShortVersionString")
        major_version = int(version.split('.')[0])
        
        print(f"✅ Detected Chrome version: {major_version} on your Mac")
        return major_version

    except Exception as e:
        print(e)
        print("⚠️ Could not detect Chrome version automatically.")
        return None

def open_browser():
  
    # Get the current directory path
    current_directory = Path(os.getcwd())
   
    # Your custom user data directory
    user_data_dir = current_directory / "driver/User Data1"
   
    # Create Chrome options using undetected_chromedriver
    options = webdriver.ChromeOptions()
    
    # Make browser visible
    options.headless = False
    
    # User data directory (keeps logins, cookies, profiles)
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument('--profile-directory=Default')
    
    # Stability arguments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")

    #for background working
    #driver.execute_script("window.focus();")  #use this for foucsing before driver.get()


    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-features=CalculateNativeWinOcclusion")

    # Auto-detect Chrome version on your PC
    chrome_version = get_installed_chrome_version()
    
    # Create driver – now it will ALWAYS match your installed Chrome version
    driver = webdriver.Chrome(
        options=options,
        version_main=chrome_version,      # ← Automatically uses your PC's Chrome version

    )
    for tab in driver.window_handles:
        driver.switch_to.window(tab)
        url = driver.current_url
    
        if  "chrome://new-tab-page/" in url:
            break  # stop when found
    print("🚀 Browser opened successfully with your current Chrome version!")
    return driver

def visit_channel(driver,channel): 

    try:
        driver.get(channel)
    except:
        print("Invalid channel name or URL")
        return
    return driver

def scroll_youtube_channel(driver , delay = 5):

    print("🚀 Starting YouTube Scroller")

    no_change = 0

    last_height = driver.execute_script(
        "return document.documentElement.scrollHeight"
    )

    while True:

        try:
            # Scroll to bottom
            driver.execute_script(
                "window.scrollTo(0, document.documentElement.scrollHeight);"
            )

            time.sleep(random.randint(delay , delay + 6))

            # Get new height
            new_height = driver.execute_script(
                "return document.documentElement.scrollHeight"
            )

            # Detect new loaded content
            if new_height > last_height:

                print("✅ New Videos Loaded")

                last_height = new_height
                no_change = 0

            else:
                no_change += 1
            # Stop condition
            if no_change >= 6:
                print("✅ Scrolling Finished")
                break

        except Exception as e:
            print(f"❌ Error: {e}")
            break

def scroll_bottom_to_top(driver,step=200):
    current_scroll = driver.execute_script("return window.pageYOffset;")
    while current_scroll > 0:
        driver.execute_script(f"window.scrollBy(0, -{step});")
        time.sleep(random.randint(1, 4))
        current_scroll = driver.execute_script("return window.pageYOffset;")        
def get_views(data):
    views_text = data.find_element(
    By.XPATH,
    './/span[contains(@aria-label,"views")]'
    ).text

    views_text = views_text.lower().replace("views", "").strip()

    multipliers = {
        "k": 1_000,
        "m": 1_000_000,
        "b": 1_000_000_000
    }

    last_char = views_text[-1]

    if last_char in multipliers:
        return int(float(views_text[:-1]) * multipliers[last_char])

    return int(float(views_text))
def scrape_videoes(driver): 
    scroll_youtube_channel(driver)
    scroll_bottom_to_top(driver,step=200)
    channel_data = []
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"videoes_data_{timestamp}.xlsx"
    try:
        containers = driver.find_elements(
                        By.CSS_SELECTOR,
                        "ytd-rich-item-renderer, ytd-rich-item-renderer[is-shorts-grid]"
                    )
    except:
        print("No data found")

    for data in containers:
        title = data.find_element(
        By.CSS_SELECTOR,
        "a[href*='/watch'] span"
        ).text
    
        upload_date = data.find_element(
        By.XPATH,
        './/span[contains(@aria-label,"ago")]'
        ).text

        element = data.find_element(
                By.CSS_SELECTOR,
                "a[href*='/watch'] , a[href*='/shorts/']"
            )
    
        duration = (
            element.get_attribute("title")
            or element.text
        ).strip()

        # Link
        link = element.get_attribute("href")
        
        #views
        views = get_views(data)

        channel_data.append(
            {
                "Title":title,
                "Duration":duration,
                "Views":views,
                "Uploded-Time":upload_date,
                "Url":link,
            }
        )
        if len(channel_data) % 20 == 0:
            print(f"✅ Scraped {len(channel_data)} properties so far...")
            df = pd.DataFrame(channel_data)
            df.to_excel(filename, index=False)
                
    if channel_data:  # Save any remaining properties after the loop        
        print(f"💾 Final save: {len(channel_data)} properties")        
        df = pd.DataFrame(channel_data)
        df.to_excel(filename, index=False) 
        return df
    return pd.DataFrame()

