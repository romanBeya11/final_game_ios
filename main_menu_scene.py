
# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
from shop_scene import *
from game_scene import *
from credits_scene import *

import ui


class MainMenuScene(Scene):
    def setup(self):
      # this method is called, when user moves to this scene
		# set background image
		self.background = SpriteNode('./assets/sprites/main_menu_bg.PNG',position = self.size / 2, parent = self, size = self.size)
		
		self.opacity = 0
		
		self.p1_pos = Vector2() 
		self.p1_pos.x = self.size.x / 2
		self.p1_pos.y = self.size.y / 2 + 100     
		self.start_button = SpriteNode('./assets/sprites/play.PNG', position = self.p1_pos, parent = self, size = self.size / 1)
		
		self.p1_pos_1 = Vector2() 
		self.p1_pos_1.x = self.size.x / 2 + 50
		self.p1_pos_1.y = self.size.y / 2 + 100
		self.start_button_1 = SpriteNode('plf:Enemy_Bee' , position = self.p1_pos_1, parent = self, size = self.size / 4, alpha = self.opacity)
		
		self.p1_pos_2 = Vector2() 
		self.p1_pos_2.x = self.size.x / 2 - 100
		self.p1_pos_2.y = self.size.y / 2 + 100 
		self.start_button_2 = SpriteNode('plf:Enemy_Bee' , position = self.p1_pos_2, parent = self, size = self.size / 4, alpha = self.opacity)
		
		self.p1_pos_3 = Vector2() 
		self.p1_pos_3.x = self.size.x / 2 + 200
		self.p1_pos_3.y = self.size.y / 2 + 100
		#self.start_button = SpriteNode('./assets/sprites/play.PNG', position = self.p1_pos_1, parent = self, size = self.size / 8)
		self.start_button_3 = SpriteNode('plf:Enemy_Bee' , position = self.p1_pos_3, parent = self, size = self.size / 4, alpha = self.opacity)
		
		# PLAYER 2!!!!!!!!
		self.p2_pos = Vector2() 
		self.p2_pos.x = self.size.x / 2
		self.p2_pos.y = self.size.y / 2 - 50
		self.shop_button = SpriteNode('./assets/sprites/shop.PNG', position = self.p2_pos, parent = self, size = self.size / 1)
		self.shop_button_1 = SpriteNode('plf:Enemy_FishPink' , position = self.p2_pos, parent = self, size = self.size / 4, alpha = self.opacity) 
	
		self.p2_pos_1 = Vector2() 
		self.p2_pos_1.x = self.size.x / 2 - 100
		self.p2_pos_1.y = self.size.y / 2 - 100
		self.shop_button_2 = SpriteNode('plf:Enemy_FishPink' , position = self.p2_pos_1, parent = self, size = self.size / 4, alpha = self.opacity)
		
		self.p2_pos_2 = Vector2() 
		self.p2_pos_2.x = self.size.x / 2 + 100
		self.p2_pos_2.y = self.size.y / 2 - 100
		self.shop_button_3 = SpriteNode('plf:Enemy_FishPink' , position = self.p2_pos_2, parent = self, size = self.size / 4, alpha = self.opacity)
		
		# PLAYER 3!!!!!!!!	
		self.p3_pos = Vector2() 
		self.p3_pos.x = self.size.x / 2
		self.p3_pos.y = self.size.y / 2 - 100
		self.credits_button = SpriteNode('./assets/sprites/credits.PNG', position = self.p3_pos, parent = self, size = self.size / 1)
		self.credits_button_1 = SpriteNode('plf:Enemy_Frog' , position = self.p3_pos, parent = self, size = self.size / 4, alpha = self.opacity) 
	
		self.p3_pos_1 = Vector2() 
		self.p3_pos_1.x = self.size.x / 2 - 100
		self.p3_pos_1.y = self.size.y / 2 - 300
		self.credits_button_2 = SpriteNode('plf:Enemy_Frog' , position = self.p3_pos_1, parent = self, size = self.size / 4, alpha = self.opacity)
		
		self.p3_pos_2 = Vector2() 
		self.p3_pos_2.x = self.size.x / 2 + 100
		self.p3_pos_2.y = self.size.y / 2 - 300
		self.credits_button_3 = SpriteNode('plf:Enemy_Frog' , position = self.p3_pos_2, parent = self, size = self.size / 4, alpha = self.opacity)                      
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
      if self.start_button_1.frame.contains_point(touch.location) or self.start_button_2.frame.contains_point(touch.location) or self.start_button_3.frame.contains_point(touch.location):
				self.present_modal_scene(GameScene())
		
      if self.shop_button_1.frame.contains_point(touch.location) or self.shop_button_2.frame.contains_point(touch.location) or self.shop_button_3.frame.contains_point(touch.location):
				self.present_modal_scene(ShopScene())
				
      if self.credits_button_1.frame.contains_point(touch.location) or self.credits_button_2.frame.contains_point(touch.location) or self.credits_button_3.frame.contains_point(touch.location):
				#self.present_modal_scene(CreditScene())
				print 'extra credit'
				
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
