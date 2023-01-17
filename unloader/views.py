from django.shortcuts import render, redirect
from pytube import YouTube, Channel
from django.http import FileResponse
from django.contrib import messages
from io import BytesIO
# Create your views here.

def home(request):
    if request.method == 'POST':
        request.session['link'] = request.POST['url']
        # request.session['link'] = request.GET.get('url')
        try:
            url = YouTube(request.session['link'])
            c_url= url.channel_url
            c_name = Channel(c_url)
            url.check_availability()
            streams = url.streams.filter(progressive=True)
            context = {'streams':streams, 'url':url, 'c_name':c_name, 'c_url':c_url}
        except:
            message = messages.error(request, "Ingresa un enlace de YouTube 😓")
            return render(request, 'yt_index.html', {'message':message})
        return render(request, 'index_unload.html', context)
    return render(request, "yt_index.html")

def download(request):  
    if request.method == 'POST':
        buffer = BytesIO()
        url = YouTube(request.session['link'])
        # stream = url.streams
        itag = request.POST["itag"] 
        if itag == 'audio':
            audio = url.streams.get_audio_only()
            audio.stream_to_buffer(buffer)
            buffer.seek(0)
            filename=url.title+'.mp3'
            return FileResponse(buffer, filename=filename, as_attachment=True, content_type="audio/mp3")
        else:
            video = url.streams.get_by_itag(itag)
            video.stream_to_buffer(buffer)
            buffer.seek(0)
            print(video)
            filename=url.title+'.mp4'
            return FileResponse(buffer, filename=filename, as_attachment=True, content_type="video/mp4")
    return render(request, 'Soon.html')



def donations(request):  
    return render(request, 'donations.html')

def soon(request):  
    return render(request, 'Soon.html')
