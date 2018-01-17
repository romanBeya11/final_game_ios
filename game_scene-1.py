from scene import *
from main_menu_scene import *
import sound
import random
import math
import time
A = Action

class GameScene (Scene):
	def setup(self):
		# Setting up the background
		self.screen_center_x = self.size.x / 2
		self.screen_center_y = self.size.y / 2
		self.bg_pos = Vector2(self.screen_center_x, self.screen_center_y)
		background = SpriteNode(color = 'midnightblue', position = self.bg_pos, parent = self, size = self.size)
		
		# Boundary Detection
		# Setting the ground height
		self.height_of_ground = 35
		# Setting the top of screen boundary
		self.top_of_screen_boundary = 750
		# Left side of screen
		self.left_side_of_screen_boundary = self.screen_center_x - 480
		# Right side of screen
		self.right_side_of_screen_boundary = 980
		
		# Creating player sprite
		self.player_position = Vector2()
		self.player_position.x = self.screen_center_x - 200
		self.player_position.y = self.screen_center_y - 200
		self.player = SpriteNode('plf:HudPlayer_pink', position = self.player_position, parent = self, size = self.size / 10)
		
		# HIT COUNTER FOR COINS
		self.coin_intersect = 0
		self.score_label = Vector2()
		self.score_label.x = 700
		self.score_label.y = 640
		self.score = LabelNode(text = "Coins: 0", position = self.score_label, parent = self, font = ("Copperplate", 40))
		
		self.enemy_pos = Vector2()
		self.enemy_pos.x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		self.enemy_pos.y = random.randint(self.height_of_ground, self.score_label.y - 30)
		self.enemy = SpriteNode('plf:Enemy_Saw_move', position = self.enemy_pos, parent = self, size = self.size / 12) 
		
		'''# Creating random positions for the coins
		random_coin_coordinate_x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		random_coin_coordinate_y = random.randint(self.height_of_ground, self.score_label.y - 30)
		self.coin_position = Vector2()
		self.coin_position.x = random_coin_coordinate_x
		self.coin_position.y = random_coin_coordinate_y
		self.coin = SpriteNode('plf:Item_CoinGold', position = self.coin_position, parent = self, size = self.size / 13) #/15'''
		self.create_new_coin()
		
		
		
		
		
		self.left_button_pos = Vector2()
		self.left_button_pos.x = self.screen_center_x - 450
		self.left_button_pos.y = self.screen_center_y - 300
		self.left_button = SpriteNode('./assets/sprites/left_button.png', position = self.left_button_pos, parent = self, size = self.size / 12)
		
		self.right_button_pos = Vector2()
		self.right_button_pos.x = self.screen_center_x - 160
		self.right_button_pos.y = self.screen_center_y - 300
		self.right_button = SpriteNode('./assets/sprites/right_button.png', position = self.right_button_pos, parent = self, size = self.size / 12)
		
		self.up_button_pos = Vector2()
		self.up_button_pos.x = self.screen_center_x - 200
		self.up_button_pos.y = self.screen_center_y - 450
		self.up_button = SpriteNode('./assets/sprites/left_button.png', position = self.up_button_pos, parent = self, size = self.size / 12)
		
		
		
		
		
		
		
		
		'''self.tutorial()
		#self.skip_tutorial()
		self.star_animation()
		self.how_to_move_up_tutorial()
		self.how_to_move_down_tutorial()
		self.how_to_move_left_tutorial()
		self.how_to_move_right_tutorial()
		self.collect_coins_tutorial()
		self.avoid_enemies_tutorial()'''
		#self.show_hearts()
		#self.create_new_coin()
		#self.create_new_enemy()
		#self.special_boxes()
		#self.retrieve_high_score()
		self.enemy_cross_path = 0
		self.begin_main_thread = False
		self.tutorials_completed = 0
		self.number_of_hearts = 3
		self.skip_tutorial_scenes = False
		self.high_score_array = []
		
	def did_change_size(self):
		pass
		
		
	def tutorial(self):
		self.tutorial_label = Vector2()
		self.tutorial_label.x = self.screen_center_x
		self.tutorial_label.y = self.screen_center_y
		self.tutorial = LabelNode(text = "Tap with one finger", position = self.tutorial_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5)
		self.tutorial_fade = True
			
	def how_to_move_up_tutorial(self):
		self.tutorial_up_label = Vector2()
		self.tutorial_up_label.x = self.screen_center_x
		self.tutorial_up_label.y = self.screen_center_y 
		self.tutorial_up = LabelNode(text = "Tap Upwards To Ascend", position = self.tutorial_up_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
		
	def how_to_move_down_tutorial(self):
		self.tutorial_down_label = Vector2()
		self.tutorial_down_label.x = self.screen_center_x
		self.tutorial_down_label.y = self.screen_center_y
		self.tutorial_down = LabelNode(text = "Tap Downwards To Descend", position = self.tutorial_down_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
		
	def how_to_move_left_tutorial(self):
		self.tutorial_left_label = Vector2()
		self.tutorial_left_label.x = self.screen_center_x
		self.tutorial_left_label.y = self.screen_center_y
		self.tutorial_left = LabelNode(text = "Tap Left To Jump To The Left", position = self.tutorial_left_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
	
	def how_to_move_right_tutorial(self):
		self.tutorial_right_label = Vector2()
		self.tutorial_right_label.x = self.screen_center_x
		self.tutorial_right_label.y = self.screen_center_y
		self.tutorial_right = LabelNode(text = "Tap Right To Jump To The Right", position = self.tutorial_right_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
	
	def collect_coins_tutorial(self):
		self.collect_coins_label = Vector2()
		self.collect_coins_label.x = self.screen_center_x
		self.collect_coins_label.y = self.screen_center_y
		self.collect_coins = LabelNode(text = "Collect Coins", position = self.collect_coins_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
		
	def avoid_enemies_tutorial(self):
		self.avoid_enemies_label = Vector2()
		self.avoid_enemies_label.x = self.screen_center_x
		self.avoid_enemies_label.y = self.screen_center_y
		self.avoid_enemies = LabelNode(text = "Avoid Enemies", position = self.avoid_enemies_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
		
	def star_animation(self):
		self.star_pos = Vector2()
		self.star_pos.x = self.score_label.x + 120
		self.star_pos.y = self.score_label.y + 5
		self.star = SpriteNode('plf:Item_Star', position = self.star_pos, parent = self, size = self.size / 
		12, alpha = 0)
			
	def increment_score(self):
		self.coin_intersect = self.coin_intersect + 1
		self.score.text = "Coins: " + str(self.coin_intersect)
		sound.play_effect('rpg:HandleCoins')
		if self.coin_intersect % 10 == 0:
			#for i in range(3):
				#self.create_new_enemy()
			self.star_animation()
			self.special_box.run_action(Action.fade_to(1, 1))
			self.special_boxes()
		else:
			self.star.run_action(Action.fade_to(0, 1))
			
	def decrement_score(self):
		self.coin_intersect = self.coin_intersect - 2
		self.score.text = "Coins: " + str(self.coin_intersect)
		sound.play_effect('rpg:HandleCoins2')
		if self.coin_intersect <= 3:
			self.score.color = .87, -.41, -.15
		if self.coin_intersect >= 4:
			self.score.color = 1.0, 1.0, 1.0
		if self.coin_intersect < 0:
			self.coin_intersect = 0
			self.score.text = "Coins: " + str(self.coin_intersect)
			self.score.color = .87, .29, .29
		#elif self.coin_intersect < 0 and self.number_of_hearts <= 0:
			self.game_over()
			
	def game_over(self):
		self.score.alpha = 0
		self.score_label.x = self.screen_center_x
		self.score_label.y = self.screen_center_y
		self.score.run_action(Action.move_to(self.score_label.x, self.score_label.y, 5))
		self.score.run_action(Action.fade_to(1, 3))
		self.score.font = ("Copperplate", 60)
		#self.score.text = "Game Over: " + str(self.current_high_score)
		self.score.color = (1.0, .0, .0)
		sound.play_effect('rpg:Chop')
		self.enemy.run_action(Action.fade_to(0, 3))
		self.player.run_action(Action.fade_to(0, 3))
		self.new_coin.run_action(Action.fade_to(0, 3))
		#self.increment_high_score()
		self.begin_main_thread = False
			
	def create_new_coin(self):
		# Creating random positions for the coins
		self.new_coin_position = Vector2()
		self.new_coin_position.x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		self.new_coin_position.y = random.randint(self.height_of_ground, self.top_of_screen_boundary)
		self.new_coin = SpriteNode('plf:Item_CoinGold', position = self.new_coin_position, parent = self, size = self.size / 13) #/15
	
	def move_coin(self):
		random_coin_coordinate_x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		random_coin_coordinate_y = random.randint(self.height_of_ground, self.score_label.y - 30)
		if self.new_coin_position.x <= self.size.x:
			self.new_coin.run_action(Action.move_to(random_coin_coordinate_x, random_coin_coordinate_y, 5)) 
		elif self.coin_position.x >= self.size.x:
			self.new_coin.run_action(Action.move_to(random_coin_coordinate_x, random_coin_coordinate_y, 5)) 	
		elif self.new_coin_position.x <= self.size.y:
			self.new_coin.run_action(Action.move_to(random_coin_coordinate_x, random_coin_coordinate_y, 5)) 		
		elif self.new_coin_position.x >= self.size.y:
			self.new_coin.run_action(Action.move_to(self.left_side_of_screen_boundary, self.top_of_screen_boundary, 5)) 		
				
	def coin_to_player_intersection(self):
		#if self.player.frame.intersects(self.coin.frame):
		if self.player.frame.contains_point(self.new_coin.frame):
			self.new_coin.remove_from_parent()
			self.create_new_coin()
			self.increment_score()
			self.increment_high_score()
			#self.create_new_enemy()	
			
	def create_new_enemy(self):
		self.new_enemy_pos = Vector2()
		self.new_enemy_pos.x = 100
		self.new_enemy_pos.y = 100
		self.new_enemy = SpriteNode('plf:Enemy_Saw_move', position = self.new_enemy_pos, parent = self.enemy, size = self.size / 12) 
				
	def move_enemies(self):
		self.enemy.run_action(Action.move_to(self.player_position.x, self.player_position.y, 5))
			
	def enemy_intersect(self):
		if self.player.frame.contains_point(self.enemy.frame):
			self.decrement_score()
			#self.player_respawn()
			#self.create_new_enemy()
			self.enemy_cross_path = self.enemy_cross_path + 1
			if self.enemy_cross_path == 1:
				self.heart_3.run_action(Action.fade_to(0, 1))
				self.heart_sprite_4 = Vector2()
				self.heart_sprite_4.x = 340
				self.heart_sprite_4.y = 700
				self.heart_4 = SpriteNode('plf:HudHeart_half', position = self.heart_sprite_4, parent = self, size = self.size / 14)
				sound.play_effect('rpg:Chop')
			elif self.enemy_cross_path == 2:
				self.heart_4.run_action(Action.fade_to(0, 1))
				self.heart_sprite_5 = Vector2()
				self.heart_sprite_5.x = 340
				self.heart_sprite_5.y = 700
				self.heart_5 = SpriteNode('plf:HudHeart_empty', position = self.heart_sprite_5, parent = self, size = self.size / 14)
				sound.play_effect('rpg:Chop')
			elif self.enemy_cross_path == 3:
				self.heart_5.run_action(Action.fade_to(0, 1))
				sound.play_effect('rpg:Chop')
			elif self.enemy_cross_path == 4:
				self.heart_2.run_action(Action.fade_to(0, 1))
				self.heart_sprite_6 = Vector2()
				self.heart_sprite_6.x = 270
				self.heart_sprite_6.y = 700
				self.heart_6 = SpriteNode('plf:HudHeart_half', position = self.heart_sprite_6, parent = self, size = self.size / 14)
				sound.play_effect('rpg:Chop')
			elif self.enemy_cross_path == 5:
				self.heart_6.run_action(Action.fade_to(0, 1))
				self.heart_sprite_7 = Vector2()
				self.heart_sprite_7.x = 270
				self.heart_sprite_7.y = 700
				self.heart_7 = SpriteNode('plf:HudHeart_empty', position = self.heart_sprite_7, parent = self, size = self.size / 14)
			elif self.enemy_cross_path == 6:
				self.heart_7.run_action(Action.fade_to(0, 1))
			elif self.enemy_cross_path == 7:
				self.heart_1.run_action(Action.fade_to(0, 1))
				self.heart_sprite_8 = Vector2()
				self.heart_sprite_8.x = 200
				self.heart_sprite_8.y = 700
				self.heart_8 = SpriteNode('plf:HudHeart_half', position = self.heart_sprite_8, parent = self, size = self.size / 14)
			elif self.enemy_cross_path == 8:
				self.heart_8.run_action(Action.fade_to(0, 1))
				self.heart_sprite_9 = Vector2()
				self.heart_sprite_9.x = 200
				self.heart_sprite_9.y = 700
				self.heart_9 = SpriteNode('plf:HudHeart_empty', position = self.heart_sprite_9, parent = self, size = self.size / 14)
			elif self.enemy_cross_path == 9:
				self.heart_9.run_action(Action.fade_to(0, 1))
				#self.number_of_hearts = 0
				#self.game_over()
			
	def intiate_gravity(self):
		# GRAVITY STARTS HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		if self.player_position.y == self.height_of_ground:
			self.player_position.y = self.height_of_ground
		else:
			if self.player_position.y >= self.score_label.y - 30:
				self.player_position.y = self.score_label.y - 30
			if self.player_position.x >= self.right_side_of_screen_boundary:
				self.player_position.x = self.right_side_of_screen_boundary
			if self.player_position.x <= self.left_side_of_screen_boundary:
				self.player_position.x = self.left_side_of_screen_boundary
			
			# Find the distance between the ground and the players current pos
			distance_to_grnd = self.player_position.y - self.height_of_ground
			if distance_to_grnd <= self.height_of_ground + 20:
				descend = self.player_position.y = self.player_position.y - 2
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					#self.player_position.x = self.screen_center_x
					self.player_position.y = self.height_of_ground
					#print 'reset NOW'
			elif distance_to_grnd >= self.height_of_ground + 100:
				descend = self.player_position.y = self.player_position.y - 5
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					#self.player_position.x = self.screen_center_x
					self.player_position.y = self.height_of_ground
					#print 'reset NOW'
			else:
				descend = self.player_position.y = self.player_position.y - 8
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					#self.player_position.x = self.screen_center_x
					self.player_position.y = self.height_of_ground
		
	def update(self):
		#if self.begin_main_thread == True:
			self.intiate_gravity()
			self.move_coin()
			self.coin_to_player_intersection()
			self.move_enemies()
			self.enemy_intersect()
		#else:
			#self.begin_main_thread = False
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		#self.enemy.run_action(Action.move_to(touch.location.x, touch.location.y))
		pass
		
	def touch_ended(self, touch):
		# Fade away the tutorial
			'''self.tutorials_completed = self.tutorials_completed + 1
			if self.tutorials_completed == 1:
				self.tutorial.run_action(Action.fade_to(0, 1))
			elif self.tutorials_completed == 2:
				self.tutorial_up.run_action(Action.fade_to(1, 1))
			elif self.tutorials_completed == 3:
				self.tutorial_up.run_action(Action.fade_to(0, 1))
			elif self.tutorials_completed == 4:
				self.tutorial_down.run_action(Action.fade_to(1, 1)) 
			elif self.tutorials_completed == 5:
				self.tutorial_down.run_action(Action.fade_to(0, 1)) 
			elif self.tutorials_completed == 6:
				self.tutorial_left.run_action(Action.fade_to(1, 1)) 
			elif self.tutorials_completed == 7:
				self.tutorial_left.run_action(Action.fade_to(0, 1)) 
			elif self.tutorials_completed == 8:
				self.tutorial_right.run_action(Action.fade_to(1, 1)) 
			elif self.tutorials_completed == 9:
				self.tutorial_right.run_action(Action.fade_to(0, 1)) 
			elif self.tutorials_completed == 10:
				self.collect_coins.run_action(Action.fade_to(1, 1)) 
			elif self.tutorials_completed == 11:
				self.collect_coins.run_action(Action.fade_to(0, 1)) 
			elif self.tutorials_completed == 12:
				self.avoid_enemies.run_action(Action.fade_to(1, 1)) 
			elif self.tutorials_completed == 13:
				self.avoid_enemies.run_action(Action.fade_to(0, 1)) 
				# Begin Main Thread
				self.begin_main_thread = True
			if self.begin_main_thread == True:'''
			x = self.player_position.x = touch.location.x
			y = self.player_position.y = touch.location.y
			self.player.run_action(Action.move_by(x, y, 0.5))
			if x <= self.left_side_of_screen_boundary:
				x = self.left_side_of_screen_boundary
			elif x >= self.right_side_of_screen_boundary:
				x = self.right_side_of_screen_boundary
			elif y <= self.height_of_ground:
				y = self.height_of_ground
			elif y >= self.score_label:
				y = self.score_label - 30
			#else: 
				#self.begin_main_thread = False
			
if __name__ == '__main__':
	run(GameScene(), multi_touch = False, orientation = LANDSCAPE, show_fps=True)
