from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from UrsinaLighting import *
# from ursina.shaders import ssao_shader, lit_with_shadows_shader


labyrinth = Ursina()

#Window Settings
window.title = 'Labyrinth'
window.borderless = False
window.exit_button.visible = False
vsync = False

#Mood
#camera.shader =  ssao_shader
#soundtrack = Audio('scarymusic', loop = True)
scene.fog_density = 0.07
scene.fog_color = color.rgb(4, 4, 4)


#first person
player = FirstPersonController()
player.scale_y = 1.8
player.rotation = Vec3(0, 80, 0)
player.position = Vec3(-181.651, -0.156022, 155.144)
player.speed = 3



#Entities
ceiling = Entity(model = 'cube',
                 texture = 'ceiling',
                 scale_x = 300,
                 scale_z = 300,
                 rotation = Vec3(0, 0, 0),
                 position = Vec3(-70,10,60),
                 texture_scale = (50,50))

start = Entity(model = 'start',
               texture = 'wall_diff',
               texture_scale = (1,1),
               position = Vec3(-180, 4, 152),
               scale = 3,
               scale_y = 4,
               rotation = Vec3(0, 90, 0),
               collider = 'mesh')


maze_texture = Texture("Models & Textures/wall_diff.jpg")
maze_norm = Texture("Models & Textures/wall_norm.exr")
maze_spec = Texture("Models & Textures/wall_spec.jpg")

maze = Entity(model = 'maze',
              position = Vec3(0,10,0),
              collision = True,
              texture = "empty",
              collider = 'mesh'
              )

lit_maze = LitObject(model = 'maze',
                     texture = maze_texture,
                     position = Vec3(0,10,0),
                     texture_scale = (50,50),
                     specularMap = maze_spec,
                     normalMap = maze_norm,
                     tiling = Vec2(50, 50)
                     )

pointLight = LitPointLight(position = player.position, intensity = 2)

#sun = LitDirectionalLight(direction = Vec3(-1, -0.2, -0.5), color = rgb(255, 255, 166))



ground = Entity(model = 'plane',
                scale = (1000,1,1000),
                texture = 'mud_diff',
                texture_scale = (100,100),
                collider = 'box')

fpsview = Entity(model = 'quad',
                 parent = camera.ui,
                 texture = 'torchon',
                 scale_x = 2)

def update():
    if held_keys['shift'] and held_keys['w']:
        player.speed = 7
    else:
        player.speed = 3


        
#EditorCamera()
Sky()
labyrinth.run()
