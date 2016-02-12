from _Framework.SessionComponent import SessionComponent
from _Framework.ModeSelectorComponent import ModeSelectorComponent

class SelectorComponent(ModeSelectorComponent):
	
	def __init__(self, matrix, mode_buttons):
		# raise isinstance(matrix, ButtonMatrixElement) or AssertionError
		# raise matrix.width() == 4 and matrix.height() == 1 or AssertionError
		# raise isinstance(shift_button, ButtonElement) or AssertionError
		ModeSelectorComponent.__init__(self)
		self._session = SessionComponent(matrix.width(), matrix.height())
		self._matrix = matrix
		self._mode_buttons = mode_buttons
		self._setup_session()

	def disconnect(self):
		self._session = None
		self._matrix = None
		self._shift_button = None
		ModeSelectorComponent.disconnect(self)

	def get_session_component(self):
		return self._session

	def set_mode_buttons(self, buttons):
		for button in self._mode_buttons
			button.remove_value_listener(self._mode_value)
		self._modes_buttons - []
		if buttons != None:
			for button in buttons:
				self._modes_buttons.append(button)
				button.add_value_listener(self._mode_value, identify_sender)

	def number_of_modes(self):
		return 3

	def set_mode(self, mode):
		self._mode_index = (self._mode_index != mode or mode == 2) and mode
		self.update()

	def update(self):
        super(MainSelectorComponent, self).update()

	def _setup_session(self):
		for scene_index in range(1):
			scene = self._session.scene(scene_index)
			for track_index in range(4):
				button = self._matrix.get_button(track_index, scene_index)
				scene.clip_slot(track_index).set_launch_button(button)


	

