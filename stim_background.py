from psychopy import visual, core, event

# --------------------
# Window
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
timer_box = visual.Rect(
    win,
    width=170,
    height=70,
    fillColor="black",
    lineColor="white",
    pos=(win_w/2 - 110, -win_h/2 + 45)
)

timer_text = visual.TextStim(
    win,
    text="20:00",
    pos=(win_w/2 - 110, -win_h/2 + 45),
    height=36,
    color="white",
    units="pix"
)

# --------------------
# Help button
# --------------------
help_button_pos = (-win_w / 2 + 130, -win_h / 2 + margin)

help_button = visual.Rect(
    win,
    width=220,
    height=80,
    pos=help_button_pos,
    fillColor="lightgray",
    lineColor="white"
)

help_label = visual.TextStim(
    win,
    text="Pomoc",
    pos=help_button_pos,
    height=24,
    color="black"
)

# --------------------
# Start button
# --------------------
start_button_pos = (-win_w / 2 + 390, -win_h / 2 + margin)

start_button = visual.Rect(
    win,
    width=220,
    height=80,
    pos=start_button_pos,
    fillColor="lightgreen",
    lineColor="white"
)

start_label = visual.TextStim(
    win,
    text="Start",
    pos=start_button_pos,
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
# Mouse
# --------------------
mouse = event.Mouse(win=win)

# --------------------
# Timer
# --------------------
timer_duration = 1200  # seconds (testing)
timer_clock = core.Clock()
timer_running = False

# --------------------
# State
# --------------------
help_requested = False
button_was_down = False

# --------------------
# Main loop
# --------------------
while True:

    # Keyboard
    keys = event.getKeys()

    if "escape" in keys:
        break

    if "q" in keys:
        help_requested = False

    # Mouse edge detection
    mouse_down = mouse.getPressed()[0]

    if mouse_down and not button_was_down:

        if help_button.contains(mouse):
            help_requested = True

        elif start_button.contains(mouse):
            timer_clock.reset()
            timer_running = True

    button_was_down = mouse_down

    # Timer update
    if timer_running:
        elapsed = timer_clock.getTime()
        remaining = max(0, timer_duration - elapsed)

        if remaining <= 0:
            timer_running = False
            remaining = 0
    else:
        if timer_clock.getTime() == 0:
            remaining = timer_duration
        else:
            remaining = 0

    mins = int(remaining // 60)
    secs = int(remaining % 60)

    timer_text.text = f"{mins:02d}:{secs:02d}"

    # Draw
    background.draw()

    help_button.draw()
    help_label.draw()

    start_button.draw()
    start_label.draw()

    timer_box.draw()
    timer_text.draw()

    if help_requested:
        red_overlay.opacity = 0.5
        red_overlay.draw()

    win.flip()

# --------------------
# Exit
# --------------------
win.close()
core.quit()