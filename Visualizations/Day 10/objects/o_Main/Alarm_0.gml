//Plug in
pre_base = base;
switch (ii) div (n/3) {
	case 0:
		base = o_Base;
		break;
	case 1:
		base = o_Base2;
		break;
	case 2:
		base = o_Base3;
		break;
}
if pre_base != base then iii = 0

adapters[# 0, ii].target_x = base.x;
adapters[# 0, ii].target_y = base.y - (16*n/3);
adapters[# 0, ii].state = 2;
adapters[# 0, ii].lerpspeed = 0.2;


ii += 1;
iii += 1;
if ii < n {
	alarm[0] = 4;
	alarm[1] = 3;
} else {
	ds_grid_resize(adapters, 2, n+1);
	adapters[# 0, n] = o_Super_Adapter;
	adapters[# 0, n].target_x = base.x;
	adapters[# 0, n].target_y = base.y - (16*(n)/3) - 16;
	adapters[# 0, n].depth = n - adapters[# 0, n-1]-1;
	adapters[# 0, n].state = 2;
	adapters[# 0, n].lerpspeed = 0.1;
	adapters[# 0, n].future_joltage = adapters[# 0, n-1].joltage + 3;
	adapters[# 1, n] = adapters[# 0, n-1].joltage + 3;
	n++;
}