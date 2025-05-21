class Cuenta:
    def __init__(self, saldo: float, tasa_anual: float):
        self._saldo = saldo
        self._numero_consignaciones = 0
        self._numero_retiros = 0
        self._tasa_anual = tasa_anual
        self._comision_mensual = 0.0

    def consignar(self, cantidad: float):
        self._saldo += cantidad
        self._numero_consignaciones += 1

    def retirar(self, cantidad: float):
        nuevo_saldo = self._saldo - cantidad
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo
            self._numero_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
        tasa_mensual = self._tasa_anual / 12
        interes_mensual = self._saldo * tasa_mensual
        self._saldo += interes_mensual

    def extracto_mensual(self):
        self._saldo -= self._comision_mensual
        self.calcular_interes()

    def imprimir(self):
        print(f"Saldo: ${self._saldo:.2f}")
        print(f"Comisión mensual: ${self._comision_mensual:.2f}")
        print(f"Número de transacciones: {self._numero_consignaciones + self._numero_retiros}")


class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self._activa = saldo >= 10000

    def consignar(self, cantidad: float):
        if self._activa:
            super().consignar(cantidad)

    def retirar(self, cantidad: float):
        if self._activa:
            super().retirar(cantidad)

    def extracto_mensual(self):
        if self._numero_retiros > 4:
            self._comision_mensual += (self._numero_retiros - 4) * 1000
        super().extracto_mensual()
        self._activa = self._saldo >= 10000

    def imprimir(self):
        print("Cuenta de ahorros")
        super().imprimir()
        print(f"Estado: {'Activa' if self._activa else 'Inactiva'}")


class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self._sobregiro = 0.0

    def retirar(self, cantidad: float):
        resultado = self._saldo - cantidad
        if resultado < 0:
            self._sobregiro -= resultado
            self._saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        if self._sobregiro > 0:
            residuo = self._sobregiro - cantidad
            if residuo > 0:
                self._sobregiro = 0
                self._saldo = residuo
            else:
                self._sobregiro = -residuo
                self._saldo = 0
        else:
            super().consignar(cantidad)

    def imprimir(self):
        print("Cuenta corriente")
        super().imprimir()
        print(f"Sobregiro: ${self._sobregiro:.2f}")


def main():
    print("Cuenta de ahorros")
    saldo_inicial = float(input("Ingrese saldo inicial: $"))
    tasa = float(input("Ingrese tasa de interés: "))
    
    cuenta_ahorros = CuentaAhorros(saldo_inicial, tasa)
    
    cantidad = float(input("Ingrese cantidad a consignar: $"))
    cuenta_ahorros.consignar(cantidad)
    
    cantidad = float(input("Ingrese cantidad a retirar: $"))
    cuenta_ahorros.retirar(cantidad)
    
    cuenta_ahorros.extracto_mensual()
    cuenta_ahorros.imprimir()


if __name__ == "__main__":
    main()
