from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.SessionComponent import SessionComponent
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from SelectorComponent import SelectorComponent

class AAB(ControlSurface):

	def __init__(self, c_instance):
		ControlSurface.__init__(self, c_instance)
		with self.component_guard():
			is_momentary = True
			is_not_momentary = False
			self._suppress_send_midi = True
			self._suppress_session_highlight = True
		 	matrix = ButtonMatrixElement()
		 	matrix.name = 'Button Matrix'
		 	button_row = []
		 	for k in range(4):
		 	 	button = ButtonElement(is_not_momentary, 0, 0, k)
		 	 	button_row.append(button)
		 	matrix.add_row(button_row)
		 	mode_buttons = []
		 	for k in range(3):
		 		mode_button = ButtonElement(is_not_momentary, 0, 1, k)
		 		mode_buttons.append(mode_button)
		 	self._selector = SelectorComponent(matrix, mode_buttons)
			self._selector.name = 'Main Selector'
			self.set_highlighting_session_component(self._selector.get_session_component())
			self._suppress_session_highlight = False

	# def disconnect(self):
	# 	self._suppress_send_midi = True
	# 	self._selector = None
	# 	ControlSurface.disconnect(self)
	#   self._suppress_send_midi = False
