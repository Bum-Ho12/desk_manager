# coding: utf-8
'''
@author: Bum-HO
'''
import flet as ft


def main(page: ft.page):
    def addTask(todo):
        checkBox = ft.Checkbox(value=False)
        checkBoxText = ft.Text(value=textField.value,
                        width = 350,bgcolor='purple')
        taskRow = ft.Row(controls=[checkBox,checkBoxText],
                    alignment=ft.MainAxisAlignment.START)
        page.add(taskRow)


    page.window_width = 500
    page.window_heigh = 700
    # page.bgcolor = 'white'
    textField = ft.TextField(width=350)
    # addBtn = ft.ElevatedButton(text = "Add", on_click=addTask)
    addBtn = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=addTask)
    entriesRow = ft.Row(controls=[textField,addBtn],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )

    page.add(entriesRow)

ft.app(target=main)