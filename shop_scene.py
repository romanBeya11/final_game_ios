# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
from main_menu_scene import *
import ui

class ShopScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        
        # add background color
        self.background = SpriteNode('./assets/sprites/shop_bg.PNG',
        	                           position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
                                     
                                     
                                     
                                      
        back_button_position = self.size
        back_button_position.x = 100
        back_button_position.y = back_button_position.y - 100
        self.back_button = SpriteNode('./assets/sprites/left_button.png',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.40)
                                       
        green_guy_position = self.size
        green_guy_position.x = 510
        green_guy_position.y = green_guy_position.y -350
        self.green_guy = SpriteNode('./assets/sprites/green_guy.PNG',
                                       parent = self,
                                       position = green_guy_position,
                                       scale = 0.5)
        
        purple_guy_position = self.size
        purple_guy_position.x = 510
        purple_guy_position.y = purple_guy_position.y + 1
        self.purple_guy = SpriteNode('./assets/sprites/purple_guy.PNG',
                                       parent = self,
                                       position = purple_guy_position,
                                       scale = 0.5)
                                    
        orange_guy_position = self.size
        orange_guy_position.x = purple_guy_position.x + 10
        orange_guy_position.y = purple_guy_position.y 
        self.orange_guy = SpriteNode('./assets/sprites/red_guy.PNG',
                                       parent = self,
                                       position = orange_guy_position,
                                       scale = 0.5)
                                       
        pink_guy_position = self.size
        pink_guy_position.x = orange_guy_position.x + 10
        pink_guy_position.y = orange_guy_position.y 
        self.pink_guy = SpriteNode('./assets/sprites/yellow_guy.PNG',
                                       parent = self,
                                       position = pink_guy_position,
                                       scale = 0.5)
                                       
        coin_amount_position = self.size / 2
        coin_amount_position.x = purple_guy_position.x + 100
        coin_amount_position.y = coin_amount_position.y + 200
        self.coin_amount = SpriteNode('./assets/sprites/coins.PNG',
                                       parent = self,
                                       position = coin_amount_position,
                                       scale = 0.5)
       
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
