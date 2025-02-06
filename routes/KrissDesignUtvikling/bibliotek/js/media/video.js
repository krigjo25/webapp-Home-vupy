window.addEventListener('DOMContentLoaded',function(){

	var video, play, pause, seek, progress, volume;



video = document.querySelector('video');

play  = document.getElementById('play');
pause = document.getElementById('pause');
seek     = document.getElementById('seek');
volume   = document.getElementById('volume');
playback = document.getElementById('playback');

function clickhandler(event){
    var id = event.target.id;
    if( id === 'play' ){
        video.play();
        video.preload = 'metadata';
        play.classList.add('hidden');
        pause.classList.remove('hidden');
    }
    if( id === 'pause' ){
        video.pause();
        pause.classList.add('hidden');
        play.classList.remove('hidden');
    }  
}
 
function updateduration(event){
    var durationdisplay = document.getElementById('duration'),
        elapsed = document.getElementById('elapsed');
    durationdisplay.innerHTML = formattime( event.target.duration );
    elapsed.innerHTML = formattime( event.target.currentTime );
}

function updateseekmax(event){
    if( event.target.duration ){
        seek.max = event.target.duration;
    }
}

function updateplaybackmax(event){
     if( event.target.duration ){
        playback.max = event.target.duration;
    }
}

function updateseek(event){
    if( event.target.currentTime ){
        seek.value = Math.floor( event.target.currentTime );
    }
}

function updateplayback(event){
    if( event.target.currentTime ){
        playback.value = Math.floor( event.target.currentTime );
    }
}

function updatepreload(event){
    event.target.preload == 'metadata';
}

function formattime(timeinseconds){    
    var zeroes = '0', hours, minutes, seconds, time;
    
    time = new Date(0, 0, 0, 0, 0, timeinseconds, 0);

    hours   = time.getHours();
    minutes = time.getMinutes();
    seconds = time.getSeconds()
    
    hours   = (zeroes + hours).slice(-2);
    minutes = (zeroes + minutes).slice(-2);
    seconds = (zeroes + seconds).slice(-2);
    
    time = hours + ':' + minutes + ':' + seconds;
    
    return time; 
}

function timeupdatehandler(event){
    var elapsed = document.getElementById('elapsed');
    elapsed.innerHTML = formattime( event.target.currentTime );
}

	function seekhandler(event){
    video.currentTime = event.target.value; 
    playback.value = event.target.value
}

function volumehandler(event){
    video.volume = event.target.value;   
}

function backtobeginning(event){
    video.currentTime = 0;
    seek.value = 0;
    playback.value = 0;
}


play.addEventListener('mousedown', clickhandler);
pause.addEventListener('mousedown', clickhandler);


video.addEventListener('durationchange',  updateduration);
video.addEventListener('durationchange',  updateseekmax);
video.addEventListener('durationchange',  updateplaybackmax);
    

video.addEventListener('playing',  updateseekmax);
video.addEventListener('playing',  updateplaybackmax);
video.addEventListener('playing',  updateduration);
    
video.addEventListener('timeupdate',  timeupdatehandler);
video.addEventListener('timeupdate',  updateseek );
video.addEventListener('timeupdate',  updateplayback );

seek.addEventListener('change',  seekhandler );
volume.addEventListener('change',  volumehandler );

});
