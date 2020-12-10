/// Sort
ds_grid_sort(adapters, 1, true);
for (i = 0; i < n; i++) {
	adapters[# 0, i].target_x = anchor_x + (i mod 10)*spacing;
	adapters[# 0, i].target_y = anchor_y + (i div 10)*spacing;
}
state = "Step 1: Sort input";