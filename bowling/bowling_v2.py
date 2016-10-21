def calc_score(throws):
        total = 0
        frames = []
        number_of_throws = 0
        prev_frame_carryover = []
        for throw in throws:
            total += throw
            number_of_throws += 1
            if number_of_throws in [1, 2] and prev_frame_carryover and prev_frame_carryover[0] == 'spare':
                frames[-1] += throw
                prev_frame_carryover.pop(0)
            if number_of_throws in [1, 2] and prev_frame_carryover and prev_frame_carryover[0] == 'strike':
                frames[-1] += throw
                prev_frame_carryover.pop(0)
                prev_frame_carryover.append('spare')
            if total == 15:
                frames.append(total)
                if number_of_throws == 1:
                    prev_frame_carryover.append('strike')
                elif number_of_throws == 2:
                    prev_frame_carryover.append('spare')
                total = 0
                number_of_throws = 0

        frames.append(total)

        return sum(frames)
