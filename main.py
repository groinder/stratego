from stratego.Stratego import Stratego

stratego = Stratego(4)

print('\n'.join([''.join(['{0}'.format(item) for item in row])
      for row in stratego.edges]))