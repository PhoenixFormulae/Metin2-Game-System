## System Imports

## Embedder Imports
from junctions import group

## Application Imports
from Settings.Interface.data import DebugRendering
from System.Interface.Utilities.Color import ExtendedColor

## Library Imports
from Core.Interface.View.Control.interfaces import ControlInterface


def HighlightControl(control: ControlInterface):
    if not DebugRendering:
        return

    x, y = control.GlobalPosition
    width, height = control.Width, control.Height

    group.SetColor(ExtendedColor('blue').hex_int)
    group.RenderBar(x, y, width, height)

    border_size: int = 2

    group.SetColor(ExtendedColor('red').hex_int)

    group.RenderBar(x - border_size, y - border_size, border_size, height + border_size)
    group.RenderBar(x - border_size, y - border_size, width + border_size, border_size)
    group.RenderBar(x + width, y - border_size, border_size, height + border_size)
    group.RenderBar(x - border_size, y + height, width + (border_size * 2), border_size)


def HighlightControlGradient(control: ControlInterface, first_color: str = 'red', second_color: str = 'purple'):
    if not DebugRendering:
        return

    x, y = control.GlobalPosition
    width, height = control.Width, control.Height

    HighlightAreaGradient(x, y, width, height, 3, first_color, second_color)


def HighlightAreaGradient(x: int, y: int, width: int, height: int, border_size: int = 3,
                          first_color: str = 'red', second_color: str = 'yellow'):

    if not DebugRendering:
        return

    start_color = ExtendedColor(first_color).hex_int
    end_color = ExtendedColor(second_color).hex_int

    group.RenderGradationBar(x - border_size, y - border_size, border_size, height + border_size, start_color,
                             end_color)
    group.RenderGradationBar(x - border_size, y - border_size, width + border_size, border_size, end_color,
                             start_color)
    group.RenderGradationBar(x + width, y - border_size, border_size, height + border_size, start_color, end_color)
    group.RenderGradationBar(x - border_size, y + height, width + (border_size * 2), border_size, end_color,
                             start_color)
