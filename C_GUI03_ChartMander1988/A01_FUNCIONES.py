# -*- coding: utf-8 -*-
"""
ACTUALIZACION:  2024-03-20
AUTOR:          Marcelo Ortiz Á.
SCRIPT:         A01_FUNCIONES.py
COMENTARIOS:    El siguiente código tiene como finalidad apoyar el desarrollo de 
                programas en python. Las funciones que contiene son:
                
                - show_matrix(M, Titulo): Ploteo por consola de matrices.
                
                - obtener_desplazamientos(nodos, df, t): Obtiene el desplaza-
                miento de cierto grado de libertad de un nodo, para cierto
                timepo t, de un determinado data_frame.
                
                - unit(sist): Define el sistema de unidades a emplear en un 
                modelo en Openseespy. Las unidades patrón para la definición 
                del sistema de unidades pueden ser:   
                                          s-m-N   s-IN-kip  s-cm-kgf  s-m-tonf
                
                - recorte(img, scale_dpi, ax, ubic_x): Recorta una imagen para
                que calce en espacio ax. El factor scale_dpi, mejora nitidez
                de imagen.
                
                - recorte2D(img, scale_dpi, ax, ubic_x, ubic_y): Recorta una 
                imagen para que calce en espacio ax. Tanto en x como y. 
                El factor scale_dpi,mejora nitidez de imagen.
"""

# %% [00] IMPORTACIÓN DE LIBRERÍAS
import math as mt
import numpy as np

     

# %% [01] PLOT MATRICES -------------------------------------------------------
#                   La siguiente función imprime de forma elegante las tablas
#                   NOTA: CUIDAR QUE ANCHO DE TITULO < ANCHO TABLA
def show_matrix(M, Titulo):
        #PARÁMETROS   
        #             Sea: M =[["var1", "var2","var3"],[1,2,3],[1,2,3],[1,2,3]]
        filas = len(M)          # -> 4
        columnas = len(M[0])    # -> 3
        #----------------------------------------------------------------------
        ancho_col = []          #Esta lista almacena el ancho de columnas.
                                #El ancho de las columnas está en la lista [0]
                                #ancho_col = [4, 4, 4]
        for k in range(columnas):
            ancho = len(str(M[0][k]))
            ancho_col.append(ancho)
        #----------------------------------------------------------------------
        cont_string = 0         #cont_string: Tiene el ancho efectivo de tabla.
                                #| var1 | var2 | var3 |-> (4+4+4) + 3*3 + 1 =22
        for k in range(columnas):
            cont_string = cont_string + ancho_col[k]
            
        cont_string = cont_string + columnas * 3 + 1
        #----------------------------------------------------------------------

        #IMPRIME TÍTULOS DE TABLAS
        Num_guion_tot = cont_string - len(Titulo)
                                #Si Num_guion_tot es par -> mitad y mitad.
                                #% calcula el residual de una división.
        if Num_guion_tot % 2 == 0:
            guion = "=" * int(Num_guion_tot * 0.5)
            print(guion + Titulo + guion)            
        else:                   #Si Num_guion_tot es impar -> mitad + mitad + 1
            parte_decimal, parte_entera = mt.modf(Num_guion_tot * 0.5)
            guion = "=" * int(parte_entera)
            print(guion+Titulo + guion+"=")
        #----------------------------------------------------------------------

        #IMPRIME MATRIZ
                                #Recorre matriz: |1 2 3| ->
        for i in range(filas):          #        |4 5 6| |
            for j in range(columnas):   #        |7 8 9| V
                                #El primer IF es porque al ser la primera fila
                                #los rotulos del sistema no se pueden redondear
                if i == 0:
                    if len(str(M[i][j])) >= ancho_col[j]:               
                        print("| {0} ".format(M[i][j]), sep=',', end='')
            
                if i != 0:
                                    #Se tienen 2 casos:                
                                    #1) El ancho de número supera el ancho de columna
                    if len(str(round(M[i][j],3))) >= ancho_col[j]:                 
                        print("| {0} ".format(round(M[i][j],3)), sep=',', end='')
                                    #2) El ancho de número es menor al ancho de columna
                    if len(str(round(M[i][j],3))) < ancho_col[j]:                    
                        Num_esp = ancho_col[j]-len(str(round(M[i][j],3)))
                        extra = " "*Num_esp
                        print("| "+extra+"{0} ".format(round(M[i][j],3)), sep=',', end='')            
            print('|')     
        #----------------------------------------------------------------------

        #IMPRIME LÍNEA DE CIERRE
        guion = "=" * cont_string
        print(guion)
        #----------------------------------------------------------------------


# %% [02] DESPLAZAMIENTOS NODOS -----------------------------------------------

