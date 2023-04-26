/*
runs the html page
*/
window.onload = function() {

  // Set the URL of the Flask app
  const flaskAppUrl = 'https://replit.com/@SandySomchay/CS321#index.html';

  const htmlPageUrl = `https://cs321.sandysomchay.repl.co/${flaskAppUrl}`;

  //testing out for permissions with getUserMedia
  //const constraints = { audio: true, video: true};

  //accessing 
  //navigator.mediaDevices.getUserMedia(constraints)
  //  .then(function(stream) {
  // Attach the video stream to the video element
  //    video.srcObject = stream;
  //  })
  //  .catch(function(err) {
  //    console.log('Error accessing video stream: ', err);
  //  });
  // where the flask app is running

  const iframe = document.getElementById('flask-app');
  // Set the URL of the HTML page to load in the iframe

  // Load the HTML page in the iframe
  iframe.src = htmlPageUrl;




}
