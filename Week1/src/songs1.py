def compute():
    songs = [1, 2, 5, 4, 3]
    # add your code here to compute max
    temp = songs[0]
    res = 1
    for i in range(len(songs)):
        if songs[i] > temp:
            temp = songs[i]
            res = i - 1
    print("Max song amount is", temp)
    print("The least song played is ", res)


if __name__ == "__main__":
    compute()
