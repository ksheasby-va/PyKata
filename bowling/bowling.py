def calc_score(throws):
    frame_number = 1
    balls_in_frame = 0
    frame_total = 0
    bonus = 0
    total = 0
    frames = split_throws_into_frames(throws)

    for frame, next_frame, third_frame in zip(frames, frames[1:], frames[2:]):
        i = 0
        while len(frame) < 3:
            if i < len(next_frame):
                frame.append(next_frame[i])
            else:
                frame.append(third_frame[i-1])
            i += 1

        total += sum(frame)

    total += sum(frames[-1])
    return total

def split_throws_into_frames(throws):

    frames = []
    frame = []
    balls = 0
    total = 0
    for x in throws:
        if total < 15:
            frame.append(x)
            total += x
            balls += 1
        else:
            frame.append(x)

        if total == 15 or balls == 3:
            frames.append(frame)
            balls = 0
            frame = []
            total = 0

    return frames
