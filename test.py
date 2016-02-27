from pysynfig.reader import XmlParser
import pdb
p = XmlParser("rubinetto_gio.sif")
p.parse()
p.getLayers(p.tree, p.listLayer)

list = p.getListLayers()

zero = list[0]

#attributes
zero.setActive("active_changed")
zero.setType("type_changed")
zero.setExcludeFromRendering("exclude_from_rendering_changed")
zero.setVersion("version_changed")
zero.setDesc("desc_changed")


#tag param
z = zero.getParam("z_depth")
z.setValue("z_depth_value_changed")

amount = zero.getParam("amount")
amount.setValue("amount_value_changed")

blend_method = zero.getParam("blend_method")
blend_method.setValue("blend_method_value_changed")
blend_method.setStatic("blend_method_static_changed")

origin = zero.getParam("origin")
origin.setVectorX("x_origin_value_changed")
origin.setVectorY("y_origin_value_changed")

#tag in transformation
transformation = zero.getParam("transformation")
composite = transformation.getComposite()
offset = composite.getOffset()
offset.setVectorX("x_offset_value_changed")
offset.setVectorY("y_offset_value_changed")

angle = composite.getAngle()
angle.setValue("angle_value_changed")

skew_angle = composite.getSkewAngle()
skew_angle.setValue("skew_angle_value_changed")

scale = composite.getScale()
scale.setVectorX("x_scale_value_changed")
scale.setVectorY("y_scale_value_changed")

#tag canvas in transformation
canvas = zero.getParam("canvas")
layers_canvas = canvas.getLayers()
zero_canvas = layers_canvas[0]
#from  here you can use the above method to change attributes|param|subtag for the canvas: example below z_depth
z_canvas = zero_canvas.getParam("z_depth")
z_canvas.setValue("canvas_z_depth_value_changed")

amount_canvas = zero_canvas.getParam("amount")
amount_canvas.setValue("canvas_amount_value_changed")

blend_method_canvas = zero_canvas.getParam("blend_method")
blend_method_canvas.setValue("canvas_blend_method_value_changed")
blend_method_canvas.setStatic("canvas_blend_method_static_changed")

tl = zero_canvas.getParam("tl")
tl.setVectorX("canvas_x_tl_value_changed")
tl.setVectorY("canvas_y_tl_value_changed")

br = zero_canvas.getParam("br")
br.setVectorX("canvas_x_br_value_changed")
br.setVectorY("canvavs_y_br_value_changed")

c = zero_canvas.getParam("c")
c.setValue("canvas_c_value_changed")
c.setStatic("canvas_c_static_changed")

gamma_adjust = zero_canvas.getParam("gamma_adjust")
gamma_adjust.setValue("canvas_gamma_adjust_value_changed")

filename = zero_canvas.getParam("filename")
filename.setText("canvas_filename_value_changed")

time_offset = zero_canvas.getParam("time_offset")
time_offset.setValue("canvas_time_offset_value_changed")
#
time_dilation = zero.getParam("time_dilation")
time_dilation.setValue("time_dilation_value_changed")

time_offset = zero.getParam("time_offset")
time_offset.setValue("time_offset_value_changed")

children_lock = zero.getParam("children_lock")
children_lock.setValue("children_lock_value_changed")
children_lock.setStatic("childre_lock_static_changed")

outline_grow = zero.getParam("outline_grow")
outline_grow.setValue("outline_grow_value_changed")

layer_name = zero.getParam("layer_name")
layer_name.setText("layer_name_value_changed")

p.tree.write("prova.xml")


