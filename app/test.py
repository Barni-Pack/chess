class Bishop():
  def get_moves(self):
    print('bishop')
    
class Rook():
  def get_moves(self):
    print('rook')
    
class Queen():
  def get_moves(self):
    Bishop.get_moves(self)
    Rook.get_moves(self)

q = Queen()

# q.get_moves()