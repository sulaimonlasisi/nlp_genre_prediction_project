#file parses original csv file so lyrics are separate from title.

import argparse

parser = argparse.ArgumentParser(description='Receives input file')
parser.add_argument('input_file', help='input file with first lyrics line on same line as title')
args = parser.parse_args()

def separate_first_line(file):
  fw=open("../new_song_data.csv", "a+")
  with open(file, mode="r") as f:
    for line in f:
      html_idx = line.find(".html,\"")
      if html_idx > 1:
        line1 = line[:(html_idx+5)]+'\n'
        line2 = line[(html_idx+6):(html_idx+7)]+'\n'
        line3 = line[(html_idx+7):]
        fw.write(line1)
        fw.write(line2)
        fw.write(line3)
      else:
        fw.write(line)
separate_first_line(args.input_file)