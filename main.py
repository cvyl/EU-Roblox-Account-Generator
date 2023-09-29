import time
import random
import string
import tkinter as tk
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore, Back, Style

window_size = (800, 600)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(f"--window-size={window_size[0]},{window_size[1]}")

chromedriver_path = r'webdriver\chromedriver.exe'

def generate_random_username(prefix, length):
    if length <= len(prefix):
        raise ValueError("Length should be greater than the length of the prefix.")
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(prefix)))
    username = f"{prefix}{random_chars}"
    return username

def generate_random_password(length):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def create_account():
    num_iterations = int(iterations_entry.get())
    starting_name = name_entry.get()
    name_length = int(namelength_entry.get())
    
    for _ in range(num_iterations):
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        driver.get("https://www.roblox.com/")
        wait = WebDriverWait(driver, 30)
        
        cooki = driver.find_element(By.XPATH, "//button[@class='btn-secondary-lg cookie-btn btn-primary-md btn-min-width']")
        cooki.click()
        
        time.sleep(1)

        dropdown = driver.find_element(By.CLASS_NAME, 'rbx-select')
        dropdown.click()
        time.sleep(1)

        option_29 = driver.find_element(By.XPATH, "//option[text()='29']")
        option_29.click()
        time.sleep(1)

        dropdown = driver.find_element(By.CLASS_NAME, 'rbx-select')
        dropdown.click()

        option_january = driver.find_element(By.XPATH, "//option[@value='Jan']")
        option_january.click()
        time.sleep(1)

        dropdown = driver.find_element(By.CLASS_NAME, 'rbx-select')
        dropdown.click()

        option_1999 = driver.find_element(By.XPATH, "//option[@value='1999']")
        option_1999.click()
        time.sleep(1)

        username = driver.find_element(By.XPATH, "//*[@id='signup-username']")
        random_username = generate_random_username(starting_name, name_length)
        username.send_keys(random_username)
        time.sleep(1)

        password = driver.find_element(By.XPATH, "//*[@id='signup-password']")
        random_password = generate_random_password(12)
        password.send_keys(random_password)
        time.sleep(1)

        selected_function = random.choice([lambda: Gender1(driver), lambda: Gender2(driver)])
        selected_function()
        time.sleep(1)

        try:
            sign = driver.find_element(By.XPATH, "//*[@id='signup-button']")
            sign.click()
        except:
            num_iterations += 1
            time.sleep(1)
            driver.quit()

        def save_account_to_file(random_username, random_password):
            with open("Account.txt", "a") as file:
                file.write(f"{random_username}:{random_password}\n")

        time.sleep(10)

        try:
            element = driver.find_element(By.XPATH, "//*[@id='header-menu-icon']/button[2]")
            element.click()
            driver.quit()
        except:
            num_iterations += 1
            time.sleep(1)
            driver.quit()
        save_account_to_file(random_username, random_password)
        

    result_label.config(text="Finished creating accounts")

def Gender1(driver):
    Gender = driver.find_element(By.XPATH, "//*[@id='MaleButton']")
    Gender.click()

def Gender2(driver):
    Gender2 = driver.find_element(By.XPATH, "//*[@id='FemaleButton']")
    Gender2.click()

# Create the GUI
root = tk.Tk()
root.title("EU R.A.G")
root.geometry("240x180")
root.resizable(False,False)

iterations_label = tk.Label(root, text="Enter the number of iterations:")
iterations_label.pack()
iterations_entry = tk.Entry(root)
iterations_entry.pack()

name_label = tk.Label(root, text="Starting name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

namelength_label = tk.Label(root, text="Name length:")
namelength_label.pack()
namelength_entry = tk.Entry(root)
namelength_entry.pack()

create_button = tk.Button(root, text="Create Accounts", command=create_account)
create_button.pack()

edition_label = tk.Label(root, text="EU Edition fork")
edition_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
