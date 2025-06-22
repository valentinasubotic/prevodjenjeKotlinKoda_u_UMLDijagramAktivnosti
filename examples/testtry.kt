fun test(x: Int) {
    try {
        if (x < 0) {
            throw Exception("Negativan broj")
        }
        println("Sve je u redu")
    } catch (e: Exception) {
        println("Greška: " + e.message)
    } finally {
        println("Ovo se uvek izvršava")
    }
}
