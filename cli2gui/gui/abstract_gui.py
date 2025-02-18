"""Abstract base class for GUI wrappers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable

from cli2gui import models


class AbstractGUI(ABC):
	"""Abstract base class for GUI wrappers."""

	@abstractmethod
	def __init__(self) -> None:
		"""Abstract base class for GUI wrappers."""

	@abstractmethod
	def main(
		self,
		buildSpec: models.FullBuildSpec,
		quit_callback: Callable[[], None],
		run_callback: Callable[[dict[str, Any]], None],
	) -> None:
		"""Abstract method for the main function."""
		raise NotImplementedError
