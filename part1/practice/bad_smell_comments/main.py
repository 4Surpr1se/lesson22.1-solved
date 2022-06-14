class Unit:
    def movement(self, field, cor_x: int, cor_y: int, direction, is_fly: bool, is_cradetcya: bool, speed = 1):
        if is_fly and is_cradetcya:  
            raise ValueError('Рожденный ползать летать не должен!')
    
        if is_fly: 
            speed *= 1.2
            if direction == 'UP': 
                new_y = cor_y + speed   
                new_x = cor_x  
            elif direction == 'DOWN':  
                new_y = cor_y - speed  
                new_x = cor_x  
            elif direction == 'LEFT':  
                new_y = cor_y  
                new_x = cor_x - speed 
            elif direction == 'RIGHT':  
                new_y = cor_y  
                new_x = cor_x + speed 
        if is_cradetcya:
            speed *= 0.5
            if direction == 'UP':  
                new_y = cor_y + speed  
                new_x = cor_x  
            elif direction == 'DOWN':  
                new_y = cor_y - speed  
                new_x = cor_x  
            elif direction == 'LEFT':  
                new_y = cor_y  
                new_x = cor_x - speed  
            elif direction == 'RIGHT':  
                new_y = cor_y  
                new_x = cor_x + speed  

            field.set_unit(x=new_x, y=new_y, unit=self)
