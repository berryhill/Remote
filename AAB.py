from __future__ import with_statement

import Live
import time

from _Framework.ControlSurface import ControlSurface
from _Framework.SessionComponent import SessionComponent
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement

class AAB(ControlSurface):
	def __init__(self, c_instance):
		ControlSurface.__init__(self, c_instance)
		with self.component_guard():
			self.session = SessionComponent(4, 4)
			self.session.set_offsets(0, 0)
			self.session.scene(0).clip_slot(0).set_launch_button(ButtonElement(False, 
																0, 6, 2))
			self.session.scene(0).clip_slot(1).set_launch_button(ButtonElement(False, 
																0, 6, 0))

			self.set_highlighting_session_component(self.session)

			print "Hello WOrld"

			# self._send_midi((240, 126, 0, 6, 1, 247))

			# button = ButtonElement(False, 0, 0, 0)
			# button.send_value(LED_OFF, True)

			# matrix = ButtonMatrixElement()
			# button_row = []
			# for k in range(6):
			# 	button_row.append(ButtonElement(False, MIDI_NOTE_TYPE, 0, k))
			# matrix.add_row(button_row)

