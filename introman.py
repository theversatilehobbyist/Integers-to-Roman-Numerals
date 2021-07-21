def intToRoman(self, num):
     #Integer to Roman Numeral
        x = str(num)
        digitcount = len(str(x))
        
        if num <= 3999 and num >= 1:
            rdictone = {'0' : '', '1' : 'I', '2' : 'II', '3' : 'III', '4' : 'IV', '5' : 'V', '6' : 'VI', '7' : 'VII', '8' : 'VIII', '9' : 'IX'}
            rdicttwo = {'0' : '', '1' : 'X', '2' : 'XX', '3' : 'XXX', '4' : 'XL', '5' : 'L', '6' : 'LX', '7' : 'LXX', '8' : 'LXXX', '9' : 'XC'}
            rdictthree = {'0' : '', '1' : 'C', '2' : 'CC', '3' : 'CCC', '4' : 'CD', '5' : 'D', '6' : 'DC', '7' : 'DCC', '8' : 'DCCC', '9' : 'CM'}
            rdictfour = {'1' : 'M', '2' : 'MM', '3' : 'MMM'}

            if digitcount == 1:
                rnonedigit = rdictone[x[-1]]
                return(rnonedigit)

            elif digitcount == 2:
                rnonedigit = rdictone[x[-1]]
                rntwodigit = rdicttwo[x[-2]]
                return(rntwodigit + rnonedigit)

            elif digitcount == 3:
                rnonedigit = rdictone[x[-1]]
                rntwodigit = rdicttwo[x[-2]]
                rnthreedigit = rdictthree[x[-3]]
                return(rnthreedigit + rntwodigit + rnonedigit)

            elif digitcount == 4:
                rnonedigit = rdictone[x[-1]]
                rntwodigit = rdicttwo[x[-2]]
                rnthreedigit = rdictthree[x[-3]]
                rnfourdigit = rdictfour[x[-4]]
                return(rnfourdigit + rnthreedigit + rntwodigit + rnonedigit)
            
        else:
            return False

            
