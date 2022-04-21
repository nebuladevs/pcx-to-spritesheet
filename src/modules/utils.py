def chunkArray(list, n):
    return [list[i:i + n] for i in range(0, len(list), n)]