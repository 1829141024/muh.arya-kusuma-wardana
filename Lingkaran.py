class lingkaran(object):
   def __init__(self, p, r):
      self.phi = p
      self.jarijari = r
   def hitungkeliling(self):
      return 2* self.phi * self.jarijari 
   def rumusluas(self):
      return self.phi * self.jarijari * self.jarijari
def main():
   lingkaran1 = lingkaran(3.14, 12)
   print(' SELAMAT DATANG DI DALAM PROGRAM KAMI!!!')
   print('\n')
   print(' RUMUS KELILING LINGKARAN ')
   print('|===============================|')
   print('|        {lingkaran 1}          |')
   print('|===============================|')
   print('| phi        :', lingkaran1.phi,'\t\t|')
   print('| jari-jari  :', lingkaran1.jarijari,'\t\t|')
   print('| Keliling lingkaran =', lingkaran1.hitungkeliling(),'\t|')
   print('|===============================|')
   print('|         TERIMA KASIH !!!      |')
   print('|===============================|')
   lingkaran2 = lingkaran(3.14, 8)

   print('\n')
   print('|===============================|')
   print('|        {lingkaran 2}          |')
   print('|===============================|')
   print('| phi        :', lingkaran2.phi,'\t\t|')
   print('| jari-jari  :', lingkaran2.jarijari,'\t\t|')
   print('| Keliling lingkaran =', lingkaran2.hitungkeliling(),'\t|')
   print('|===============================|')
   print('|         TERIMA KASIH !!!      |')
   print('|===============================|')

   print('\n')
   
   lingkaran1 = lingkaran(3.14, 20)
   print(' RUMUS LUAS LINGKARAN ')
   print('\n')
   print('|===============================|')
   print('|        {lingkaran 1}          |')
   print('|===============================|')
   print('| phi       : ', lingkaran1.phi ,'\t\t|')
   print('| jari-jari : ', lingkaran1.jarijari,'\t\t|')
   print('| Luas lingkaran  = ', lingkaran1.rumusluas(),'\t|')
   print('|===============================|')
   print('|         TERIMA KASIH !!!      |')
   print('|===============================|')
   lingkaran2 = lingkaran(3.14, 18)

   print('\n')
   print('|===============================|')
   print('|        {lingkaran 2}          |')
   print('|===============================|')
   print('| phi       : ', lingkaran2.phi ,'\t\t|')
   print('| jari-jari : ', lingkaran2.jarijari,'\t\t|')
   print('| Luas lingkaran  = ', lingkaran2.rumusluas(),'\t|')
   print('|===============================|')
   print('|         TERIMA KASIH !!!      |')
   print('|===============================|')
if __name__ == "__main__":
   main()
