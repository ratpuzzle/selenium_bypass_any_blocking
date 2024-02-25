from selenium_stealth import stealth
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("prefs", "preferences")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-impl-side-painting")



options.add_argument(f"user-agent={get_user_agent[f'{x}']}")
proxy_options = {"proxy": {"https": f"http://{proxy[f'{x}']}"}}

# seleniumwire_options=proxy_options включение прокси
driver = webdriver.Chrome(
    proxy_options=proxy_options,
    options=options,
    executable_path=r'C:\Users\ratmu\PycharmProjects\beastfi.org\chromedriver.exe',

)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
stealth(driver,
        languages=["ru-RU"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        run_on_insecure_origins=True
        )

