badge.eink_init()
badge.display_picture(0,-1)
ugfx.init()
ugfx.demo("HACKING")
ugfx.clear(badge.BLACK)
ugfx.thickline(1,1,100,100,badge.WHITE,10,5)
ugfx.box(30,30,50,50,badge.WHITE)
ugfx.string(150,25,"STILL","Roboto_BlackItalic24",badge.WHITE)
ugfx.string(130,50,"Hacking","PermanentMarker22",badge.WHITE)
length = ugfx.get_string_width("Hacking","PermanentMarker22")
ugfx.line(130, 72, 144 + length, 72, badge.WHITE)
ugfx.line(140 + length, 52, 140 + length, 70, badge.WHITE)
ugfx.string(140,75,"Anyway","Roboto_BlackItalic24",badge.WHITE)
ugfx.flush()

