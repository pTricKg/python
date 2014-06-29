def reverse(text):
    #return ''.join([text[i] for i in range(len(text)-1,-1,-1)])
    ochars = ''
    beyond = len(text)
    for ix in range(beyond):
        ochars += text[beyond - 1 - ix]
        return ochars
