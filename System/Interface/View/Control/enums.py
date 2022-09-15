# Standard Imports
from enum import Enum, unique, IntFlag


# Embedder Imports
from junctions import window_manager


# Library Imports


# External Imports


@unique
class HorizontalAlignment(Enum):
	"""
	Horizontal alignment of a control
	"""
	
	Right = window_manager.HORIZONTAL_ALIGN_RIGHT
	Center = window_manager.HORIZONTAL_ALIGN_CENTER
	Left = window_manager.HORIZONTAL_ALIGN_LEFT


@unique
class VerticalAlignment(Enum):
	"""
	Vertical alignment of a control
	"""
	
	Top = window_manager.VERTICAL_ALIGN_TOP
	Center = window_manager.VERTICAL_ALIGN_CENTER
	Bottom = window_manager.VERTICAL_ALIGN_BOTTOM


@unique
class Flag(Enum):
	"""
	Flags are attributes that determine how the control
	interactions are made and how should the embedder deal with it
	
	For example, if the control is not set as 'Dragable',
	when the user clicks and tries to drag the control it
	will not move from its place.
	
	Or if the control is not set as 'Movable', changing its
	location will have no effect on actually moving it, either
	by dragging or property setter
	
	"""
	
	Movable = 1 << 0
	"""
	Marks the control as movable, meaning that if the control
	is captured it can be moved by mouse movements
	
	*Note*: The control cannot be moved if marked as "Not-Capture"
	and inputs will be ignored
	"""
	
	Limit = 1 << 1
	"""
	Limits the control movement to a specified rectangle bias related to the
	parent, meaning that the control when moved will not exceed the limit
	
	For example, if the control is moved to limit A in the X axis and
	exceeds the X axis limit, it will not go further (where A is 20 and X
	is 25, the X will be set as 20 instead)
	
	*Note:* Limit Bias can be set using the "SetLimitBias" method/property
	"""
	
	Dragable = 1 << 3
	"""
	
	"""
	
	Attach = 1 << 4
	"""
	Attaches a control to the root parent, meaning events will be triggered
	on the root parent instead, for example when a mouse button is pressed
	or the control is dragged instead of those actions affect the control
	directly it will affect the root parent
	"""
	
	Restrict_X = 1 << 5
	"""
	Restricts control movement to the X axis, meaning that the control
	can only be moved up/down.
	
	*Note:* Follows the same analogy of "Movable" and also requires that the
	"Movable" flag to be set
	"""
	
	Restrict_Y = 1 << 6
	"""
	Restricts control movement to the Y axis, meaning that the control
	can only be moved left/right.
	
	*Note:* Follows the same analogy of "Movable" and also requires that the
	"Movable" flag to be set
	"""
	
	Not_Capture = 1 << 7
	"""
	Marks the control as non-capturable, meaning that the control
	cannot be captured for internal interaction, for example when clicking
	on the control with the left mouse button it will not interact with
	anything
	TODO: Better explanation because this does not explain accurately what
	happens
	"""
	
	Float = 1 << 8
	"""
	Marks the ability of the control to be set as Top-most, meaning
	if the control can or not be on the top of all other controls.
	
	*Note:* When calling the method/property "SetTop" the control
	must have this flag set to it have effect
	"""
	
	Not_Pick = 1 << 9
	"""
	Marks the ability of the control to be picked as the active
	control, which means that this control can be focused
	"""
	
	Ignore_Size = 1 << 10
	"""
	This flag has no real effect because it does not affect anything other than
	a case that doesn't occur
	"""
	
	RTL = 1 << 11
	"""
	Marks the control has RTL (Right To Left), meaning that
	when control's location, alignment or disposition is initially
	set (when control loading occurs) these attributes will have the
	opposite values instead
	
	For example, if the X axis is set to 50 and RTL flag is present,
	the value will be -50 instead
	"""


@unique
class Anchor(IntFlag):
	"""
	An anchor is a control attribute that controls size
	behaviour regarding parent's size alterations.
	
	For example when a control is anchored to the left and right
	and the parent width changes, the control's width also changes
	the same amount but the control will stay in the same location
	"""
	
	Left = 1 << 0
	Right = 1 << 1
	Top = 1 << 2
	Bottom = 1 << 3
