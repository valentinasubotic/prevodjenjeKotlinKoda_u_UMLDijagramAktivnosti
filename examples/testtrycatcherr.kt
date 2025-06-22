fun test() {
    val broj = 5
    try {
        val rezultat = broj + a
    } catch (e: Exception) {
        println(e.message)
        val poruka = e.message
        println(nedefinisanaPromjenljiva)
    } finally {
        val broj = 2 
        println(kraj)
        println(josJednaNepoznata) 
    }
}
