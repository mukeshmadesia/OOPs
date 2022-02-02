class mobile:
    def purchase(self,brand,ram,rom):
        #print('Thanks for Purchase')
            print('thanks for purchase',brand, 'ram', ram, 'with',rom,'rom')


khushbu = mobile()

##step 2
khushbu.brand = 'Apple'
khushbu.ram = '2GB'
khushbu.rom = '16gb'
#khushbu.purchase()
khushbu.purchase(khushbu.brand,khushbu.ram,khushbu.rom)

mukesh = mobile()

mukesh.brand = 'Samsung'
mukesh.ram = '2GB'
mukesh.rom = '16gb'

khushbu.purchase(mukesh.brand,mukesh.ram,mukesh.rom)

mukesh.purchase(mukesh.brand,mukesh.ram,mukesh.rom)
