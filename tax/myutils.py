day = {'Mon' : 'Senin',
       'Tue' : 'Selasa',
       'Wed' : 'Rabu',
       'Thu' : 'Kamis',
       'Fri' : 'Jumat',
       'Sat' : 'Sabtu',
       'Sun' : 'Minggu'}

month = {'Jan' : 'Januari',
       'Feb' : 'Februari',
       'Mar' : 'Maret',
       'Apr' : 'April',
       'May' : 'Mei',
       'Jun' : 'Juni',
       'Jul' : 'Juli',
       'Aug' : 'Agustus',
       'Sep' : 'September',
       'Oct' : 'Oktober',
       'Nov' : 'November',
       'Dec' : 'Desember',}

brackets = {       0:0,
             1000000:5,
             3000000:10,
             6000000:15,
            10000000:20,
            20000000:25,
            35000000:30,
            55000000:35,
            80000000:40,
          }

def calculateTax(param):
    lPoint,lPercent,totalTax, has, totalBracket, resultData = 0, 0, 0, param, len(brackets), []
    for enum,(key,item) in enumerate(brackets.items(),1):
        lOc = key - lPoint
        if lOc > 0 :
            if has > lOc:
                added = lOc * lPercent / 100
                totalTax += added
                resultData.append((str(thousandsMarkerCur(lPoint))+" ⎯⎯ "+str(thousandsMarkerCur(key)),(str(lPercent)+"%"), thousandsMarkerCur(int(added))))
                has -= lOc
            else:
                added = has * lPercent / 100
                totalTax += added
                resultData.append((str(thousandsMarkerCur(lPoint))+" ⎯⎯ "+str(thousandsMarkerCur(key)),(str(lPercent)+"%"), thousandsMarkerCur(int(added))))
                has = 0
            if enum == totalBracket:
                added = has * item / 100
                totalTax += added
                resultData.append((str(thousandsMarkerCur(key))+" ⎯⎯ ...", (str(item)+"%"), thousandsMarkerCur(int(added))))
        lPercent = item
        lPoint = key
    return resultData

def countVowels(s):
    count = 0
    vowels = "aiueo"
    for i in s.lower():
        if i in vowels:
            count += 1
    return count

def countConsonants(s):
    count = 0
    consonants = "qwrtypsdfghjklzxcvbnm"
    for i in s.lower():
        if i in consonants:
            count += 1
    return count

def showDate(param):
    _day = param[:3]
    _month = param[4:7]
    _numDay = param[8:10]
    _time = param[11:19]
    _year = param[20:24]

    result = day[_day] + " " + _numDay + " " + month[_month] + " "+ _year + " pukul " + _time
    return result

def thousandsMarker(param):
    reversed = str(param)[::-1]
    result =  '.'.join(reversed[x:x+3] for x in range(0, len(reversed), 3))
    return result[::-1]

def thousandsMarkerCur(param):
    reversed = str(param)[::-1]
    result =  '.'.join(reversed[x:x+3] for x in range(0, len(reversed), 3))
    return "Rp "+str(result[::-1])
