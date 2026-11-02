def schedule_meetings(intervals: list[tuple[int, int]]) -> tuple[int, list]:
    rooms = []
    for meeting in sorted(intervals, key=lambda m: m[0]):
        for room in rooms:
            if room[-1][1] <= meeting[0]:
                room.append(meeting)
                break
        else:
            rooms.append([meeting])
    return len(rooms), rooms

if __name__ == "__main__":
    print(schedule_meetings([(0, 30), (5, 10), (15, 20)]))