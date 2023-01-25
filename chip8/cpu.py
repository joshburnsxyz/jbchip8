from pyglet import pyglet
class cpu(pyglet.window.Window):
  def __init__(self):
    self.key_inputs = [0]*16
    self.display_buffer = [0]*32*64
    self.memory = [0]*16
    self.gpio = [0]*16
    self.sound_timer = 0
    self.delay_timer = 0
    self.index = 0
    self.program_counter = 0
    self.opcode = 0
    self.stack = []
    self.should_draw = False

  def on_key_press(self,symbol,modifiers):
    pass

  def on_key_release(self,symbol,modifiers):
    pass

  def main_loop(self, rom_path):
    self.initialize()
    self.load_rom(rom_path)
    while not self.has_exit:
      self.dispatch_events()
      self.cycle()
      self.draw()

  def initialize(self):
    # Clear memory
    self.clear()

    # Re-initialize values
    self.__init__()

    # Set Program Counter
    self.program_counter = 0x200

    i = 0
    while i < 80:
      # 80 Character font set loaded into memory
      self.memory[i] = self.fonts[i]
      i += 1

  def load_rom(self,rom_path):
    binary = open(rom_path, "rb")
    i = 0
    while i < len(binary):
      self.memory[i+0x200] = ord(binary[i])
      i += 1

  def cycle(self):
    self.opcode = self.memory[self.program_counter]

    # Process opcode
    self.vx = (self.opcode & 0x0f00) >> 8
    self.vy = (self.opcode & 0x00f0) >> 4

    self.program_counter += 2

    extracted_op = self.opcode & 0xf000
    try:
      self.funcmap[extracted_op]()
    except:
      print(f"Unknown instruction: {self.opcode}")

    # Check timers
    self.program_counter += 2
    if self.delay_timer > 0:
      self.delay_timer -= 1
    if self.sound_timer > 0:
      self.sound_timer -= 1
      if self.sound_timer == 0:
        # TODO: play sound

  def draw(self):
    pass
