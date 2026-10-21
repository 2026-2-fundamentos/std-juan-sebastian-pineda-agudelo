# Preparacion

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd



# Carga de la tabla drivers

drivers = pd.read_csv(
    "../data/drivers.csv",
    sep=",",
    thousands=None,
    decimal=".",
)
drivers.head()



# Carga de la tabla timesheet

timesheet = pd.read_csv(
    "../data/timesheet.csv",
    sep=",",
    thousands=None,
    decimal=".",
)
timesheet.head()

# Media de las horas y las millas de cada conductor

mean_timesheet = timesheet.groupby("driverId").mean()
mean_timesheet.head()



# Eliminación de la columna 'week'

mean_timesheet.pop("week")
mean_timesheet.head()


# Registros con valores por debajo de la media del grupo



# Cómputo de la cantidad de horas y millas de cada conductor por año

sum_timesheet = timesheet.groupby("driverId").sum()
sum_timesheet.head(10)




sum_timesheet = sum_timesheet[["hours-logged", "miles-logged"]]
sum_timesheet.head()



timesheet.groupby("driverId")["hours-logged"].agg(["min", "max"])



# Unión de las tablas usando join

summary = pd.merge(
    sum_timesheet,
    drivers[["driverId", "name"]],
    on="driverId",
)
summary




# Almacenamiento de los resultados

import os


summary.to_csv(
    "../submission/summary.csv",
    sep=",",
    header=True,
    index=False,
)




# Ordenamiento por la cantidad de millas registradas

top10 = summary.sort_values(by="miles-logged", ascending=False).head(10)
top10






# Creación de un gráfico de barras horizontales
# La columna 'name' pasa a ser el nombre de las filas

top10 = top10.set_index("name")

# Paleta de colores:
#   tab:blue     tab:red       tab:pink
#   tab:orange   tab:purple    tab:gray
#   tab:green    tab:brown     tab:olive
#   tab:cyan

top10["miles-logged"].plot.barh(color="tab:orange", alpha=0.6)

plt.gca().invert_yaxis()

plt.gca().get_xaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ","))
)

plt.xticks(rotation=90)

plt.gca().spines["left"].set_color("lightgray")
plt.gca().spines["bottom"].set_color("gray")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.savefig("../submission/top10_drivers.png", bbox_inches="tight")










