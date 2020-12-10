joltage = "?";
connected = false;
image_xscale = 2.5;
image_yscale = image_xscale;
state = 1;
lerpspeed = 1;
target_x = x;
target_y = y;
depth = -1;

close = function(a, b) {
	var eps = 8;
	return abs(a - b) < eps 
}