import ipywidgets as widgets
import pandas as pd
import datetime
import locale

def create_slider():
    # Aplicando locale para portugues
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    
    # Período dos dados (jan 2019 - mai 2024)
    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2024, 6, 1)
    
    #dates = [start_date + datetime.timedelta(days=30 * i) for i in range((end_date.year - start_date.year) * 12 + (end_date.month - start_date.month) + 1)]
    dates = pd.date_range(start=start_date, end=end_date, freq='MS').date.tolist() 
    options = [(i.strftime('%b %Y').capitalize(), i) for i in dates]

    preset_start_date = datetime.date(2019, 1, 1)  # Change to your desired start date
    preset_end_date = datetime.date(2024, 6, 1)   # Change to your desired end date
    
    # Get indices for preset start and end dates
    start_index = dates.index(preset_start_date)
    end_index = dates.index(preset_end_date)

    return widgets.SelectionRangeSlider(
        options=options,
        index=(start_index, end_index),  # Set to the preset start and end indices
        description='Período',
        disabled=False,
        layout={'width': '1000px'}
    )

def create_radio_buttons(options, description):
    return widgets.RadioButtons(
        options=options,
        value=options[0],
        description=description,
    )

def create_dropdowns(options, description, layout=None, value=None):
    if layout is None:
        layout = widgets.Layout()

    if value is None:
        value = None
    
    return widgets.Dropdown(
        options=options,
        value=value,
        description=description,
        layout = layout,
    )

def create_buttons(description):
    return widgets.Button(
        description=description,
    )

def create_labels(value, layout):
    return widgets.Label(
        value = value,
        layout = layout,
    )