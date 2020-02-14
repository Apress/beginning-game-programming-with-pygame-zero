# Piano Game

# Screen resolution based on Raspberry Pi 7" screen
WIDTH = 800
HEIGHT = 410

# Notes are stored as quarter time intervals
# where no note is played use ''
# There is no error checking of the tune, all must be valid notes
# When the saints go marching in
tune = [
    '', 'C4', 'E4', 'F4', 'G4', '', '', '', '', 'C4', 'E4', 'F4', 'G4', '', '', '',
    '', 'C4', 'E4', 'F4', 'G4', 'E4', 'C4', 'E4', 'D4', '', '', 'E4', 'E4', 'D4', 'C4', 'C4',
    'E4', 'G4', 'G4', 'G4', 'F4', '', '', 'E4', 'F4', 'G4', 'E4' , 'C4', 'D4', 'C4'
    ]

# State allows 'menu' (waiting), 'demo' (play demo), 'game' (game mode), 'gameover' (show score)
state = 'menu'
score = 0

note_start = (50,250)
note_size = (50,160)
# List of notes to include on noteboard
notes_include_natural = ['F3','G3','A3','B3','C4','D4','E4','F4','G4','A4','B4','C5','D5','E5']
# List of sharps (just reference note without sharp)
notes_include_sharp = ['F3','G3','A3','C4','D4','F4','G4','A4','C5','D5']
note_rect_sharp = {}
note_rect_natural = {}
notes_tones = {}

beats_per_minute = 116
# Crotchet is a quarter note
# 1 min div by bpm
time_crotchet = (60/beats_per_minute)
time_note = time_crotchet/2

# how long has elapsed since the last note was started - or a rest
time_since_beat = 0
# The current position that is playing in the list
# A negative number indicates that the notes are shown falling,
# but hasn't reached the play line
note_position = -10

button_demo = Actor("button_demo", (650,40))
button_start = Actor("button_start", (150,40))

# Setup notes
def setup():
    global note_rect_natural, note_rect_sharp, notes_tones
    i = 0
    sharp_width = 2*note_size[0]/3
    sharp_height = 2*note_size[1]/3
    for note_ref in notes_include_natural:
        note_rect_natural[note_ref] = Rect(
            (note_start[0]+(note_size[0]*i),note_start[1]),(note_size)
            )
        # Add note
        notes_tones[note_ref]=tone.create(note_ref, time_note)
        # Is there a sharp note?
        if note_ref in notes_include_sharp:
            note_rect_sharp[note_ref] = Rect(
                (note_start[0]+(note_size[0]*i)+sharp_width, note_start[1]),
                (sharp_width,sharp_height)
                )
            # Create version in Note#Octave eg. C#4
            note_ref_sharp = note_ref[0]+"#"+note_ref[1]
            notes_tones[note_ref_sharp]=tone.create(note_ref_sharp, time_note)
        i+=1

def draw():
    screen.fill('white')
    button_demo.draw()
    button_start.draw()
    draw_piano()
    if (state == 'demo' or state == 'game'):
        draw_notes()
        # draw line for hit point
        screen.draw.line ((50, 220), (WIDTH-50, 220), "black")
    if (state == 'game'):
        screen.draw.text("Score {}".format(score), center=(WIDTH/2,50), fontsize=60,
            shadow=(1,1), color=("black"), scolor="white")
    if (state == 'gameover'):
        screen.draw.text("Game over. Score {}".format(score), center=(WIDTH/2,150), fontsize=60,
            shadow=(1,1), color=("black"), scolor="white")

def draw_notes():
    for i in range (0, 10):
        if (note_position + i < 0):
            continue
        # If no more notes then finish
        if (note_position + i >= len(tune)):
            break
        draw_a_note (tune[note_position+i], i)

# position is how far ahead
# 0 = current_note, 1 = next_note etc.
def draw_a_note(note_value, position):
    if (len(note_value) > 2 and note_value[2] == 's'):
        sharp = True
        note_value = note_value[0:2]
    else:
        sharp = False
    if (position == 0) :
        color = 'green'
    else:
        color = 'black'
    if note_value != '':
        if sharp == False:
            screen.draw.filled_circle((note_rect_natural[note_value].centerx, 220-(15*position)), 10, color)
        else:
            screen.draw.filled_circle((note_rect_sharp[note_value].centerx, 220-(15*position)), 10, color)
            screen.draw.text("#", center=(note_rect_sharp[note_value].centerx+20, 220-(15*position)),
                fontsize=30, color=(color))

def update(time_interval):
    global time_since_beat, note_position, state
    time_since_beat += time_interval
    # Only update when the time since last beat is reached
    if (time_since_beat < time_crotchet):
        return

    # reset timer
    time_since_beat = 0

    if state == 'demo':
        note_position += 1
        if (note_position >= len(tune)):
            note_position = -10
            state = 'menu'
        # Play current note
        if (note_position >= 0 and tune[note_position] != ''):
            notes_tones[tune[note_position]].play()

    elif state == 'game':
        note_position += 1
        if (note_position >= len(tune)):
            note_position = -10
            state = 'gameover'

def draw_piano():
    for this_note_rect in note_rect_natural.values() :
        screen.draw.rect(this_note_rect, 'black')
    for this_note_rect in note_rect_sharp.values() :
        screen.draw.filled_rect(this_note_rect, 'black')

def on_mouse_down(pos, button):
    global state, note_position, score
    if (button == mouse.LEFT):
        if button_demo.collidepoint(pos):
            note_position = -10
            state = "demo"
        elif button_start.collidepoint(pos):
            note_position = -10
            state = "game"
        else:
            # First check sharp notes as they overlap the natural keys
            for note_key, note_rect in note_rect_sharp.items():
                if (note_rect.collidepoint(pos)):
                    note_key_sharp = note_key[0]+"#"+note_key[1]
                    if (note_key_sharp == tune[note_position]):
                        score += 1
                    notes_tones[note_key_sharp].play()
                    return
            for note_key, note_rect in note_rect_natural.items():
                if (note_rect.collidepoint(pos)):
                    if (note_key == tune[note_position]):
                        score += 1
                    notes_tones[note_key].play()
                    return
setup()