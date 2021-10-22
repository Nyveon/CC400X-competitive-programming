joltage = 0
image_xscale = 2;
image_yscale = 2;
connected = false;
target_x = x;
target_y = y;
state = 1;
diff = 0;
lerpspeed = 0.05;

close = function(a, b) {
	var eps = 8;
	return abs(a - b) < eps 
}