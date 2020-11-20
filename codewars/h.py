# https://www.codewars.com/kata/52742f58faf5485cae000b9a


def format_duration(seconds):
    if seconds == 0:
        return('now')
    else:
        minutes = seconds//60
        hours = minutes//60
        days = hours//24
        years = days//365

        stdyrs = years
        stddays = days - years*365
        stdhrs = hours - days*24
        stdmins = minutes - hours*60
        stdsec = seconds - minutes*60

        tup = [stdyrs, stddays, stdhrs, stdmins, stdsec]

        dic = {
            0: 'year',
            1: 'day',
            2: 'hour',
            3: 'minute',
            4: 'second'
        }
        output = []
        for dt, tm in enumerate(tup):
            if tm != 0:
                st = dic.get(dt)
                if tm > 1:

                    temp = st + 's' + ','
                    output.append(str(tm))
                    output.append(" ")
                    output.append(temp)
                    output.append(" ")
                else:
                    output.append(str(tm))
                    output.append(" ")
                    output.append(st + ',')
                    output.append(" ")
        if len(output) > 5:
            temp = output[-6]
            temp = temp[0:-1]
            output[-6] = temp
            output[-5] = ' and '

        return ''.join(output)[0:-2:]
