fun obradiListu() : Int {
    val brojevi = arrayOf(1, 2, 3, 4, 5)
    var suma = 0

    for (broj in brojevi) {
        if (broj % 2 == 0) {
            suma += broj
        }
    }
    return suma
}
