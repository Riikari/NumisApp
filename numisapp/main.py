# -*- coding: utf-8 -*-

from items import Moneda


def main():
    al2002 = Moneda("2 Euros", "Alemania", 2002)

    print("Esta moneda es una de %s de %s, acuñada en %d") % (al2002.getValor(), al2002.getPais(), al2002.getFecha())

if __name__ == "__main__":
    main()