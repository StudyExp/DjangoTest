from django.shortcuts import render
# import qrcode
# from django.utils.six import BytesIO
# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')


# def qrcode(request, data):
#     img = qrcode.make(data)
#     buf = BytesIO()
#     img.save(buf)
#     img_stream = buf.getvalue()
#
#     response = HttpResponse(img_stream, content_type="image/png")
#     return response