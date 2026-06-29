# This class represent of server in Pyhon

class MinecraftServer:
	def __init__(self, serverName, serverEdition, serverRoot_path, serverExecuteable, serverVersion, serverProperties, serverWorld):
		serverName = self.serverName
		serverEdition = self.serverEdition
		serverRoot_path = self.serverRoot_path
		serverExecuteable = self.serverExecuteable
		serverProperties = self.serverProperties
		serverWorld = self.serverWorld
		serverStatus = "stop"
	
	def status(self):
	  return self.serverStatus



MinecraftServer
│
├── name
├── edition
├── root_path
├── executable
├── version
├── properties
├── worlds
└── running