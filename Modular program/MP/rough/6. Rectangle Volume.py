def GetVolume(l, w, h):
    rahi = float()
    rahi = l*w*h
    return rahi

l = float()
w= float()
h = float()

l = float(input())
w = float(input())
h = float(input())

newgetvolume = GetVolume(l, w, h)
print(newgetvolume)
