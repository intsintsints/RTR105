#!/usr/bin/python
# -*- coding: utf-8 -*-

a = input("Cien. liet., lūdzu, ievadi skaitli: ")
# 3. python'ā visi input rezultāti ir ar str tipu 
# tāpēc ievadītā lieluma datu tips vēlāk ir jāpārveido
a = int(a)

# python valoda balstās uz C valodas => print strādā līdzīgi printf
# https://www.cplusplus.com/reference/cstdio/printf/
print("Liet., Tu esi ievadījis skaitli: %d"%(a))
aa = a * a 
print("Tavs skaitlis kvadrātā ie: %d"%(aa))

