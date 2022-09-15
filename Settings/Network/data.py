# Standard Imports
from enum import Enum
from dataclasses import dataclass

# External Imports

# Library Imports



LoginAttemptLimit: int = 0

SequencePacketMode: bool = True

AccountKeepConnectionAlive: bool = True


class ChannelType(Enum):
	Authentication = 'Auth'
	Game = 'Game'


class State(Enum):
	Unknown = '...'
	Available = 'OK'
	Normal = 'Normal'
	Busy = 'Busy'
	Full = 'Full'


@dataclass(frozen=True, slots=True, order=True)
class ChannelData:
	
	name: str
	type: ChannelType
	tcp_port: int
	udp_port: int


@dataclass(frozen=True, slots=True, order=True)
class ServerData:
	
	name: str
	channels: list[ChannelData]
	tcp_port: int
	udp_port: int
	mark_tcp_port: int
	mark_udp_port: int
	ipv4: str = '127.0.0.1'
	ipv6: str = '0:0:0:0:0:0:0:1'
	
	def PrintServerInformation(self):
		print(f'')
		print(f'Server: {self.name}')
		print(f'IP and Port Settings:')
		print(f' - IPv4: {self.ipv4} | IPv6: {self.ipv4}')
		print(f' - TCP: {self.tcp_port} | UDP: {self.udp_port}')
		print(f' - MarkTCP: {self.mark_tcp_port} | MarkUDP: {self.mark_udp_port}')
		print(f'Channels: {len(self.channels)}')
		
		idx = 0
		for channel in self.channels:
			idx += 1
			print(f' - {idx} | {channel.name} \t| TCP: {channel.tcp_port} | UDP {channel.udp_port}')
		
		print('')

