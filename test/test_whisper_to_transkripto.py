import pytest
import os
import filecmp
from src.whisper_to_transkripto import (
    convert_whisper_to_transcripto,
    convert_line,
    convert_timestamp,
)


# TODO: try to remove line breaks when speaker not changing? -> adapt in ground truth file
def test_component():
    dir = os.path.dirname(__file__)
    input_path = os.path.join(dir, "input.json")
    output_path = os.path.join(dir, "output.txt")
    with open(input_path, "r") as input_file, open(output_path, "w+") as output_file:
        convert_whisper_to_transcripto(input_file, output_file)

    expected_output_path = os.path.join(dir, "expected_output.txt")
    same_content = filecmp.cmp(expected_output_path, output_path, shallow=False)
    assert same_content


def test_convert_line():
    assert (
        convert_line("in the end it doesn't even matter", 27.89)
        == "in the end it doesn't even matter #00:00:27-8#"
    )


def test_convert_line_beginning_with_space():
    assert (
        convert_line(" in the end it doesn't even matter", 27.89)
        == "in the end it doesn't even matter #00:00:27-8#"
    )


def test_convert_timestamp():
    assert convert_timestamp(27.89) == "#00:00:27-8#"


def test_convert_timestamp_with_hours_and_minutes():
    assert convert_timestamp(99089.345) == "#27:31:29-3#"
