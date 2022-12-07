#Global variables

from sala import sala


def main():
    # Call the function
    sala_1 = sala(18, 23, 24, 25, 8, 7, 1, 12, 16, 20, 21, 26)
    sala_1.control_lampadas(2,1)
    #sala_1.desligar_lampada(2)




# Call the function
if __name__ == '__main__':
    main()