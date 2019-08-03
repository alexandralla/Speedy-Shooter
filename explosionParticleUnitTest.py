import unittest
import bug
import explosion

class Test_Explosion_Particle(unittest.TestCase):
    def test_thou_shall_not_pass(self):
        self.assertEqual(3, 4)

#   def __init__(self):
#       self.bug1=None
 
    def setUp(self):
        self.bug1=bug.Bug('bug.png', 100, 100, 0, 0)
 
    def tearDown(self):
        pass
 
    def test_ParticleGoingStraitDown(self):
        particle=explosion.Explosion_Particle(self.bug1, 0, 5)
        particle.update()    
        self.assertEqual(particle.velocityY, 4)

if __name__ == '__main__':
    unittest.main()