#!/usr/bin/env python

entero1 = 23  # Type(entero1) daria int
entero2 = 23L  # Type(entero2) daria long
entero3 = 027  # 027 octal = 23 en base 10
entero4 = 0x17  # 0x17 hexadecimal, anteponiendo un 0x
print entero1
print entero2
print entero3
print entero4

real1 = 0.2703
real2 = 0.1e-3
real3 = real1 * real2
print real1
print real2
print real3

complejo = 3 + 2j
complejo2 = -1 + 3j
complejo3 = complejo * complejo2
print complejo
print complejo2
print complejo3

# Operadores
print 2.1 ** 4
print 7.2 // 2

print 10 & 9
print ~7
