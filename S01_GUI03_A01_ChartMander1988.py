# -*- coding: utf-8 -*-
"""
ACTUALIZACION:  2024-07-05
AUTOR:          Marcelo Ortiz Á.
SCRIPT:         S01_GUI03_A01_ChartMander1988.py
COMENTARIOS:    Interfaz gráfica de usuario para calculo de esfuerzo de confinamiento Mander 1988.
"""

# %% [00] INTRODUCTION
# GUI in Jupyter Notebook that generate the Mander 1988 confinement chart.

# There are developed the cart presented in "THEORETICAL STRESS-STRAIN MODEL FOR CON-
# FINED CONCRETE", By J. B. Mander, M. J. N. Priestley, and R. Park, 1988.

# To determine the confined concrete compressive strength f'cc, a constitutive 
# model involving a specified ultimate strength surface for multiaxial compre-
# ssive stresses is used in this model. The "five-parameter" multiaxial failure 
# surface described by William and Warnke (1975) is adopted, since it provides 
# excellent agreement with triaxial test data. The calculated ultimate strength 
# surface based on the triaxial tests of Schickert and Winkler (1977) is adopted 
# here. Details of the calculations have been given by Elwi and Murray (1979).

# Elwi, A. A., and Murray, D. W. (1979). "A 3D hypoelastic concrete constitutive 
# relationship."
# William, K. J., and Warnke, E. P. (1975). "Constitutive model for the triaxial 
# behavior of concrete."
# Schickert, G., and Winkler, H. (1979). "Results of tests concerning strength 
# and strain of concrete subjected to multiaxial compressive stresses." 

# %% [01] LIBRARIES

import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import HBox, VBox, Dropdown, IntText, Textarea, Output, Text
from IPython.display import display, Image, Video
import os
import shutil
import sys
import win32clipboard
from PIL import Image as PILImage
import io
import win32con

sys.path.insert(0, './C_GUI03_ChartMander1988')
import S01_GUI03_A02_WilliamWarnken5P as ww5p


