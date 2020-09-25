// Cache DOM elements
const standby = document.querySelector(".standby");
const power = document.querySelector(".power");
const test = document.querySelector(".test");

const mechanism = document.querySelector(".mechanism");
const ball = document.querySelector(".ball");
let roll;
let pitch;

standby.classList.remove("off");
power.classList.add("on");

function handleOrientation(event) {
	var doc = document,
		x = Math.round(event.beta),
		z = Math.round(event.gamma);
	
	var roll = -1*z;
	var pitch = 75+x;

	mechanism.style.transform = "rotate(" + roll + "deg)";
  	ball.style.top = pitch + "px";
}

var temp = false;

function getSimulatorData(){
	$.getJSON($SCRIPT_ROOT + '/datapoint/PLANE_BANK_DEGREES/get', {}, function(data) {
		var z = Math.round(data * (180/Math.PI));
		if ((z > 100) || (z < -100)){
			return;
		}
		roll = z;
		mechanism.style.transform = "rotate(" + roll + "deg)";

	});
	$.getJSON($SCRIPT_ROOT + '/datapoint/PLANE_PITCH_DEGREES/get', {}, function(data) {
		var x = Math.round(data * (180/Math.PI));
		if ((x > 10) || (x < -10)){
			return;
		}
		pitch =  75+(-5*x);
		ball.style.top = pitch + "px";
	});
}

function displayData(){
	if (temp){
		temp = false;
		//test.classList.remove("on");
	}else{
		temp = true;
		//test.classList.add("on");
	}

}

window.setInterval(function(){
    getSimulatorData();
    displayData();
}, 500);
