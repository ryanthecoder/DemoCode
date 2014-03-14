import Replicator2Connection
import CraneConnection

printer = Replicator2Connection('/dev/ttyACM0', simpleCar.x3g)
crane = CraneConnection('/dev/ttyUSB0',toolFile.tool)
listeners = crane.getListeners()
for l in listeners :
	printer.addListener(l)
printer.start()
