var canvas = document.getElementById("LeftCanvas");
var ctx = canvas.getContext("2d");

//variable 
joystickX = 0
joystickY = 0
leftTriggerValue = 1
rightTriggerValue = 0

function draw() {
  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
	
	var radius = 100;

	ctx.font = 'bold 50px Roboto';

	//joystick base 
	ctx.beginPath();
	ctx.arc(150, 450, radius, 0, 2 * Math.PI, false);
	ctx.fillStyle = '#A6051A';
	ctx.fill();
	ctx.lineWidth = 5;
	ctx.strokeStyle = 'black';
	ctx.stroke();

	//joystick position 
	ctx.beginPath();
	ctx.fillStyle = 'black';
	ctx.fill();
  ctx.arc(joystickX+150, joystickY+450, 20, 0, 2 * Math.PI);
	ctx.lineWidth = 5;
	ctx.strokeStyle = 'black';
  ctx.stroke();


  //Draw the left and right trigger values
	ctx.fillStyle = 'black';
	ctx.fill();
  ctx.fillRect(150, 100, leftTriggerValue * 70, 120);
	ctx.fillStyle = 'white';
	ctx.fill();
	ctx.fillText("LT", 155, 150, leftTriggerValue * 60);

	ctx.fillStyle = 'black';
	ctx.fill();
  ctx.fillRect(1100, 100, rightTriggerValue * 70, 120);
	ctx.fillStyle = 'white';
	ctx.fill();
	ctx.fillText("RT", 1105, 150, rightTriggerValue * 60);
  
  // Call this function again on the next frame
  requestAnimationFrame(draw);
}

// Call the draw function to start rendering the visuals
draw();


window.addEventListener("gamepadconnected", function(e) {
  console.log("Gamepad connected: " + e.gamepad.id);
});

window.addEventListener("gamepaddisconnected", function(e) {
  console.log("Gamepad disconnected: " + e.gamepad.id);
});

function update() {
  var gamepads = navigator.getGamepads();
  for (var i = 0; i < gamepads.length; i++) {
    var gamepad = gamepads[i];
    if (gamepad) {
      if (gamepad.buttons[7].pressed) {
        console.log("Button " + 7 + " pressed.");
        rightTriggerValue = 1;
      }
      else if (gamepad.buttons[6].pressed) {
        console.log("Button " + 6 + " pressed.");
        leftTriggerValue = 1;
      } 
      else {
          leftTriggerValue = 0;
          rightTriggerValue = 0;
      }
      joystickX = gamepad.axes[0] * 100;
      console.log("joystickX: " + joystickX);

      joystickY = gamepad.axes[1] * 100;
      console.log("joystickY: " + joystickY);

      draw();
    }
  }
  window.requestAnimationFrame(update);
}

window.requestAnimationFrame(update);


function changeStream() {
	let ipAddress = ""
	const currentSrc = document.getElementById('feed').getAttribute('src');
	newSrc = `${ipAddress}`;
	document.getElementById('stream').setAttribute('src', newSrc);
}