import BGConsole
from BGConsole import BGC



BGC.write(BGC.__version__) #view module version
BGC.write(BGC.__github__) #view repository link

BGC.write('Hello World (Random color, random param)', BGC.random_param(), BGC.random_color())
BGC.write('Hello World (Red underlined text)', BGC.Param.UNDERLINE, BGC.Color.RED)

BGC.scan("Enter your age: ", BGC.Param.BOLD, BGC.Color.BLUE, BGC.random_param(), BGC.random_color())