# %% [02] INITIALIZATION
# Create directories for the GUI in case it doesn't exist.
def create_directory(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


# Directories to create
directories = ['C_GUI03_ChartMander1988/C_GUI03_ChartMander1988',
               'C_GUI03_ChartMander1988/C_GUI03_ChartMander1988/Charts']

# Create all directories
for dir_i in directories:
    create_directory(dir_i)
    

# %% [03] FUNCTIONS

# %%% [03-02] BUTTONS

# %%%% [03-02-00] UPDATE CHART
# Function to update the chart
def update_chart(change=None):
    # Clear the output window
    output_windows.value = ''
    
    # Clear the plot
    with out:
        out.clear_output()
    
    # Valores ejemplo de Mander, 1988
    # abs(fcc) > abs(fl2) > abs(fl3)
    fc0 = float(fco_input.value)
    fl2 = float(fl2_input.value)
    fl3 = float(fl3_input.value)
    
    # Verify that: abs(fcc) > abs(fl2) > abs(fl3)
    # If not, swap fl2 and fl3
    if abs(fl2) < abs(fl3):
        fl2_old = fl2
        fl3_old = fl3
        fl2 = fl3_old
        fl3 = fl2_old
    
    coef_largest  = int(fl2 / fc0 * 100000) / 100000
    coef_smallest = int(fl3 / fc0 * 100000) / 100000
    coef_fcc      = int(ww5p.solve_equation(fl2,fl3, fc0) * 100000) / 100000
    
    # Calculate fcc
    fcc = int(coef_fcc * fc0 * 100000) / 100000
    
    # Report
    report = f"""Input values:
fc0 = {fc0}
fl1 = {fl3}
fl2 = {fl2}

Coefficients:
fl1/fc0 = {coef_smallest}
fl2/fc0 = {coef_largest}

Output:
fcc/fc0 = {coef_fcc}

Confinement stress:
fcc = {fcc}

"THEORETICAL STRESS-STRAIN MODEL FOR CONFINED CONCRETE", By J. B. Mander, M. J. N. Priestley, and R. Park, 1988.
"""

    # Display coef_fcc
    fcc_input.value = str(fcc)
    
    # Update the output window
    output_windows.value = report
    
    # Make the plot
    ww5p.abaco_mander(fc0, fl3, fl2, "C_GUI03_ChartMander1988\C_GUI03_ChartMander1988\Test\Mander_1988.png", aux_graph=True, aux_CalculateData=False)
    
    # Display the plot
    with out:
        display(Image("C_GUI03_ChartMander1988\C_GUI03_ChartMander1988\Test\Mander_1988.png"))


# %%%% [03-02-03] SHOW INSTRUCTIONS
# Function to show instructions
def show_instructions(change=None):
    # Report
    report = f"""Instructions:
1. Enter fc0 value.
2. Enter fl2 value.
3. Enter fl3 value.
4. Press "Solve".

The output will show the value of fcc.
"""
    output_windows.value = report
    

# %%%% [03-02-03] COPY_IMAGE
# Function copy image to clipboard
def copy_image_to_clipboard(image_path):
    # Obtiene la ruta absoluta de la imagen
    abs_image_path = os.path.abspath(image_path)
    
    # Abre la imagen
    image = PILImage.open(abs_image_path)
    
    # Guarda la imagen en un buffer en formato BMP
    output = io.BytesIO()
    image.convert("RGB").save(output, 'BMP')
    data = output.getvalue()[14:]  # Elimina los primeros 14 bytes del encabezado BMP
    
    # Abre el portapapeles y limpia su contenido
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    
    # Coloca la imagen en el portapapeles
    win32clipboard.SetClipboardData(win32con.CF_DIB, data)
    
    # Cierra el portapapeles
    win32clipboard.CloseClipboard()

# Function to copy image from GUI
def copy_image(change=None):
    # Obtain url from graph_output
    url_image = 'C_GUI03_ChartMander1988/C_GUI03_ChartMander1988/Test/Mander_1988.png'
    
    # Copy image to clipboard
    if url_image != "":
        try:
            copy_image_to_clipboard(url_image)
        except:
            pass


# %% [04] WIDGETS
# Dimension para ingresar datos numericos.
layout_var_1 = widgets.Layout(width='200px')


# %%% [04-01] Text
# Interactive widgets for calculate the compress confinement stress.
fco_input = Text(value='250.00', description='fco:', continuous_update=False, layout=layout_var_1)
fl2_input = Text(value='42.53', description='fl_2:', continuous_update=False, layout=layout_var_1)
fl3_input = Text(value='22.42', description='fl_3:', continuous_update=False, layout=layout_var_1)
fcc_input = Text(value='', description='fcc:', disabled = True, continuous_update=False, layout=layout_var_1)


# %%% [04-02] ZIP WDGT
# Define a VBox to zip widgets associated with the parameters of material strength.
strength_widgets = VBox(layout=widgets.Layout(width='240px', height='660px', padding='0px'))


# %%% [04-05] BUTTONS
# Button to see instructions
instructions_button_layout = widgets.Layout(width='215px', margin='0 0 0 5px')
instructions_button = widgets.Button(description='Show Instructions', layout=instructions_button_layout)
instructions_button.on_click(show_instructions)
# Button to solve the confinement stress.
solve_fcc_button_layout = widgets.Layout(width='102px', height= '27px', margin='2px 0 0 7px')
solve_fcc_button = widgets.Button(description='Solve', layout=solve_fcc_button_layout)
solve_fcc_button.disabled = False
solve_fcc_button.on_click(update_chart)
# Button to copy image to clipboard
copy_image_button_layout = widgets.Layout(width='102px', height='27px', margin='2px 0 0 4px')
copy_image_button = widgets.Button(description='Copy Image', layout=copy_image_button_layout)
copy_image_button.on_click(copy_image)


# %%% [04-06] TEXTAREA
# Display Output Window
output_windows = Textarea(value='', layout=widgets.Layout(width='225px', height='360px'))

# %%% [04-07] OUTPUT
# Output widget to contain the plot
layout_rigth = widgets.Layout(width='870px', height='664px')
out = Output(layout=layout_rigth)  # Output


# %%% [04-08] MATH IN WIDGETS & DYNAMIC GRAPHICS
# Widgets in the GUI
Text_Widgets_list = [fco_input, fl2_input, fl3_input]

# Helper function to observe the widgets with mathematical expressions 
def observe_widget(widget_x):
    def handler(change):
        # Check if 'change['new']' is a mathematical expression or already a number
        try:
            # Attempt to convert 'change['new']' to float
            new_value = float(change['new'])
            # If successful, it's already a number, so no need to eval
            is_number = True
        except ValueError:
            # If conversion fails, it's not a simple number
            is_number = False
        
        # Only graph if 'change['new']' is already a number:
        if is_number:
                update_chart()
        # Only evaluate if 'change['new']' is not already a number
        if not is_number:
            widget_x.value = str(eval(change['new']))
            
    widget_x.observe(handler, names='value')
    

# Apply the observation to all Text widgets
for widget in Text_Widgets_list:
    observe_widget(widget)


# %% [05] LAYOUT
# Layout of the interface

# %%% [05-00] TEXT
title = widgets.HTML(
    value="<b style='text-align: center; display: block;'>f<sub>cc</sub> - Mander 1988</b>",
    layout=widgets.Layout(
        width='228px',
        display="flex",
        justify_content="center",
        margin="0px 0px 9px 0px"
    )
)
title.style.font_size = '22px'
text_strength = widgets.HTML(value="Define Strength:", layout=widgets.Layout(margin="0px 0 0 2px"))
text_strength.style.font_size = '14px'
text_output_window = widgets.HTML(value="Output Window:", layout=widgets.Layout(margin="6px 0 0 2px"))
text_output_window.style.font_size = '14px'
text3 = widgets.HTML(value="<i>GUI developed by M. Ortiz.<i>", layout=widgets.Layout(width='700px', margin="0 0 0 2px"))
text3.style.font_size = '14px'


# %%% [05-01] INTERFACE
buttons_line = HBox([solve_fcc_button, copy_image_button])
strength_inputs_list = [title, instructions_button, text_strength, fco_input, fl2_input, fl3_input, 
                    fcc_input, buttons_line, text_output_window, output_windows]
strength_widgets.children = strength_inputs_list
interface = HBox([strength_widgets, out])
interface_B = VBox([interface, text3])
display(interface_B)


# %% [06] DEVELOPER

# Layout programer
aux_show_layout_programmer = False
if aux_show_layout_programmer:
    import inspect
    programer_output = Textarea(value='', layout=widgets.Layout(width='1072px', height='380px'))  # 
    display(programer_output)

    # # Function to display in GUI variable in certain line of code
    def GUI_info(Text_in_string, line_of_code,  variable):
        """
        Function to display in GUI certain line of code
        :param Text_in_string: Variable in string
        :param line_of_code: Line of code
        :param variable: Variable to display
        :return: None
        
        Calling using:
        current_line = inspect.currentframe().f_lineno
        GUI_info('load_args = ', current_line, load_args)
        """
        template_message = f"""
    Line of Code: {line_of_code}
    {Text_in_string}
    """
        template_close_message = f"""
    --------------------------------------------
    """
        programer_output.value = programer_output.value + template_message + str(variable) + template_close_message

