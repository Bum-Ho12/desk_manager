import flet as ft
from home_screen import HomeScreen

from process_fetcher import retriever

class MaterialApp(ft.UserControl):
    def build(self):
        self.processes = retriever()
        self.value = 0.3
        # self.materialBuilder = ft.NavigationBar
        home_screen = HomeScreen(self.processes,self.value)
        finalMat =  ft.Column(controls=[
            home_screen
        ])
        return finalMat

def main(page:ft.page):
    page.title = "Desk Manager"
    materialApp = MaterialApp()
    page.add(materialApp)


ft.app(target = main)