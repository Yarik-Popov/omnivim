from common.mode import Mode, ModeCallback


class ModeManager:
    def __init__(self, mode: Mode, set_callbacks: list[ModeCallback]) -> None:
        self._mode = mode
        self._set_callbacks = set_callbacks

    def _notify_subscribers(self) -> None:
        for callback in self._set_callbacks:
            callback(self._mode)


    def set_mode(self, mode: Mode) -> None:
        self._mode = mode
        self._notify_subscribers()

    def get_mode(self) -> Mode:
        return self._mode


