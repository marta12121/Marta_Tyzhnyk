def areYouPlayingBanjo(name):
    if name[0] == 'R' or name[0] == 'r':
        name = name + ' ' 'plays banjo'
        return name
    else:
        name = name +' ' 'does not play banjo'
        return name
print(areYouPlayingBanjo('micc'))