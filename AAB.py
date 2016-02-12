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
		 	matrix = ButtonMatrixElement()
		 	matrix.name = 'Button Matrix'
		 	button_row = []
		 	for k in range(4):
		 	 	button = ButtonElement(False, 0, 0, k)
		 	 	button_row.append(button)
		 	matrix.add_row(button_row)
		 	shift_button = 'shift_button'
		 	self._selector = SelectorComponent(matrix, shift_button)
			self._selector.name = 'Main Selector'
			self.set_highlighting_session_component(self._selector.get_session_component())
			