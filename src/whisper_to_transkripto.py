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


def convert_line(input, time_point):
    return "{} {}".format(input.lstrip(), convert_timestamp(time_point))


def convert_whisper_to_transcripto(input_file, output_file):
    input = json.load(input_file)
    segments = input["segments"]
    number_of_segments = len(segments)
    print(number_of_segments)
    for i in range(number_of_segments):
        text = segments[i]["text"]
        time_point = (
            segments[i + 1]["start"]
            if (i < number_of_segments - 1)
            else segments[i]["end"]
        )
        output_file.write("{}\n\n".format(convert_line(text, time_point)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert the json file that is output from whisper to the format required by transkripto"
    )
    parser.add_argument("input_file", type=argparse.FileType("r"))
    parser.add_argument("output_file", type=argparse.FileType("w+"))
    args = parser.parse_args()

    convert_whisper_to_transcripto(args.input_file, args.output_file)
