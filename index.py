import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"], index_col="date")
#change style?
#plt.style.use('Solarize_Light2')
def plot_timeseries(axes, x, y, color, xlabel, ylabel, label):

    axes.plot(x, y, color=color, label=label)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)

fig, ax = plt.subplots()

plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', "Time (years)", "CO2 levels", "CO2 levels")
ax2 = ax.twinx()
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', "Time (years)", "Relative temperature (Celsius)", "Relative temperature")
ax.set_title("Time, CO2 levels, relative temperature")
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
#return style?
#plt.style.use('default')
fig.savefig("TimeCO2levelsRelativeTemperature.png")

fig2, ax3 = plt.subplots()
scatter=ax3.scatter(climate_change["co2"],climate_change['relative_temp'], c=climate_change.index)
ax3.set_title("Relation between time, CO2 levels and relative temperature")
ax3.set_ylabel("Relative Temp")    
ax3.set_xlabel("CO2 ppm")
#fig.set_size_inches([3, 5])
fig.savefig("RelationTimeCO2levelsRelativeTemp.png")
plt.show()