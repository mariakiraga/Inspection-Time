from psychopy import visual, core, event

# --------------------
# Window (IMPORTANT: no fake size fighting fullscreen)
# --------------------
win = visual.Window(
    fullscr=True,
    color="black",
    units="pix"
)

win_w, win_h = win.size
margin = 50

# --------------------
# Background
# --------------------
background = visual.ImageStim(
    win,
    image="background.jpg",
    size=win.size,
    pos=(0, 0)
)

# --------------------
# Timer (bottom-right)
# --------------------
timer_text = visual.TextStim(
    win,
    text="",
    pos=(0.9 * win.size[0] / 2, -0.9 * win.size[1] / 2),
    height=30,
    color="white",
    alignText="right"
)

# --------------------
# Button (bottom-left)
# --------------------
button_pos = (-win_w/2 + 130, -win_h/2 + margin)

button = visual.Rect(
    win,
    width=220,
    height=80,
    pos=button_pos,
    fillColor="lightgray",
    lineColor="white"
)

button_label = visual.TextStim(
    win,
    text="Pomoc",
    pos=button_pos,
    height=24,
    color="black"
)

# --------------------
# Red overlay
# --------------------
red_overlay = visual.Rect(
    win,
    width=win_w * 2,
    height=win_h * 2,
    pos=(0, 0),
    fillColor="red",
    opacity=0.0,
    lineColor=None
)

# --------------------
# Input + clock
# --------------------
mouse = event.Mouse(win=win)
clock = core.Clock()

help_requested = False
button_was_down = False
duration = 1200  # 20 min

# --------------------
# Main loop
# --------------------
while clock.getTime() < duration:

    # ---- Keys (single poll) ----
    keys = event.getKeys()

    if "escape" in keys:
        core.quit()

    if "q" in keys:
        help_requested = False

    # ---- Timer ----
    t = clock.getTime()
    remaining = max(0, duration - t)

    mins = int(remaining // 60)
    secs = int(remaining % 60)

    timer_text.text = f"{mins:02d}:{secs:02d}"

    # ---- Mouse click edge detection ----
    mouse_down = mouse.isPressedIn(button)

    if mouse_down and not button_was_down:
        help_requested = True

    button_was_down = mouse_down

    # ---- Draw order (critical) ----
    background.draw()

    button.draw()
    button_label.draw()

    timer_text.draw()

    if help_requested:
        red_overlay.opacity = 0.5
        red_overlay.draw()

    win.flip()

# --------------------
# End
# --------------------
win.close()
core.quit()