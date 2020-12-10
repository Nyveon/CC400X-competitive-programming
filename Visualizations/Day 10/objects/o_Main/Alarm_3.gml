var inst = instance_create_depth(adapters[# 0, ii].x - 39 , adapters[# 0, ii].y, ii, o_Jolt);
ds_list_add(circles, inst);
inst.diff = adapters[# 0, ii].diff;
inst.target_x = anchor_x + (ii mod 10)*spacing
inst.target_y = anchor_y + (ii div 10)*spacing
instance_destroy(adapters[# 0, ii]);
inst.image_xscale = 2;
inst.image_yscale = 2;

ii++;
if ii < n {
	alarm[3] = 3;
}