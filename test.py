from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def testSearch():
    driver.find_element_by_css_selector("[type=search]").send_keys(cl)  
    sleep(1)
    driver.find_element_by_css_selector("[type=search]").send_keys(Keys.ENTER)
    sleep(2)
    title = driver.find_elements_by_class_name("grid-product__title-inner")
    for a in title:
        if cl.capitalize()  in a.text or cl in a.text :
            print("Yeah! That is ", cl)
        else:
            print("Test failed. It's not a",cl)
    sleep(3)
    driver.find_element_by_link_text("Очистить" or "Clear").click()

def testSurf():
    sleep(2)
    checkEl = driver.find_elements_by_class_name("form-control__inline-label")
    sleep(2)
    for i in checkEl:
        if i.text == "Surfboards":
            i.click()
            sleep(4)
            title = driver.find_elements_by_class_name("grid-product__title-inner")
            for a in title:
                if "Surfboard" in a.text:
                    print("YEAH. It's a Surfboard")
                else:
                    print("oh, no. It's not a Surfboard")
            sleep(2)
            i.click()
            break
        


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)


driver.get("https://www.ecwid.ru/demo/search")

sleep(10)
print("Test menu \n 1.Seach Test\n 2.Surf Test\n 3.Exit\n")
try:
    choice = int(input())
except TypeError:
    choice = 3
    print("Bad option. Exit....")
while choice < 3 and choice > 0:
    if choice == 1:
        print("Enter the type of clothing to search the site")
        cl = input()
        testSearch()

    if choice == 2:
        testSurf()

    else:
        choice = 3
    print("Menu \n 1.Seach Test \n 2.Surf Test\n 3.Exit\n")
    choice = int(input())
driver.close()
print("test end")
