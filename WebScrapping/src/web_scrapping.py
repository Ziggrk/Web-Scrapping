from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import Entity

def sanctions_list(entity_search):
    entities = []
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Ejecuta Chrome en modo sin cabeza
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    
    driver = Chrome(service=service, options=options)
    driver.get("https://sanctionssearch.ofac.treas.gov/Default.aspx")

    # Interactúa con la página web para realizar la búsqueda
    driver.find_element(By.ID, "ctl00_MainContent_txtLastName").send_keys(entity_search)
    driver.find_element(By.ID, "ctl00_MainContent_btnSearch").click()

    # Espera a que la tabla de resultados se cargue
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_MainContent_lblCity"))
    )

    rows = len(driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[3]/div/div/div/div[4]/div[2]/div/table/tbody/tr"))
    cols = len(driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[3]/div/div/div/div[4]/div[2]/div/table/tbody/tr[1]/td"))

    for r in range(1, rows + 1):
        name = driver.find_element(By.XPATH, f"/html/body/form/div[3]/div/div/div[3]/div/div/div/div[4]/div[2]/div/table/tbody/tr[{r}]/td[1]").text
        address = driver.find_element(By.XPATH, f"/html/body/form/div[3]/div/div/div[3]/div/div/div/div[4]/div[2]/div/table/tbody/tr[{r}]/td[2]").text
        type_ = driver.find_element(By.XPATH, f"/html/body/form/div[3]/div/div/div[3]/div/div/div/div[4]/div[2]/div/table/tbody/tr[{r}]/td[3]").text
        programs = driver.find_element(By.XPATH, f"/html/body/form/div[3]/div/div/div[3]/div/div/div/div[4]/div[2]/div/table/tbody/tr[{r}]/td[4]").text
        list_ = driver.find_element(By.XPATH, f"/html/body/form/div[3]/div/div/div[3]/div/div/div/div[4]/div[2]/div/table/tbody/tr[{r}]/td[5]").text
        score = driver.find_element(By.XPATH, f"/html/body/form/div[3]/div/div/div[3]/div/div/div/div[4]/div[2]/div/table/tbody/tr[{r}]/td[6]").text
        
        entity = Entity.Entity(name, address, type_, programs, list_, score)
        entities.append(entity)
        
    driver.quit()
    return entities
