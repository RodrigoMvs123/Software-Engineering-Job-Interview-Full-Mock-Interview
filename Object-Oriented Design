“””

class book:
        def __init__(self, id, title, content):
              self.id = id
              self.title = title 
              self.content = content # now just a long string of chars
              self.last_page = 0

              self.font_size = 12 
              self.chars_per_page = calculate (self.font_size) 

        def display_page(self):
              start_idx = self.char_per_page * self.last_page 
              idx = start_idx + self.char_per_page
              return self.content [start_idx:end_idx ] 
              # return self.content [self.last_page]
 
        def turn_page(self): 
              self.last_page += 1 
              return self display_page()
              

class Library: 
        def__init__(self): 
               self.collection = dict() 
               self.active_book = None
               self.id_counter = 0
          
         def add_to_collection(self, title, content):
               new_book = Book(self.id_counter, title, content) 
               self.collection [new_book.id] = new_book 
               self.id_counter += 1       

          def remove_from_collection (self, id): 
               del self.collection[id] 

          def set_active_book(self,id): 
               self.activ_book = id 

          def display_page(self):
               return self.collection [self.active_book].display_page()

          def turn_page(self):
               return self.collection [self.active_book].turn_page()




“””
