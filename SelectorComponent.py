from _Framework.SessionComponent import SessionComponent
from _Framework.ModeSelectorComponent import ModeSelectorComponent


class SelectorComponent(ModeSelectorComponent):
	
	def __init__(self, matrix, shift_button):
		raise isinstance(matrix, ButtonMatrixElement) or AssertionError
		raise matrix.width() == 6 and matrix.height() == 1 or AssertionError
		raise isinstance(shift_button, ButtonElement) or AssertionError
		ModeSelectorComponent.__init__(self)
		self._session = SessionComponent(matrix.width(), matrix.height())
		self._matrix = matrix
		self._shift_button = shift_button
		self._setup_session()

	def get_session_component(self):
		return self._session

	def _setup_session(self):
		for scene_index in range(1):
			scene = self._session.scene(scene_index)
			for track_index in range(4):
				button = self._matrix.get_button(track_index, scene_index)
				scene.clip_slot(track_index).set_launch_button(button)