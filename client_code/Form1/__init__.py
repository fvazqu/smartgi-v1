from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def categorize_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    try:
        
        self.species_label.visible = True
        self.species_label.text = "Predicting..."

        pet_category = anvil.server.call('predict_pet',
                                         self.url.txt,
                                         self.color.txt)
        
        color = self.color.txt
        if pet_category:
            self.species_label.text = f"The pet is a {pet_category.capitalize()} with color {color.capitalize()}"
        else:
            self.species_label.text = "Prediction failed"
    except Exception as e:
        self.species_label.text = "Error: " + str(e)
    pass

