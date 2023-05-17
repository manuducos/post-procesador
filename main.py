import re

def main():
    regex1 = '^Perfil.*'
    regex2 = '^G1 Z0 F2000'
    regex3 = '^.*M3 S1000'

    newFile = ''

    alturaRetraccion = input('Altura de retracción: ')
    tiempoDeBandeo = input('Tiempo de bandeo: ')

    with open('./cortes-plasma.gcode', 'r') as f:
        for line in f:
            result1 = re.search(regex1, line)
            result2 = re.search(regex2, line)
            result3 = re.search(regex3, line)

            if not result1:
                if result2:
                    newFile += ';z-probe\n'
                    newFile += 'G91\n'
                    newFile += 'G38.2 Z-100 F1500\n'
                    newFile += 'G90\n'
                    newFile += 'G10 L20 P1 Z0\n'
                    newFile += 'G91\n'
                    newFile += f'G0 Z{alturaRetraccion}\n'
                    newFile += 'G90\n'
                elif result3:
                    newFile += f'M3 S1000 G4 P{tiempoDeBandeo}\n'
                else:
                    newFile += line
    
    with open('./cortes-plasma.gcode', 'w') as f:
        f.write(newFile)
        

if __name__ == '__main__':
    main()

    # ^Perfil.*