def calc_score(throws):
        total = 0
        frames = []
        number_of_throws = 0
        prev_frame_carryover = ''
        for throw in throws:
            total += throw
            number_of_throws += 1
            if number_of_throws in [1, 2] and prev_frame_carryover == 'spare':
                frames[-1] += throw
                prev_frame_carryover = ''
            if number_of_throws in [1, 2] and prev_frame_carryover == 'strike':
                frames[-1] += throw
                if len(frames) > 1:
                    frames[-2] += throw
                    prev_frame_carryover = 'spare'
                else:
                    prev_frame_carryover = 'spare'
            if total == 15:
                frames.append(total)
                if number_of_throws == 1:
                    prev_frame_carryover = 'strike'
                elif number_of_throws == 2:
                    prev_frame_carryover = 'spare'
                total = 0
                number_of_throws = 0

        frames.append(total)

        return sum(frames)
