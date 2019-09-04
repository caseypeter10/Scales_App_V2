from PIL import Image, ImageDraw, ImageFont

def string_prep(start, notes):
    # This function provides an organized string of notes that can be used to generate the
    # note values for a guitar string. The value passed into the start variable represents
    # the note that would sound on an open string.

    prepared_notes = []
    note_counter = 0
    found_note = 0

    # Following while and if statement
    while note_counter < len(notes):
        if notes[note_counter] == start:

            # records the location of the open string note in the raw note list
            found_note = note_counter

            while note_counter < len(notes):

                prepared_notes.append(notes[note_counter])
                note_counter = note_counter + 1

                #End of the note list
                if note_counter > 11:

                    # following if statement necessary for handling key of C
                    if start == 'C':
                        return prepared_notes

                    # Once the end of the note list is reached, the while loop resets to access the beginning
                    # of the note list
                    note_counter = 0  # starts over at beginning of notes


                elif note_counter == found_note:  # breaks out of prepared list creation

                    return prepared_notes
                # note_counter = note_counter + 1

        else:
            note_counter = note_counter + 1


def note_filter(key):
    # This function determines whether sharps or flats are necessary in the rendering of the

    if key in ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']:

        return ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', ]

    else:

        return ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']


def scale_finder(key, notes):
    # generates major_scale based on filtering a list returned by the string_prep
    # function

    organized_on_key = string_prep(key, notes)
    note_number = 0
    major_scale = []

    print("len(organized_on_key)", organized_on_key)

    while note_number <= len(organized_on_key):
        if note_number == 0:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 2:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 4:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 5:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 7:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 9:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 11:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 12:
            major_scale.append(major_scale[0])

        note_number = note_number + 1

    return major_scale


def fretboard(tunings, key):
    # takes in a list of tunings and then strings are generated from those tunings
    # using the string prep function and appending the result of each string creation
    # to the list fretboard

    fretboard = []
    for i in tunings:
        fretboard.append(string_prep(i, note_filter(key)))

    return fretboard


def fretboard_printer(fretboard):
    # formats the printing of the fretboard nicely
    for i in fretboard:
        print(i)
    return


def scale_on_board(scale, fretboard):
    # adds a * to list values that are also in the scale

    for string_index, string in enumerate(fretboard):
        for fret, pitch in enumerate(string):
            if pitch in scale:
                fretboard[string_index][fret] += 'v'

    return fretboard

def c_major_test():
    standard_fretboard = fretboard(['F', 'A#', 'D#', 'G#', 'C', 'F'], 'C')
    fretboard_w_scale = scale_on_board(scale_finder('C', note_filter('C')), standard_fretboard)
    fretboard_w_scale.reverse()
    fretboard_printer(fretboard_w_scale)

    draw_board()
    return


