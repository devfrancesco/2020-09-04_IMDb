import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        r_input = self._view._txt_rank.value
        if r_input is None:
            self._view.create_alert("Scrivi un rank da 0.0 da 10.0")
            return
        try:
            float_r = float(r_input)
        except ValueError:
            self._view.create_alert("Inserisci un rank nel formato float")
            return
        if float_r < 0.0 or float_r > 10.0:
            self._view.create_alert("Scrivi un rank da 0.0 da 10.0")
            return
        self._model.buildGraph(float_r)
        nNodes, nEdges = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente"))
        self._view.txt_result.controls.append(ft.Text(f"Numero vertici: {nNodes}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero Archi: {nEdges}"))
        self._view._dd_film.options.clear()
        self.fillDDFilm()
        self._view.update_page()

    def handleGradoMassimo(self, e):
        self._view.txt_result.controls.clear()
        film, grado = self._model.getTopFilm()
        if film is None:
            self._view.txt_result.controls.append(ft.Text(f"Non esiste un film di grafo massimo"))
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"Film Grado massimo"))
        self._view.txt_result.controls.append(ft.Text(f"{film} - {grado}"))
        self._view.update_page()

    def handleCamminoIncremento(self, e):
        self._view.txt_result.controls.clear()
        film = self._view._dd_film.value
        if film is None:
            self._view.create_alert("Seleziona un film")
            return
        bestPath = self._model.getBestPath(film)
        self._view.txt_result.controls.append(ft.Text(f"Cammino più lungo: {len(bestPath)}"))
        for f in bestPath:
            self._view.txt_result.controls.append(ft.Text(f"{f}"))
        self._view.update_page()

    def fillDDFilm(self):
        allMovies = self._model.getAllMoviesInGraph()
        for m in allMovies:
            self._view._dd_film.options.append(ft.dropdown.Option(key=str(m.id), text=str(m)))
        self._view.update_page()