from django.shortcuts import render

def hi(request,w,w2):
   s = w + w2
    return render(request, 'hi.html', {
       #html use : hi() use
       's':s
   })


def r(request, start, stop):
   if start > stop:
      start, stop = stop, start
   rr = range(start, stop+1)

   if start > stop:
      rr = reversed(rr)
   return render(request, 'r.html', {
       # html use : hi() use
       'rr': rr
   })


def tag_test(request):
   ll = [1,2,3,4,5,6,7,8]
   return render(request, 'tag_test.html',{
       'll': ll
   })
