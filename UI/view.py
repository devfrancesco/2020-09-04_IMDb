import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Esame 04/09/2020 IMDB"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT

        # controller
        self._controller = None

        # graphical elements
        self._title = None
        self._txt_rank = None
        self._dd_film = None
        self._btn_crea_grafo = None
        self._btn_grado_massimo = None
        self._btn_cammino_incremento = None
        self.txt_result = None

    def load_interface(self):
        # Title
        self._title = ft.Text("Esame 04/09/2020 IMDB", color="blue", size=24)
        self._page.controls.append(self._title)

        # Riga 1: Inserimento Rank (r) e Bottone Crea Grafo
        self._txt_rank = ft.TextField(label="Rank (r)", hint_text="Inserisci un valore tra 0.0 e 10.0", width=300)
        self._btn_crea_grafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo,
                                                 width=200)

        row1 = ft.Row([self._txt_rank, self._btn_crea_grafo],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)
        self._page.controls.append(row1)

        # Riga 2: Selezione Film (m) e Bottone Film di Grado Massimo
        self._dd_film = ft.Dropdown(label="Film (m)", hint_text="Seleziona un film dal grafo", width=300)
        self._btn_grado_massimo = ft.ElevatedButton(text="Film di Grado Massimo",
                                                    on_click=self._controller.handleGradoMassimo, width=200)

        row2 = ft.Row([self._dd_film, self._btn_grado_massimo],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)
        self._page.controls.append(row2)

        # Riga 3: Bottone Cammino Incremento
        self._btn_cammino_incremento = ft.ElevatedButton(text="Cammino Incremento",
                                                         on_click=self._controller.handleCamminoIncremento, width=200)

        row3 = ft.Row([self._btn_cammino_incremento],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # Area di testo per la stampa dei risultati (ListView)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()