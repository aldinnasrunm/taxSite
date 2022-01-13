from django.shortcuts import render
from time import ctime
from tax.myutils import showDate, calculateTax, thousandsMarkerCur

# Create your views here.

def home(request):
    now = ctime()
    timeFormat = showDate(now)
    #konteks nya diganti biar buat ngisi datanya
    group = {
    "Agus Ardiansyah Nh" : "L200214397",
    "Aldin Nasrun Minalloh" : "L200214208",
    "Hanifah Afkar Nabila" : "L200214252"
    }
    context = {
        "title" : "Tugas AP 2021",
        "group" : group,
        "lecturer" : "Fajar Suryawan, Ph.D",
        "time" : timeFormat,
    }

    if request.POST:
        rt = request.POST.get('tax')
        try:
            if int(rt) > 0:
                resultTaxt = calculateTax(int(rt))
                total = 0
                for x in resultTaxt:
                    total += int(x[2].replace("Rp ", "").replace(".", ""))
                total = thousandsMarkerCur(total)
                rtCur = thousandsMarkerCur(int(rt))
                context.update({"rt" : rt, "rtCur" : rtCur , "resultTax" : resultTaxt, "totalTax" : total, })
            else:
                context.update({"exc":"Please insert positive integer! "})

        except:
            context.update({"exc":"Please insert positive integer! "})

    return render(request, 'tax/index.html', context)



def about(request):
    return render(request, 'tax/about.html')
