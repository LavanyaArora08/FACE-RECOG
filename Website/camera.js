// get the video element
var video = document.getElementById('video');

// get the canvas element
var canvas = document.getElementById('canvas');

// get the snap button
var snap = document.getElementById('snap');

// get the image download button
var download = document.createElement('a');
download.innerHTML = 'Download Image';
download.href = '';
download.download = 'user_picture.jpg';
document.body.appendChild(download);

// get the context for the canvas
var context = canvas.getContext('2d');

// get user media
navigator.mediaDevices.getUserMedia({video: true})
.then(function(stream) {
    video.srcObject = stream;
    video.play();
})
.catch(function(error) {
    console.log(error);
});

// when the user clicks the snap button
snap.addEventListener('click', function() {
    // draw the video frame on the canvas
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    // get the canvas data as a data URL
    var dataURL = canvas.toDataURL();
    
    // set the download link href to the data URL
    download.href = dataURL;
});
