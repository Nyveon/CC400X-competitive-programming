draw_self()
if not connected then draw_sprite_ext(s_Pins, 0, x, y, image_xscale, image_yscale, 0, c_white, 1);

//Joltage meter
draw_set_halign(fa_center);
draw_set_valign(fa_middle);
draw_set_font(f_Pixel);
draw_set_color(c_black);
draw_text(x, y + 1, joltage);

if state == 4 {
	draw_line(x,y, x-39, y);
	draw_text(x-38, y + 1, "+" + string(diff));
	draw_set_color(c_yellow);
	draw_text(x-39, y, "+" + string(diff));
}