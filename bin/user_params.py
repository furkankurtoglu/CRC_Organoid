 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='organoid_cell_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.organoid_cell_apoptosis_rate = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name3 = Button(description='organoid_cell_r01', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.organoid_cell_r01 = FloatText(
          value=0.005,
          step=0.001,
          style=style, layout=widget_layout)

        param_name4 = Button(description='organoid_cell_r10', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.organoid_cell_r10 = FloatText(
          value=0.0015,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='organoid_cell_G01S_thr', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.organoid_cell_G01S_thr = FloatText(
          value=8.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='organoid_cell_relative_adhesion', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.organoid_cell_relative_adhesion = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        param_name7 = Button(description='fibroblast_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.fibroblast_apoptosis_rate = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name8 = Button(description='fibroblast_r01', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.fibroblast_r01 = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name9 = Button(description='fibroblast_r10', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.fibroblast_r10 = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name10 = Button(description='fibroblast_relative_adhesion', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.fibroblast_relative_adhesion = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        param_name11 = Button(description='initial_tumor_radius', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.initial_tumor_radius = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name12 = Button(description='organoid_distance', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.organoid_distance = FloatText(
          value=930,
          step=10,
          style=style, layout=widget_layout)

        param_name13 = Button(description='apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.apoptosis_rate = FloatText(
          value=9e99,
          step=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
          style=style, layout=widget_layout)

        param_name14 = Button(description='cell_default_inital_energy', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.cell_default_inital_energy = FloatText(
          value=7.01,
          step=0.1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='cell_default_cycle_energy_threshold', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.cell_default_cycle_energy_threshold = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='cell_default_death_energy_threshold', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.cell_default_death_energy_threshold = FloatText(
          value=6,
          step=0.1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='k_aerobe', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.k_aerobe = FloatText(
          value=0.00000001,
          step=1e-09,
          style=style, layout=widget_layout)

        param_name18 = Button(description='k_anaerobe', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.k_anaerobe = FloatText(
          value=0.00000001,
          step=1e-09,
          style=style, layout=widget_layout)

        param_name19 = Button(description='k_glut', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.k_glut = FloatText(
          value=0.00000001,
          step=1e-09,
          style=style, layout=widget_layout)

        param_name20 = Button(description='k_usage', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.k_usage = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name21 = Button(description='alpha', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.alpha = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name22 = Button(description='beta', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.beta = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name23 = Button(description='gamma', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.gamma = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='au', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'

        desc_button1 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.organoid_cell_apoptosis_rate, units_button2, desc_button2] 
        row3 = [param_name3, self.organoid_cell_r01, units_button3, desc_button3] 
        row4 = [param_name4, self.organoid_cell_r10, units_button4, desc_button4] 
        row5 = [param_name5, self.organoid_cell_G01S_thr, units_button5, desc_button5] 
        row6 = [param_name6, self.organoid_cell_relative_adhesion, units_button6, desc_button6] 
        row7 = [param_name7, self.fibroblast_apoptosis_rate, units_button7, desc_button7] 
        row8 = [param_name8, self.fibroblast_r01, units_button8, desc_button8] 
        row9 = [param_name9, self.fibroblast_r10, units_button9, desc_button9] 
        row10 = [param_name10, self.fibroblast_relative_adhesion, units_button10, desc_button10] 
        row11 = [param_name11, self.initial_tumor_radius, units_button11, desc_button11] 
        row12 = [param_name12, self.organoid_distance, units_button12, desc_button12] 
        row13 = [param_name13, self.apoptosis_rate, units_button13, desc_button13] 
        row14 = [param_name14, self.cell_default_inital_energy, units_button14, desc_button14] 
        row15 = [param_name15, self.cell_default_cycle_energy_threshold, units_button15, desc_button15] 
        row16 = [param_name16, self.cell_default_death_energy_threshold, units_button16, desc_button16] 
        row17 = [param_name17, self.k_aerobe, units_button17, desc_button17] 
        row18 = [param_name18, self.k_anaerobe, units_button18, desc_button18] 
        row19 = [param_name19, self.k_glut, units_button19, desc_button19] 
        row20 = [param_name20, self.k_usage, units_button20, desc_button20] 
        row21 = [param_name21, self.alpha, units_button21, desc_button21] 
        row22 = [param_name22, self.beta, units_button22, desc_button22] 
        row23 = [param_name23, self.gamma, units_button23, desc_button23] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.organoid_cell_apoptosis_rate.value = float(uep.find('.//organoid_cell_apoptosis_rate').text)
        self.organoid_cell_r01.value = float(uep.find('.//organoid_cell_r01').text)
        self.organoid_cell_r10.value = float(uep.find('.//organoid_cell_r10').text)
        self.organoid_cell_G01S_thr.value = float(uep.find('.//organoid_cell_G01S_thr').text)
        self.organoid_cell_relative_adhesion.value = float(uep.find('.//organoid_cell_relative_adhesion').text)
        self.fibroblast_apoptosis_rate.value = float(uep.find('.//fibroblast_apoptosis_rate').text)
        self.fibroblast_r01.value = float(uep.find('.//fibroblast_r01').text)
        self.fibroblast_r10.value = float(uep.find('.//fibroblast_r10').text)
        self.fibroblast_relative_adhesion.value = float(uep.find('.//fibroblast_relative_adhesion').text)
        self.initial_tumor_radius.value = float(uep.find('.//initial_tumor_radius').text)
        self.organoid_distance.value = float(uep.find('.//organoid_distance').text)
        self.apoptosis_rate.value = float(uep.find('.//apoptosis_rate').text)
        self.cell_default_inital_energy.value = float(uep.find('.//cell_default_inital_energy').text)
        self.cell_default_cycle_energy_threshold.value = float(uep.find('.//cell_default_cycle_energy_threshold').text)
        self.cell_default_death_energy_threshold.value = float(uep.find('.//cell_default_death_energy_threshold').text)
        self.k_aerobe.value = float(uep.find('.//k_aerobe').text)
        self.k_anaerobe.value = float(uep.find('.//k_anaerobe').text)
        self.k_glut.value = float(uep.find('.//k_glut').text)
        self.k_usage.value = float(uep.find('.//k_usage').text)
        self.alpha.value = float(uep.find('.//alpha').text)
        self.beta.value = float(uep.find('.//beta').text)
        self.gamma.value = float(uep.find('.//gamma').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//organoid_cell_apoptosis_rate').text = str(self.organoid_cell_apoptosis_rate.value)
        uep.find('.//organoid_cell_r01').text = str(self.organoid_cell_r01.value)
        uep.find('.//organoid_cell_r10').text = str(self.organoid_cell_r10.value)
        uep.find('.//organoid_cell_G01S_thr').text = str(self.organoid_cell_G01S_thr.value)
        uep.find('.//organoid_cell_relative_adhesion').text = str(self.organoid_cell_relative_adhesion.value)
        uep.find('.//fibroblast_apoptosis_rate').text = str(self.fibroblast_apoptosis_rate.value)
        uep.find('.//fibroblast_r01').text = str(self.fibroblast_r01.value)
        uep.find('.//fibroblast_r10').text = str(self.fibroblast_r10.value)
        uep.find('.//fibroblast_relative_adhesion').text = str(self.fibroblast_relative_adhesion.value)
        uep.find('.//initial_tumor_radius').text = str(self.initial_tumor_radius.value)
        uep.find('.//organoid_distance').text = str(self.organoid_distance.value)
        uep.find('.//apoptosis_rate').text = str(self.apoptosis_rate.value)
        uep.find('.//cell_default_inital_energy').text = str(self.cell_default_inital_energy.value)
        uep.find('.//cell_default_cycle_energy_threshold').text = str(self.cell_default_cycle_energy_threshold.value)
        uep.find('.//cell_default_death_energy_threshold').text = str(self.cell_default_death_energy_threshold.value)
        uep.find('.//k_aerobe').text = str(self.k_aerobe.value)
        uep.find('.//k_anaerobe').text = str(self.k_anaerobe.value)
        uep.find('.//k_glut').text = str(self.k_glut.value)
        uep.find('.//k_usage').text = str(self.k_usage.value)
        uep.find('.//alpha').text = str(self.alpha.value)
        uep.find('.//beta').text = str(self.beta.value)
        uep.find('.//gamma').text = str(self.gamma.value)
