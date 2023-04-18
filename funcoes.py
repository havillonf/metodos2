#--------------fechadas--------------

def grau_1_fechada(fx, a, b):
  f0 = fx(a)
  f1 = fx(b)
  return ((b - a) / 2) * (f0 + f1)

def grau_2_fechada(fx, a, b):
  dx = (b - a)
  h = dx / 2

  f0 = fx(a)
  f1 = fx(a + h)
  f2 = fx(b)

  return (dx / 6) * (f0 + 4*f1 + f2)

def grau_3_fechada(fx, a, b):
  dx = (b - a)
  h = dx / 3

  f0 = fx(a)
  f1 = fx(a + h)
  f2 = fx(a + 2*h)
  f3 = fx(b)

  result = (dx / 8) * (f0 + 3*f1 + 3*f2 + f3)
  return result

def grau_4_fechada(fx, a, b):
  dx = (b - a)
  h = dx / 4

  f0 = fx(a)
  f1 = fx(a + h)
  f2 = fx(a + 2*h)
  f3 = fx(a + 3*h)
  f4 = fx(b)

  return (dx / 90) * (7*f0 + 32*f1 + 12*f2 + 32*f3 + 7*f4)


#--------------abertas--------------

def grau_1_aberta(fx, a, b):
  dx = (b - a)
  h = dx / 3

  f0 = fx(a + h)
  f1 = fx(a + 2*h)

  return (dx / 2) * (f0 + f1)
  
def grau_2_aberta(fx, a, b):
  dx = (b - a)
  h = dx / 4

  f0 = fx(a + h)
  f1 = fx(a + 2*h)
  f2 = fx(a + 3*h)

  return (dx / 3) * (2*f0 - f1 + 2*f2)

def grau_3_aberta(fx, a, b):
  dx = (b - a)
  h = dx / 5

  f0 = fx(a + h)
  f1 = fx(a + 2*h)
  f2 = fx(a + 3*h)
  f3 = fx(a + 4*h)

  return (dx / 24) * (11*f0 + f1 + f2 + 11*f3)

def grau_4_aberta(fx, a, b):
  dx = (b - a)
  h = dx / 6

  f0 = fx(a + h)
  f1 = fx(a + 2*h)
  f2 = fx(a + 3*h)
  f3 = fx(a + 4*h)
  f4 = fx(a + 5*h)

  return (dx / 20) * (11*f0 - 14*f1 + 26*f2 - 14*f3 + 11*f4)