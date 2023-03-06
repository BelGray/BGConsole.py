import random
class BGC:
  __version__ = "1.0.0"
  __github__ = "https://github.com/BelGray/BGConsole.py"
  
  class Color:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RED = "\033[31m"
    GREEN = '\033[92m'
    MUSTARD = '\033[93m'
    CRIMSON = '\033[91m'
    YELLOW = '\033[33m'
    PURPLE = "\033[35m"
    BLACK = "\033[30m"
    WHITE = "\033[37m"
    list = ['\033[95m', '\033[94m', '\033[96m', "\033[31m", '\033[92m', '\033[93m', '\033[91m', '\033[33m', "\033[35m", "\033[30m", "\033[37m", '']

    def random():
      random_color = random.choice(BGC.Color.list)
      return random_color

  class Param:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    list = ['\033[1m', '\033[4m', '']

    def random():
      random_param = random.choice(BGC.Param.list)
      return random_param

  class Tool:
    EMPTY = ""
    OFF = '\033[0m'


    
  def write(text: str, param: str = None, color: str = None):
    OFF = '\033[0m'
    if param == None:
      param = ""
    if color == None:
      color = ""
    if param not in BGC.Param.list:
      return print(BGC.Color.RED + """Error message from BGConsole.
-------
Method: write(text, param, color)
-------
Message:
The text parameters must belong to the "Param" class. For example:
BGC.Param.UNDERLINE""" + OFF)
    if color not in BGC.Color.list:
      return print(BGC.Color.RED + """Error message from BGConsole.
-------
Method: write(text, param, color)
-------
Message:
The text colors must belong to the "Color" class. For example:
BGC.Color.GREEN""" + OFF)

    print(OFF + param + color + str(text) + OFF)
    return OFF + param + color + str(text) + OFF


  
  def clear_last_line():
      print ("\033[A                                             \033[A")



  
  def scan(label: str, label_param: str = None, label_color: str = None, input_text_param: str = None, input_text_color: str = None):
    OFF = '\033[0m'
    if label == None:
      label = ""
    if label_color == None:
      label_color = ""
    if input_text_color == None:
      input_text_color = ""
    if label_param == None:
      label_param = ""
    if input_text_param == None:
      input_text_param = ""

    if label_param not in BGC.Param.list or input_text_param not in BGC.Param.list:
        
        return print(BGC.Color.RED + """Error message from BGConsole.
-------
Method: scan(label, label_param, label_color, input_text_param, input_text_color)
-------
Message:
The text parameters must belong to the "Param" class. For example:
BGC.Param.UNDERLINE""" + OFF)
    if label_color not in BGC.Color.list or input_text_color not in BGC.Color.list:
        
        return print(BGC.Color.RED + """Error message from BGConsole.
-------
Method: scan(label, label_param, label_color, input_text_param, input_text_color)
-------
Message:
The text colors must belong to the "Color" class. For example:
BGC.Color.GREEN""" + OFF)
    
    return str(input(OFF + label_param + label_color + str(label) + OFF + input_text_param + input_text_color))    