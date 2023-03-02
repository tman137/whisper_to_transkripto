import pytest
import os
import filecmp
from src.whisper_to_transkripto import convert_whisper_to_transcripto


# TODO: try to remove line breaks when speaker not changing? -> adapt in ground truth file
def test_component():
    dir = os.path.dirname(__file__)
    input_file = os.path.join(dir, "input.txt")
    output_file = os.path.join(dir, "output.txt")
    convert_whisper_to_transcripto(input_file, output_file)
    assert filecmp.cmp(
        os.path.join(dir, "expected_output.txt"), output_file, shallow=False
    )
