//Move towards target


x = lerp(x, target_x, lerpspeed);
y = lerp(y, target_y, lerpspeed);



if state == 2 {
	if close(y, target_y) and close(x, target_x) {
		y -= 4;
		target_y -= 4;
		state = 3;
		connected = true;
	}
}
