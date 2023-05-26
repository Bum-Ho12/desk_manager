import flet as ft

class HomeScreen(ft.UserControl):
    def __init__(self,processes,value):
        super().__init__()
        self.processes = processes
        self.value = value

    def build(self):
        self.card_container = ft.Card(
            content=ft.Container(
                width=400,
                padding=ft.Padding(
                    left=8,
                    right=8,
                    bottom=8,
                    top=8,
                ),
                content= self.computerSummary(),
            )
        )
        self.performance_indicator = self.performanceIndicator(self.value)
        # self.performance_info = self.performanceInfo()
        return ft.Column(controls=[self.card_container,
                ft.Card(
            content=ft.Container(
                width=700,
                padding=ft.Padding(
                    left=8,
                    right=8,
                    bottom=8,
                    top=8,
                ),
                content= self.performanceInfo(),
            )
        )
            ],
            alignment= ft.MainAxisAlignment.SPACE_EVENLY,
        )

    # container for data
    def computerSummary(self):
        return ft.ListView(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.LAPTOP,size=70),
                        ft.Container(
                            padding= ft.Padding(
                                top=8.0,
                                bottom=8.0,
                                left=8.0,
                                right=8.0
                            ),
                            content= ft.Text('OS Platform: ',
                                max_lines=6,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            )
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.BAR_CHART_ROUNDED,size=70),
                        ft.Container(
                            padding= ft.Padding(
                                top=8.0,
                                bottom=8.0,
                                left=8.0,
                                right=8.0
                            ),
                            content= ft.Text('CPU Processors: ',
                                max_lines=6,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            )
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.STORAGE_ROUNDED,size=70),
                        ft.Container(
                            padding= ft.Padding(
                                top=8.0,
                                bottom=8.0,
                                left=8.0,
                                right=8.0
                            ),
                            content= ft.Text('Primary Drive ',
                                max_lines=6,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            )
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.ACCOUNT_CIRCLE_OUTLINED,size=70),
                        ft.Container(
                            padding= ft.Padding(
                                top=8.0,
                                bottom=8.0,
                                left=8.0,
                                right=8.0
                            ),
                            content= ft.Text('User Name: ',
                                max_lines=6,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            )
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.WINDOW_ROUNDED,size=70),
                        ft.Container(
                            padding= ft.Padding(
                                top=8.0,
                                bottom=8.0,
                                left=8.0,
                                right=8.0
                            ),
                            content= ft.Text('Platform Version: ',
                                max_lines=6,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            )
                        )
                    ]
                )
            ]
        )

    def contentGenerator(self,content):
        return ft.Row(
            controls=[
                self.performanceIndicator(0.4),
                ft.Column(
                    controls=[
                        ft.Container(
                            padding= ft.Padding(
                                top= 8,bottom= 8,
                                left=8,right=8,
                            ),
                            content=ft.Text(f'{content[0]}')
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    padding=ft.Padding(
                                        top=4,bottom=4,
                                        left=4,right=4
                                    ),
                                    content=ft.Stack(
                                        controls=[
                                            ft.Container(
                                                height=10,
                                                width = 350,
                                                border_radius= ft.BorderRadius(
                                                    top_left= 10,top_right=10,
                                                    bottom_left=10,bottom_right=10
                                                    ),
                                                bgcolor='white'
                                            ),
                                            ft.Container(
                                                height=10,
                                                width = 350,
                                                border_radius= ft.BorderRadius(
                                                    top_left= 10,top_right=10,
                                                    bottom_left=10,bottom_right=10
                                                    ),
                                                bgcolor='blue'
                                            ),
                                        ]
                                    )
                                ),
                                ft.Container(
                                    padding=ft.Padding(
                                        top=2,bottom=2,
                                        left=2,right=2
                                    ),
                                    content=ft.Text(f'{content[1]}')
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def performanceInfo(self):
        self.lst = [
            ['GPU Performance','3.4 GB/8 GB'],
            ['CPU Performance','3.4 GB/8 GB'],
            ['HOME DRIVE','112 GB/256 GB'],
        ]

        return ft.Container(
            border_radius= ft.BorderRadius(
                    top_left=10,top_right=10,
                    bottom_left=10,bottom_right=10,
            ),
            content= ft.ListView(
                padding= ft.Padding(top=10,left=10,right = 10,bottom=10),
                controls=[
                    self.contentGenerator(self.lst[0]),
                    self.contentGenerator(self.lst[1]),
                    self.contentGenerator(self.lst[2])
                ]
            )
        )

    #performance indicator widget
    def performanceIndicator(self,value):
        percentage_value = value*100
        percentage_value= str(percentage_value)
        return ft.Container(
            height=80,
            width=80,
            border_radius= ft.BorderRadius(
                top_left=10,
                top_right=10,
                bottom_left=10,
                bottom_right=10
                ),
            content=ft.Column(
                controls=[
                    ft.Container(
                        padding= ft.Padding(
                            top=4,
                            bottom=4,
                            right=4,
                            left= 4,
                        ),
                        content= ft.Text(
                            f'{percentage_value}%',
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                    )
                ]
            )
        )

    def powerIndicator(self):
        return ft.Container(
            border_radius=ft.BorderRadius(
                top_left=10,
                top_right=10,
                bottom_left=10,
                bottom_right=10,
            ),
            content=ft.Column(
                padding= ft.Padding(
                    top= 4,
                    bottom=4,
                    left=4,
                    right = 4,
                ),
                controls=[
                    self.batteryConsumption(),
                ]
            )
        )

    def batteryConsumption(self):
        return ft.ListView(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text('Chrome'),
                        ft.Stack(
                            controls=[
                                ft.Container(
                                    height=10,
                                    width = 350,
                                    border_radius= ft.BorderRadius(
                                        top_left= 10,top_right=10,
                                        bottom_left=10,bottom_right=10
                                        ),
                                    bgcolor='white'
                                ),
                                ft.Container(
                                    height=10,
                                    width = 350,
                                    border_radius= ft.BorderRadius(
                                        top_left= 10,top_right=10,
                                        bottom_left=10,bottom_right=10
                                        ),
                                    bgcolor='blue'
                                ),
                            ]
                        )
                    ]
                )
            ]
        )