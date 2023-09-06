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
                                    self.url.text),

    if pet_category:
      self.image_1.source = self.url.text
      self.image_1.visible=True
      self.species_label.visible = True
      self.species_label.text = pet_category.capitalize()
      self.chatlabel.text = "ChatGPT: Ask me more if you have any questions?"
      # if pet_category == "Cat":
      #   self.chatlabel.text = "ChatCat: Cats are domesticated carnivorous mammals known for their playful behavior, independent nature, and strong bond with humans throughout history. Ask me more if you have more questions!"
      # else: 
      #   self.chatlabel.text = "ChatCat: Dogs are loyal and social domesticated animals that belong to the Canidae family, characterized by their diverse breeds, wide range of sizes and appearances, and their roles as companions, working animals, and service animals. Ask me more if you have more questions!"
      self.chatlabel.visible=True
      self.chat_input.visible=True
      self.chatbutton.visible=True
      
    get_image = anvil.server.call('yolo_image',
                                    self.url.text)
    if get_image:
      self.image_3.source = get_image
      self.image_3.visible = 
    
      
  def chatbutton_click(self, **event_args):
    """This method is called when the button is clicked"""
    chat_output = anvil.server.call('ask_question',
                                      self.chat_input.text)
    self.chat_output_label.visible = True
    self.chat_output_label.text = chat_output
      
    pass








