# Software-Engineering-Job-Interview-Full-Mock-Interview

https://youtu.be/1qw5ITr3k9E

https://app.coderpad.io/  

“””
Online cloud reading application
Similar to amazon kindle (for short stories)
We need help designing actual application ( code that implement 
this ) 
A few things looking for: 
Users have a library of books that they can add to or remove from 
Users can set a book from their library as active
The reading application remembers where a user left off in a given book
The reading application only displays a page of text at a time in the active book

All books in library 
Remember active book
Remembers last pages in all books 
Display a page in active book 

Classes:
      - representing a book (Book) 
             - Id: str/int ?
             - title: str
             - pages/content in the book: list of strings (per page) 
             - last page user looked at: int (remember off-by-one)
      - representing a library 
             - collection of books: {id: book()}
             - active book: variable correspond to id
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
Avoid plagiarism 
detect two most likely books that might have plagiarism:
       longest shared common section of text 


“ . i have this book i like to read” . < . base sentence
….^
“she has this book i like to watch”
……^

Bases cases:
….-.match “read” to “read” 
….-.””to non-empty 
“””

‘’’
A..hello world
B..world.
‘’’
# LCS(A,B,3,4)   

def find_longest_substring(stringa, stringb, idxa=0, idxb=0, memo=None): 
                if memo is None: memo = [[-1]  * len(stringb)] * len(stringa)    
                if idxa == len(stringa) or idxb == len(stringb): return 0 
                if memo [idxa] [idxb] != -1 : return memo [idxa] [idxb] 
      possibility_1 = find_longest_substring(stringa, stringb, idxa+1, idxb) 
      possibility_2 find_longest_substring(stringa, stringb, idxa, idxb+1) 
                if stringa [idxa] == stringb [idxb]: 
      possibility_3 = find_longest_substring(stringa, stringb, idxa+1, idxb+1) 
                    +1 

           memo [idxa] [idxb] = max(possi_1, possi_2, possi_3 if applicable) 

           return memo [idxa] [idxb] 
