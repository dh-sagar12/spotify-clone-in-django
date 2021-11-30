let masterPlayer = document.getElementById("masterPlayer");
let music = "/media/music/bensound-memories.mp3"
music = localStorage.getItem('latestplay')
console.log(music)
let audioElement = new Audio(music);
let playBtn = document.querySelectorAll('.playBtn')
let playCheck = document.querySelectorAll('.playCheck')
let myProgressBar = document.getElementById('myProgressBar');
let myVolumeBar = document.getElementById('myVolumeBar');
myVolumeBar.value = audioElement.volume * 100


let musicBannerName = document.getElementById('song-name-banner')
let artistBannerName = document.getElementById('song-artist')
let musicBannerImg = document.getElementById('music-img-banner')
let volumeButton = document.getElementById('volumeButton')

musicBannerName.innerText = localStorage.getItem('musicname')
artistBannerName.innerText = localStorage.getItem('artistname')
musicBannerImg.src = localStorage.getItem('musicimg')


masterPlayer.addEventListener("click", () => {
    console.log("player");
    if (audioElement.paused || audioElement.currentTime <= 0) {
        audioElement.play();
        masterPlayer.innerHTML = '<i class="material-icons text-dark">pause</i>'

    } else {
        audioElement.pause();
        masterPlayer.innerHTML = '<i class="material-icons text-dark">play_arrow</i>'
    }
});


document.addEventListener('keyup', (e) => {
    if (e.code == 'Space') {
        if (audioElement.paused || audioElement.currentTime <= 0) {
            audioElement.play();
            masterPlayer.innerHTML = '<i class="material-icons text-dark">pause</i>'

        } else {
            audioElement.pause();
            masterPlayer.innerHTML = '<i class="material-icons text-dark">play_arrow</i>'
        }
    }
})



playBtn.forEach((elem) => {
    elem.addEventListener('click', (e) => {
        console.log(e)
        music = elem.getAttribute('js-data')
        audioElement.src = music
        ariaLabel = elem.getAttribute('aria-label')
        artistName = elem.getAttribute('artist-name')
        musicName = elem.getAttribute('music-name')
        musicImg = elem.getAttribute('music-img')

        localStorage.setItem('musicname', musicName)
        localStorage.setItem('artistname', artistName)
        localStorage.setItem('musicimg', musicImg)

        myProgressBar.max = audioElement.duration

        if (ariaLabel == 'play' || audioElement.currentTime < 0) {
            console.log('played')
            audioElement.play()
            localStorage.setItem('latestplay', audioElement.src)
            elem.innerHTML = ' <i class="material-icons">pause</i>'
            masterPlayer.innerHTML = '<i class="material-icons text-dark">pause</i>'
            elem.setAttribute('aria-label', 'pause')
            artistBannerName.innerText = artistName
            musicBannerName.innerText = musicName
            musicBannerImg.src = musicImg




        }
        else if (ariaLabel = 'pause' || audioElement.currentTime > 0) {
            console.log('paused')
            audioElement.pause()
            elem.innerHTML = ' <i class="material-icons">play_arrow</i>'
            masterPlayer.innerHTML = '<i class="material-icons text-dark">play_arrow</i>'
            elem.setAttribute('aria-label', 'play')

        }
    })
})

// audioElement.addEventListener('')


audioElement.addEventListener('timeupdate', () => {
    // Update Seekbar
    myProgressBar.max = audioElement.duration
    myProgressBar.value = (audioElement.currentTime)


    if (audioElement.currentTime === audioElement.duration) {
        masterPlayer.innerHTML = '<i class="material-icons text-dark">play_arrow</i>'
    }

})





myProgressBar.addEventListener('change', () => {
    audioElement.currentTime = myProgressBar.value;


})



myVolumeBar.addEventListener('change', () => {
    audioElement.volume = myVolumeBar.value / 100
    if (audioElement.volume == 0) {
        volumeButton.innerText = 'volume_off'

    }
    else {
        volumeButton.innerText = 'volume_up'
    }
})

volumeButton.addEventListener('click', () => {
    if (myVolumeBar.value > 0) {
        audioElement.volume = 0
        myVolumeBar.value = 0
        volumeButton.innerText = 'volume_off'
        volumeButton.classList.add('text-muted')
    }
    else {
        audioElement.volume = 0.5
        myVolumeBar.value = 50
        volumeButton.innerText = 'volume_up'
    }
})




