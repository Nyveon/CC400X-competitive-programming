if ii != 0 {
	adapters[# 0, ii].diff = adapters[# 1, ii] - adapters[# 1, ii-1];
} else {
	adapters[# 0, ii].diff = 0;
}
adapters[# 0, ii].state = 4;

ii++;
if ii < n {
	alarm[2] = 2;
}
