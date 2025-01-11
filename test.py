from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the path to the ChromeDriver executable
path = "C:\selenium\chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.bigbasket.com")
print("Page title is:", driver.title)
driver.maximize_window()

# click on login  -------- Case 1--------------
def login_to_bigbasket():
    try:
        button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))
        )
        button_element.click()
        print("Login button clicked successfully!")
    except Exception as e:
        print(f"Failed to find or click the login button: {e}")

# Enter phone number  -------------Case 2-------------
def parsing_phone_number():
    try:
        phone_input = driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div/div/div/div[2]/form/div/input")
        phone_input.clear()
        ####  phone_input.send_keys("-----Enter phone number-----")
        print("\nPhone number entered successfully!")
        time.sleep(2)
        button_element = driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div/div/div/div[2]/form/button")
        button_element.click()
    except Exception as e:
        print(f"\nFailed to enter the phone number: {e}")

# Click on gotit --------Case---------
def gotit():
    try:
        button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id=siteLayout]/header[2]/div[1]/div[2]/div[1]/div/div/div/button"))
        )
        button_element.click()
    except Exception as e:
        print(f"Failed to find or click the login button: {e}")


# Enter for OTP input  -------------Case 3-------------
def enter_otp(otp):
    try:
        otp_input = driver.find_element(By.XPATH, "//input[@class = 'p-2.5 w-10 text-center rounded-2xs text-md leading-none font-regular focus:outline-none focus:shadow-outline border text-darkOnyx-700 border-darkOnyx-400 border [appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none']")
        otp_input.send_keys(otp)
        verify_button = driver.find_element(By.XPATH, "//button[@class='w-71.5 px-2.5 h-8.5 text-base font-semibold leading-sm transition-all bg-rossoCorsa-500 text-rossoCorsa-50 outline-none rounded-2xs disabled:opacity-30']")
        verify_button.click()
        print("\nEntered OTP successfully!")
    except Exception as e :
        print(f"\nFailed to verify the otp: {e}")

    time.sleep(5)

# Search for a product - ------------Case 4-------------
def product_search(product):
    try:
        search_input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'flex-1 w-full leading-md lg:text-sm xl:text-md placeholder-silverSurfer-700')]"))
        )
        search_input_element.send_keys(product)
        search_input_element.send_keys(Keys.RETURN)
        print(f"\nSearched for {product} successfully!")
    except Exception as e:
        print(f"\nFailed to search for {product} : {e}")


# Add a item to the cart - ------------Case 5-------------
def add_to_cart():
    try:
        product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[6]/div[2]/section[2]/section/ul/li[1]/div/div/div[5]/div/div[2]/button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(1)  # Allow time for scrolling
        driver.execute_script("arguments[0].click();", product)
        print("\nItem added to basket successfully!")
        time.sleep(4)
    except Exception as e:
        print(f"\nFailed to add item to basket: {e}")


# Add another item to cart - ------------Case 6-------------
def increment_item():
    try:
        increment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[6]/div[2]/section[2]/section/ul/li[1]/div/div/div[5]/div/div[2]/div/button[2]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", increment_button)
        time.sleep(1)  # Allow time for scrolling
        driver.execute_script("arguments[0].click();", increment_button)
        print("\nItem incremented in basket successfully!")
        time.sleep(4)
    except Exception as e:
        print(f"\nFailed to increment item in basket: {e}")


# remove item from cart - ------------Case 7-------------
def decrement_item():
    try:
        decrement_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[6]/div[2]/section[2]/section/ul/li[1]/div/div/div[5]/div/div[2]/div/button[1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", decrement_button)
        time.sleep(1)  # Allow time for scrolling
        driver.execute_script("arguments[0].click();", decrement_button)
        print("\nItem decremented in basket successfully!")
    except Exception as e:
        print(f"\nFailed to decrement item in basket: {e}")

def click_on_cart():
    try:
        button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/viewcart']"))
        )
        button_element.click()
        print("Cart button clicked successfully!")
    except Exception as e:
        print(f"Failed to find or click the cart button: {e}")

def click_on_checkout():
    try:
        button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Checkout')]"))
        )
        button_element.click()
        print("Checkout button clicked successfully!")
    except Exception as e:
        print(f"Failed to find or click the Checkout button: {e}")

def click_on_proceed_to_payment():
    try:
        button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Proceed to Payment')]"))
        )
        button_element.click()
        print("Proceed To Payment button clicked successfully!")
    except Exception as e:
        print(f"Failed to find or click the Proceed To Payment button: {e}")


 # Click in Got-it poppup message -------------Case 11--------------
def click_on_gotit():
    try:
        button_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/header[2]/div[1]/div[2]/div[1]/div/div/div/button")
        button_element.click()
        print("\nLogin button clicked successfully!")
    except Exception as e:
        print(f"\nFailed to find or click the login button: {e}")

def main():
    try:
        login_to_bigbasket()
        parsing_phone_number()
        otp = input("Enter the OTP for completing login process: ")
        time.sleep(2)
        enter_otp(otp)
        time.sleep(2)
        click_on_gotit()
        gotit()
        
        while True:
            print("\nMenu:")
            print("1. Search for a new item")
            print("2. Increment an existing item")
            print("3. Decrement an existing item")
            print("4. Check my Cart")
            print("5. End searching")
            choice = input("Enter your choice: ")

            if choice == "1":
                product = input("Enter the product that you want to search for: ")
                product_search(product)
                time.sleep(5)
                add_to_cart()
            elif choice == "2":
                increment_item()
                time.sleep(5)
            elif choice == "3":
                decrement_item()
            elif choice == "4":
                click_on_cart()
                time.sleep(5)
            elif choice == "5":
                print("You have chosen to end searching. The browser will remain open.")
                break
            else:
                print("Invalid choice, please try again.")
        
        time.sleep(5)
        click_on_cart()
        time.sleep(5)
        click_on_checkout()
        time.sleep(5)
        click_on_proceed_to_payment()
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(10000)

if __name__ == "__main__":
    main()