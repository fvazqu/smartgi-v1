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
    pet_category = anvil.server.call('predict_pet',
                                    self.url.text)

    if pet_category:
      self.species_label.visible = True
      self.species_label.text = "The species is a " + self.color.text + " " + pet_category.capitalize()   
    pass

