"""Tests an advanced parser"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

THISDIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THISDIR.parent.parent))
from cli2gui import Cli2Gui


def handle(args: argparse.Namespace) -> None:
	"""Handle the args."""
	print(args)


@Cli2Gui(
	run_function=handle,
	menu={
		"File": f"{THISDIR}/file.md",
		"Another File": f"{THISDIR}/another_file.md",
	},
	gui="pysimplegui",
)
def cli() -> None:
	"""Cli entrypoint."""
	parser = argparse.ArgumentParser("Simple Parser")

	# Positional and file
	parser.add_argument("positional", help="positional arg")
	parser.add_argument(
		"positional-file", type=argparse.FileType("r"), help="positional arg for a file"
	)
	parser.add_argument("--optional", help="optional arg")

	# Store true, false, store, count, choices
	parser.add_argument("--store-true", action="store_true", help="optional arg store true")
	parser.add_argument("--store-false", action="store_false", help="optional arg store false")
	parser.add_argument("--store", action="store", help="optional arg store")
	parser.add_argument("--count", action="count", help="optional arg count")
	parser.add_argument(
		"--choices",
		action="store",
		choices=["choice1", "choice2"],
		help="optional arg store with choices",
	)
	parser.add_argument(
		"--somefile",
		type=argparse.FileType("r"),
		required=False,
	)

	group = parser.add_argument_group(
		"choose one of the following", "use the following arguments to change the look of the image"
	)
	mxg = group.add_mutually_exclusive_group()

	mxg.add_argument("--mxg-true", action="store_true", help="mutually exclusive arg store true")
	mxg.add_argument("--mxg-false", action="store_false", help="mutually exclusive arg store false")
	mxg.add_argument("--mxg", action="store", help="mutually exclusive arg store")
	mxg.add_argument("--mxg-count", action="count", help="mutually exclusive arg count")
	mxg.add_argument(
		"--mxg-choices",
		action="store",
		choices=["choice1", "choice2"],
		help="mutually exclusive arg store with choices",
	)

	args = parser.parse_args()

	handle(args)


cli()