def obtener_desplazamientos(nodos, df, t):
    # Seleccionar las columnas correspondientes a los nodos que se encuentran en la lista de nodos que se nos entregó.
    columnas = [f"nodo_{nodo}_d_{i}" for nodo in nodos for i in range(1, 4)]
    df_nodos = df[columnas]
    
    # Seleccionar la fila correspondiente al instante de tiempo t.
    fila = df_nodos.iloc[t]
    
    # Crear un arreglo con los desplazamientos en las direcciones X, Y y Z.
    desplazamientos = np.array(fila).reshape(len(nodos), 3)
    
    return desplazamientos


# %% [03] SISTEMA DE UNIDADES -------------------------------------------------
"""
Define el sistema de unidades a emplear en un modelo en Openseespy.
Las unidades patrón para la definición del sistema de unidades pueden ser:
    s-m-N
    s-IN-kip
    s-cm-kgf
    s-m-tonf

Las unidades de esfuerzo, masa, aceleracion, etc. Se derivan de estas.
"""

def unit(sist):
    print("\n")
    print("===============================")
    print(f"Sistema de unidades: {sist}")
    print("===============================")
    print("\n")
    
    # UNIDADES FUNDAMENTALES
    if sist == "s-m-N":
        # Longitud:
        m   =   1
        cm  =   0.01*m
        IN  =   0.0254*m
        # Fuerza:
        N   =   1
        kip =   4.4482216152605*10**3*N
        kgf =   9.80665*N
        tonf=   10**3*kgf
        # Tiempo:
        s   =   1
        # Aceleracion:
        g   =   9.80665*m/(s**2)
    
    if sist == "s-IN-kip":
        # Longitud:
        IN  =   1
        m   =   39.3700787401575*IN
        cm  =   0.01*m
        # Fuerza:
        kip =   1
        N   =   0.0002248089431*kip
        kgf =   0.002204622621849*kip
        tonf=   10**3*kgf
        # Tiempo:
        s   =   1
        # Aceleracion:
        g   =   386.088582677165*IN/(s**2)
        
    if sist == "s-cm-kgf":
        # Longitud:
        cm  =   1
        m   =   100*cm
        IN  =   2.54*cm
        # Fuerza:
        kgf =   1
        N   =   0.101971621297793*kgf
        kip =   453.59237*kgf
        tonf=   10**3*kgf
        # Tiempo:
        s   =   1
        # Aceleracion:
        g   =   980.665*cm/(s**2)
        
    if sist == "s-m-tonf":
        # Longitud:
        m   =   1
        cm  =   0.01*m
        IN  =   0.0254*m
        # Fuerza:
        tonf=   1
        N   =   0.000101971621298*tonf
        kip =   0.45359237*tonf
        kgf =   0.001*tonf
        # Tiempo:
        s   =   1
        # Aceleracion:
        g   =   9.80665*m/(s**2)
    
    if sist == "s-cm-tonf":
        # Longitud:
        cm  =   1
        m   =   100*cm
        IN  =   2.54*cm
        # Fuerza:
        tonf=   1
        N   =   0.000101971621298*tonf
        kip =   0.45359237*tonf
        kgf =   0.001*tonf
        # Tiempo:
        s   =   1
        # Aceleracion:
        g   =   980.665*cm/(s**2)
        
    # UNIDADES DERIVADAS
    # Tiempo:
    MIN =   60*s
    hr  =   3600*s
    
    # Longitud:
    mm  =   0.1*cm
    ft  =   12*IN
    
    # Fuerza:
    lbf =   0.001*kip
    
    # Esfuerzo:
    ksi =   1*kip/(IN**2)
    Pa  =   1*N/(m**2)
    MPa =   10**6*Pa
    GPa =   10**9*Pa
    
    # Masa
    kg  =   0.101971621297793*(((s**2)/m)*kgf)
    lb  =   0.45359237*kg
    ton =   1000*kg
    
    # Constantes:
    PI  =   np.pi
    
    return m, cm, IN, kip, kgf, tonf, s, MIN, hr, mm, ft, lbf, ksi, Pa, MPa, GPa, g, kg, lb, ton, PI



# %% [04] RECORTE IMG

