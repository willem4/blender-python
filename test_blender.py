'''
Created on 8 mei 2015

@author: willem
'''

#----------------------------------------------------------
# File meshes.py
#----------------------------------------------------------
import bpy
 
def createMesh(name, origin, verts, edges, faces):
    # Create mesh and object
    me = bpy.data.meshes.new(name+'Mesh')
    ob = bpy.data.objects.new(name, me)
    ob.location = origin
    ob.show_name = False
    # Link object to scene
    bpy.context.scene.objects.link(ob)
 
    # Create mesh from given verts, edges, faces. Either edges or
    # faces should be [], or you ask for problems
    me.from_pydata(verts, edges, faces)
 
    # Update mesh with new data
    me.update(calc_edges=True)
    return ob
 
def spiralUVs(mesh, xPlus):
    # add a UV layer called "spiral" and make it slanted.
    mesh.uv_textures.new("spiral")
    bm = bmesh.new()
    bm.from_mesh(mesh)

    uv_layer = bm.loops.layers.uv[0]

    nFaces = len(bm.faces)
    for fi in range(nFaces):
        x0 = fi*2/nFaces
        x1 = (fi+1)*2/nFaces
        bm.faces[fi].loops[0][uv_layer].uv = (x0, 0)
        bm.faces[fi].loops[1][uv_layer].uv = (x1, 0)
        bm.faces[fi].loops[2][uv_layer].uv = (xPlus+x1, 1)
        bm.faces[fi].loops[3][uv_layer].uv = (xPlus+x0, 1)
    bm.to_mesh(mesh)
     
def run(origin):
    (x,y,z) = (0.60, 0.80, 0.05)
    verts1 = ((x/2,y/2,-z), (x/2,-y/2,-z), (-x/2,-y/2,-z), (-x/2,y/2,-z), 
              (x/2,y/2,0), (x/2,-y/2,0), (-x/2,-y/2,0), (-x/2,y/2,0))
    #faces1 = ((0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7),(4,5,6,7))
    faces1 = ((4,5,1,0),(5,6,2,1),(6,7,3,2),(7,4,0,3),(7,6,5,4))
    ob1 = createMesh('Solid', origin, verts1, [], faces1)
    
    
    #verts2 = ((x,x,0), (y,-z,0), (-z,y,0))
    #edges2 = ((1,0), (1,2), (2,0))
    #ob2 = createMesh('Edgy', origin, verts2, edges2, [])
 
    # Move second object out of the way
    #ob1.select = False
    #ob2.select = True
    #bpy.ops.transform.translate(value=(0,2,0))
    return


def cleanup():
    
    scene = bpy.context.scene
    
    for ob in scene.objects:
        if ob.type == 'MESH' and ob.name.startswith("Cube"):
            ob.select = True
        else: 
            ob.select = False
    
    bpy.ops.object.delete()
        
def zoom(origin):
    scene = bpy.context.scene
    for ob in scene.objects:
        if ob.name.startswith("Camera"):
            ob.select = True
    bpy.ops.transform.translate(value=(-3.27202, 3.05119, -2.22467), constraint_axis=(False, False, True), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
     
#if __name__ == "__main__":    
cleanup()
origin = (0,0,0)
run(origin)
#zoom(origin)

    
# def main():
#     cube = bpy.data.objects["Cube"]
#     print(cube.name)
#     cube.delta_location = [0,0,10]
#     #bpy.ops.transform.rotate(value=0.530483, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
#     print('Done')
# main()
    
