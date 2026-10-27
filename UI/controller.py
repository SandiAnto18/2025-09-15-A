import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillAllYears(self):
        years=self._model.getAllYears()
        for year in years:
            self._view._ddAnno1.options.append(ft.dropdown.Option(year))
            self._view._ddAnno2.options.append(ft.dropdown.Option(year))

        self._view.update_page()



    def handleCreaGrafo(self,e):
        # Leggo gli anni selezionati
        da = self._view._ddAnno1.value
        a = self._view._ddAnno2.value

        # Costruisco il grafo
        self._model.buildGraph(da, a)

        # Pulisco i risultati precedenti
        self._view.txt_result.controls.clear()

        # Mostro il numero di nodi e archi
        self._view.txt_result.controls.append(
            ft.Text("Grafo correttamente creato:")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Numero di nodi: {self._model.getNumNodi()}")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Numero di archi: {self._model.getNumArchi()}")
        )

        self._view.update_page()

    def handleDettagli(self, e):
        pass
    def handleCerca(self, e):
        pass

    def getNumNodi(self):
        # Restituisco il numero di nodi
        return len(self._graph.nodes())

    def getNumArchi(self):
        # Restituisco il numero di archi
        return len(self._graph.edges())
