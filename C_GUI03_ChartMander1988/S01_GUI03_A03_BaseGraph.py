# Extract of code from S01_GUI03_A01_ChartMander1988.py. Create the base for the Mander 1988 chart.


                                                        # Anotaciones de grafica.
plt.annotate(r"Confined   Strength   Ratio   $f_{cc} '/f_{co} '$", xy=(0.4641, 0.9545), 
                fontsize = 17 * factor_reduccion, fontproperties=font, style='italic', xycoords='figure fraction')
plt.annotate(r"Smallest   Confining   Stress   Ratio   $f_{l1} '/f_{co} '$", xy=(0.3191, 0.0387), 
                fontsize = 17 * factor_reduccion, fontproperties=font, style='italic', xycoords='figure fraction')
plt.annotate(r"Largest   Confining   Stress   Ratio   $f_{l2} '/f_{co} '$",
                xy=(0.0218, 0.0972), fontsize=17 * factor_reduccion, fontproperties=font, xycoords='figure fraction',
                rotation=90)
                                                    # Identificacion de curvas.
plt.annotate("0", xy=(0.606, 0.1149), fontsize = 15 * factor_reduccion, fontproperties=font, 
                style='italic', xycoords='figure fraction')
plt.annotate("0.1", xy=(0.775, 0.1149), fontsize = 15 * factor_reduccion, fontproperties=font, 
                style='italic', xycoords='figure fraction')
plt.annotate("0.2", xy=(0.878, 0.1149), fontsize = 15 * factor_reduccion, fontproperties=font, 
                style='italic', xycoords='figure fraction')
plt.annotate("0.3", xy=(0.949, 0.1149), fontsize = 15 * factor_reduccion, fontproperties=font, 
                style='italic', xycoords='figure fraction')
                                                        # Valor de fl1/fco.
if aux_graph:
    coef_smallest_1 = str(int(coef_smallest * 1000) / 1000)
    plt.annotate(r"$f_{l1} '/f_{co} ' = $" + f"{coef_smallest_1}", xy=(c_x1+0.35*w_f1, c_y1+0.015), 
                    fontsize = 15 * factor_reduccion, fontproperties=font, color = 'red',
                    style='italic', xycoords='figure fraction')
                                                            # Grafica de curvas.
for i in np.arange(0, 0.32, 0.02):
    key = f"Datos_fl1_fc0_{i:.2f}"
    plt.plot(Data_Abaco[key][0], Data_Abaco[key][1], color = 'b', lw=1.5 * factor_reduccion)
                                                    # Grafica de curva fl1 = fl2.
key = "Datos_fl1_fl2"
plt.plot(Data_Abaco[key][0], Data_Abaco[key][1], color = 'b', lw=1.6 * factor_reduccion)
                                                # Definir los límites de los ejes.
plt.xlim(-0.044, 2.304)
plt.ylim(0, 0.30)
                                                            # Invertir el eje y.
plt.gca().invert_yaxis()
                                            # Mover los ticks del eje x al top.
plt.gca().xaxis.tick_top()
                                                    # Grafica de grid horizontal.
for i in np.arange(0.02, 0.3, 0.02):
    key = f"Datos_fl1_fc0_{i:.2f}"
    for ID, data in enumerate(Data_Abaco[key][1]):
        tol = 1e-4
        if abs(data-i)<=tol:
            ID_data = ID
            break
    x_start = -0.044
    x_end = Data_Abaco[key][0][ID_data]
    y_start, y_end = i, i
    plt.plot([x_start, x_end], [y_start, y_end], linestyle='--', linewidth=0.4 * factor_reduccion,
                color='gray')
                                                    # Grafica de grid vertical.
key = "Datos_fl1_fl2"
for k in np.arange(1.1, 2.3, 0.1):
    for ID, data in enumerate(Data_Abaco[key][0]):
        tol = 1e-2
        if abs(data-k)<=tol:
            ID_data = ID
            break
    x_start, x_end = k, k
    y_start = 0
    y_end = Data_Abaco[key][1][ID_data]
    plt.plot([x_start, x_end], [y_start, y_end], linestyle='--', linewidth=0.4 * factor_reduccion,
                color='gray')
                                                            # Grafica de flechas.
plt.arrow(1.05, 0.25, 0.15, 0.0, head_width=0.01 * factor_reduccion, head_length=0.05 * factor_reduccion, fc='gray', ec='gray')
plt.arrow(2.05, 0.165, -0.07, 0.022, head_width=0.01 * factor_reduccion, head_length=0.05 * factor_reduccion, fc='gray', ec='gray')
                                                        # Anotaciones de grafica.
plt.annotate("Biaxial", xy=(0.428, 0.261), fontsize = 15 * factor_reduccion, fontproperties=font, 
                style='italic', color='gray', xycoords='figure fraction')
plt.annotate(r"$f_{l1} ' = f_{l2} '$", xy=(0.860, 0.5003), 
                fontsize = 15 * factor_reduccion, fontproperties=font, style='italic', color='gray', xycoords='figure fraction')
