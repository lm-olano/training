class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    str = "{}. {}. {}, {}. {}, {}".format(self.artist, self.title, self.medium, self.year, self.owner.name, self.owner.location)
    return str
  
class Marketplace:
  def __init__(self):
    self.listings = []
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  def remove_listing(self, listing):
    self.listings.remove(listing)
  def show_listing(self):
    for el in self.listings:
      print(el)
      
class Client:
  def __init__(self, name, location, wallet, is_museum):
    self.name = name
    self.location = location
    self.wallet = wallet
    self.is_museum = is_museum
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      lst = Listing(artwork, price, self)
      self.wallet += price
      veneer.add_listing(lst)
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      for lst in veneer.listings:
        if lst.art == artwork:
          artwork.owner = self
          self.wallet -= lst.price
          veneer.remove_listing(lst)
      
    
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    str = "{}, {} €".format(self.art.title, self.price)
    return str
    
  
  
               
veneer = Marketplace()
edytta = Client("Edytta Halpirt", "Private Collection", 2e6, False)
moma = Client("The MOMA", "New York", 12e6, True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)

edytta.sell_artwork(girl_with_mandolin, 6e6)
veneer.show_listing()

moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listing()