def calculate(segments):
    segments.sort(key=lambda x: x[1])

    dots = []
    while segments:
        dot = segments[0][1]
        dots.append(dot)
        segments = segments[1:]
        for seg in segments[:]:
            segm = range(seg[0], seg[1] + 1)
            if dot in segm:
                segments.remove(seg)

    print(len(dots))
    print(*dots)

if __name__ == "__main__":
    n = int(input())

    segments = []
    for _ in range(n):
        a, b = map(int, input().split())
        segments.append((a, b))

    calculate(segments)