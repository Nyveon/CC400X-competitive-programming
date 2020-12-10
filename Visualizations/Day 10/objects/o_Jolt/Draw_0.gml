draw_sprite_ext(sprite_index, col, x, y, image_xscale, image_yscale, 0, c_white, 1);

//Joltage meter
draw_set_halign(fa_center);
draw_set_valign(fa_middle);
draw_set_font(f_Pixel);
draw_set_color(c_black);
draw_text(x+1, y + 1, diff);
draw_set_color(c_yellow);
draw_text(x, y, diff);