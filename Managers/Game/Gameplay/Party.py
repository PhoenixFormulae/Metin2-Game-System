## System Imports

## Embedder Imports
from junctions import player
from junctions import network

## Application Imports
from Settings.Game.Gameplay.data import PartyInviteDistance

## Library Imports
from FSM.enums import PhaseState
from FSM.decorators import register_state
from System.Manager.base import BaseManager


@register_state(PhaseState.Game)
class PartyManager(BaseManager):
	
	__incoming_invites: dict[int, str] = {}
	__incoming_requests: list[int] = []
	
	__party: dict[int, int | str] = {}
	__party_distribution: int = 0
	
	__party_can_heal: bool = False
	
	@classmethod
	def Ready(cls):
		pass
	
	## Embedder Calls
	def RecvPartyInviteQuestion(self, leader: int, name: str):
		self.__incoming_invites[leader] = name
	
	@classmethod
	def AnswerPartyRequest(cls, leader: int, answer: bool):
		if answer:
			network.SendChatPacket(f'/party_request_accept {leader}')
		else:
			network.SendChatPacket(f'/party_request_deny {leader}')

	@classmethod
	def AnswerPartyInvite(cls, leader: int, answer: bool):
		distance = player.GetCharacterDistance(leader)
		
		if distance < 0 or distance > PartyInviteDistance:
			answer = False

		network.SendPartyInviteAnswerPacket(leader, answer)

	def AddPartyMember(self, player_id: int, name: str):
		self.__party[player_id] = name
		self.__presenter.AddPartyMember(player_id, name)

	def UpdatePartyMemberInfo(self, player_id):
		self.__presenter.UpdatePartyMember(player_id)

	def RemovePartyMember(self, player_id: int):
		self.__party.pop(player_id)
		self.__presenter.RemovePartyMember(player_id)

	def LinkPartyMember(self, player_id: int, virtual_id: int):
		self.__party[player_id] = virtual_id
		self.__presenter.LinkPartyMember(player_id, virtual_id)

	def UnlinkPartyMember(self, player_id: int):
		if player_id not in self.__party:
			return
		
		self.__party.pop(player_id)
		self.__presenter.UnlinkPartyMember(player_id)

	def UnlinkAllPartyMember(self):
		self.__party.clear()
		self.__presenter.UnlinkParty()

	def ExitParty(self):
		self.__party.clear()
		self.__presenter.ExitParty()

	def ChangePartyParameter(self, distribution: int):
		self.__party_distribution = distribution
		self.__presenter.ChangePartyDistribution(distribution)
	
	## Command Calls
	def COMMAND_PartyHealReady(self):
		self.__party_can_heal = True
		self.__presenter.PartyHealReady()
	
	def COMMAND_PartyRequest(self):
		pass
	
	def COMMAND_PartyRequestDenie(self):
		pass
	
