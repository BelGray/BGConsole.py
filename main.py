import BGConsole
from BGConsole import BGC

BGC.write("RED TEXT", BGC.Param.UNDERLINE, BGC.Color.RED) #Writes red underlined text using method write() from BGConsole
print(BGC.Tool.OFF + BGC.Param.UNDERLINE + BGC.Color.RED + "RED TEXT" + BGC.Tool.OFF) #Writes red underlined text using method print()

BGC.write(BGC.__version__) #view module version
BGC.write(BGC.__github__) #view repository link

BGC.write("Random COLOR and random PARAM", BGC.Param.random(), BGC.Color.random()) #Writes random color and random parameter text

BGC.scan("CRIMSON LABEL", BGC.Param.BOLD, BGC.Color.CRIMSON, BGC.Param.UNDERLINE, BGC.Color.PINK) #Method scan() from BGConsole
input(BGC.Tool.OFF + BGC.Param.BOLD + BGC.Color.CRIMSON + "CRIMSON LABEL" + BGC.Tool.OFF + BGC.Param.UNDERLINE + BGC.Color.PINK) #Method input()



