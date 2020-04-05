#!/usr/bin/env python3

from math import cos,sin,pi

sheme =  """
     pentagon angles            &                rectangle size included
     angles du pentagone                         taille du rectangle inclus

     360° / 5 = 108°                               ^<------(w)------>^
                                                   |        .        |
       _/\_                                        |     .     .    (hp)
     _/    \_  108/2 = 54° --> (l) * cos(54°)      |  .           .  |
    /        \                                    (h)................v
    \        /                                     |  .            . T
     | (108-90) = 18°     --> (l) * cos(18°)       |    .        .   |
      \____/                                       v<(r)><.(l).><(r)>|


      
        """


def penta_height_from_len(l):
    return l*(cos(2*pi*59/360) +cos(2*pi*18/360))

def penta_len_from_height (h):
    return h/(cos(2*pi*54/360) +cos(2*pi*18/360))

def penta_width_from_len(l):
    return l*sin(2*pi*54/360)*2

# height / hauteur :
# TO BE CHANGED ACCORDING TO THE NEEDED SIZE / A MODIFIER SELON LA TAILLE DEMANDEE
h = 348.0

# penta side length / longueur d'un coté du pentagone : 
l = penta_len_from_height(h)

# max width of the pentagon (laid on one side) / largeur maximale du pentagone (posé sur un coté) :
w = penta_width_from_len(l)

# height shared by the "top" triangle
hp = h * cos(2*pi*54/360) / (cos(2*pi*54/360) +cos(2*pi*18/360))
print(sheme)
print("for/pour h:",h," =>\n l:",l,"\n w:",w,"\n hp:",hp,"\n r:(w/2-l/2):",w/2-l/2,"\n\n BEFORE CUTTING, CHECK THE 5 SIDE LENGTHS OF THE PENTAGON !!\n AVANT DE COUPER, VERIFIER LES 5 LONGUEURS DES COTES DU PENTAGONE !!\n")
