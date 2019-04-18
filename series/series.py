def slices(series, length):
    if len(series) < length or length <= 0 or len(series) < 1:
        raise ValueError("Lenght of serise must be greater or equal one and lenght number'")
    a = []
    for i in range(len(series)):
        if length + i > len(series):
            break
        a.append(series[i:length+i])
    return a