import pandas as pd
import plotly.express as px


data = pd.read_excel("ventas.xlsx")

groupeddata = data.groupby(["tienda","forma_pago"])["precio"].sum().to_frame()

groupeddata.to_excel("Grouped_data.xlsx")
lista_columnas = ["tienda", "Ciudad", "País", "tamaño", "local_consumo"]
for columna in lista_columnas:
    graf = px.histogram(data, x=columna,
                        y= "precio",
                        text_auto=True,
                        title="Facturación",
                        color="forma_pago")
    graf.show()
    graf.write_html(f"Facturación-{columna}.html")