def draw_board(board, width=1080, height=200):

    #prepping fonts
    #ont_path = "fonts\\AGENCYB.ttf"
    arial = ImageFont.truetype("arial", 13)
    left_shift = -2

    font = arial
    note_fill = 'yellow'


    img = Image.new('RGB',(width,height),color='white')
    draw = ImageDraw.Draw(img)

    init_fret_dis = 165
    current_fret_dis = init_fret_dis
    fret_distance_list = []
    cumulative_distance_list = [0]
    cumulative_dist = 0
    act_fret_list = []

    # drawing frets
    for i in range(13):

        act_fret_x = (i*current_fret_dis + (init_fret_dis/2))
        act_fret_list.append(act_fret_x)

        draw.line([(act_fret_x,0),(act_fret_x,height)], fill=0, width= 7)
        fret_distance_list.append(current_fret_dis)
        current_fret_dis *= 1/(pow(2,(1/12)))

    # drawing strings

    for i in range(6):
        draw.line([(0,i*(height/6)+(height/12)),(width,i*(height/6)+(height/12))], fill=0, width=i + 1)

    for i in range(len(fret_distance_list)):
        print(fret_distance_list[i])
        cumulative_dist += fret_distance_list[i]
        cumulative_distance_list.append(cumulative_dist)

    midpoint_list = []
    #Calculating midpoints of each fret
    for i in range(len(act_fret_list)):
        try:
            midpoint = (act_fret_list[i] + act_fret_list[i+1])/2
            midpoint_list.append(midpoint)
        except:
            print("end of list")

    print("cumulative_distance_list ",cumulative_distance_list)
    print("midpoint list", midpoint_list)


    #iterating all strings in the board
    for i in range(len(board)):
        string_y = i*(height/6)+(height/12)
        #iterating through all frets in a string
        for j in range(len(midpoint_list)):

            # Checking if note is an "open note"
            if j == 0:
                print("cumulative_distance_list[j]", cumulative_distance_list[j])

                #Setting bounding box to the left of the first fret
                top_left_bound = (cumulative_distance_list[j] + 50, string_y - 10)
                bottom_right_bound = (cumulative_distance_list[j] + 70, string_y + 10)
                draw.ellipse((top_left_bound, bottom_right_bound), fill=(100, 0, 0), outline=(80, 0, 10), width=3)

                #Checking if note is in major scale
                if 'v' in board[i][j]:
                    draw.ellipse((top_left_bound, bottom_right_bound), fill=(100, 0, 0), outline=(80, 0, 10), width=3)

                    if '#' in board[i][j] or 'b' in board[i][j]:
                        draw.text((cumulative_distance_list[j] + 55 + left_shift,string_y-7), board[i][j][:2], fill=note_fill, font=font)
                    else:
                        draw.text((cumulative_distance_list[j] + 58 + left_shift, string_y - 7), board[i][j][:1], fill=note_fill, font=font)

                #Note is not in major scale
                else:
                    draw.ellipse((top_left_bound,bottom_right_bound),fill=(100,100,100),outline=(80,80,90),width=3)
                    if '#' in board[i][j] or 'b' in board[i][j]:
                        draw.text((cumulative_distance_list[j] + 55 + left_shift, string_y-7), board[i][j], fill=note_fill, font=font)
                    else:
                        draw.text((cumulative_distance_list[j] + 58 + left_shift, string_y - 7), board[i][j][:1], fill=note_fill, font=font)


            # Note is not an "open note"
            else:

                top_left_bound = (midpoint_list[j-1] - 10, string_y - 10)
                print(top_left_bound)
                bottom_right_bound = (midpoint_list[j-1] + 10, string_y + 10)

                #Checking if the note is in a major scale
                if 'v' in board[i][j]:
                    draw.ellipse((top_left_bound, bottom_right_bound), fill=(100, 0, 0), outline=(80, 0, 10), width=3)

                    if '#' in board[i][j] or 'b' in board[i][j]:
                        draw.text((midpoint_list[j-1]-5 + left_shift,string_y-7), board[i][j][:2], fill=note_fill, font=font)

                    else:
                        draw.text((midpoint_list[j-1] - 2 + left_shift, string_y - 7), board[i][j][:1], fill=note_fill, font=font)

                else:
                    draw.ellipse((top_left_bound,bottom_right_bound),fill=(100,100,100),outline=(80,80,90),width=3)

                    if '#' in board[i][j] or 'b' in board[i][j]:
                        draw.text((midpoint_list[j-1]-5 + left_shift, string_y-7), board[i][j], fill=note_fill, font=font)
                    else:
                        draw.text((midpoint_list[j-1] - 2 + left_shift, string_y - 7), board[i][j][:1], fill=note_fill, font=font)

        #Handling octave at 12th fret
        top_left_bound = (midpoint_list[j] - 10, string_y - 10)
        print(top_left_bound)
        bottom_right_bound = (midpoint_list[j] + 10, string_y + 10)

        if 'v' in board[i][0]:
            draw.ellipse((top_left_bound, bottom_right_bound), fill=(100, 0, 0), outline=(80, 0, 10), width=3)

            if '#' in board[i][0] or 'b' in board[i][0]:
                draw.text((midpoint_list[j] - 5 + left_shift, string_y - 7), board[i][0][:2], fill=note_fill, font=font)

            else:
                draw.text((midpoint_list[j] - 2 + left_shift, string_y - 7), board[i][0][:1], fill=note_fill, font=font)

        else:
            draw.ellipse((top_left_bound, bottom_right_bound), fill=(100, 100, 100), outline=(80, 80, 90), width=3)

            if '#' in board[i][0] or 'b' in board[i][0]:
                draw.text((midpoint_list[j] - 5 + left_shift, string_y - 7), board[i][0], fill=note_fill, font=font)
            else:
                draw.text((midpoint_list[j] - 2 + left_shift, string_y - 7), board[i][0][:1], fill=note_fill, font=font)
    #img.show()
    return img


def gen_board(scale, tunings):
    fretboard_w_scale = scale_on_board(scale_finder(scale, note_filter(scale)), fretboard(tunings, scale))
    fretboard_w_scale.reverse()
    img = draw_board(fretboard_w_scale)
    return img
