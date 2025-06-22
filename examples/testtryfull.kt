fun obradaPodataka(broj: Int) {
    try {
        val rezultat = 100 / broj
        println("Rezultat je $rezultat")
    } catch (e: ArithmeticException) {
        println("Greška: dijeljenje nulom")
    } finally {
        println("Završena obrada.")
    }
}
