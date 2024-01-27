# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.image import Image
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput

# class Aggie_Dining(App):
#     def build(self):
#         # self.window = GridLayout()

#         button = Button(text="Commons Dining Hall", size_hint=(.5, .5),
#                         pos_hint={'center_x': .5, 'center_y': .5})
#         button.bind(on_press=self.on_press_button)

#         # return self.window
    
#     def on_press_button(self, instance):
#         print("test")
        

# if __name__ == "__main__":
#     app = Aggie_Dining()
#     app.run()

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
# from web_scraping import locations


from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time as t

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

start_url = "https://dineoncampus.com/tamu/hours-of-operation"

driver.get(start_url)
t.sleep(7)
full_html = driver.page_source.encode("utf-8")
driver.quit()

soup = BeautifulSoup(full_html, "html.parser")

locations = []
for loc in soup.find_all(class_='hours-of-operation-section_locationName_1vUeF'):
    locations.append(loc.text.strip())

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text="Choose a Location", color="500000"))

        self.add_widget(Image(source="test_img.jpeg"))

        # self.add_widget(Label(text='The Commons Dining Hall (South Campus)'))
        # self.add_widget(Label(text='Sbisa Dining Hall (North Campus)'))
        # self.add_widget(Label(text='Duncan Dining Hall (South Campus/Quad)'))
        for loc in locations:
            self.add_widget(Label(text=loc))



class Aggie_Dining(App):
    def build(self):
        return MyGrid()
        # label1 = Label(
        #     text='Commons Dining Hall')
        
        # label2 = Label(
        #     text='Commons Dining Hall')
        # return label1, 


        # my_label.text = 'hello'
        # # the label is usually not drawn until needed, so force it to draw.
        # my_label.refresh()
        # return my_label
        # # button1 = Button(text='Commons Dining Hall')
        # # button1.bind(on_press=self.on_press_button)

        # # return button1

    # def on_press_button(self, instance):
        # print('You pressed the button!')

if __name__ == "__main__":
    app = Aggie_Dining()
    app.run()