def recorte(img, scale_dpi, ax, ubic_x):
    # img:       Imagen a recortar.
    # scale_dpi: Relacion entre dpi de img y obj. axes.
    # ax:        Elemento axes donde disponer imagen.
    # ubic_x:    [0.00, 1.00] Def. ubicacion en x donde hacer recorte.
    #
    # Se recorta imagen. Se asumen que imagen es mas grande que ax.
    #
    #    ----------------------
    #    |      -----         |
    #    |     |     |        |
    #    |     | ax  |        | img
    #    |     |     |        |
    #    |     °-----         |
    #    ----------------------
    #    ubic_x^
    #
                                                   # Dim de imagen y obj. axes.
 	width_img, height_img = img.size                                            # Dim de imagen [px].
 	bbox                  = ax.get_window_extent()  	                        # Get the Bbox object representing the axes area.
 	width_ax, height_ax = bbox.width, bbox.height  	                            # Dim de ax [px].
 	                                                                            # Corta imagen.                  
 	crd_x_1   = int((ubic_x * (width_img - width_ax*scale_dpi)))                # Ubicación en x de recorte. Asegura que recorte este sobre figura.
 	crd_y_1   = int(0)
 	crd_x_2   = int((crd_x_1 + width_ax*scale_dpi))                             # Dim de recorte aseguran calce con dim. ax.
 	crd_y_2   = int((crd_y_1 + height_ax*scale_dpi))
 	img_crop  = img.crop((crd_x_1, crd_y_1, crd_x_2, crd_y_2))                  # crds de pixeles a dejar.
 	                                         # img recortada se inserta en ax.
 	ax.imshow(img_crop)                                                         # Display the cropped image on the target axs.
 	ax.set_axis_off()                                       # Util para ubic_x  # Oculta el marco de objeto axes. 
 	img.close()
 	img_crop.close()


# %%% [04-00] Reporte [*Opcional]
 	# width_img_crop, height_img_crop = img_crop.size                             # Dim de img.
  #   # Print para verificacion:
 	# n = 25                                                                      # N° "="  
 	# print('~'*n, "img", '~'*n)
 	# print('width_img =', round(width_img, 4), ' '*8, 'height_img =', round(height_img, 4))
 	# print('~'*n, "ax", '~'*n)
 	# print('width_ax =', round(width_ax, 4), ' '*8, 'height_ax =', round(height_ax, 4))
 	# print('Coordenadas corte IMG:', ' '*4,'[', crd_x_1, ', ', crd_y_1, ', ', crd_x_2, ', ', crd_y_2, ']')
 	# print('~'*n, "img_crop", '~'*n)
 	# print('width_img_crop =', round(width_img_crop, 4), ' '*8, 'height_img_crop =', round(height_img_crop, 4))
 	# print('\n'*3, '/'*60, '\n'*3)
          
 	return ax



# %% [05] RECORTE IMG 2D

def recorte2D(img, scale_dpi, ax, ubic_x, ubic_y):
    # img:       Imagen a recortar.
    # scale_dpi: Relacion entre dpi de img y obj. axes.
    # ax:        Elemento axes donde disponer imagen.
    # ubic_x:    [0.00, 1.00] Def. ubicacion en x donde hacer recorte.
    #
    # Se recorta imagen. Se asumen que imagen es mas grande que ax.
    #
    #        ----------------------
    #        |      -----         |
    #        |     |     |        |
    #        |     | ax  |        | img
    #        |     |     |        |
    # ubic_y>|     °-----         |
    #        ----------------------
    #    ubic_x^
    #
                                                   # Dim de imagen y obj. axes.
 	width_img, height_img = img.size                                            # Dim de imagen [px].
 	bbox                  = ax.get_window_extent()  	                        # Get the Bbox object representing the axes area.
 	width_ax, height_ax = bbox.width, bbox.height  	                            # Dim de ax [px].
 	                                                                            # Corta imagen.                  
 	crd_x_1   = int((ubic_x * (width_img - width_ax*scale_dpi)))                # Ubicación en x de recorte. Asegura que recorte este sobre figura.
 	crd_y_1   = int((ubic_y * (height_img - height_ax*scale_dpi)))
 	crd_x_2   = int((crd_x_1 + width_ax*scale_dpi))                             # Dim de recorte aseguran calce con dim. ax.
 	crd_y_2   = int((crd_y_1 + height_ax*scale_dpi))
 	img_crop  = img.crop((crd_x_1, crd_y_1, crd_x_2, crd_y_2))                  # crds de pixeles a dejar.
 	                                         # img recortada se inserta en ax.
 	ax.imshow(img_crop)                                                         # Display the cropped image on the target axs.
 	ax.set_axis_off()                                       # Util para ubic_x  # Oculta el marco de objeto axes. 
 	img.close()
 	img_crop.close()


# %%% [05-00] Reporte [*Opcional]
 	# width_img_crop, height_img_crop = img_crop.size                             # Dim de img.
  #   # Print para verificacion:
 	# n = 25                                                                      # N° "="  
 	# print('~'*n, "img", '~'*n)
 	# print('width_img =', round(width_img, 4), ' '*8, 'height_img =', round(height_img, 4))
 	# print('~'*n, "ax", '~'*n)
 	# print('width_ax =', round(width_ax, 4), ' '*8, 'height_ax =', round(height_ax, 4))
 	# print('Coordenadas corte IMG:', ' '*4,'[', crd_x_1, ', ', crd_y_1, ', ', crd_x_2, ', ', crd_y_2, ']')
 	# print('~'*n, "img_crop", '~'*n)
 	# print('width_img_crop =', round(width_img_crop, 4), ' '*8, 'height_img_crop =', round(height_img_crop, 4))
 	# print('\n'*3, '/'*60, '\n'*3)
          
 	return ax