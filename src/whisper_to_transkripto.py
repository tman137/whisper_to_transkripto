import argparse
import json
import math


def convert_timestamp(seconds):
    return "#{hours:02d}:{minutes:02d}:{seconds:02d}-{decimal:01d}#".format(
        hours=int(seconds // 3600),
        minutes=int((seconds % 3600) // 60),
        seconds=int(seconds % 60),
        decimal=int(round(math.floor((seconds % 1) * 10), 0)),
    )


def convert_line(input, end):
    return "{} {}".format(input.lstrip(), convert_timestamp(end))


def convert_whisper_to_transcripto(input_file, output_file):
    input = json.load(input_file)
    for segment in input["segments"]:
        output_file.write(
            "{}\n\n".format(convert_line(segment["text"], segment["end"]))
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert the json file that is output from whisper to the format required by transkripto"
    )
    parser.add_argument("input_file", type=argparse.FileType("r"))
    parser.add_argument("output_file", type=argparse.FileType("w+"))
    args = parser.parse_args()

    convert_whisper_to_transcripto(args.input_file, args.output_file)
