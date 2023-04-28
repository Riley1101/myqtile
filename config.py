from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from libqtile import extension


# dracula color scheme
theme_background = "#282a36"
theme_current_line = "#44475a"
theme_foreground = "#f8f8f2"
theme_command = "#6272a4"
theme_cyan = "#8be9fd"
theme_green = "#50fa7b"
theme_orange = "#ffb86c"
theme_pink = "#ff79c6"
theme_purple = "#bd93f9"
theme_red = "#ff5555"
theme_yellow = "#f1fa8c"

# applications
mod = "mod4"
terminal = 'kitty'

# keybindings
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout."),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen",),
    Key([mod], 'd', lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="🧛",
        dmenu_font="Andika-8",
    ))),
    # set hide/unhide widgets with mod+shift+f
    Key([mod, "shift"], "f", lazy.hide_show_bar("bottom")),
]


groups = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
]

keys.extend([
    Key([mod], '1', lazy.group['1'].toscreen(),
        desc="Switch to group {}".format('1'))
])
keys.extend([
    Key([mod], '2', lazy.group['2'].toscreen(),
        desc="Switch to group {}".format('code'))
])
keys.extend([
    Key([mod], '3', lazy.group['3'].toscreen(),
        desc="Switch to group {}".format('3'))
])
keys.extend([
    Key([mod], '4', lazy.group['4'].toscreen(),
        desc="Switch to group {}".format('4'))
])
keys.extend([
    Key([mod], '5', lazy.group['5'].toscreen(),
        desc="Switch to group {}".format('5'))
])

# layouts


def init_layout_theme():
    return {"border_width": 2,
            "margin": 2,
            "border_focus": theme_purple,
            "border_normal": theme_current_line
            }


layout_themes = init_layout_theme()

layouts = [
    layout.Max(),
    layout.Columns(border_focus_stack=[
                   theme_purple, theme_command],  **layout_themes),
    layout.Floating(),
]

# widgets default settings
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=4,
)
extension_defaults = widget_defaults.copy()

# screens and widgets
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(foreground=theme_purple),
                widget.GroupBox(highlight_method='text', this_current_screen_border=theme_purple,
                                active=theme_command, disable_drag=True, inactive=theme_current_line,),
                widget.Spacer(length=15),
                widget.WindowName(foreground=theme_foreground,
                                  fmt='{}', fontsize=12),
                widget.Spacer(length=bar.STRETCH),
                widget.Mpris2(),
                widget.Chord(
                    chords_colors={
                        "launch": (theme_pink, theme_foreground),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Wallpaper(
                    directory='/home/arkar/Pictures/wallpapers', random_selection=True, fmt=''),
                widget.Notify(),
                widget.CPUGraph(type='line', line_width=1, border_width=0,
                                fill_color=theme_current_line, graph_color=theme_purple, samples=50),
                # widget.Net(format='{down} ↓↑ {up}', foreground=theme_green),
                widget.NetGraph(type='line', line_width=1, border_width=0,
                                theme_foreground=theme_current_line, graph_color=theme_pink, samples=50),
                widget.CheckUpdates(
                    distro='Arch', colour_have_updates=theme_green,),
                widget.Spacer(length=5),
                widget.Volume(foreground=theme_yellow,
                              fmt='{}'),
                widget.Spacer(length=5),
                widget.Battery(format="{char} {percent:2.0%}", charge_char="↑", discharge_char="↓",
                               full_char="f", empty_char="empty", low_percentage=0.2, update_interval=5, foreground=theme_green,
                               low_foreground=theme_red),
                widget.Spacer(length=5),
                widget.Backlight(foreground=theme_pink,
                                 backlight_name='intel_backlight', fmt='{}', scroll=True, width=50),
                widget.Spacer(length=5),
                widget.Clock(format="%I:%M %p",
                             padding=6,
                             foreground=theme_orange, ),
                widget.Spacer(length=5),
                widget.KeyboardLayout(
                    configured_keyboards=['us', ],
                    display_map={'us': '🇺🇸',  },
                ),
                widget.Spacer(length=5),
            ],
            24,
            border_width=[2, 0, 2, 0],
            border_color=[theme_foreground],
            background=[theme_background],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Gideon"

