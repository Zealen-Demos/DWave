from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:\Development\Python\DWave\chromedriver.exe")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver.get("https://cloud.dwavesys.com/leap/login/")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
