import argparse
from . import cpu

parser = argparse.ArgumentParser(
  prog = "chip8",
  description = "chip8 emulator",
  epilog = "chip8 emulator by Josh Burns"
)

parser.add_argument('filename')

def run():
  args = parser.parse_args()
  f = cpu.cpu(640,320)
  f.main(args.filename)

