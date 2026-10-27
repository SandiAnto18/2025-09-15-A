import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillAllYears(self):
        # Recupero gli anni dal Model
        years = self._model.getAllYears()

        # Inserisco gli anni in entrambi i menu
        # Popolo i due menu a tendina
        for year in years:
            self._view._ddAnno1.options.append(ft.dropdown.Option(year))
            self._view._ddAnno2.options.append(ft.dropdown.Option(year))

        self._view.update_page()

    def handleCreaGrafo(self, e):
        # Leggo da VIEW gli anni selezionati
        da = self._view._ddAnno1.value
        a = self._view._ddAnno2.value

        # costruisco il grafo sugli anni selezionati (da ,a)
        self._model.buildGraph(da,a)

        # Pulisco i risultati precedenti
        self._view.txt_result.controls.clear()

        # Visualizzo il numero di nodi e archi
        self._view.txt_result.controls.append(
            ft.Text("Grafo correttamente creato")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Numero di nodi: {self._model.getNumNodi()}")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Numero di archi: {self._model.getNumArchi()}")
        )

        # Aggiorno la pagina
        self._view.update_page()

    def handleDettagli(self, e):
        pass
    def handleCerca(self, e):
        pass

