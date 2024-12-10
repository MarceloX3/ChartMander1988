# Extract of code from S01_GUI03_A01_ChartMander1988.py. Create the higlighted curve with the intrested data for the Mander 1988 chart.

key = f"Datos_fl1_fc0_{coef_smallest:.2f}"
plt.plot(Data_interes[key][0], Data_interes[key][1], color = 'r', lw=1.5 * factor_reduccion)
coef_largest  = fl2 / fc0
i = coef_largest
coef_fcc = solve_equation(fl2,fl3, fc0)
k = coef_fcc
                                                # Grafica de line horizontal.
x_start, x_end = -0.044, k
y_start, y_end = i, i
plt.plot([x_start, x_end], [y_start, y_end], linestyle='--', linewidth=1.0 * factor_reduccion,
            color='red')
                                                # Grafica de line vertical.
x_start, x_end = k, k
y_start, y_end = 0, i
plt.plot([x_start, x_end], [y_start, y_end], linestyle='--', linewidth=1.0 * factor_reduccion,
            color='red')
                                                            # Grafica punto.
plt.scatter(k, i, marker='o', color='red', s=9 * factor_reduccion)
                                                    # Specify the tick values.
xtick = [1.0, 1.5, 2.0]
ytick = [0, 0.1, 0.2, 0.3]
xtick2 = xtick
ytick2 = ytick
xtick_labels = []
ytick_labels = []
                                # Se ajustan labels para no se superpongan.
for ID, x in enumerate(xtick):
    if abs(x-k) <= 0.12:
        xtick2.pop(ID)          # Elimina el elemento en la posicion ID.
        if len(xtick)>ID:       # Si elimino un elemento, es porque se superponia etiqueta. 
            xtick_labels.append(str(int(xtick[ID] * 100) / 100))  # Asi que se agrega valor de interes en el eje.
    else:
        xtick_labels.append(str(int(x * 100) / 100))  # En caso que no se superpongan, simplemente agrega el termino a las etiquetas del eje.
        
for ID, y in enumerate(ytick):
    if abs(y-i) <= 0.015:
        ytick2.pop(ID)          # Elimina el elemento en la posicion ID.
        if len(ytick)>ID:       # Si elimino un elemento, es porque se superponia etiqueta. 
            ytick_labels.append(str(int(ytick[ID] * 100) / 100))  # Asi que se agrega valor de interes en el eje.
    else:
        ytick_labels.append(str(int(y * 100) / 100))  # En caso que no se superpongan, simplemente agrega el label a las etiquetas del eje.
                                            # Se agrega tick de valor deseado.
xtick2.append(k) # Trunca en el segundo decimal. No redondea.
ytick2.append(i) # Trunca en el segundo decimal. No redondea.
xtick_labels.append(str(int(k * 1000) / 1000))
ytick_labels.append(str(int(i * 1000) / 1000))

plt.xticks(xtick2, xtick_labels)
plt.yticks(ytick2, ytick_labels)

for tick in plt.gca().get_xticklabels():
    if tick.get_text() == str(int(k * 1000) / 1000):
        tick.set_fontproperties(font)
        tick.set_color('r')
        tick.set_fontsize(13 * factor_reduccion)
    else:
        tick.set_fontproperties(font)
        tick.set_fontsize(15 * factor_reduccion)
        
        
for tick in plt.gca().get_yticklabels():
    if tick.get_text() == str(int(i * 1000) / 1000):
        tick.set_fontproperties(font)
        tick.set_color('r')
        tick.set_fontsize(13 * factor_reduccion)
    else:
        tick.set_fontproperties(font)
        tick.set_fontsize(15 * factor_reduccion)

plt.savefig(URL)